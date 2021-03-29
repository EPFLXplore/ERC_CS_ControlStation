set(HEADER_FILES
        IOBus.h
        IODriver.h
        MessageBus.h
        NetworkBus.h
        NetworkClientIO.h
        NetworkIO.h
        NetworkServerIO.h
        )

set(SOURCE_FILES
        IOBus.cpp
        MessageBus.cpp
        NetworkBus.cpp
        NetworkClientIO.cpp
        NetworkServerIO.cpp
        )

add_library(Src STATIC ${SOURCE_FILES} ${HEADER_FILES})
add_definitions(-DBUILD_FOR_TESTING)