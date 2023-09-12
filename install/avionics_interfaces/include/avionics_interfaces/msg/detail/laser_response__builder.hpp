// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/LaserResponse.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__LASER_RESPONSE__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__LASER_RESPONSE__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/laser_response__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_LaserResponse_success
{
public:
  explicit Init_LaserResponse_success(::avionics_interfaces::msg::LaserResponse & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::LaserResponse success(::avionics_interfaces::msg::LaserResponse::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::LaserResponse msg_;
};

class Init_LaserResponse_id
{
public:
  Init_LaserResponse_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LaserResponse_success id(::avionics_interfaces::msg::LaserResponse::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_LaserResponse_success(msg_);
  }

private:
  ::avionics_interfaces::msg::LaserResponse msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::LaserResponse>()
{
  return avionics_interfaces::msg::builder::Init_LaserResponse_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__LASER_RESPONSE__BUILDER_HPP_
