#include "Build.h"

#ifdef BUILD_FOR_TESTING


#include <cstdint>
#include <iomanip>
#include <iostream>
#include <thread>
#include <cstring>
#include <unistd.h>

#include "RoCo.h"

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
  //client_1_bus->send(&packet);
  char input;

  while(true){
    std::cout<<"Please enter number (0 - 6) : ";
    std::cin >> input;
    std::cout<<std::endl;

    switch (input){
      case '0':
        Avionics_BaroTempPacket p;
        p.pressure = 1000;
        p.temperature = 42;
        server_bus->send<Avionics_BaroTempPacket>(&p);
        std::cout<<"Avionics_BaroTempPacket sent!"<<std::endl;
        break;
      case '1':
        Avionics_AccelMagPacket p1;
        p1.acceleration[0] = 1; p1.acceleration[1] = -1; p1.acceleration[2] = 12;
        p1.angular[0] = 1.5; p1.angular[1] = 14; p1.angular[2] = 23;
        p1.magneto[0] = 0.01; p1.magneto[1] = 0.03; p1.magneto[2] = 0.4;
        // p1.angular = {1.5, 14, 23};
        // p1.magneto = {0.01, 0.03, 0.4}
        server_bus->send<Avionics_AccelMagPacket>(&p1);
        std::cout<<"Avionics_AccelMagPacket sent!"<<std::endl;
        break;
      case '2':
        Handling_GripperPacket p2;
        p2.voltage = 24;
        server_bus->send<Handling_GripperPacket>(&p2);
        std::cout<<"Handling_GripperPacket sent!"<<std::endl;
        break;
      case '3':
        Power_VoltagePacket p3;
        //p3.voltages = {12, 24, 48, 16};
        p3.voltages[0] = 12; p3.voltages[1] = 24; p3.voltages[2] = 48; p3.voltages[3] = 16;
        server_bus->send<Power_VoltagePacket>(&p3);
        std::cout<<"Power_VoltagePacket sent!"<<std::endl;
        break;
      case '4':
        Power_CurrentPacket p4;
        //p4.currents = {1, 4, 1.64, 12};
        p4.currents[0] = 1; p4.currents[1] = 4; p4.currents[2] = 1.64; p4.currents[3] = 12;
        server_bus->send<Power_CurrentPacket>(&p4);
        std::cout<<"Power_CurrentPacket sent!"<<std::endl;
        break;
      case '5':
        Power_SystemPacket p5;
        p5.battery_charge = 0.88;
        p5.state = 4;
        server_bus->send<Power_SystemPacket>(&p5);
        std::cout<<"Power_SystemPacket sent!"<<std::endl;
        break;
      case '6':
        Science_MeasurePacket p6;
        p6.mass = 120;
        server_bus->send<Science_MeasurePacket>(&p6);
        std::cout<<"Science_MeasurePacket sent!"<<std::endl;
        break;
      default:
        std::cout<<"Please enter a valid number!"<<std::endl;
        break;
    }

    // PingPacket packet;
    // server_bus->send<PingPacket>(&packet);
    // std::cout << "PingPacket "<<count<<" sent" << std::endl;

    std::this_thread::sleep_for(std::chrono::seconds(1));
  }

}
#endif
