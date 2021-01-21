#include "Build.h"

#ifdef BUILD_FOR_TESTING


#include <cstdint>
#include <iomanip>
#include <iostream>
#include <thread>
#include <cstring>
#include <unistd.h>

#include "RoCo.h"


// Simulates the avionics, sends message to talker.cpp using RoCo

void handle_data_packet(uint8_t sender_id, DataPacket* packet){
	if ((*packet).data==1){
		std::cout<<"Message received by receiver \n";
	} else if((*packet).data==2){
		std::cout<<"Returned message received \n";
	}
}

int main() {
	std::cout << "Starting send test..." << std::endl;


	NetworkServerIO* server_io = new NetworkServerIO(PORT_B);

	// server_io->receive(&handle_input);

	int32_t result = server_io->connectServer();

	if(result < 0) {
		std::cout << "Network Server IO connection failed with error code " << result << std::endl;
		std::cout << std::strerror(errno) << std::endl;
	} else {
		std::cout << "Connected to network server IO" << std::endl;
	}


	NetworkBus* server_bus = new NetworkBus(server_io);
	//NetworkBus* client_1_bus = new NetworkBus(client_io_1);
	//NetworkBus* client_2_bus = new NetworkBus(client_io_2);


	//server_bus->forward<PingPacket>(server_bus);
	//client_2_bus->handle(handle_packet);
  int count = 0;
  //client_1_bus->send(&packet);

  while(true){
    PingPacket packet;
    server_bus->send<PingPacket>(&packet);
    count+=1;
    std::cout << "PingPacket "<<count<<" sent" << std::endl;

		server_bus->handle(handle_data_packet);

    std::this_thread::sleep_for(std::chrono::seconds(1));
  }

}

#endif /* BUILD_FOR_TESTING */
