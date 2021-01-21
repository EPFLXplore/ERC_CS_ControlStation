CXX = g++
CC = $(CXX)
CXXFLAGS = -std=c++17 -Wall
LDLIBS = -lm

MainTest: MainTest.o IOBus.o MessageBus.o NetworkBus.o NetworkClientIO.o NetworkServerIO.o
	g++ -pthread MainTest.o IOBus.o MessageBus.o NetworkBus.o NetworkClientIO.o NetworkServerIO.o -o MainTest

MainTest.o: MainTest.cpp Build.h RoCo.h
	g++ -c MainTest.cpp

IOBus.o: IOBus.cpp IOBus.h MessageBus.h
	g++ -c IOBus.cpp
MessageBus.o: MessageBus.cpp MessageBus.h
	g++ -c MessageBus.cpp
NetworkBus.o: NetworkBus.cpp Protocol.h NetworkBus.h IOBus.h
	g++ -c NetworkBus.cpp
NetworkClientIO.o: NetworkClientIO.cpp NetworkClientIO.h IODriver.h NetworkIO.h
	g++ -c -pthread NetworkClientIO.cpp
NetworkServerIO.o: NetworkServerIO.cpp NetworkServerIO.h IODriver.h NetworkIO.h
	g++ -c -pthread NetworkServerIO.cpp

clean:
	rm -r *.o
