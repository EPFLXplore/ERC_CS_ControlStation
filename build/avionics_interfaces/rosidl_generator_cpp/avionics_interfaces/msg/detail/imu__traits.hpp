// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from avionics_interfaces:msg/Imu.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__IMU__TRAITS_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__IMU__TRAITS_HPP_

#include "avionics_interfaces/msg/detail/imu__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'imu'
#include "sensor_msgs/msg/detail/imu__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<avionics_interfaces::msg::Imu>()
{
  return "avionics_interfaces::msg::Imu";
}

template<>
inline const char * name<avionics_interfaces::msg::Imu>()
{
  return "avionics_interfaces/msg/Imu";
}

template<>
struct has_fixed_size<avionics_interfaces::msg::Imu>
  : std::integral_constant<bool, has_fixed_size<sensor_msgs::msg::Imu>::value> {};

template<>
struct has_bounded_size<avionics_interfaces::msg::Imu>
  : std::integral_constant<bool, has_bounded_size<sensor_msgs::msg::Imu>::value> {};

template<>
struct is_message<avionics_interfaces::msg::Imu>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__IMU__TRAITS_HPP_
