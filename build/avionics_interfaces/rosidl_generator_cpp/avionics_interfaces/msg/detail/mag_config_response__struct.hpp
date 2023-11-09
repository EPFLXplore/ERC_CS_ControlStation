// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avionics_interfaces:msg/MagConfigResponse.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_RESPONSE__STRUCT_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_RESPONSE__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__avionics_interfaces__msg__MagConfigResponse __attribute__((deprecated))
#else
# define DEPRECATED__avionics_interfaces__msg__MagConfigResponse __declspec(deprecated)
#endif

namespace avionics_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct MagConfigResponse_
{
  using Type = MagConfigResponse_<ContainerAllocator>;

  explicit MagConfigResponse_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
      std::fill<typename std::array<float, 3>::iterator, float>(this->hard_iron.begin(), this->hard_iron.end(), 0.0f);
      std::fill<typename std::array<float, 9>::iterator, float>(this->soft_iron.begin(), this->soft_iron.end(), 0.0f);
      this->remote_command = false;
      this->set_hard_iron = false;
      this->set_soft_iron = false;
      this->success = false;
    }
  }

  explicit MagConfigResponse_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : hard_iron(_alloc),
    soft_iron(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
      std::fill<typename std::array<float, 3>::iterator, float>(this->hard_iron.begin(), this->hard_iron.end(), 0.0f);
      std::fill<typename std::array<float, 9>::iterator, float>(this->soft_iron.begin(), this->soft_iron.end(), 0.0f);
      this->remote_command = false;
      this->set_hard_iron = false;
      this->set_soft_iron = false;
      this->success = false;
    }
  }

  // field types and members
  using _id_type =
    uint16_t;
  _id_type id;
  using _hard_iron_type =
    std::array<float, 3>;
  _hard_iron_type hard_iron;
  using _soft_iron_type =
    std::array<float, 9>;
  _soft_iron_type soft_iron;
  using _remote_command_type =
    bool;
  _remote_command_type remote_command;
  using _set_hard_iron_type =
    bool;
  _set_hard_iron_type set_hard_iron;
  using _set_soft_iron_type =
    bool;
  _set_soft_iron_type set_soft_iron;
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
  Type & set__hard_iron(
    const std::array<float, 3> & _arg)
  {
    this->hard_iron = _arg;
    return *this;
  }
  Type & set__soft_iron(
    const std::array<float, 9> & _arg)
  {
    this->soft_iron = _arg;
    return *this;
  }
  Type & set__remote_command(
    const bool & _arg)
  {
    this->remote_command = _arg;
    return *this;
  }
  Type & set__set_hard_iron(
    const bool & _arg)
  {
    this->set_hard_iron = _arg;
    return *this;
  }
  Type & set__set_soft_iron(
    const bool & _arg)
  {
    this->set_soft_iron = _arg;
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
    avionics_interfaces::msg::MagConfigResponse_<ContainerAllocator> *;
  using ConstRawPtr =
    const avionics_interfaces::msg::MagConfigResponse_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avionics_interfaces::msg::MagConfigResponse_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avionics_interfaces::msg::MagConfigResponse_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::MagConfigResponse_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::MagConfigResponse_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::MagConfigResponse_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::MagConfigResponse_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avionics_interfaces::msg::MagConfigResponse_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avionics_interfaces::msg::MagConfigResponse_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avionics_interfaces__msg__MagConfigResponse
    std::shared_ptr<avionics_interfaces::msg::MagConfigResponse_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avionics_interfaces__msg__MagConfigResponse
    std::shared_ptr<avionics_interfaces::msg::MagConfigResponse_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MagConfigResponse_ & other) const
  {
    if (this->id != other.id) {
      return false;
    }
    if (this->hard_iron != other.hard_iron) {
      return false;
    }
    if (this->soft_iron != other.soft_iron) {
      return false;
    }
    if (this->remote_command != other.remote_command) {
      return false;
    }
    if (this->set_hard_iron != other.set_hard_iron) {
      return false;
    }
    if (this->set_soft_iron != other.set_soft_iron) {
      return false;
    }
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const MagConfigResponse_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MagConfigResponse_

// alias to use template instance with default allocator
using MagConfigResponse =
  avionics_interfaces::msg::MagConfigResponse_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MAG_CONFIG_RESPONSE__STRUCT_HPP_
