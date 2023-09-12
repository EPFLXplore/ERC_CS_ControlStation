// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/Imu.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__IMU__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__IMU__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/imu__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_Imu_imu
{
public:
  explicit Init_Imu_imu(::avionics_interfaces::msg::Imu & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::Imu imu(::avionics_interfaces::msg::Imu::_imu_type arg)
  {
    msg_.imu = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::Imu msg_;
};

class Init_Imu_id
{
public:
  Init_Imu_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Imu_imu id(::avionics_interfaces::msg::Imu::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_Imu_imu(msg_);
  }

private:
  ::avionics_interfaces::msg::Imu msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::Imu>()
{
  return avionics_interfaces::msg::builder::Init_Imu_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__IMU__BUILDER_HPP_
