// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/MassArray.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MASS_ARRAY__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__MASS_ARRAY__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/mass_array__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_MassArray_mass
{
public:
  explicit Init_MassArray_mass(::avionics_interfaces::msg::MassArray & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::MassArray mass(::avionics_interfaces::msg::MassArray::_mass_type arg)
  {
    msg_.mass = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::MassArray msg_;
};

class Init_MassArray_id
{
public:
  Init_MassArray_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MassArray_mass id(::avionics_interfaces::msg::MassArray::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_MassArray_mass(msg_);
  }

private:
  ::avionics_interfaces::msg::MassArray msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::MassArray>()
{
  return avionics_interfaces::msg::builder::Init_MassArray_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MASS_ARRAY__BUILDER_HPP_
