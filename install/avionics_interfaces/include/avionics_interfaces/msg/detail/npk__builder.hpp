// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/NPK.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__NPK__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__NPK__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/npk__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_NPK_potassium
{
public:
  explicit Init_NPK_potassium(::avionics_interfaces::msg::NPK & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::NPK potassium(::avionics_interfaces::msg::NPK::_potassium_type arg)
  {
    msg_.potassium = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::NPK msg_;
};

class Init_NPK_phosphorus
{
public:
  explicit Init_NPK_phosphorus(::avionics_interfaces::msg::NPK & msg)
  : msg_(msg)
  {}
  Init_NPK_potassium phosphorus(::avionics_interfaces::msg::NPK::_phosphorus_type arg)
  {
    msg_.phosphorus = std::move(arg);
    return Init_NPK_potassium(msg_);
  }

private:
  ::avionics_interfaces::msg::NPK msg_;
};

class Init_NPK_nitrogen
{
public:
  explicit Init_NPK_nitrogen(::avionics_interfaces::msg::NPK & msg)
  : msg_(msg)
  {}
  Init_NPK_phosphorus nitrogen(::avionics_interfaces::msg::NPK::_nitrogen_type arg)
  {
    msg_.nitrogen = std::move(arg);
    return Init_NPK_phosphorus(msg_);
  }

private:
  ::avionics_interfaces::msg::NPK msg_;
};

class Init_NPK_id
{
public:
  Init_NPK_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_NPK_nitrogen id(::avionics_interfaces::msg::NPK::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_NPK_nitrogen(msg_);
  }

private:
  ::avionics_interfaces::msg::NPK msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::NPK>()
{
  return avionics_interfaces::msg::builder::Init_NPK_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__NPK__BUILDER_HPP_
