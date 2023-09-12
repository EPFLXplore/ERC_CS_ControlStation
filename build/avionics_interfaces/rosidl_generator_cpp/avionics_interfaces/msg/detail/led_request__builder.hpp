// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/LEDRequest.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__LED_REQUEST__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__LED_REQUEST__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/led_request__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_LEDRequest_state
{
public:
  explicit Init_LEDRequest_state(::avionics_interfaces::msg::LEDRequest & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::LEDRequest state(::avionics_interfaces::msg::LEDRequest::_state_type arg)
  {
    msg_.state = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::LEDRequest msg_;
};

class Init_LEDRequest_destination_id
{
public:
  Init_LEDRequest_destination_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LEDRequest_state destination_id(::avionics_interfaces::msg::LEDRequest::_destination_id_type arg)
  {
    msg_.destination_id = std::move(arg);
    return Init_LEDRequest_state(msg_);
  }

private:
  ::avionics_interfaces::msg::LEDRequest msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::LEDRequest>()
{
  return avionics_interfaces::msg::builder::Init_LEDRequest_destination_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__LED_REQUEST__BUILDER_HPP_
