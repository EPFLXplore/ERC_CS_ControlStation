// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/ServoResponse.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__SERVO_RESPONSE__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__SERVO_RESPONSE__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/servo_response__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_ServoResponse_success
{
public:
  explicit Init_ServoResponse_success(::avionics_interfaces::msg::ServoResponse & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::ServoResponse success(::avionics_interfaces::msg::ServoResponse::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoResponse msg_;
};

class Init_ServoResponse_angle
{
public:
  explicit Init_ServoResponse_angle(::avionics_interfaces::msg::ServoResponse & msg)
  : msg_(msg)
  {}
  Init_ServoResponse_success angle(::avionics_interfaces::msg::ServoResponse::_angle_type arg)
  {
    msg_.angle = std::move(arg);
    return Init_ServoResponse_success(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoResponse msg_;
};

class Init_ServoResponse_channel
{
public:
  explicit Init_ServoResponse_channel(::avionics_interfaces::msg::ServoResponse & msg)
  : msg_(msg)
  {}
  Init_ServoResponse_angle channel(::avionics_interfaces::msg::ServoResponse::_channel_type arg)
  {
    msg_.channel = std::move(arg);
    return Init_ServoResponse_angle(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoResponse msg_;
};

class Init_ServoResponse_id
{
public:
  Init_ServoResponse_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ServoResponse_channel id(::avionics_interfaces::msg::ServoResponse::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_ServoResponse_channel(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoResponse msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::ServoResponse>()
{
  return avionics_interfaces::msg::builder::Init_ServoResponse_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__SERVO_RESPONSE__BUILDER_HPP_
