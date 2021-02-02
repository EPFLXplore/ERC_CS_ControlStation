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

// Simulates the control station - avionics ROS-RoCo interface, receives message
// from sender.cpp (RoCo) and forwards it to listener.py using ROS

int main(int argc, char **argv)
{
  // call of init needed before anything else, "" is the name of the node
  ros::init(argc, argv, "interface");

  // main access point to communications with ROS system
  // NodeHandle initializes this node
  ros::NodeHandle n;

  // define ROS topics on which to publish
  ros::Publisher av_barotemp_pub = n.advertise<std_msgs::Float32MultiArray>("barotemp", 1000);
  ros::Publisher av_accelmag_pub = n.advertise<std_msgs::Float32MultiArray>("accelmag", 1000);

  ros::Publisher ha_gripper_pub = n.advertise<std_msgs::Float32>("gripper", 1000);

  ros::Publisher po_system_pub = n.advertise<std_msgs::Float32MultiArray>("system", 1000);
  ros::Publisher po_voltage_pub = n.advertise<std_msgs::Float32MultiArray>("voltage", 1000);
  ros::Publisher po_current_pub = n.advertise<std_msgs::Float32MultiArray>("current", 1000);

  ros::Publisher sc_measure_pub = n.advertise<std_msgs::Float32>("measure", 1000);

  ros::Publisher ping_pub = n.advertise<std_msgs::Float32>("ping", 1000);
  ros::Publisher request_pub = n.advertise<std_msgs::UInt32MultiArray>("request", 1000);
  ros::Publisher response_pub = n.advertise<std_msgs::UInt32MultiArray>("response", 1000);
  ros::Publisher progress_pub = n.advertise<std_msgs::UInt32MultiArray>("progress", 1000);
  ros::Publisher error_pub = n.advertise<std_msgs::UInt8>("error", 1000);

  // the only one that might need a subscribe might be for the request 


  // advertise() function indicates to ROS we are publishing on topic "chatter"
  // returns a Publisher object, which allows to publish on that topic using the
  // publish() function. The second parameter is the message queue, number indicates
  // how many messages to buffer up before throwing some away
  ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);

  // 1 Hz refresh rate of the node
  ros::Rate loop_rate(1);

  // count of how many messages sent
  int count = 0;



	std::cout << "Starting main test..." << std::endl;


  // create RoCo client, ip address of server, port of server
	NetworkClientIO* client_io_2 = new NetworkClientIO("127.0.0.1", PORT_B);

	// client_io_2->receive(&handle_input);
  // connect client
	int result = client_io_2->connectClient();

	if(result < 0) {
		std::cout << "Network Client IO connection failed with error code " << result << std::endl;
		std::cout << std::strerror(errno) << std::endl;
	}



	PingPacket packet;

	//NetworkBus* server_bus = new NetworkBus(server_io);
	//NetworkBus* client_1_bus = new NetworkBus(client_io_1);
	NetworkBus* client_2_bus = new NetworkBus(client_io_2);


	//server_bus->forward<PingPacket>(server_bus);


	//bool sent = client_1_bus->send(&packet);


  // Add code to send back to sender.cpp to indicate that the message
  // has been received, so that sender.cpp can stop sending it

  ////
  ros::Subscriber return_msg = n.subscribe<std_msgs::String>("msg", 1000, boost::bind(return_message, _1, client_2_bus));
  ////


  while (ros::ok())
  {

    client_2_bus->handle(handle_packet);

    std_msgs::String msg;
    if (ss != ""){
      DataPacket received;
      received.data = 1;
      client_2_bus->send<DataPacket>(&received);
    }

    ss += " " + std::to_string(count);
    msg.data = ss;
    ss="";

    ROS_INFO("%s", msg.data.c_str());

    // publish() function to send messages (parameter). Type of object must
    // agree with type given as template parameter to advertise<>() call
    chatter_pub.publish(msg);

    // used to handle ros communication events
    ros::spinOnce();

    // enforces the frequency at which this while loop runs (here at 1H z, see above)
    loop_rate.sleep();

    ++count;
  }

  return 0;
}
#endif
