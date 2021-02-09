#include "Build.h"

#ifdef BUILD_FOR_TESTING


#include <cstdint>
#include <iomanip>
#include <iostream>
#include <thread>
#include <cstring>
#include <unistd.h>

#include "RoCo.h"
#include <boost/bind.hpp>
#include <functional>

std::string ss;

void handle_packet(uint8_t sender_id, PingPacket* packet, void* var) {
  ss = "Ping C2C: " + std::to_string((PingPacket().time - packet->time).count()) + "ns";
  std::cout<<*(int *)var<<std::endl;
  //ss << "Ping C2C: " << (PingPacket().time - packet->time).count() << "ns" << std::endl;
}

int main() {
	std::cout << "Starting receive test..." << std::endl;


	NetworkClientIO* client_io = new NetworkClientIO("127.0.0.1", PORT_B);

	// server_io->receive(&handle_input);

  int result = client_io->connectClient();

	if(result < 0) {
		std::cout << "Network Client IO connection failed with error code " << result << std::endl;
		std::cout << std::strerror(errno) << std::endl;
	}


	NetworkBus* client_bus = new NetworkBus(client_io);
  int num = 12;
  int* pnum = &num;
  void* pvnum = (void*) pnum;

  while(true){
    client_bus->handle(handle_packet, pvnum);
    std::cout<<ss<<std::endl;
    std::this_thread::sleep_for(std::chrono::seconds(1));
  }

}
#endif
