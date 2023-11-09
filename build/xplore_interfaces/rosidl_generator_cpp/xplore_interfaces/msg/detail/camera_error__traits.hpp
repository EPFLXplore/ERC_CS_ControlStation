// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from xplore_interfaces:msg/CameraError.idl
// generated code does not contain a copyright notice

#ifndef XPLORE_INTERFACES__MSG__DETAIL__CAMERA_ERROR__TRAITS_HPP_
#define XPLORE_INTERFACES__MSG__DETAIL__CAMERA_ERROR__TRAITS_HPP_

#include "xplore_interfaces/msg/detail/camera_error__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<xplore_interfaces::msg::CameraError>()
{
  return "xplore_interfaces::msg::CameraError";
}

template<>
inline const char * name<xplore_interfaces::msg::CameraError>()
{
  return "xplore_interfaces/msg/CameraError";
}

template<>
struct has_fixed_size<xplore_interfaces::msg::CameraError>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<xplore_interfaces::msg::CameraError>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<xplore_interfaces::msg::CameraError>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // XPLORE_INTERFACES__MSG__DETAIL__CAMERA_ERROR__TRAITS_HPP_
