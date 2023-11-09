// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from avionics_interfaces:msg/Mag.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MAG__TRAITS_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__MAG__TRAITS_HPP_

#include "avionics_interfaces/msg/detail/mag__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'mag_raw'
// Member 'mag_cal'
#include "sensor_msgs/msg/detail/magnetic_field__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<avionics_interfaces::msg::Mag>()
{
  return "avionics_interfaces::msg::Mag";
}

template<>
inline const char * name<avionics_interfaces::msg::Mag>()
{
  return "avionics_interfaces/msg/Mag";
}

template<>
struct has_fixed_size<avionics_interfaces::msg::Mag>
  : std::integral_constant<bool, has_fixed_size<sensor_msgs::msg::MagneticField>::value> {};

template<>
struct has_bounded_size<avionics_interfaces::msg::Mag>
  : std::integral_constant<bool, has_bounded_size<sensor_msgs::msg::MagneticField>::value> {};

template<>
struct is_message<avionics_interfaces::msg::Mag>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MAG__TRAITS_HPP_
