// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/MassCalibScale.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MASS_CALIB_SCALE__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__MASS_CALIB_SCALE__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/mass_calib_scale__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_MassCalibScale_expected_weight
{
public:
  explicit Init_MassCalibScale_expected_weight(::avionics_interfaces::msg::MassCalibScale & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::MassCalibScale expected_weight(::avionics_interfaces::msg::MassCalibScale::_expected_weight_type arg)
  {
    msg_.expected_weight = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::MassCalibScale msg_;
};

class Init_MassCalibScale_channel
{
public:
  explicit Init_MassCalibScale_channel(::avionics_interfaces::msg::MassCalibScale & msg)
  : msg_(msg)
  {}
  Init_MassCalibScale_expected_weight channel(::avionics_interfaces::msg::MassCalibScale::_channel_type arg)
  {
    msg_.channel = std::move(arg);
    return Init_MassCalibScale_expected_weight(msg_);
  }

private:
  ::avionics_interfaces::msg::MassCalibScale msg_;
};

class Init_MassCalibScale_destination_id
{
public:
  Init_MassCalibScale_destination_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MassCalibScale_channel destination_id(::avionics_interfaces::msg::MassCalibScale::_destination_id_type arg)
  {
    msg_.destination_id = std::move(arg);
    return Init_MassCalibScale_channel(msg_);
  }

private:
  ::avionics_interfaces::msg::MassCalibScale msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::MassCalibScale>()
{
  return avionics_interfaces::msg::builder::Init_MassCalibScale_destination_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MASS_CALIB_SCALE__BUILDER_HPP_
