// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avionics_interfaces:msg/SpectroRequest.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__SPECTRO_REQUEST__STRUCT_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__SPECTRO_REQUEST__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__avionics_interfaces__msg__SpectroRequest __attribute__((deprecated))
#else
# define DEPRECATED__avionics_interfaces__msg__SpectroRequest __declspec(deprecated)
#endif

namespace avionics_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct SpectroRequest_
{
  using Type = SpectroRequest_<ContainerAllocator>;

  explicit SpectroRequest_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->destination_id = 0;
      this->measure = false;
    }
  }

  explicit SpectroRequest_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->destination_id = 0;
      this->measure = false;
    }
  }

  // field types and members
  using _destination_id_type =
    uint16_t;
  _destination_id_type destination_id;
  using _measure_type =
    bool;
  _measure_type measure;

  // setters for named parameter idiom
  Type & set__destination_id(
    const uint16_t & _arg)
  {
    this->destination_id = _arg;
    return *this;
  }
  Type & set__measure(
    const bool & _arg)
  {
    this->measure = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    avionics_interfaces::msg::SpectroRequest_<ContainerAllocator> *;
  using ConstRawPtr =
    const avionics_interfaces::msg::SpectroRequest_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avionics_interfaces::msg::SpectroRequest_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avionics_interfaces::msg::SpectroRequest_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::SpectroRequest_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::SpectroRequest_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::SpectroRequest_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::SpectroRequest_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avionics_interfaces::msg::SpectroRequest_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avionics_interfaces::msg::SpectroRequest_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avionics_interfaces__msg__SpectroRequest
    std::shared_ptr<avionics_interfaces::msg::SpectroRequest_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avionics_interfaces__msg__SpectroRequest
    std::shared_ptr<avionics_interfaces::msg::SpectroRequest_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SpectroRequest_ & other) const
  {
    if (this->destination_id != other.destination_id) {
      return false;
    }
    if (this->measure != other.measure) {
      return false;
    }
    return true;
  }
  bool operator!=(const SpectroRequest_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SpectroRequest_

// alias to use template instance with default allocator
using SpectroRequest =
  avionics_interfaces::msg::SpectroRequest_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__SPECTRO_REQUEST__STRUCT_HPP_
