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

std::string ss;

void handle_packet(uint8_t sender_id, PingPacket* packet) {
  ss = "Ping C2C: " + std::to_string((PingPacket().time - packet->time).count()) + "ns";
  //ss << "Ping C2C: " << (PingPacket().time - packet->time).count() << "ns" << std::endl;
}

// void return_message(const std_msgs::String::ConstPtr& msg, NetworkBus *client_bus)

void return_message(const boost::shared_ptr<std_msgs::String const> msg, NetworkBus *client_bus)
{
  std::cout<<(*msg);
  DataPacket returned;
  returned.data = 2;
  client_bus->send<DataPacket>(&returned);
}

// Simulates the control station - avionics ROS-RoCo interface, receives message
// from sender.cpp (RoCo) and forwards it to listener.py using ROS

int main(int argc, char **argv)
{
  // call of init needed before anything else, "" is the name of the node
  ros::init(argc, argv, "talker");

  // main access point to communications with ROS system
  // NodeHandle initializes this node
  ros::NodeHandle n;

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
