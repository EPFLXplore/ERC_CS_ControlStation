/* DESCRIPTION

This file serves as an interface between the RoCo protocol and the ROS
environment.
Packets received over RoCo are dealt with and transferred to their
corresponding topic on ROS.
Nodes subscribed to certain topics receive data which is transferred to the
corresponding subsystem through RoCo.
*/

/* PACKETS TO IMPLEMENT

Avionics_BaroTempPacket
Avionics_AccelMagPacket

Handling_GripperPacket

Power_SystemPacket
Power_VoltagePacket
Power_CurrentPacket

Science_MeasurePacket

PingPacket
RequestPacket
ResponsePacket
ProgressPacket
ErrorPacket
*/

#include "ros/ros.h"
#include "std_msgs/String.h"
#include "std_msgs/Float32MultiArray.h"
#include "std_msgs/UInt32MultiArray.h"
#include "std_msgs/Float32.h"
#include "std_msgs/UInt8.h"
#include "std_msgs/Time.h"

#include <sstream>
#include <string>

#include "Build.h"

#ifdef BUILD_FOR_TESTING


#include <cstdint>
#include <iomanip>
#include <iostream>
#include <thread>
#include <cstring>
#include <boost/bind.hpp>

#include "RoCo.h"
#include "handlers.h"

// Simulates the control station - avionics ROS-RoCo interface, receives message
// from sender.cpp (RoCo) and forwards it to listener.py using ROS

int main(int argc, char **argv)
{
  // call of init needed before anything else, "" is the name of the node
  ros::init(argc, argv, "interface");

  // main access point to communications with ROS system
  // NodeHandle initializes this node
  ros::NodeHandle n;

  //-----define ROS topics on which to publish-----

  // advertise() function indicates to ROS we are publishing on topic "chatter"
  // returns a Publisher object, which allows to publish on that topic using the
  // publish() function. The second parameter is the message queue, number indicates
  // how many messages to buffer up before throwing some away
  ros::Publisher av_barotemp_pub = n.advertise<std_msgs::Float32MultiArray>("barotemp", 1000);
  ros::Publisher av_accelmag_pub = n.advertise<std_msgs::Float32MultiArray>("accelmag", 1000);

  ros::Publisher ha_gripper_pub = n.advertise<std_msgs::Float32>("gripper", 1000);

  ros::Publisher po_system_pub = n.advertise<std_msgs::Float32MultiArray>("system", 1000);
  ros::Publisher po_voltage_pub = n.advertise<std_msgs::Float32MultiArray>("voltages", 1000);
  ros::Publisher po_current_pub = n.advertise<std_msgs::Float32MultiArray>("currents", 1000);

  ros::Publisher sc_measure_pub = n.advertise<std_msgs::Float32>("measures", 1000);

  // ros::Publisher ping_pub = n.advertise<std_msgs::Float32>("ping", 1000); // use time msgeg
  // ros::Publisher request_pub = n.advertise<std_msgs::UInt32MultiArray>("request", 1000);
  // ros::Publisher response_pub = n.advertise<std_msgs::UInt32MultiArray>("response", 1000);
  // ros::Publisher progress_pub = n.advertise<std_msgs::UInt32MultiArray>("progress", 1000);
  // ros::Publisher error_pub = n.advertise<std_msgs::UInt8>("error", 1000);

  // the only one that might need a subscribe might be for the request



  // 1 Hz refresh rate of the node
  ros::Rate loop_rate(10);


	std::cout << "Starting main test..." << std::endl;


  // create RoCo client, ip address of server, port of server
	NetworkClientIO* client_io_2 = new NetworkClientIO("192.168.1.2", PORT_B);

	// client_io_2->receive(&handle_input);
  // connect client
	int result = client_io_2->connectClient();

	if(result < 0) {
		std::cout << "Network Client IO connection failed with error code " << result << std::endl;
		std::cout << std::strerror(errno) << std::endl;
	}


	NetworkBus* client_2_bus = new NetworkBus(client_io_2);


  while (ros::ok())
  {
    //-----set client bus to handle different packets-----

    // have to use boost:bind for the handle functions so that each handler
    // uses the right publisher
    client_2_bus->handle(handle_barotemp,  (void*)&av_barotemp_pub);
    client_2_bus->handle(handle_accelmag,  (void*)&av_accelmag_pub);

    client_2_bus->handle(handle_gripper,  (void*)&ha_gripper_pub);

    client_2_bus->handle(handle_system,  (void*)&po_system_pub);
    client_2_bus->handle(handle_voltages,  (void*)&po_voltage_pub);
    client_2_bus->handle(handle_currents,  (void*)&po_current_pub);

    client_2_bus->handle(handle_measures,  (void*)&sc_measure_pub);

    // client_2_bus->handle(handle_ping,  (void*)&ping_pub);
    // client_2_bus->handle(handle_request,  (void*)&request_pub);
    // client_2_bus->handle(handle_response,  (void*)&response_pub);
    // client_2_bus->handle(handle_progress,  (void*)&progress_pub);
    // client_2_bus->handle(handle_error,  (void*)&error_pub);

    // used to handle ros communication events, i.e. callback to function
    ros::spinOnce();

    // enforces the frequency at which this while loop runs (here at 1H z, see above)
    loop_rate.sleep();

  }

  return 0;
}
#endif
