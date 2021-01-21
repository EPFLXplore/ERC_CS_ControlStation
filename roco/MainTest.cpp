/*
 * MainTest.cpp
 *
 *  Created on: 27 Apr 2020
 *      Author: Arion
 */


#include "Build.h"

#ifdef BUILD_FOR_TESTING


#include <cstdint>
#include <iomanip>
#include <iostream>
#include <thread>
#include <cstring>

#include "RoCo.h"

/*
void handle_input(uint8_t sender_id, uint8_t* buffer, uint32_t length) {
	std::cout << std::endl << "---------- Frame begin from sender ID " << (uint32_t) sender_id << " ----------" << std::endl << std::endl << " ";

	for(int32_t i = 0; i < length; i++) {
		std::cout << std::setfill('0') << std::setw(2) << std::hex << (uint32_t) buffer[i] << " ";

		if(i % 16 == 15 || i == length - 1) {
			std::cout << std::endl;
		}

		if(i % 4 == 3) {
			std::cout << " ";
		}
	}

	std::cout << std::dec << std::endl << "---------- Frame end ----------" << std::endl << std::endl;
}*/

void handle_packet(uint8_t sender_id, PingPacket* packet) {
	std::cout << "Ping C2C: " << (PingPacket().time - packet->time).count() << "ns" << std::endl;
}

int main() {
	std::cout << "Starting main test..." << std::endl;


	NetworkServerIO* server_io = new NetworkServerIO(PORT_B);

	// server_io->receive(&handle_input);

	int32_t result = server_io->connectServer();

	if(result < 0) {
		std::cout << "Network Server IO connection failed with error code " << result << std::endl;
		std::cout << std::strerror(errno) << std::endl;
	} else {
		std::cout << "Connected to network server IO" << std::endl;
	}



	NetworkClientIO* client_io_1 = new NetworkClientIO("127.0.0.1", PORT_B);

	// client_io_1->receive(&handle_input);

	result = client_io_1->connectClient();

	if(result < 0) {
		std::cout << "Network Client IO connection failed with error code " << result << std::endl;
		std::cout << std::strerror(errno) << std::endl;
	}

	NetworkClientIO* client_io_2 = new NetworkClientIO("127.0.0.1", PORT_B);

	// client_io_2->receive(&handle_input);

	result = client_io_2->connectClient();

	if(result < 0) {
		std::cout << "Network Client IO connection failed with error code " << result << std::endl;
		std::cout << std::strerror(errno) << std::endl;
	}





	PingPacket packet;


	NetworkBus* server_bus = new NetworkBus(server_io);
	NetworkBus* client_1_bus = new NetworkBus(client_io_1);
	NetworkBus* client_2_bus = new NetworkBus(client_io_2);


	//server_bus->forward<PingPacket>(server_bus);
	client_2_bus->handle(handle_packet);

	//client_1_bus->send(&packet);

	std::cout << "Test finished" << std::endl;

	switch (/* expression */) {
		case /* value */:
	}


	while(true);
}

#endif /* BUILD_FOR_TESTING */
