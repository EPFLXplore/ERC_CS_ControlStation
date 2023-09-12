// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/FourInOne.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__FOUR_IN_ONE__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__FOUR_IN_ONE__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/four_in_one__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_FourInOne_ph
{
public:
  explicit Init_FourInOne_ph(::avionics_interfaces::msg::FourInOne & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::FourInOne ph(::avionics_interfaces::msg::FourInOne::_ph_type arg)
  {
    msg_.ph = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::FourInOne msg_;
};

class Init_FourInOne_conductivity
{
public:
  explicit Init_FourInOne_conductivity(::avionics_interfaces::msg::FourInOne & msg)
  : msg_(msg)
  {}
  Init_FourInOne_ph conductivity(::avionics_interfaces::msg::FourInOne::_conductivity_type arg)
  {
    msg_.conductivity = std::move(arg);
    return Init_FourInOne_ph(msg_);
  }

private:
  ::avionics_interfaces::msg::FourInOne msg_;
};

class Init_FourInOne_moisture
{
public:
  explicit Init_FourInOne_moisture(::avionics_interfaces::msg::FourInOne & msg)
  : msg_(msg)
  {}
  Init_FourInOne_conductivity moisture(::avionics_interfaces::msg::FourInOne::_moisture_type arg)
  {
    msg_.moisture = std::move(arg);
    return Init_FourInOne_conductivity(msg_);
  }

private:
  ::avionics_interfaces::msg::FourInOne msg_;
};

class Init_FourInOne_temperature
{
public:
  explicit Init_FourInOne_temperature(::avionics_interfaces::msg::FourInOne & msg)
  : msg_(msg)
  {}
  Init_FourInOne_moisture temperature(::avionics_interfaces::msg::FourInOne::_temperature_type arg)
  {
    msg_.temperature = std::move(arg);
    return Init_FourInOne_moisture(msg_);
  }

private:
  ::avionics_interfaces::msg::FourInOne msg_;
};

class Init_FourInOne_id
{
public:
  Init_FourInOne_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_FourInOne_temperature id(::avionics_interfaces::msg::FourInOne::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_FourInOne_temperature(msg_);
  }

private:
  ::avionics_interfaces::msg::FourInOne msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::FourInOne>()
{
  return avionics_interfaces::msg::builder::Init_FourInOne_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__FOUR_IN_ONE__BUILDER_HPP_
