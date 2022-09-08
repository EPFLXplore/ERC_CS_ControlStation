; Auto-generated. Do not edit!


(cl:in-package vision_no_ros-msg)


;//! \htmlinclude panel_object.msg.html

(cl:defclass <panel_object> (roslisp-msg-protocol:ros-message)
  ((id
    :reader id
    :initarg :id
    :type cl:fixnum
    :initform 0)
   (reliability
    :reader reliability
    :initarg :reliability
    :type cl:fixnum
    :initform 0)
   (x_pos
    :reader x_pos
    :initarg :x_pos
    :type cl:float
    :initform 0.0)
   (y_pos
    :reader y_pos
    :initarg :y_pos
    :type cl:float
    :initform 0.0)
   (z_pos
    :reader z_pos
    :initarg :z_pos
    :type cl:float
    :initform 0.0)
   (x_rot
    :reader x_rot
    :initarg :x_rot
    :type cl:float
    :initform 0.0)
   (y_rot
    :reader y_rot
    :initarg :y_rot
    :type cl:float
    :initform 0.0)
   (z_rot
    :reader z_rot
    :initarg :z_rot
    :type cl:float
    :initform 0.0)
   (w_quaternion
    :reader w_quaternion
    :initarg :w_quaternion
    :type cl:float
    :initform 0.0)
   (x_quaternion
    :reader x_quaternion
    :initarg :x_quaternion
    :type cl:float
    :initform 0.0)
   (y_quaternion
    :reader y_quaternion
    :initarg :y_quaternion
    :type cl:float
    :initform 0.0)
   (z_quaternion
    :reader z_quaternion
    :initarg :z_quaternion
    :type cl:float
    :initform 0.0))
)

(cl:defclass panel_object (<panel_object>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <panel_object>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'panel_object)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name vision_no_ros-msg:<panel_object> is deprecated: use vision_no_ros-msg:panel_object instead.")))

(cl:ensure-generic-function 'id-val :lambda-list '(m))
(cl:defmethod id-val ((m <panel_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_no_ros-msg:id-val is deprecated.  Use vision_no_ros-msg:id instead.")
  (id m))

(cl:ensure-generic-function 'reliability-val :lambda-list '(m))
(cl:defmethod reliability-val ((m <panel_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_no_ros-msg:reliability-val is deprecated.  Use vision_no_ros-msg:reliability instead.")
  (reliability m))

(cl:ensure-generic-function 'x_pos-val :lambda-list '(m))
(cl:defmethod x_pos-val ((m <panel_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_no_ros-msg:x_pos-val is deprecated.  Use vision_no_ros-msg:x_pos instead.")
  (x_pos m))

(cl:ensure-generic-function 'y_pos-val :lambda-list '(m))
(cl:defmethod y_pos-val ((m <panel_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_no_ros-msg:y_pos-val is deprecated.  Use vision_no_ros-msg:y_pos instead.")
  (y_pos m))

(cl:ensure-generic-function 'z_pos-val :lambda-list '(m))
(cl:defmethod z_pos-val ((m <panel_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_no_ros-msg:z_pos-val is deprecated.  Use vision_no_ros-msg:z_pos instead.")
  (z_pos m))

(cl:ensure-generic-function 'x_rot-val :lambda-list '(m))
(cl:defmethod x_rot-val ((m <panel_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_no_ros-msg:x_rot-val is deprecated.  Use vision_no_ros-msg:x_rot instead.")
  (x_rot m))

(cl:ensure-generic-function 'y_rot-val :lambda-list '(m))
(cl:defmethod y_rot-val ((m <panel_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_no_ros-msg:y_rot-val is deprecated.  Use vision_no_ros-msg:y_rot instead.")
  (y_rot m))

(cl:ensure-generic-function 'z_rot-val :lambda-list '(m))
(cl:defmethod z_rot-val ((m <panel_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_no_ros-msg:z_rot-val is deprecated.  Use vision_no_ros-msg:z_rot instead.")
  (z_rot m))

(cl:ensure-generic-function 'w_quaternion-val :lambda-list '(m))
(cl:defmethod w_quaternion-val ((m <panel_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_no_ros-msg:w_quaternion-val is deprecated.  Use vision_no_ros-msg:w_quaternion instead.")
  (w_quaternion m))

(cl:ensure-generic-function 'x_quaternion-val :lambda-list '(m))
(cl:defmethod x_quaternion-val ((m <panel_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_no_ros-msg:x_quaternion-val is deprecated.  Use vision_no_ros-msg:x_quaternion instead.")
  (x_quaternion m))

(cl:ensure-generic-function 'y_quaternion-val :lambda-list '(m))
(cl:defmethod y_quaternion-val ((m <panel_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_no_ros-msg:y_quaternion-val is deprecated.  Use vision_no_ros-msg:y_quaternion instead.")
  (y_quaternion m))

(cl:ensure-generic-function 'z_quaternion-val :lambda-list '(m))
(cl:defmethod z_quaternion-val ((m <panel_object>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader vision_no_ros-msg:z_quaternion-val is deprecated.  Use vision_no_ros-msg:z_quaternion instead.")
  (z_quaternion m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <panel_object>) ostream)
  "Serializes a message object of type '<panel_object>"
  (cl:let* ((signed (cl:slot-value msg 'id)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'reliability)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x_pos))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y_pos))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'z_pos))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x_rot))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y_rot))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'z_rot))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'w_quaternion))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'x_quaternion))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'y_quaternion))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'z_quaternion))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <panel_object>) istream)
  "Deserializes a message object of type '<panel_object>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'id) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'reliability) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x_pos) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y_pos) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'z_pos) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x_rot) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y_rot) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'z_rot) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'w_quaternion) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x_quaternion) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y_quaternion) (roslisp-utils:decode-single-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'z_quaternion) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<panel_object>)))
  "Returns string type for a message object of type '<panel_object>"
  "vision_no_ros/panel_object")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'panel_object)))
  "Returns string type for a message object of type 'panel_object"
  "vision_no_ros/panel_object")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<panel_object>)))
  "Returns md5sum for a message object of type '<panel_object>"
  "898cda956b9cf305c691a0c55e5ce854")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'panel_object)))
  "Returns md5sum for a message object of type 'panel_object"
  "898cda956b9cf305c691a0c55e5ce854")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<panel_object>)))
  "Returns full string definition for message of type '<panel_object>"
  (cl:format cl:nil "int8 id~%int8 reliability~%float32 x_pos~%float32 y_pos~%float32 z_pos~%float32 x_rot~%float32 y_rot~%float32 z_rot~%float32 w_quaternion~%float32 x_quaternion~%float32 y_quaternion~%float32 z_quaternion~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'panel_object)))
  "Returns full string definition for message of type 'panel_object"
  (cl:format cl:nil "int8 id~%int8 reliability~%float32 x_pos~%float32 y_pos~%float32 z_pos~%float32 x_rot~%float32 y_rot~%float32 z_rot~%float32 w_quaternion~%float32 x_quaternion~%float32 y_quaternion~%float32 z_quaternion~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <panel_object>))
  (cl:+ 0
     1
     1
     4
     4
     4
     4
     4
     4
     4
     4
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <panel_object>))
  "Converts a ROS message object to a list"
  (cl:list 'panel_object
    (cl:cons ':id (id msg))
    (cl:cons ':reliability (reliability msg))
    (cl:cons ':x_pos (x_pos msg))
    (cl:cons ':y_pos (y_pos msg))
    (cl:cons ':z_pos (z_pos msg))
    (cl:cons ':x_rot (x_rot msg))
    (cl:cons ':y_rot (y_rot msg))
    (cl:cons ':z_rot (z_rot msg))
    (cl:cons ':w_quaternion (w_quaternion msg))
    (cl:cons ':x_quaternion (x_quaternion msg))
    (cl:cons ':y_quaternion (y_quaternion msg))
    (cl:cons ':z_quaternion (z_quaternion msg))
))
