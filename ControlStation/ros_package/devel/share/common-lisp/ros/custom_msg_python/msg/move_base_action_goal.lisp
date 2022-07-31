; Auto-generated. Do not edit!


(cl:in-package custom_msg_python-msg)


;//! \htmlinclude move_base_action_goal.msg.html

(cl:defclass <move_base_action_goal> (roslisp-msg-protocol:ros-message)
  ((currId
    :reader currId
    :initarg :currId
    :type std_msgs-msg:Int8
    :initform (cl:make-instance 'std_msgs-msg:Int8))
   (moveBaseGoal
    :reader moveBaseGoal
    :initarg :moveBaseGoal
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose)))
)

(cl:defclass move_base_action_goal (<move_base_action_goal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <move_base_action_goal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'move_base_action_goal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name custom_msg_python-msg:<move_base_action_goal> is deprecated: use custom_msg_python-msg:move_base_action_goal instead.")))

(cl:ensure-generic-function 'currId-val :lambda-list '(m))
(cl:defmethod currId-val ((m <move_base_action_goal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:currId-val is deprecated.  Use custom_msg_python-msg:currId instead.")
  (currId m))

(cl:ensure-generic-function 'moveBaseGoal-val :lambda-list '(m))
(cl:defmethod moveBaseGoal-val ((m <move_base_action_goal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader custom_msg_python-msg:moveBaseGoal-val is deprecated.  Use custom_msg_python-msg:moveBaseGoal instead.")
  (moveBaseGoal m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <move_base_action_goal>) ostream)
  "Serializes a message object of type '<move_base_action_goal>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'currId) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'moveBaseGoal) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <move_base_action_goal>) istream)
  "Deserializes a message object of type '<move_base_action_goal>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'currId) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'moveBaseGoal) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<move_base_action_goal>)))
  "Returns string type for a message object of type '<move_base_action_goal>"
  "custom_msg_python/move_base_action_goal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'move_base_action_goal)))
  "Returns string type for a message object of type 'move_base_action_goal"
  "custom_msg_python/move_base_action_goal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<move_base_action_goal>)))
  "Returns md5sum for a message object of type '<move_base_action_goal>"
  "512860f1cd6d90bb8cf7bd87927bb3d7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'move_base_action_goal)))
  "Returns md5sum for a message object of type 'move_base_action_goal"
  "512860f1cd6d90bb8cf7bd87927bb3d7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<move_base_action_goal>)))
  "Returns full string definition for message of type '<move_base_action_goal>"
  (cl:format cl:nil "~%std_msgs/Int8 currId~%geometry_msgs/Pose moveBaseGoal~%~%================================================================================~%MSG: std_msgs/Int8~%int8 data~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'move_base_action_goal)))
  "Returns full string definition for message of type 'move_base_action_goal"
  (cl:format cl:nil "~%std_msgs/Int8 currId~%geometry_msgs/Pose moveBaseGoal~%~%================================================================================~%MSG: std_msgs/Int8~%int8 data~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <move_base_action_goal>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'currId))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'moveBaseGoal))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <move_base_action_goal>))
  "Converts a ROS message object to a list"
  (cl:list 'move_base_action_goal
    (cl:cons ':currId (currId msg))
    (cl:cons ':moveBaseGoal (moveBaseGoal msg))
))
