// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/LaserRequest.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__LASER_REQUEST__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__LASER_REQUEST__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/laser_request__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_LaserRequest_enable
{
public:
  explicit Init_LaserRequest_enable(::avionics_interfaces::msg::LaserRequest & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::LaserRequest enable(::avionics_interfaces::msg::LaserRequest::_enable_type arg)
  {
    msg_.enable = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::LaserRequest msg_;
};

class Init_LaserRequest_destination_id
{
public:
  Init_LaserRequest_destination_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LaserRequest_enable destination_id(::avionics_interfaces::msg::LaserRequest::_destination_id_type arg)
  {
    msg_.destination_id = std::move(arg);
    return Init_LaserRequest_enable(msg_);
  }

private:
  ::avionics_interfaces::msg::LaserRequest msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::LaserRequest>()
{
  return avionics_interfaces::msg::builder::Init_LaserRequest_destination_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__LASER_REQUEST__BUILDER_HPP_
