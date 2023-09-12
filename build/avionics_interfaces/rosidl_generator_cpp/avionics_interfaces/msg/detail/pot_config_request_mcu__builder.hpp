// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/PotConfigRequestMCU.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__POT_CONFIG_REQUEST_MCU__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__POT_CONFIG_REQUEST_MCU__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/pot_config_request_mcu__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_PotConfigRequestMCU_req_channels_status
{
public:
  explicit Init_PotConfigRequestMCU_req_channels_status(::avionics_interfaces::msg::PotConfigRequestMCU & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::PotConfigRequestMCU req_channels_status(::avionics_interfaces::msg::PotConfigRequestMCU::_req_channels_status_type arg)
  {
    msg_.req_channels_status = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::PotConfigRequestMCU msg_;
};

class Init_PotConfigRequestMCU_req_max_angles
{
public:
  explicit Init_PotConfigRequestMCU_req_max_angles(::avionics_interfaces::msg::PotConfigRequestMCU & msg)
  : msg_(msg)
  {}
  Init_PotConfigRequestMCU_req_channels_status req_max_angles(::avionics_interfaces::msg::PotConfigRequestMCU::_req_max_angles_type arg)
  {
    msg_.req_max_angles = std::move(arg);
    return Init_PotConfigRequestMCU_req_channels_status(msg_);
  }

private:
  ::avionics_interfaces::msg::PotConfigRequestMCU msg_;
};

class Init_PotConfigRequestMCU_req_min_angles
{
public:
  explicit Init_PotConfigRequestMCU_req_min_angles(::avionics_interfaces::msg::PotConfigRequestMCU & msg)
  : msg_(msg)
  {}
  Init_PotConfigRequestMCU_req_max_angles req_min_angles(::avionics_interfaces::msg::PotConfigRequestMCU::_req_min_angles_type arg)
  {
    msg_.req_min_angles = std::move(arg);
    return Init_PotConfigRequestMCU_req_max_angles(msg_);
  }

private:
  ::avionics_interfaces::msg::PotConfigRequestMCU msg_;
};

class Init_PotConfigRequestMCU_req_max_voltages
{
public:
  explicit Init_PotConfigRequestMCU_req_max_voltages(::avionics_interfaces::msg::PotConfigRequestMCU & msg)
  : msg_(msg)
  {}
  Init_PotConfigRequestMCU_req_min_angles req_max_voltages(::avionics_interfaces::msg::PotConfigRequestMCU::_req_max_voltages_type arg)
  {
    msg_.req_max_voltages = std::move(arg);
    return Init_PotConfigRequestMCU_req_min_angles(msg_);
  }

private:
  ::avionics_interfaces::msg::PotConfigRequestMCU msg_;
};

class Init_PotConfigRequestMCU_req_min_voltages
{
public:
  explicit Init_PotConfigRequestMCU_req_min_voltages(::avionics_interfaces::msg::PotConfigRequestMCU & msg)
  : msg_(msg)
  {}
  Init_PotConfigRequestMCU_req_max_voltages req_min_voltages(::avionics_interfaces::msg::PotConfigRequestMCU::_req_min_voltages_type arg)
  {
    msg_.req_min_voltages = std::move(arg);
    return Init_PotConfigRequestMCU_req_max_voltages(msg_);
  }

private:
  ::avionics_interfaces::msg::PotConfigRequestMCU msg_;
};

class Init_PotConfigRequestMCU_id
{
public:
  Init_PotConfigRequestMCU_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PotConfigRequestMCU_req_min_voltages id(::avionics_interfaces::msg::PotConfigRequestMCU::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_PotConfigRequestMCU_req_min_voltages(msg_);
  }

private:
  ::avionics_interfaces::msg::PotConfigRequestMCU msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::PotConfigRequestMCU>()
{
  return avionics_interfaces::msg::builder::Init_PotConfigRequestMCU_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__POT_CONFIG_REQUEST_MCU__BUILDER_HPP_
