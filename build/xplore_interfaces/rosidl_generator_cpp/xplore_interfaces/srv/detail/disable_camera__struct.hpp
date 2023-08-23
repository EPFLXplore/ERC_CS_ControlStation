// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from xplore_interfaces:srv/DisableCamera.idl
// generated code does not contain a copyright notice

#ifndef XPLORE_INTERFACES__SRV__DETAIL__DISABLE_CAMERA__STRUCT_HPP_
#define XPLORE_INTERFACES__SRV__DETAIL__DISABLE_CAMERA__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__xplore_interfaces__srv__DisableCamera_Request __attribute__((deprecated))
#else
# define DEPRECATED__xplore_interfaces__srv__DisableCamera_Request __declspec(deprecated)
#endif

namespace xplore_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct DisableCamera_Request_
{
  using Type = DisableCamera_Request_<ContainerAllocator>;

  explicit DisableCamera_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->index = 0;
    }
  }

  explicit DisableCamera_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    xplore_interfaces::srv::DisableCamera_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const xplore_interfaces::srv::DisableCamera_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<xplore_interfaces::srv::DisableCamera_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<xplore_interfaces::srv::DisableCamera_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      xplore_interfaces::srv::DisableCamera_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<xplore_interfaces::srv::DisableCamera_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      xplore_interfaces::srv::DisableCamera_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<xplore_interfaces::srv::DisableCamera_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<xplore_interfaces::srv::DisableCamera_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<xplore_interfaces::srv::DisableCamera_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__xplore_interfaces__srv__DisableCamera_Request
    std::shared_ptr<xplore_interfaces::srv::DisableCamera_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__xplore_interfaces__srv__DisableCamera_Request
    std::shared_ptr<xplore_interfaces::srv::DisableCamera_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DisableCamera_Request_ & other) const
  {
    if (this->index != other.index) {
      return false;
    }
    return true;
  }
  bool operator!=(const DisableCamera_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DisableCamera_Request_

// alias to use template instance with default allocator
using DisableCamera_Request =
  xplore_interfaces::srv::DisableCamera_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace xplore_interfaces


#ifndef _WIN32
# define DEPRECATED__xplore_interfaces__srv__DisableCamera_Response __attribute__((deprecated))
#else
# define DEPRECATED__xplore_interfaces__srv__DisableCamera_Response __declspec(deprecated)
#endif

namespace xplore_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct DisableCamera_Response_
{
  using Type = DisableCamera_Response_<ContainerAllocator>;

  explicit DisableCamera_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit DisableCamera_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    xplore_interfaces::srv::DisableCamera_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const xplore_interfaces::srv::DisableCamera_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<xplore_interfaces::srv::DisableCamera_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<xplore_interfaces::srv::DisableCamera_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      xplore_interfaces::srv::DisableCamera_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<xplore_interfaces::srv::DisableCamera_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      xplore_interfaces::srv::DisableCamera_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<xplore_interfaces::srv::DisableCamera_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<xplore_interfaces::srv::DisableCamera_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<xplore_interfaces::srv::DisableCamera_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__xplore_interfaces__srv__DisableCamera_Response
    std::shared_ptr<xplore_interfaces::srv::DisableCamera_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__xplore_interfaces__srv__DisableCamera_Response
    std::shared_ptr<xplore_interfaces::srv::DisableCamera_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const DisableCamera_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const DisableCamera_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct DisableCamera_Response_

// alias to use template instance with default allocator
using DisableCamera_Response =
  xplore_interfaces::srv::DisableCamera_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace xplore_interfaces

namespace xplore_interfaces
{

namespace srv
{

struct DisableCamera
{
  using Request = xplore_interfaces::srv::DisableCamera_Request;
  using Response = xplore_interfaces::srv::DisableCamera_Response;
};

}  // namespace srv

}  // namespace xplore_interfaces

#endif  // XPLORE_INTERFACES__SRV__DETAIL__DISABLE_CAMERA__STRUCT_HPP_
