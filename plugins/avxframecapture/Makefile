include ../../config.mak

ifeq ($(SRCPATH),.)
        SRCPATH=../..
endif

SRC_PATH = $(SRCPATH)/plugins/avxframecapture/src
OBJ_PATH = ./src

OBJECTS = \
	$(OBJ_PATH)/AvxFrameCapture.o     \
	$(OBJ_PATH)/FrameCaptureProfile.o \
	$(OBJ_PATH)/FrameRenderer.o

INCLUDES = \
	-I$(SRCPATH)/include/utils \
	-I$(SRCPATH)/include

LIBS = -L../../avxutils -lavxutils -ljpeg

EXECUTABLE = libavxframecapture$(SONAME)

../$(EXECUTABLE): $(OBJECTS)
	$(LD) ../$(EXECUTABLE) $(OBJECTS) $(LIBS) $(LDFLAGS) $(LDFLAGS_DYN)

$(OBJ_PATH)/%.o: $(SRC_PATH)/%.cpp
	$(CXX) $(CFLAGS) $(CFLAGS_DYN) $(INCLUDES) -c $< -o $@

clean:
	rm -f $(OBJECTS) ../$(EXECUTABLE)

install:
	install -T -D ../$(EXECUTABLE) "$(DESTDIR)$(plugindir)/$(EXECUTABLE)"
