UNAME_S 		:= 		$(shell uname -s)
RELEASE_PATH 	= 		.Build
DEBUG_PATH 		= 		.Debug

# ------------------------------------------------------
# Debug processing
# ------------------------------------------------------
ifeq ($(DEBUG),1)
   	OUTPUT_PATH = $(DEBUG_PATH)
   	CPPFLAGS += -DDEBUG -ggdb
else
	OUTPUT_PATH = $(RELEASE_PATH)
	CPPFLAGS +=
endif

# ------------------------------------------------------
# Compiler selection
# ------------------------------------------------------
ifeq ($(UNAME_S), Darwin)
	CPP = /usr/local/opt/llvm/bin/clang++
	CPPFLAGS += -I/usr/local/opt/llvm/include -fopenmp -std=c++11
	LDFLAGS += -L/usr/local/opt/llvm/lib
else
	CPP = g++
	CPPFLAGS += -fopenmp -std=c++11
	LDFLAGS +=
endif

# ------------------------------------------------------
# Output path setup
# ------------------------------------------------------
SETUP_OUTPUT	=		mkdir -p $(OUTPUT_PATH)


# ------------------------------------------------------
# Build target setup
# ------------------------------------------------------
%.o: %.cpp
	$(SETUP_OUTPUT)
	$(CPP) $(CPPFLAGS) $(LDFLAGS) $^ -o $(OUTPUT_PATH)/$@

clean:
	rm -rf $(RELEASE_PATH)
	rm -rf $(DEBUG_PATH)
