// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/LEDResponse.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__LED_RESPONSE__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__LED_RESPONSE__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/led_response__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_LEDResponse_success
{
public:
  explicit Init_LEDResponse_success(::avionics_interfaces::msg::LEDResponse & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::LEDResponse success(::avionics_interfaces::msg::LEDResponse::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::LEDResponse msg_;
};

class Init_LEDResponse_state
{
public:
  explicit Init_LEDResponse_state(::avionics_interfaces::msg::LEDResponse & msg)
  : msg_(msg)
  {}
  Init_LEDResponse_success state(::avionics_interfaces::msg::LEDResponse::_state_type arg)
  {
    msg_.state = std::move(arg);
    return Init_LEDResponse_success(msg_);
  }

private:
  ::avionics_interfaces::msg::LEDResponse msg_;
};

class Init_LEDResponse_id
{
public:
  Init_LEDResponse_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LEDResponse_state id(::avionics_interfaces::msg::LEDResponse::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_LEDResponse_state(msg_);
  }

private:
  ::avionics_interfaces::msg::LEDResponse msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::LEDResponse>()
{
  return avionics_interfaces::msg::builder::Init_LEDResponse_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__LED_RESPONSE__BUILDER_HPP_
