// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from avionics_interfaces:msg/ServoConfigRequestMCU.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__SERVO_CONFIG_REQUEST_MCU__BUILDER_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__SERVO_CONFIG_REQUEST_MCU__BUILDER_HPP_

#include "avionics_interfaces/msg/detail/servo_config_request_mcu__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace avionics_interfaces
{

namespace msg
{

namespace builder
{

class Init_ServoConfigRequestMCU_req_max_angles
{
public:
  explicit Init_ServoConfigRequestMCU_req_max_angles(::avionics_interfaces::msg::ServoConfigRequestMCU & msg)
  : msg_(msg)
  {}
  ::avionics_interfaces::msg::ServoConfigRequestMCU req_max_angles(::avionics_interfaces::msg::ServoConfigRequestMCU::_req_max_angles_type arg)
  {
    msg_.req_max_angles = std::move(arg);
    return std::move(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigRequestMCU msg_;
};

class Init_ServoConfigRequestMCU_req_min_angles
{
public:
  explicit Init_ServoConfigRequestMCU_req_min_angles(::avionics_interfaces::msg::ServoConfigRequestMCU & msg)
  : msg_(msg)
  {}
  Init_ServoConfigRequestMCU_req_max_angles req_min_angles(::avionics_interfaces::msg::ServoConfigRequestMCU::_req_min_angles_type arg)
  {
    msg_.req_min_angles = std::move(arg);
    return Init_ServoConfigRequestMCU_req_max_angles(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigRequestMCU msg_;
};

class Init_ServoConfigRequestMCU_req_max_duty
{
public:
  explicit Init_ServoConfigRequestMCU_req_max_duty(::avionics_interfaces::msg::ServoConfigRequestMCU & msg)
  : msg_(msg)
  {}
  Init_ServoConfigRequestMCU_req_min_angles req_max_duty(::avionics_interfaces::msg::ServoConfigRequestMCU::_req_max_duty_type arg)
  {
    msg_.req_max_duty = std::move(arg);
    return Init_ServoConfigRequestMCU_req_min_angles(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigRequestMCU msg_;
};

class Init_ServoConfigRequestMCU_req_min_duty
{
public:
  explicit Init_ServoConfigRequestMCU_req_min_duty(::avionics_interfaces::msg::ServoConfigRequestMCU & msg)
  : msg_(msg)
  {}
  Init_ServoConfigRequestMCU_req_max_duty req_min_duty(::avionics_interfaces::msg::ServoConfigRequestMCU::_req_min_duty_type arg)
  {
    msg_.req_min_duty = std::move(arg);
    return Init_ServoConfigRequestMCU_req_max_duty(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigRequestMCU msg_;
};

class Init_ServoConfigRequestMCU_id
{
public:
  Init_ServoConfigRequestMCU_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ServoConfigRequestMCU_req_min_duty id(::avionics_interfaces::msg::ServoConfigRequestMCU::_id_type arg)
  {
    msg_.id = std::move(arg);
    return Init_ServoConfigRequestMCU_req_min_duty(msg_);
  }

private:
  ::avionics_interfaces::msg::ServoConfigRequestMCU msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::avionics_interfaces::msg::ServoConfigRequestMCU>()
{
  return avionics_interfaces::msg::builder::Init_ServoConfigRequestMCU_id();
}

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__SERVO_CONFIG_REQUEST_MCU__BUILDER_HPP_
