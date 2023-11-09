// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from avionics_interfaces:msg/ServoConfigResponse.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__SERVO_CONFIG_RESPONSE__TRAITS_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__SERVO_CONFIG_RESPONSE__TRAITS_HPP_

#include "avionics_interfaces/msg/detail/servo_config_response__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<avionics_interfaces::msg::ServoConfigResponse>()
{
  return "avionics_interfaces::msg::ServoConfigResponse";
}

template<>
inline const char * name<avionics_interfaces::msg::ServoConfigResponse>()
{
  return "avionics_interfaces/msg/ServoConfigResponse";
}

template<>
struct has_fixed_size<avionics_interfaces::msg::ServoConfigResponse>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<avionics_interfaces::msg::ServoConfigResponse>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<avionics_interfaces::msg::ServoConfigResponse>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__SERVO_CONFIG_RESPONSE__TRAITS_HPP_
