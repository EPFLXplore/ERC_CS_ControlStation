/* DESCRIPTION

This file contains all the handle functions for the different packets received
from RoCo.

Probably have to use boost:bind to be able to pass publisher objects to
handlers.
*/

#include "ros/ros.h"
// add the different types od data needed
#include "std_msgs/String.h"
#include "std_msgs/Float32MultiArray.h"
#include "std_msgs/UInt32MultiArray.h"
#include "std_msgs/Float32.h"
#include "std_msgs/UInt32.h"
#include "std_msgs/Bool.h"

#include <sstream>
#include <string>

#include "Build.h"

#include <cstdint>
#include <iomanip>
#include <iostream>
#include <thread>
#include <cstring>

#include "RoCo.h"

/* MULTI ARRAY
 are made of a
 layout  // specification of data layout
 data   // array of data
 */

///// Avionics

void handle_barotemp(uint8_t sender_id, Avionics_BaroTempPacket* packet, void* ros_publisher)
{
  std_msgs::Float32MultiArray msg;
  // //Clear array
	msg.data.clear();
  msg.data.push_back(packet->pressure);
  msg.data.push_back(packet->temperature);
  std::cout<<packet->pressure<<"\n"<<packet->temperature<<std::endl;
  //
  ((ros::Publisher *)ros_publisher)->publish(msg);
}

void handle_accelmag(uint8_t sender_id, Avionics_AccelMagPacket* packet, void* ros_publisher)
{
  std_msgs::Float32MultiArray msg;
  //Clear array
	msg.data.clear();

  // float a[] = {packet->acceleration};
  // float ang[] = {packet->angular};
  // float m[] = {packet->magneto};
  for (int i(0); i < 3; ++i) msg.data.push_back(packet->acceleration[i]);
  for (int i(0); i < 3; ++i) msg.data.push_back(packet->angular[i]);
  for (int i(0); i < 3; ++i) msg.data.push_back(packet->magneto[i]);
  //msg.data = {packet->acceleration, packet->angular, packet->magneto};

  ((ros::Publisher *)ros_publisher)->publish(msg);
}

///// Handling Device

void handle_gripper(uint8_t sender_id, Handling_GripperPacket* packet, void* ros_publisher)
{
  std_msgs::Float32 msg;
  msg.data = packet->voltage;

  ((ros::Publisher *)ros_publisher)->publish(msg);
}

///// Power

void handle_system(uint8_t sender_id, Power_SystemPacket* packet, void* ros_publisher)
{
  std_msgs::Float32MultiArray msg;
  //Clear array
	msg.data.clear();

  msg.data.push_back(packet->battery_charge);
  msg.data.push_back(packet->state);

  ((ros::Publisher *)ros_publisher)->publish(msg);
}

void handle_voltages(uint8_t sender_id, Power_VoltagePacket* packet, void* ros_publisher)
{
  std_msgs::Float32MultiArray msg;
  //Clear array
	msg.data.clear();
  for (int i(0); i < 3; ++i) msg.data.push_back(packet->voltages[i]);

  ((ros::Publisher *)ros_publisher)->publish(msg);
}

void handle_currents(uint8_t sender_id, Power_CurrentPacket* packet, void* ros_publisher)
{
  std_msgs::Float32MultiArray msg;
  //Clear array
	msg.data.clear();
  for (int i(0); i < 3; ++i) msg.data.push_back(packet->currents[i]);

  ((ros::Publisher *)ros_publisher)->publish(msg);
}

///// Science

void handle_measures(uint8_t sender_id, Science_MeasurePacket* packet, void* ros_publisher)
{
  std_msgs::Float32 msg;
  msg.data = packet->mass;

  ((ros::Publisher *)ros_publisher)->publish(msg);
}

///// General

void handle_ping(uint8_t sender_id, PingPacket* packet, void* ros_publisher)
{
  ////// USE time msg
}

void handle_request(uint8_t sender_id, RequestPacket* packet, void* ros_publisher)
{

}

void handle_response(uint8_t sender_id, ResponsePacket* packet, void* ros_publisher)
{

}

void handle_progress(uint8_t sender_id, ProgressPacket* packet, void* ros_publisher)
{

}

void handle_error(uint8_t sender_id, ErrorPacket* packet, void* ros_publisher)
{

}


///// Send to power control unit 

void reset_power_supply_callback(const boost::shared_ptr<std_msgs::Bool const> msg, NetworkBus* sender)
{
  std::cout<<msg->data<<std::endl;
  Reset_PowerSupplyPacket packet;
  packet.reset = msg->data;
  sender->send<Reset_PowerSupplyPacket>(&packet);
  std::cout<<packet.reset<<" sent!"<<std::endl;
}

void switch_avionics_callback(const boost::shared_ptr<std_msgs::Bool const> msg, NetworkBus* sender)
{
  Switch_AvionicsPacket packet;
  packet.on = msg->data;
  sender->send<Switch_AvionicsPacket>(&packet);
}

void switch_raman_callback(const boost::shared_ptr<std_msgs::Bool const> msg, NetworkBus* sender)
{
  Switch_RamanPacket packet;
  packet.on = msg->data;
  sender->send<Switch_RamanPacket>(&packet);
}

void switch_jetson_callback(const boost::shared_ptr<std_msgs::Bool const> msg, NetworkBus* sender)
{
  Switch_JetsonPacket packet;
  packet.on = msg->data;
  sender->send<Switch_JetsonPacket>(&packet);
}

void switch_lidar_callback(const boost::shared_ptr<std_msgs::Bool const> msg, NetworkBus* sender)
{
  Switch_LidarPacket packet;
  packet.on = msg->data;
  sender->send<Switch_LidarPacket>(&packet);
}

void switch_ethernet_callback(const boost::shared_ptr<std_msgs::Bool const> msg, NetworkBus* sender)
{
  Switch_EthernetPacket packet;
  packet.on = msg->data;
  sender->send<Switch_EthernetPacket>(&packet);
}