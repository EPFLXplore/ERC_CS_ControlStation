// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/SpectroResponse.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__SPECTRO_RESPONSE__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__SPECTRO_RESPONSE__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/spectro_response__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_SpectroResponse_success
{
public:
  explicit Init_SpectroResponse_success(::avionics_interfaces::msg::SpectroResponse & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::SpectroResponse success(::avionics_interfaces::msg::SpectroResponse::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::SpectroResponse msg_;
};

class Init_SpectroResponse_data
{
public:
  explicit Init_SpectroResponse_data(::avionics_interfaces::msg::SpectroResponse & msg)
  : msg_(msg)
  {}
  Init_SpectroResponse_success data(::avionics_interfaces::msg::SpectroResponse::_data_type arg)
  {
    msg_.data = std::move(arg);
    return Init_SpectroResponse_success(msg_);
  }

private:
  ::avionics_interfaces::msg::SpectroResponse msg_;
};

class Init_SpectroResponse_id
{
public:
  Init_SpectroResponse_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SpectroResponse_data id(::avionics_interfaces::msg::SpectroResponse::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_SpectroResponse_data(msg_);
  }

private:
  ::avionics_interfaces::msg::SpectroResponse msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::SpectroResponse>()
{
  return avionics_interfaces::msg::builder::Init_SpectroResponse_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__SPECTRO_RESPONSE__BUILDER_HPP_
