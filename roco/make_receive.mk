CXX = g++
CC = $(CXX)
CXXFLAGS = -std=c++17 -Wall
LDLIBS = -lm

TARGET = receive
TARGETo = $(TARGET).o
TARGETcpp = $(TARGET).cpp


$(TARGET): $(TARGETo) IOBus.o MessageBus.o NetworkBus.o NetworkClientIO.o NetworkServerIO.o
	$(CC) -pthread $(TARGETo) IOBus.o MessageBus.o NetworkBus.o NetworkClientIO.o NetworkServerIO.o -o $(TARGET)

$(TARGETo): $(TARGETcpp) Build.h RoCo.h
	$(CC) -c $(TARGETcpp)

IOBus.o: IOBus.cpp IOBus.h MessageBus.h
	$(CC) -c IOBus.cpp
MessageBus.o: MessageBus.cpp MessageBus.h
	$(CC) -c MessageBus.cpp
NetworkBus.o: NetworkBus.cpp Protocol.h NetworkBus.h IOBus.h
	$(CC) -c NetworkBus.cpp
NetworkClientIO.o: NetworkClientIO.cpp NetworkClientIO.h IODriver.h NetworkIO.h
	$(CC) -c -pthread NetworkClientIO.cpp
NetworkServerIO.o: NetworkServerIO.cpp NetworkServerIO.h IODriver.h NetworkIO.h
	$(CC) -c -pthread NetworkServerIO.cpp

clean:
	rm -r *.o
