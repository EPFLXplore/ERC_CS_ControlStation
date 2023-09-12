// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/Mag.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MAG__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__MAG__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/mag__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_Mag_mag_cal
{
public:
  explicit Init_Mag_mag_cal(::avionics_interfaces::msg::Mag & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::Mag mag_cal(::avionics_interfaces::msg::Mag::_mag_cal_type arg)
  {
    msg_.mag_cal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::Mag msg_;
};

class Init_Mag_mag_raw
{
public:
  explicit Init_Mag_mag_raw(::avionics_interfaces::msg::Mag & msg)
  : msg_(msg)
  {}
  Init_Mag_mag_cal mag_raw(::avionics_interfaces::msg::Mag::_mag_raw_type arg)
  {
    msg_.mag_raw = std::move(arg);
    return Init_Mag_mag_cal(msg_);
  }

private:
  ::avionics_interfaces::msg::Mag msg_;
};

class Init_Mag_id
{
public:
  Init_Mag_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Mag_mag_raw id(::avionics_interfaces::msg::Mag::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_Mag_mag_raw(msg_);
  }

private:
  ::avionics_interfaces::msg::Mag msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::Mag>()
{
  return avionics_interfaces::msg::builder::Init_Mag_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MAG__BUILDER_HPP_
