#include "Build.h"

#ifdef BUILD_FOR_TESTING


#include <cstdint>
#include <iomanip>
#include <iostream>
#include <thread>
#include <cstring>
#include <unistd.h>
#include <chrono>

#include "RoCo.h"
#include <boost/bind.hpp>
#include <functional>

void handle_packet(uint8_t sender_id, PingPacket* packet, void* var) {
  //std::cout<<"Ping C2C: "<<(PingPacket().time - packet->time).count()<<"ns";
  // uint64_t current_time = static_cast<uint64_t>(std::chrono::duration_cast<std::chrono::nanoseconds> (std::chrono::time_point<std::chrono::system_clock>{}.time_since_epoch()).count());
  //std::cout<<packet->time<<std::endl;
  std::cout<<"Ping C2C: "<<PingPacket().time - packet->time<<"ns"<<std::endl;
  // std::cout<<*(int *)var<<std::endl;
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
    //std::this_thread::sleep_for(std::chrono::seconds(1));
  }

}
#endif
