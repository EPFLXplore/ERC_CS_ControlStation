// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from xplore_interfaces:srv/EnableCamera.idl
// generated code does not contain a copyright notice

#ifndef XPLORE_INTERFACES__SRV__DETAIL__ENABLE_CAMERA__STRUCT_HPP_
#define XPLORE_INTERFACES__SRV__DETAIL__ENABLE_CAMERA__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__xplore_interfaces__srv__EnableCamera_Request __attribute__((deprecated))
#else
# define DEPRECATED__xplore_interfaces__srv__EnableCamera_Request __declspec(deprecated)
#endif

namespace xplore_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct EnableCamera_Request_
{
  using Type = EnableCamera_Request_<ContainerAllocator>;

  explicit EnableCamera_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->index = 0;
    }
  }

  explicit EnableCamera_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->index = 0;
    }
  }

  // field types and members
  using _index_type =
    int8_t;
  _index_type index;

  // setters for named parameter idiom
  Type & set__index(
    const int8_t & _arg)
  {
    this->index = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    xplore_interfaces::srv::EnableCamera_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const xplore_interfaces::srv::EnableCamera_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<xplore_interfaces::srv::EnableCamera_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<xplore_interfaces::srv::EnableCamera_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      xplore_interfaces::srv::EnableCamera_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<xplore_interfaces::srv::EnableCamera_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      xplore_interfaces::srv::EnableCamera_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<xplore_interfaces::srv::EnableCamera_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<xplore_interfaces::srv::EnableCamera_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<xplore_interfaces::srv::EnableCamera_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__xplore_interfaces__srv__EnableCamera_Request
    std::shared_ptr<xplore_interfaces::srv::EnableCamera_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__xplore_interfaces__srv__EnableCamera_Request
    std::shared_ptr<xplore_interfaces::srv::EnableCamera_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const EnableCamera_Request_ & other) const
  {
    if (this->index != other.index) {
      return false;
    }
    return true;
  }
  bool operator!=(const EnableCamera_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct EnableCamera_Request_

// alias to use template instance with default allocator
using EnableCamera_Request =
  xplore_interfaces::srv::EnableCamera_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace xplore_interfaces


#ifndef _WIN32
# define DEPRECATED__xplore_interfaces__srv__EnableCamera_Response __attribute__((deprecated))
#else
# define DEPRECATED__xplore_interfaces__srv__EnableCamera_Response __declspec(deprecated)
#endif

namespace xplore_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct EnableCamera_Response_
{
  using Type = EnableCamera_Response_<ContainerAllocator>;

  explicit EnableCamera_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->ip_adresse = 0ll;
    }
  }

  explicit EnableCamera_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->ip_adresse = 0ll;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;
  using _ip_adresse_type =
    int64_t;
  _ip_adresse_type ip_adresse;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
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
    xplore_interfaces::srv::EnableCamera_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const xplore_interfaces::srv::EnableCamera_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<xplore_interfaces::srv::EnableCamera_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<xplore_interfaces::srv::EnableCamera_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      xplore_interfaces::srv::EnableCamera_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<xplore_interfaces::srv::EnableCamera_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      xplore_interfaces::srv::EnableCamera_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<xplore_interfaces::srv::EnableCamera_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<xplore_interfaces::srv::EnableCamera_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<xplore_interfaces::srv::EnableCamera_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__xplore_interfaces__srv__EnableCamera_Response
    std::shared_ptr<xplore_interfaces::srv::EnableCamera_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__xplore_interfaces__srv__EnableCamera_Response
    std::shared_ptr<xplore_interfaces::srv::EnableCamera_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const EnableCamera_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    if (this->ip_adresse != other.ip_adresse) {
      return false;
    }
    return true;
  }
  bool operator!=(const EnableCamera_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct EnableCamera_Response_

// alias to use template instance with default allocator
using EnableCamera_Response =
  xplore_interfaces::srv::EnableCamera_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace xplore_interfaces

namespace xplore_interfaces
{

namespace srv
{

struct EnableCamera
{
  using Request = xplore_interfaces::srv::EnableCamera_Request;
  using Response = xplore_interfaces::srv::EnableCamera_Response;
};

}  // namespace srv

}  // namespace xplore_interfaces

#endif  // XPLORE_INTERFACES__SRV__DETAIL__ENABLE_CAMERA__STRUCT_HPP_
