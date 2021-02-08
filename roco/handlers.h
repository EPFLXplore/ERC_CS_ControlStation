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
#include "std_msgs/UInt8.h"

#include <sstream>
#include <string>

#include "Build.h"

#include <cstdint>
#include <iomanip>
#include <iostream>
#include <thread>
#include <cstring>
#include <boost/bind.hpp>

#include "RoCo.h"

/* MULTI ARRAY
 are made of a
 layout  // specification of data layout
 data   // array of data
 */

///// Avionics

void handle_barotemp(uint8_t sender_id, Avionics_BaroTempPacket* packet, ros::Publisher ros_publisher)
{
  std_msgs::Float32MultiArray msg;
  //Clear array
	msg.data.clear();
  msg.data.push_back(packet->pressure);
  msg.data.push_back(packet->temperature);

  ros_publisher.publish(msg);
}

void handle_accelmag(uint8_t sender_id, Avionics_AccelMagPacket* packet, ros::Publisher ros_publisher)
{
  std_msgs::Float32MultiArray msg;
  //Clear array
	msg.data.clear();

  float a[3] = packet->acceleration;
  float ang[3] = packet->angular;
  float m[3] = packet->magneto;

  msg.data = {a, ang, m};

  ros_publisher.publish(msg);
}

///// Handling Device

void handle_gripper(uint8_t sender_id, Handling_GripperPacket* packet, ros::Publisher ros_publisher)
{
  std_msgs::Float32 msg;
  msg.data = packet->voltage;

  ros_publisher.publish(msg);
}

///// Power

void handle_system(uint8_t sender_id, Power_SystemPacket* packet, ros::Publisher ros_publisher)
{
  std_msgs::Float32MultiArray msg;
  //Clear array
	msg.data.clear();

  msg.data.push_back(packet->battery_charge);
  msg.data.push_back(packet->state);

  ros_publisher.publish(msg);
}

void handle_voltages(uint8_t sender_id, Power_VoltagePacket* packet, ros::Publisher ros_publisher)
{
  std_msgs::Float32MultiArray msg;
  //Clear array
	msg.data.clear();
  msg.data = packet->voltages;

  ros_publisher.publish(msg);
}

void handle_currents(uint8_t sender_id, Power_CurrentPacket* packet, ros::Publisher ros_publisher)
{
  std_msgs::Float32MultiArray msg;
  //Clear array
	msg.data.clear();
  msg.data = packet->currents;

  ros_publisher.publish(msg);
}

///// Science

void handle_measures(uint8_t sender_id, Science_MeasurePacket* packet, ros::Publisher ros_publisher)
{
  std_msgs::Float32 msg;
  msg.data = packet->mass;

  ros_publisher.publish(msg);
}

///// General

void handle_ping(uint8_t sender_id, PingPacket* packet, ros::Publisher ros_publisher)
{
  ////// USE time msg
}

void handle_request(uint8_t sender_id, RequestPacket* packet, ros::Publisher ros_publisher)
{

}

void handle_response(uint8_t sender_id, ResponsePacket* packet, ros::Publisher ros_publisher)
{

}

void handle_progress(uint8_t sender_id, ProgressPacket* packet, ros::Publisher ros_publisher)
{

}

void handle_error(uint8_t sender_id, ErrorPacket* packet, ros::Publisher ros_publisher)
{

}
