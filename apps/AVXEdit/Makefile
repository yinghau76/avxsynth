#############################################################################
# Makefile for building: AVXEdit
# Generated by qmake (2.01a) (Qt 4.7.0) on: Mon Feb 6 23:23:29 2012
# Project:  AVXEdit
# Template: app
# Command: /usr/bin/qmake-qt4 -o Makefile
#############################################################################

####### Compiler, tools and options
include ../../common.mk
#
# Import includes
#
COMMON_INCLUDES  = -I../../include          \
				   -I../../avxsynth/common/include \
				-I../avxframeserver/frameserverlib/src

FRAMESERVER_LIB  = -L../avxframeserver/frameserverlib -lavxframeserver

CC            = gcc
CXX           = g++
DEFINES       = -DQT_NO_DEBUG -DQT_GUI_LIB -DQT_CORE_LIB -DQT_SHARED
CFLAGS        = -pipe -O2 -Wall -W -D_REENTRANT $(DEFINES)
CXXFLAGS      = -pipe -O2 -Wall -W -D_REENTRANT $(DEFINES)
INCPATH       = -I/usr/share/qt4/mkspecs/linux-g++ -I. -I/usr/include/qt4/QtCore -I/usr/include/qt4/QtGui -I/usr/include/qt4 -I. $(COMMON_INCLUDES)
LINK          = g++
LFLAGS        = -Wl,-O1
PLUGIN_LIBRARIES = -L$(AVXSYNTH_DEPLOY_PLUGINS)
LIBS          = $(SUBLIBS)  -L/usr/lib -lQtGui -lQtCore -lpthread -Bdynamic $(PLUGIN_LIBRARIES) $(FRAMESERVER_LIB) $(AVXCOMMON_LIB)
RUNTIME_LIB_PATH = -Wl,-R$(AVXSYNTH_DEPLOY_PLUGINS) -Wl,-R$(AVXSYNTH_DEPLOY_ROOT) -Wl,-R/usr/local/lib/
AR            = ar cqs
RANLIB        = 
QMAKE         = make
TAR           = tar -cf
COMPRESS      = gzip -9f
COPY          = cp -f
SED           = sed
COPY_FILE     = $(COPY)
COPY_DIR      = $(COPY) -r
STRIP         = strip
INSTALL_FILE  = install -m 644 -p
INSTALL_DIR   = $(COPY_DIR)
INSTALL_PROGRAM = install -m 755 -p
DEL_FILE      = rm -f
SYMLINK       = ln -f -s
DEL_DIR       = rmdir
MOVE          = mv -f
CHK_DIR_EXISTS= test -d
MKDIR         = mkdir -p
MKDEP		  = cd ../avxframeserver/frameserverlib/ ; make clean ; make deploy; cd -

####### Output directory

OBJECTS_DIR   = ./

####### Source directory

SRC_DIR       = ./src

####### Files

SOURCES       = $(SRC_DIR)/main.cpp \
		$(SRC_DIR)/mainwindow.cpp $(SRC_DIR)/moc_mainwindow.cpp \
		$(SRC_DIR)/qrc_application.cpp
OBJECTS       = $(SRC_DIR)/main.o \
		$(SRC_DIR)/mainwindow.o \
		$(SRC_DIR)/moc_mainwindow.o \
		$(SRC_DIR)/qrc_application.o
DIST          = /usr/share/qt4/mkspecs/common/g++.conf \
		/usr/share/qt4/mkspecs/common/unix.conf \
		/usr/share/qt4/mkspecs/common/linux.conf \
		/usr/share/qt4/mkspecs/qconfig.pri \
		/usr/share/qt4/mkspecs/modules/qt_webkit_version.pri \
		/usr/share/qt4/mkspecs/features/qt_functions.prf \
		/usr/share/qt4/mkspecs/features/qt_config.prf \
		/usr/share/qt4/mkspecs/features/exclusive_builds.prf \
		/usr/share/qt4/mkspecs/features/default_pre.prf \
		/usr/share/qt4/mkspecs/features/release.prf \
		/usr/share/qt4/mkspecs/features/default_post.prf \
		/usr/share/qt4/mkspecs/features/warn_on.prf \
		/usr/share/qt4/mkspecs/features/qt.prf \
		/usr/share/qt4/mkspecs/features/unix/thread.prf \
		/usr/share/qt4/mkspecs/features/moc.prf \
		/usr/share/qt4/mkspecs/features/resources.prf \
		/usr/share/qt4/mkspecs/features/uic.prf \
		/usr/share/qt4/mkspecs/features/yacc.prf \
		/usr/share/qt4/mkspecs/features/lex.prf \
		/usr/share/qt4/mkspecs/features/include_source_dir.prf \
QMAKE_TARGET  = AVXEdit
DESTDIR       = 
TARGET        = AVXEdit

rebuild: first

deploy: first
	test -d $(AVXSYNTH_BIN_PATH) || mkdir -p $(AVXSYNTH_BIN_PATH); \
	$(MPLDEPLOY) $(TARGET) $(AVXSYNTH_BIN_PATH)

first: all
####### Implicit rules

.SUFFIXES: .o .c .cpp .cc .cxx .C

.cpp.o:
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o "$@" "$<"

.cc.o:
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o "$@" "$<"

.cxx.o:
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o "$@" "$<"

.C.o:
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o "$@" "$<"

.c.o:
	$(CC) -c $(CFLAGS) $(INCPATH) -o "$@" "$<"

####### Build rules

all: Makefile $(TARGET)

$(TARGET): $(OBJECTS)  
	#$(MKDEP)
	$(LINK) -rdynamic $(RUNTIME_LIB_PATH) $(LFLAGS) -o $(TARGET) $(OBJECTS) $(OBJCOMP) $(LIBS)

Makefile: /usr/share/qt4/mkspecs/linux-g++/qmake.conf /usr/share/qt4/mkspecs/common/g++.conf \
		/usr/share/qt4/mkspecs/common/unix.conf \
		/usr/share/qt4/mkspecs/common/linux.conf \
		/usr/share/qt4/mkspecs/qconfig.pri \
		/usr/share/qt4/mkspecs/modules/qt_webkit_version.pri \
		/usr/share/qt4/mkspecs/features/qt_functions.prf \
		/usr/share/qt4/mkspecs/features/qt_config.prf \
		/usr/share/qt4/mkspecs/features/exclusive_builds.prf \
		/usr/share/qt4/mkspecs/features/default_pre.prf \
		/usr/share/qt4/mkspecs/features/release.prf \
		/usr/share/qt4/mkspecs/features/default_post.prf \
		/usr/share/qt4/mkspecs/features/warn_on.prf \
		/usr/share/qt4/mkspecs/features/qt.prf \
		/usr/share/qt4/mkspecs/features/unix/thread.prf \
		/usr/share/qt4/mkspecs/features/moc.prf \
		/usr/share/qt4/mkspecs/features/resources.prf \
		/usr/share/qt4/mkspecs/features/uic.prf \
		/usr/share/qt4/mkspecs/features/yacc.prf \
		/usr/share/qt4/mkspecs/features/lex.prf \
		/usr/share/qt4/mkspecs/features/include_source_dir.prf \
		/usr/lib/libQtGui.prl \
		/usr/lib/libQtCore.prl
	$(QMAKE) -o Makefile
/usr/share/qt4/mkspecs/common/g++.conf:
/usr/share/qt4/mkspecs/common/unix.conf:
/usr/share/qt4/mkspecs/common/linux.conf:
/usr/share/qt4/mkspecs/qconfig.pri:
/usr/share/qt4/mkspecs/modules/qt_webkit_version.pri:
/usr/share/qt4/mkspecs/features/qt_functions.prf:
/usr/share/qt4/mkspecs/features/qt_config.prf:
/usr/share/qt4/mkspecs/features/exclusive_builds.prf:
/usr/share/qt4/mkspecs/features/default_pre.prf:
/usr/share/qt4/mkspecs/features/release.prf:
/usr/share/qt4/mkspecs/features/default_post.prf:
/usr/share/qt4/mkspecs/features/warn_on.prf:
/usr/share/qt4/mkspecs/features/qt.prf:
/usr/share/qt4/mkspecs/features/unix/thread.prf:
/usr/share/qt4/mkspecs/features/moc.prf:
/usr/share/qt4/mkspecs/features/resources.prf:
/usr/share/qt4/mkspecs/features/uic.prf:
/usr/share/qt4/mkspecs/features/yacc.prf:
/usr/share/qt4/mkspecs/features/lex.prf:
/usr/share/qt4/mkspecs/features/include_source_dir.prf:
/usr/lib/libQtGui.prl:
/usr/lib/libQtCore.prl:
qmake:  FORCE
	@$(QMAKE) -o Makefile

dist: 
	@$(CHK_DIR_EXISTS) .tmp/application1.0.0 || $(MKDIR) .tmp/application1.0.0 
	$(COPY_FILE) --parents $(SOURCES) $(DIST) .tmp/application1.0.0/ && $(COPY_FILE) --parents $(SRC_DIR)/mainwindow.h .tmp/application1.0.0/ && $(COPY_FILE) --parents application.qrc .tmp/application1.0.0/ && $(COPY_FILE) --parents $(SRC_DIR)/main.cpp $(SRC_DIR)/mainwindow.cpp .tmp/application1.0.0/ && (cd `dirname .tmp/application1.0.0` && $(TAR) application1.0.0.tar application1.0.0 && $(COMPRESS) application1.0.0.tar) && $(MOVE) `dirname .tmp/application1.0.0`/application1.0.0.tar.gz . && $(DEL_FILE) -r .tmp/application1.0.0


clean:compiler_clean 
	-$(DEL_FILE) $(OBJECTS)
	-$(DEL_FILE) $(TARGET)
	-$(DEL_FILE) *~ core *.core


####### Sub-libraries

distclean: clean
	-$(DEL_FILE) $(TARGET) 
	-$(DEL_FILE) Makefile


check: first

mocclean: compiler_moc_header_clean compiler_moc_source_clean

mocables: compiler_moc_header_make_all compiler_moc_source_make_all

compiler_moc_header_make_all: $(SRC_DIR)/moc_mainwindow.cpp
compiler_moc_header_clean:
	-$(DEL_FILE) $(SRC_DIR)/moc_mainwindow.cpp
$(SRC_DIR)/moc_mainwindow.cpp: $(SRC_DIR)/mainwindow.h
	/usr/bin/moc-qt4 $(DEFINES) $(INCPATH) $(SRC_DIR)/mainwindow.h -o $(SRC_DIR)/moc_mainwindow.cpp

compiler_rcc_make_all: $(SRC_DIR)/qrc_application.cpp
compiler_rcc_clean:
	-$(DEL_FILE) $(SRC_DIR)/qrc_application.cpp
$(SRC_DIR)/qrc_application.cpp: application.qrc \
		images/new.png \
		images/copy.png \
		images/cut.png \
		images/save.png \
		images/paste.png \
		images/mplayer.png \
		images/open.png
	/usr/bin/rcc -name application application.qrc -o $(SRC_DIR)/qrc_application.cpp

compiler_image_collection_make_all: $(SRC_DIR)/qmake_image_collection.cpp
compiler_image_collection_clean:
	-$(DEL_FILE) $(SRC_DIR)/qmake_image_collection.cpp
compiler_moc_source_make_all:
compiler_moc_source_clean:
compiler_uic_make_all:
compiler_uic_clean:
compiler_yacc_decl_make_all:
compiler_yacc_decl_clean:
compiler_yacc_impl_make_all:
compiler_yacc_impl_clean:
compiler_lex_make_all:
compiler_lex_clean:
compiler_clean: compiler_moc_header_clean compiler_rcc_clean 

####### Compile

main.o: $(SRC_DIR)/main.cpp $(SRC_DIR)/mainwindow.h
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o $(SRC_DIR)/main.o $(SRC_DIR)/main.cpp

mainwindow.o: $(SRC_DIR)/mainwindow.cpp $(SRC_DIR)/mainwindow.h
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o $(SRC_DIR)/mainwindow.o $(SRC_DIR)/mainwindow.cpp

moc_mainwindow.o: $(SRC_DIR)/moc_mainwindow.cpp 
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o $(SRC_DIR)/moc_mainwindow.o $(SRC_DIR)/moc_mainwindow.cpp

qrc_application.o: $(SRC_DIR)/qrc_application.cpp 
	$(CXX) -c $(CXXFLAGS) $(INCPATH) -o qrc_application.o $(SRC_DIR)/qrc_application.cpp

####### Install

install_target: first FORCE
	@$(CHK_DIR_EXISTS) $(INSTALL_ROOT)/usr/lib/qt4/examples/mainwindows/application/ || $(MKDIR) $(INSTALL_ROOT)/usr/lib/qt4/examples/mainwindows/application/ 
	-$(INSTALL_PROGRAM) "$(QMAKE_TARGET)" "$(INSTALL_ROOT)/usr/lib/qt4/examples/mainwindows/application/$(QMAKE_TARGET)"
	-$(STRIP) "$(INSTALL_ROOT)/usr/lib/qt4/examples/mainwindows/application/$(QMAKE_TARGET)"

uninstall_target:  FORCE
	-$(DEL_FILE) "$(INSTALL_ROOT)/usr/lib/qt4/examples/mainwindows/application/$(QMAKE_TARGET)"
	-$(DEL_DIR) $(INSTALL_ROOT)/usr/lib/qt4/examples/mainwindows/application/ 

uninstall_sources:  FORCE
	-$(DEL_FILE) -r $(INSTALL_ROOT)/usr/lib/qt4/examples/mainwindows/application/src/main.cpp 
	 -$(DEL_FILE) -r $(INSTALL_ROOT)/usr/lib/qt4/examples/mainwindows/application/src/mainwindow.cpp 
	 -$(DEL_FILE) -r $(INSTALL_ROOT)/usr/lib/qt4/examples/mainwindows/application/src/mainwindow.h 
	 -$(DEL_FILE) -r $(INSTALL_ROOT)/usr/lib/qt4/examples/mainwindows/application/application.qrc 
	 -$(DEL_FILE) -r $(INSTALL_ROOT)/usr/lib/qt4/examples/mainwindows/application/images
	-$(DEL_DIR) $(INSTALL_ROOT)/usr/lib/qt4/examples/mainwindows/application/ 

install:  install_target install_sources  FORCE

uninstall: uninstall_target uninstall_sources   FORCE

FORCE:
