# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "vision_no_ros: 2 messages, 0 services")

set(MSG_I_FLAGS "-Ivision_no_ros:/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(vision_no_ros_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/object_list.msg" NAME_WE)
add_custom_target(_vision_no_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "vision_no_ros" "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/object_list.msg" "vision_no_ros/panel_object"
)

get_filename_component(_filename "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/panel_object.msg" NAME_WE)
add_custom_target(_vision_no_ros_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "vision_no_ros" "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/panel_object.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(vision_no_ros
  "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/object_list.msg"
  "${MSG_I_FLAGS}"
  "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/panel_object.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/vision_no_ros
)
_generate_msg_cpp(vision_no_ros
  "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/panel_object.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/vision_no_ros
)

### Generating Services

### Generating Module File
_generate_module_cpp(vision_no_ros
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/vision_no_ros
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(vision_no_ros_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(vision_no_ros_generate_messages vision_no_ros_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/object_list.msg" NAME_WE)
add_dependencies(vision_no_ros_generate_messages_cpp _vision_no_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/panel_object.msg" NAME_WE)
add_dependencies(vision_no_ros_generate_messages_cpp _vision_no_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(vision_no_ros_gencpp)
add_dependencies(vision_no_ros_gencpp vision_no_ros_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS vision_no_ros_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(vision_no_ros
  "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/object_list.msg"
  "${MSG_I_FLAGS}"
  "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/panel_object.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/vision_no_ros
)
_generate_msg_eus(vision_no_ros
  "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/panel_object.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/vision_no_ros
)

### Generating Services

### Generating Module File
_generate_module_eus(vision_no_ros
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/vision_no_ros
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(vision_no_ros_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(vision_no_ros_generate_messages vision_no_ros_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/object_list.msg" NAME_WE)
add_dependencies(vision_no_ros_generate_messages_eus _vision_no_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/panel_object.msg" NAME_WE)
add_dependencies(vision_no_ros_generate_messages_eus _vision_no_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(vision_no_ros_geneus)
add_dependencies(vision_no_ros_geneus vision_no_ros_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS vision_no_ros_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(vision_no_ros
  "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/object_list.msg"
  "${MSG_I_FLAGS}"
  "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/panel_object.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/vision_no_ros
)
_generate_msg_lisp(vision_no_ros
  "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/panel_object.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/vision_no_ros
)

### Generating Services

### Generating Module File
_generate_module_lisp(vision_no_ros
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/vision_no_ros
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(vision_no_ros_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(vision_no_ros_generate_messages vision_no_ros_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/object_list.msg" NAME_WE)
add_dependencies(vision_no_ros_generate_messages_lisp _vision_no_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/panel_object.msg" NAME_WE)
add_dependencies(vision_no_ros_generate_messages_lisp _vision_no_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(vision_no_ros_genlisp)
add_dependencies(vision_no_ros_genlisp vision_no_ros_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS vision_no_ros_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(vision_no_ros
  "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/object_list.msg"
  "${MSG_I_FLAGS}"
  "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/panel_object.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/vision_no_ros
)
_generate_msg_nodejs(vision_no_ros
  "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/panel_object.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/vision_no_ros
)

### Generating Services

### Generating Module File
_generate_module_nodejs(vision_no_ros
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/vision_no_ros
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(vision_no_ros_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(vision_no_ros_generate_messages vision_no_ros_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/object_list.msg" NAME_WE)
add_dependencies(vision_no_ros_generate_messages_nodejs _vision_no_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/panel_object.msg" NAME_WE)
add_dependencies(vision_no_ros_generate_messages_nodejs _vision_no_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(vision_no_ros_gennodejs)
add_dependencies(vision_no_ros_gennodejs vision_no_ros_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS vision_no_ros_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(vision_no_ros
  "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/object_list.msg"
  "${MSG_I_FLAGS}"
  "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/panel_object.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/vision_no_ros
)
_generate_msg_py(vision_no_ros
  "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/panel_object.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/vision_no_ros
)

### Generating Services

### Generating Module File
_generate_module_py(vision_no_ros
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/vision_no_ros
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(vision_no_ros_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(vision_no_ros_generate_messages vision_no_ros_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/object_list.msg" NAME_WE)
add_dependencies(vision_no_ros_generate_messages_py _vision_no_ros_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/xplore/Desktop/CS_workspace/cs_ws/src/vision_no_ros/msg/panel_object.msg" NAME_WE)
add_dependencies(vision_no_ros_generate_messages_py _vision_no_ros_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(vision_no_ros_genpy)
add_dependencies(vision_no_ros_genpy vision_no_ros_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS vision_no_ros_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/vision_no_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/vision_no_ros
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/vision_no_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/vision_no_ros
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/vision_no_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/vision_no_ros
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/vision_no_ros)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/vision_no_ros
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/vision_no_ros)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/vision_no_ros\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/vision_no_ros
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
