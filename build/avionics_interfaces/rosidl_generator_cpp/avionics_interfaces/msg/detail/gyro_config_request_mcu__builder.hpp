// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/GyroConfigRequestMCU.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__GYRO_CONFIG_REQUEST_MCU__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__GYRO_CONFIG_REQUEST_MCU__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/gyro_config_request_mcu__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_GyroConfigRequestMCU_req_bias
{
public:
  explicit Init_GyroConfigRequestMCU_req_bias(::avionics_interfaces::msg::GyroConfigRequestMCU & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::GyroConfigRequestMCU req_bias(::avionics_interfaces::msg::GyroConfigRequestMCU::_req_bias_type arg)
  {
    msg_.req_bias = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::GyroConfigRequestMCU msg_;
};

class Init_GyroConfigRequestMCU_id
{
public:
  Init_GyroConfigRequestMCU_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GyroConfigRequestMCU_req_bias id(::avionics_interfaces::msg::GyroConfigRequestMCU::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_GyroConfigRequestMCU_req_bias(msg_);
  }

private:
  ::avionics_interfaces::msg::GyroConfigRequestMCU msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::GyroConfigRequestMCU>()
{
  return avionics_interfaces::msg::builder::Init_GyroConfigRequestMCU_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__GYRO_CONFIG_REQUEST_MCU__BUILDER_HPP_
