; Auto-generated. Do not edit!


(cl:in-package vision_no_ros-msg)


;//! \htmlinclude object_list.msg.html

(cl:defclass <object_list> (roslisp-msg-protocol:ros-message)
  ((detected_objects
    :reader detected_objects
    :initarg :detected_objects
    :type (cl:vector vision_no_ros-msg:panel_object)
   :initform (cl:make-array 0 :element-type 'vision_no_ros-msg:panel_object :initial-element (cl:make-instance 'vision_no_ros-msg:panel_object))))
)

(cl:defclass object_list (<object_list>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <object_list>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'object_list)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision_no_ros-msg:<object_list> is deprecated: use vision_no_ros-msg:object_list instead.")))

(cl:ensure-generic-function 'detected_objects-val :lambda-list '(m))
(cl:defmethod detected_objects-val ((m <object_list>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_no_ros-msg:detected_objects-val is deprecated.  Use vision_no_ros-msg:detected_objects instead.")
  (detected_objects m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <object_list>) ostream)
  "Serializes a message object of type '<object_list>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'detected_objects))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'detected_objects))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <object_list>) istream)
  "Deserializes a message object of type '<object_list>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'detected_objects) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'detected_objects)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'vision_no_ros-msg:panel_object))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<object_list>)))
  "Returns string type for a message object of type '<object_list>"
  "vision_no_ros/object_list")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'object_list)))
  "Returns string type for a message object of type 'object_list"
  "vision_no_ros/object_list")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<object_list>)))
  "Returns md5sum for a message object of type '<object_list>"
  "93cc90f8ec35aa397138799e59c6bb47")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'object_list)))
  "Returns md5sum for a message object of type 'object_list"
  "93cc90f8ec35aa397138799e59c6bb47")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<object_list>)))
  "Returns full string definition for message of type '<object_list>"
  (cl:format cl:nil "panel_object[] detected_objects~%================================================================================~%MSG: vision_no_ros/panel_object~%int8 id~%int8 reliability~%float32 x_pos~%float32 y_pos~%float32 z_pos~%float32 x_rot~%float32 y_rot~%float32 z_rot~%float32 w_quaternion~%float32 x_quaternion~%float32 y_quaternion~%float32 z_quaternion~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'object_list)))
  "Returns full string definition for message of type 'object_list"
  (cl:format cl:nil "panel_object[] detected_objects~%================================================================================~%MSG: vision_no_ros/panel_object~%int8 id~%int8 reliability~%float32 x_pos~%float32 y_pos~%float32 z_pos~%float32 x_rot~%float32 y_rot~%float32 z_rot~%float32 w_quaternion~%float32 x_quaternion~%float32 y_quaternion~%float32 z_quaternion~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <object_list>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'detected_objects) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <object_list>))
  "Converts a ROS message object to a list"
  (cl:list 'object_list
    (cl:cons ':detected_objects (detected_objects msg))
))
