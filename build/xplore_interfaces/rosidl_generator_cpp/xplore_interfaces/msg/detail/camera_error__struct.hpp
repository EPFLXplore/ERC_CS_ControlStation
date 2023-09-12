// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from xplore_interfaces:msg/CameraError.idl
// generated code does not contain a copyright notice

#ifndef XPLORE_INTERFACES__MSG__DETAIL__CAMERA_ERROR__STRUCT_HPP_
#define XPLORE_INTERFACES__MSG__DETAIL__CAMERA_ERROR__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__xplore_interfaces__msg__CameraError __attribute__((deprecated))
#else
# define DEPRECATED__xplore_interfaces__msg__CameraError __declspec(deprecated)
#endif

namespace xplore_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct CameraError_
{
  using Type = CameraError_<ContainerAllocator>;

  explicit CameraError_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->index = 0;
      this->ip_adresse = 0ll;
    }
  }

  explicit CameraError_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->index = 0;
      this->ip_adresse = 0ll;
    }
  }

  // field types and members
  using _index_type =
    int8_t;
  _index_type index;
  using _ip_adresse_type =
    int64_t;
  _ip_adresse_type ip_adresse;

  // setters for named parameter idiom
  Type & set__index(
    const int8_t & _arg)
  {
    this->index = _arg;
    return *this;
  }
  Type & set__ip_adresse(
    const int64_t & _arg)
  {
    this->ip_adresse = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    xplore_interfaces::msg::CameraError_<ContainerAllocator> *;
  using ConstRawPtr =
    const xplore_interfaces::msg::CameraError_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<xplore_interfaces::msg::CameraError_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<xplore_interfaces::msg::CameraError_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      xplore_interfaces::msg::CameraError_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<xplore_interfaces::msg::CameraError_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      xplore_interfaces::msg::CameraError_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<xplore_interfaces::msg::CameraError_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<xplore_interfaces::msg::CameraError_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<xplore_interfaces::msg::CameraError_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__xplore_interfaces__msg__CameraError
    std::shared_ptr<xplore_interfaces::msg::CameraError_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__xplore_interfaces__msg__CameraError
    std::shared_ptr<xplore_interfaces::msg::CameraError_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const CameraError_ & other) const
  {
    if (this->index != other.index) {
      return false;
    }
    if (this->ip_adresse != other.ip_adresse) {
      return false;
    }
    return true;
  }
  bool operator!=(const CameraError_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct CameraError_

// alias to use template instance with default allocator
using CameraError =
  xplore_interfaces::msg::CameraError_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace xplore_interfaces

#endif  // XPLORE_INTERFACES__MSG__DETAIL__CAMERA_ERROR__STRUCT_HPP_
