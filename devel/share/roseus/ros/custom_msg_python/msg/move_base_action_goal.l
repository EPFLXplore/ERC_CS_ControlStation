;; Auto-generated. Do not edit!


(when (boundp 'custom_msg_python::move_base_action_goal)
  (if (not (find-package "CUSTOM_MSG_PYTHON"))
    (make-package "CUSTOM_MSG_PYTHON"))
  (shadow 'move_base_action_goal (find-package "CUSTOM_MSG_PYTHON")))
(unless (find-package "CUSTOM_MSG_PYTHON::MOVE_BASE_ACTION_GOAL")
  (make-package "CUSTOM_MSG_PYTHON::MOVE_BASE_ACTION_GOAL"))

(in-package "ROS")
;;//! \htmlinclude move_base_action_goal.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass custom_msg_python::move_base_action_goal
  :super ros::object
  :slots (_currId _moveBaseGoal ))

(defmethod custom_msg_python::move_base_action_goal
  (:init
   (&key
    ((:currId __currId) (instance std_msgs::Int8 :init))
    ((:moveBaseGoal __moveBaseGoal) (instance geometry_msgs::Pose :init))
    )
   (send-super :init)
   (setq _currId __currId)
   (setq _moveBaseGoal __moveBaseGoal)
   self)
  (:currId
   (&rest __currId)
   (if (keywordp (car __currId))
       (send* _currId __currId)
     (progn
       (if __currId (setq _currId (car __currId)))
       _currId)))
  (:moveBaseGoal
   (&rest __moveBaseGoal)
   (if (keywordp (car __moveBaseGoal))
       (send* _moveBaseGoal __moveBaseGoal)
     (progn
       (if __moveBaseGoal (setq _moveBaseGoal (car __moveBaseGoal)))
       _moveBaseGoal)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Int8 _currId
    (send _currId :serialization-length)
    ;; geometry_msgs/Pose _moveBaseGoal
    (send _moveBaseGoal :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Int8 _currId
       (send _currId :serialize s)
     ;; geometry_msgs/Pose _moveBaseGoal
       (send _moveBaseGoal :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Int8 _currId
     (send _currId :deserialize buf ptr-) (incf ptr- (send _currId :serialization-length))
   ;; geometry_msgs/Pose _moveBaseGoal
     (send _moveBaseGoal :deserialize buf ptr-) (incf ptr- (send _moveBaseGoal :serialization-length))
   ;;
   self)
  )

(setf (get custom_msg_python::move_base_action_goal :md5sum-) "512860f1cd6d90bb8cf7bd87927bb3d7")
(setf (get custom_msg_python::move_base_action_goal :datatype-) "custom_msg_python/move_base_action_goal")
(setf (get custom_msg_python::move_base_action_goal :definition-)
      "
std_msgs/Int8 currId
geometry_msgs/Pose moveBaseGoal

================================================================================
MSG: std_msgs/Int8
int8 data

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

")



(provide :custom_msg_python/move_base_action_goal "512860f1cd6d90bb8cf7bd87927bb3d7")


