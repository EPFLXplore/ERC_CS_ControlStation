// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from avionics_interfaces:msg/NPK.idl
// generated code does not contain a copyright notice

#ifndef AVIONICS_INTERFACES__MSG__DETAIL__NPK__STRUCT_HPP_
#define AVIONICS_INTERFACES__MSG__DETAIL__NPK__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__avionics_interfaces__msg__NPK __attribute__((deprecated))
#else
# define DEPRECATED__avionics_interfaces__msg__NPK __declspec(deprecated)
#endif

namespace avionics_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct NPK_
{
  using Type = NPK_<ContainerAllocator>;

  explicit NPK_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
      this->nitrogen = 0;
      this->phosphorus = 0;
      this->potassium = 0;
    }
  }

  explicit NPK_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id = 0;
      this->nitrogen = 0;
      this->phosphorus = 0;
      this->potassium = 0;
    }
  }

  // field types and members
  using _id_type =
    uint16_t;
  _id_type id;
  using _nitrogen_type =
    uint16_t;
  _nitrogen_type nitrogen;
  using _phosphorus_type =
    uint16_t;
  _phosphorus_type phosphorus;
  using _potassium_type =
    uint16_t;
  _potassium_type potassium;

  // setters for named parameter idiom
  Type & set__id(
    const uint16_t & _arg)
  {
    this->id = _arg;
    return *this;
  }
  Type & set__nitrogen(
    const uint16_t & _arg)
  {
    this->nitrogen = _arg;
    return *this;
  }
  Type & set__phosphorus(
    const uint16_t & _arg)
  {
    this->phosphorus = _arg;
    return *this;
  }
  Type & set__potassium(
    const uint16_t & _arg)
  {
    this->potassium = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    avionics_interfaces::msg::NPK_<ContainerAllocator> *;
  using ConstRawPtr =
    const avionics_interfaces::msg::NPK_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<avionics_interfaces::msg::NPK_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<avionics_interfaces::msg::NPK_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::NPK_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::NPK_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      avionics_interfaces::msg::NPK_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<avionics_interfaces::msg::NPK_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<avionics_interfaces::msg::NPK_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<avionics_interfaces::msg::NPK_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__avionics_interfaces__msg__NPK
    std::shared_ptr<avionics_interfaces::msg::NPK_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__avionics_interfaces__msg__NPK
    std::shared_ptr<avionics_interfaces::msg::NPK_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const NPK_ & other) const
  {
    if (this->id != other.id) {
      return false;
    }
    if (this->nitrogen != other.nitrogen) {
      return false;
    }
    if (this->phosphorus != other.phosphorus) {
      return false;
    }
    if (this->potassium != other.potassium) {
      return false;
    }
    return true;
  }
  bool operator!=(const NPK_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct NPK_

// alias to use template instance with default allocator
using NPK =
  avionics_interfaces::msg::NPK_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace avionics_interfaces

#endif  // AVIONICS_INTERFACES__MSG__DETAIL__NPK__STRUCT_HPP_
