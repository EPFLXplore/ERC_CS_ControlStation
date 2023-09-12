// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avionics_interfaces:msg/AccelConfigRequestMCU.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__ACCEL_CONFIG_REQUEST_MCU__STRUCT_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__ACCEL_CONFIG_REQUEST_MCU__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__avionics_interfaces__msg__AccelConfigRequestMCU __attribute__((deprecated))
#else
# define DEPRECATED__avionics_interfaces__msg__AccelConfigRequestMCU __declspec(deprecated)
#endif

namespace avionics_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct AccelConfigRequestMCU_
{
  using Type = AccelConfigRequestMCU_<ContainerAllocator>;

  explicit AccelConfigRequestMCU_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
      this->req_bias = false;
      this->req_transform = false;
    }
  }

  explicit AccelConfigRequestMCU_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
      this->req_bias = false;
      this->req_transform = false;
    }
  }

  // field types and members
  using _id_type =
    uint16_t;
  _id_type id;
  using _req_bias_type =
    bool;
  _req_bias_type req_bias;
  using _req_transform_type =
    bool;
  _req_transform_type req_transform;

  // setters for named parameter idiom
  Type & set__id(
    const uint16_t & _arg)
  {
    this->id = _arg;
    return *this;
  }
  Type & set__req_bias(
    const bool & _arg)
  {
    this->req_bias = _arg;
    return *this;
  }
  Type & set__req_transform(
    const bool & _arg)
  {
    this->req_transform = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    avionics_interfaces::msg::AccelConfigRequestMCU_<ContainerAllocator> *;
  using ConstRawPtr =
    const avionics_interfaces::msg::AccelConfigRequestMCU_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avionics_interfaces::msg::AccelConfigRequestMCU_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avionics_interfaces::msg::AccelConfigRequestMCU_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::AccelConfigRequestMCU_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::AccelConfigRequestMCU_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::AccelConfigRequestMCU_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::AccelConfigRequestMCU_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avionics_interfaces::msg::AccelConfigRequestMCU_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avionics_interfaces::msg::AccelConfigRequestMCU_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avionics_interfaces__msg__AccelConfigRequestMCU
    std::shared_ptr<avionics_interfaces::msg::AccelConfigRequestMCU_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avionics_interfaces__msg__AccelConfigRequestMCU
    std::shared_ptr<avionics_interfaces::msg::AccelConfigRequestMCU_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AccelConfigRequestMCU_ & other) const
  {
    if (this->id != other.id) {
      return false;
    }
    if (this->req_bias != other.req_bias) {
      return false;
    }
    if (this->req_transform != other.req_transform) {
      return false;
    }
    return true;
  }
  bool operator!=(const AccelConfigRequestMCU_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AccelConfigRequestMCU_

// alias to use template instance with default allocator
using AccelConfigRequestMCU =
  avionics_interfaces::msg::AccelConfigRequestMCU_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__ACCEL_CONFIG_REQUEST_MCU__STRUCT_HPP_
