// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avionics_interfaces:msg/MassArray.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__MASS_ARRAY__STRUCT_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__MASS_ARRAY__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__avionics_interfaces__msg__MassArray __attribute__((deprecated))
#else
# define DEPRECATED__avionics_interfaces__msg__MassArray __declspec(deprecated)
#endif

namespace avionics_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct MassArray_
{
  using Type = MassArray_<ContainerAllocator>;

  explicit MassArray_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
      std::fill<typename std::array<float, 4>::iterator, float>(this->mass.begin(), this->mass.end(), 0.0f);
    }
  }

  explicit MassArray_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : mass(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
      std::fill<typename std::array<float, 4>::iterator, float>(this->mass.begin(), this->mass.end(), 0.0f);
    }
  }

  // field types and members
  using _id_type =
    uint16_t;
  _id_type id;
  using _mass_type =
    std::array<float, 4>;
  _mass_type mass;

  // setters for named parameter idiom
  Type & set__id(
    const uint16_t & _arg)
  {
    this->id = _arg;
    return *this;
  }
  Type & set__mass(
    const std::array<float, 4> & _arg)
  {
    this->mass = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    avionics_interfaces::msg::MassArray_<ContainerAllocator> *;
  using ConstRawPtr =
    const avionics_interfaces::msg::MassArray_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avionics_interfaces::msg::MassArray_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avionics_interfaces::msg::MassArray_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::MassArray_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::MassArray_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::MassArray_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::MassArray_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avionics_interfaces::msg::MassArray_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avionics_interfaces::msg::MassArray_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avionics_interfaces__msg__MassArray
    std::shared_ptr<avionics_interfaces::msg::MassArray_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avionics_interfaces__msg__MassArray
    std::shared_ptr<avionics_interfaces::msg::MassArray_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MassArray_ & other) const
  {
    if (this->id != other.id) {
      return false;
    }
    if (this->mass != other.mass) {
      return false;
    }
    return true;
  }
  bool operator!=(const MassArray_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MassArray_

// alias to use template instance with default allocator
using MassArray =
  avionics_interfaces::msg::MassArray_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__MASS_ARRAY__STRUCT_HPP_
