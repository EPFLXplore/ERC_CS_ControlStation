// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/MassCalibOffset.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MASS_CALIB_OFFSET__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__MASS_CALIB_OFFSET__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/mass_calib_offset__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_MassCalibOffset_channel
{
public:
  explicit Init_MassCalibOffset_channel(::avionics_interfaces::msg::MassCalibOffset & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::MassCalibOffset channel(::avionics_interfaces::msg::MassCalibOffset::_channel_type arg)
  {
    msg_.channel = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::MassCalibOffset msg_;
};

class Init_MassCalibOffset_destination_id
{
public:
  Init_MassCalibOffset_destination_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MassCalibOffset_channel destination_id(::avionics_interfaces::msg::MassCalibOffset::_destination_id_type arg)
  {
    msg_.destination_id = std::move(arg);
    return Init_MassCalibOffset_channel(msg_);
  }

private:
  ::avionics_interfaces::msg::MassCalibOffset msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::MassCalibOffset>()
{
  return avionics_interfaces::msg::builder::Init_MassCalibOffset_destination_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MASS_CALIB_OFFSET__BUILDER_HPP_
