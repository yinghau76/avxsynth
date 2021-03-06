# Automated testing framework for AvxSynth.
# Script execution and output handling.

import datetime
import hashlib
import os
import subprocess
import sys

from AvxTestCommon import *


class AvxFrameServer(object):
    '''AvxFrameServer:

    Evalues an AvxSynth script and computes hashsums of output
    '''
    def __init__(self, avs_name, extra_file_list=[]):
        '''Parameters:

        avs_name: pathname of script to open
        extra_file_list: list of additional files generated by script
        '''
        self.avs_name = avs_name
        self.extra_file_list = extra_file_list
        
        self._main_hash = None
        self._extra_hash_table = {}
        self.ready = True

    def run(self):
        '''Evalute script.  Check the status of self.ready first.'''
        if not self.ready:
            raise AvxNotReadyError('Subprocess already completed')

        # Change these as needed.
        BUFSIZE = 4 * 2 ** 20
        MAXSIZE = 1 * 2 ** 30
        MAXTIME = datetime.timedelta(seconds=600)
        
        devnull = open(os.devnull, 'wb')
        try:
            process = subprocess.Popen(
                ['avxFrameServer', self.avs_name, 'N'],
#                ['avs2pipemod', self.avs_name, '-rawvideo'],
                bufsize=BUFSIZE, stdout=subprocess.PIPE, stderr=devnull)
        except OSError as err:
            raise AvxScriptError(err)        
        start_time = datetime.datetime.now()
        hashsum = hashlib.md5()
        read_bytes = 0
        while process.poll() == None:
            buf = process.stdout.read(BUFSIZE)
            read_bytes += len(buf)
            hashsum.update(buf)
            if read_bytes > MAXSIZE:
                process.terminate()
                errmsg = 'More data than maximum of {0} was produced'
                raise AvxRuntimeError(errmsg.format(MAXSIZE))
            if datetime.datetime.now() - start_time > MAXTIME:
                process.terminate()
                errmsg = 'Script taking longer than maximum of {0} to execute'
                raise AvxRuntimeError(errmsg.format(MAXTIME))
        # The process will terminate if less than BUFSIZE bytes remain
        hashsum.update(process.stdout.read())
        devnull.close()
        if process.returncode != 0:
            raise AvxRuntimeError('Script returned nonzero exit status')
        self._main_hash = hashsum.hexdigest()
        for i in self.extra_file_list:
            try:
                file = open(i, 'rb')
                self._extra_hash_table[i] = hashlib.md5(file.read()).hexdigest()
                file.close()
            except IOError as err:
                errmsg = 'Extra file {0} was not found'
                raise AvxFileError(errmsg.format(i))
        self.ready = False
        
    def query_results(self):
        '''Return a tuple of the main output hash and a dict of the hashes
        of all the additional files in self.extra_file_list.  Check the status
        of self.ready first.
        '''
        if self.ready:
            raise AvxNotReadyError('Subprocess has not yet executed')
        return self._main_hash, self._extra_hash_table

    def cleanup(self):
        '''Delete generated files listed in self.extra_file_list and reset
        self.ready'''
        for i in self.extra_file_list:
            try:
                os.unlink(i)
            except OSError:
                errmsg = 'Auto-generated file {0} was not found\n'
                sys.stderr.write(errmsg.format(i))
        self._main_hash = None
        self._extra_hash_table = {}
        self.ready = True
