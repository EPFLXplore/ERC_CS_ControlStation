// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/SpectroRequest.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__SPECTRO_REQUEST__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__SPECTRO_REQUEST__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/spectro_request__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_SpectroRequest_measure
{
public:
  explicit Init_SpectroRequest_measure(::avionics_interfaces::msg::SpectroRequest & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::SpectroRequest measure(::avionics_interfaces::msg::SpectroRequest::_measure_type arg)
  {
    msg_.measure = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::SpectroRequest msg_;
};

class Init_SpectroRequest_destination_id
{
public:
  Init_SpectroRequest_destination_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SpectroRequest_measure destination_id(::avionics_interfaces::msg::SpectroRequest::_destination_id_type arg)
  {
    msg_.destination_id = std::move(arg);
    return Init_SpectroRequest_measure(msg_);
  }

private:
  ::avionics_interfaces::msg::SpectroRequest msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::SpectroRequest>()
{
  return avionics_interfaces::msg::builder::Init_SpectroRequest_destination_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__SPECTRO_REQUEST__BUILDER_HPP_
