// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/ImuCalib.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__IMU_CALIB__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__IMU_CALIB__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/imu_calib__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_ImuCalib_calib_offset_gyro
{
public:
  explicit Init_ImuCalib_calib_offset_gyro(::avionics_interfaces::msg::ImuCalib & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::ImuCalib calib_offset_gyro(::avionics_interfaces::msg::ImuCalib::_calib_offset_gyro_type arg)
  {
    msg_.calib_offset_gyro = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::ImuCalib msg_;
};

class Init_ImuCalib_calib_offset_accel
{
public:
  explicit Init_ImuCalib_calib_offset_accel(::avionics_interfaces::msg::ImuCalib & msg)
  : msg_(msg)
  {}
  Init_ImuCalib_calib_offset_gyro calib_offset_accel(::avionics_interfaces::msg::ImuCalib::_calib_offset_accel_type arg)
  {
    msg_.calib_offset_accel = std::move(arg);
    return Init_ImuCalib_calib_offset_gyro(msg_);
  }

private:
  ::avionics_interfaces::msg::ImuCalib msg_;
};

class Init_ImuCalib_destination_id
{
public:
  Init_ImuCalib_destination_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ImuCalib_calib_offset_accel destination_id(::avionics_interfaces::msg::ImuCalib::_destination_id_type arg)
  {
    msg_.destination_id = std::move(arg);
    return Init_ImuCalib_calib_offset_accel(msg_);
  }

private:
  ::avionics_interfaces::msg::ImuCalib msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::ImuCalib>()
{
  return avionics_interfaces::msg::builder::Init_ImuCalib_destination_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__IMU_CALIB__BUILDER_HPP_
