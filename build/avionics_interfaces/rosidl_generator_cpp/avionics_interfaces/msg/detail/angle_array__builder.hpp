// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/AngleArray.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__ANGLE_ARRAY__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__ANGLE_ARRAY__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/angle_array__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_AngleArray_angles
{
public:
  explicit Init_AngleArray_angles(::avionics_interfaces::msg::AngleArray & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::AngleArray angles(::avionics_interfaces::msg::AngleArray::_angles_type arg)
  {
    msg_.angles = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::AngleArray msg_;
};

class Init_AngleArray_id
{
public:
  Init_AngleArray_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AngleArray_angles id(::avionics_interfaces::msg::AngleArray::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_AngleArray_angles(msg_);
  }

private:
  ::avionics_interfaces::msg::AngleArray msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::AngleArray>()
{
  return avionics_interfaces::msg::builder::Init_AngleArray_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__ANGLE_ARRAY__BUILDER_HPP_
