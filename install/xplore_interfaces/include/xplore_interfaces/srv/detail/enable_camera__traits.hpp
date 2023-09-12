// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from xplore_interfaces:srv/EnableCamera.idl
// generated code does not contain a copyright notice

#ifndef XPLORE_INTERFACES__SRV__DETAIL__ENABLE_CAMERA__TRAITS_HPP_
#define XPLORE_INTERFACES__SRV__DETAIL__ENABLE_CAMERA__TRAITS_HPP_

#include "xplore_interfaces/srv/detail/enable_camera__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<xplore_interfaces::srv::EnableCamera_Request>()
{
  return "xplore_interfaces::srv::EnableCamera_Request";
}

template<>
inline const char * name<xplore_interfaces::srv::EnableCamera_Request>()
{
  return "xplore_interfaces/srv/EnableCamera_Request";
}

template<>
struct has_fixed_size<xplore_interfaces::srv::EnableCamera_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<xplore_interfaces::srv::EnableCamera_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<xplore_interfaces::srv::EnableCamera_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<xplore_interfaces::srv::EnableCamera_Response>()
{
  return "xplore_interfaces::srv::EnableCamera_Response";
}

template<>
inline const char * name<xplore_interfaces::srv::EnableCamera_Response>()
{
  return "xplore_interfaces/srv/EnableCamera_Response";
}

template<>
struct has_fixed_size<xplore_interfaces::srv::EnableCamera_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<xplore_interfaces::srv::EnableCamera_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<xplore_interfaces::srv::EnableCamera_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<xplore_interfaces::srv::EnableCamera>()
{
  return "xplore_interfaces::srv::EnableCamera";
}

template<>
inline const char * name<xplore_interfaces::srv::EnableCamera>()
{
  return "xplore_interfaces/srv/EnableCamera";
}

template<>
struct has_fixed_size<xplore_interfaces::srv::EnableCamera>
  : std::integral_constant<
    bool,
    has_fixed_size<xplore_interfaces::srv::EnableCamera_Request>::value &&
    has_fixed_size<xplore_interfaces::srv::EnableCamera_Response>::value
  >
{
};

template<>
struct has_bounded_size<xplore_interfaces::srv::EnableCamera>
  : std::integral_constant<
    bool,
    has_bounded_size<xplore_interfaces::srv::EnableCamera_Request>::value &&
    has_bounded_size<xplore_interfaces::srv::EnableCamera_Response>::value
  >
{
};

template<>
struct is_service<xplore_interfaces::srv::EnableCamera>
  : std::true_type
{
};

template<>
struct is_service_request<xplore_interfaces::srv::EnableCamera_Request>
  : std::true_type
{
};

template<>
struct is_service_response<xplore_interfaces::srv::EnableCamera_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // XPLORE_INTERFACES__SRV__DETAIL__ENABLE_CAMERA__TRAITS_HPP_
