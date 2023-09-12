// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/AccelConfigRequestMCU.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__ACCEL_CONFIG_REQUEST_MCU__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__ACCEL_CONFIG_REQUEST_MCU__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/accel_config_request_mcu__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_AccelConfigRequestMCU_req_transform
{
public:
  explicit Init_AccelConfigRequestMCU_req_transform(::avionics_interfaces::msg::AccelConfigRequestMCU & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::AccelConfigRequestMCU req_transform(::avionics_interfaces::msg::AccelConfigRequestMCU::_req_transform_type arg)
  {
    msg_.req_transform = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::AccelConfigRequestMCU msg_;
};

class Init_AccelConfigRequestMCU_req_bias
{
public:
  explicit Init_AccelConfigRequestMCU_req_bias(::avionics_interfaces::msg::AccelConfigRequestMCU & msg)
  : msg_(msg)
  {}
  Init_AccelConfigRequestMCU_req_transform req_bias(::avionics_interfaces::msg::AccelConfigRequestMCU::_req_bias_type arg)
  {
    msg_.req_bias = std::move(arg);
    return Init_AccelConfigRequestMCU_req_transform(msg_);
  }

private:
  ::avionics_interfaces::msg::AccelConfigRequestMCU msg_;
};

class Init_AccelConfigRequestMCU_id
{
public:
  Init_AccelConfigRequestMCU_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_AccelConfigRequestMCU_req_bias id(::avionics_interfaces::msg::AccelConfigRequestMCU::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_AccelConfigRequestMCU_req_bias(msg_);
  }

private:
  ::avionics_interfaces::msg::AccelConfigRequestMCU msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::AccelConfigRequestMCU>()
{
  return avionics_interfaces::msg::builder::Init_AccelConfigRequestMCU_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__ACCEL_CONFIG_REQUEST_MCU__BUILDER_HPP_
