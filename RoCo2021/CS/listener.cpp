#include "ros/ros.h"
#include "std_msgs/String.h"

/**
 * This tutorial demonstrates simple receipt of messages over the ROS system.
 */
void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("I heard: [%s]", msg->data.c_str());
}

int main(int argc, char **argv)
{
  // call of init needed before anything else, "" is the name of the node
  ros::init(argc, argv, "listener");

  // main access point to communications with ROS system
  // NodeHandle initializes this node
  ros::NodeHandle n;

  // subscribe() function indicates to ROS we are subscribing to topic "chatter"
  // returns a Subscriber object needed until we want to unsubscribe. The second
  // parameter is the message queue, number indicates how many messages to
  // buffer up before throwing some away
  // Messages are passed to a callback function "chatterCallback"
  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);

  /**
   * ros::spin() will enter a loop, pumping callbacks.  With this version, all
   * callbacks will be called from within this thread (the main one).  ros::spin()
   * will exit when Ctrl-C is pressed, or the node is shutdown by the master.
   */
  // enters a loop. All callbacks called within this thread. Exits with Ctrl-C.
  ros::spin();

  return 0;
}
