// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/Voltage.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__VOLTAGE__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__VOLTAGE__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/voltage__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_Voltage_voltage
{
public:
  explicit Init_Voltage_voltage(::avionics_interfaces::msg::Voltage & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::Voltage voltage(::avionics_interfaces::msg::Voltage::_voltage_type arg)
  {
    msg_.voltage = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::Voltage msg_;
};

class Init_Voltage_id
{
public:
  Init_Voltage_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Voltage_voltage id(::avionics_interfaces::msg::Voltage::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_Voltage_voltage(msg_);
  }

private:
  ::avionics_interfaces::msg::Voltage msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::Voltage>()
{
  return avionics_interfaces::msg::builder::Init_Voltage_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__VOLTAGE__BUILDER_HPP_
