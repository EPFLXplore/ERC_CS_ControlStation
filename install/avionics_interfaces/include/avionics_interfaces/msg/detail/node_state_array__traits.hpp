// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from avionics_interfaces:msg/NodeStateArray.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__NODE_STATE_ARRAY__TRAITS_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__NODE_STATE_ARRAY__TRAITS_HPP_

#include "avionics_interfaces/msg/detail/node_state_array__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<avionics_interfaces::msg::NodeStateArray>()
{
  return "avionics_interfaces::msg::NodeStateArray";
}

template<>
inline const char * name<avionics_interfaces::msg::NodeStateArray>()
{
  return "avionics_interfaces/msg/NodeStateArray";
}

template<>
struct has_fixed_size<avionics_interfaces::msg::NodeStateArray>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<avionics_interfaces::msg::NodeStateArray>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<avionics_interfaces::msg::NodeStateArray>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__NODE_STATE_ARRAY__TRAITS_HPP_
