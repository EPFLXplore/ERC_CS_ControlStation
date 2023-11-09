// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avionics_interfaces:msg/GyroConfigResponse.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__GYRO_CONFIG_RESPONSE__STRUCT_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__GYRO_CONFIG_RESPONSE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__avionics_interfaces__msg__GyroConfigResponse __attribute__((deprecated))
#else
# define DEPRECATED__avionics_interfaces__msg__GyroConfigResponse __declspec(deprecated)
#endif

namespace avionics_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct GyroConfigResponse_
{
  using Type = GyroConfigResponse_<ContainerAllocator>;

  explicit GyroConfigResponse_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
      std::fill<typename std::array<float, 3>::iterator, float>(this->bias.begin(), this->bias.end(), 0.0f);
      this->remote_command = false;
      this->set_bias = false;
      this->success = false;
    }
  }

  explicit GyroConfigResponse_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : bias(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
      std::fill<typename std::array<float, 3>::iterator, float>(this->bias.begin(), this->bias.end(), 0.0f);
      this->remote_command = false;
      this->set_bias = false;
      this->success = false;
    }
  }

  // field types and members
  using _id_type =
    uint16_t;
  _id_type id;
  using _bias_type =
    std::array<float, 3>;
  _bias_type bias;
  using _remote_command_type =
    bool;
  _remote_command_type remote_command;
  using _set_bias_type =
    bool;
  _set_bias_type set_bias;
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__id(
    const uint16_t & _arg)
  {
    this->id = _arg;
    return *this;
  }
  Type & set__bias(
    const std::array<float, 3> & _arg)
  {
    this->bias = _arg;
    return *this;
  }
  Type & set__remote_command(
    const bool & _arg)
  {
    this->remote_command = _arg;
    return *this;
  }
  Type & set__set_bias(
    const bool & _arg)
  {
    this->set_bias = _arg;
    return *this;
  }
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    avionics_interfaces::msg::GyroConfigResponse_<ContainerAllocator> *;
  using ConstRawPtr =
    const avionics_interfaces::msg::GyroConfigResponse_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avionics_interfaces::msg::GyroConfigResponse_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avionics_interfaces::msg::GyroConfigResponse_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::GyroConfigResponse_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::GyroConfigResponse_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::GyroConfigResponse_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::GyroConfigResponse_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avionics_interfaces::msg::GyroConfigResponse_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avionics_interfaces::msg::GyroConfigResponse_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avionics_interfaces__msg__GyroConfigResponse
    std::shared_ptr<avionics_interfaces::msg::GyroConfigResponse_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avionics_interfaces__msg__GyroConfigResponse
    std::shared_ptr<avionics_interfaces::msg::GyroConfigResponse_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GyroConfigResponse_ & other) const
  {
    if (this->id != other.id) {
      return false;
    }
    if (this->bias != other.bias) {
      return false;
    }
    if (this->remote_command != other.remote_command) {
      return false;
    }
    if (this->set_bias != other.set_bias) {
      return false;
    }
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const GyroConfigResponse_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GyroConfigResponse_

// alias to use template instance with default allocator
using GyroConfigResponse =
  avionics_interfaces::msg::GyroConfigResponse_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__GYRO_CONFIG_RESPONSE__STRUCT_HPP_
