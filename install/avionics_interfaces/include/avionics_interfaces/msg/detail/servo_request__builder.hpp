// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/ServoRequest.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__SERVO_REQUEST__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__SERVO_REQUEST__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/servo_request__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_ServoRequest_angle
{
public:
  explicit Init_ServoRequest_angle(::avionics_interfaces::msg::ServoRequest & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::ServoRequest angle(::avionics_interfaces::msg::ServoRequest::_angle_type arg)
  {
    msg_.angle = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoRequest msg_;
};

class Init_ServoRequest_channel
{
public:
  explicit Init_ServoRequest_channel(::avionics_interfaces::msg::ServoRequest & msg)
  : msg_(msg)
  {}
  Init_ServoRequest_angle channel(::avionics_interfaces::msg::ServoRequest::_channel_type arg)
  {
    msg_.channel = std::move(arg);
    return Init_ServoRequest_angle(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoRequest msg_;
};

class Init_ServoRequest_destination_id
{
public:
  Init_ServoRequest_destination_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ServoRequest_channel destination_id(::avionics_interfaces::msg::ServoRequest::_destination_id_type arg)
  {
    msg_.destination_id = std::move(arg);
    return Init_ServoRequest_channel(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoRequest msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::ServoRequest>()
{
  return avionics_interfaces::msg::builder::Init_ServoRequest_destination_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__SERVO_REQUEST__BUILDER_HPP_
