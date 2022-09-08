;; Auto-generated. Do not edit!


(when (boundp 'vision_no_ros::object_list)
  (if (not (find-package "VISION_NO_ROS"))
    (make-package "VISION_NO_ROS"))
  (shadow 'object_list (find-package "VISION_NO_ROS")))
(unless (find-package "VISION_NO_ROS::OBJECT_LIST")
  (make-package "VISION_NO_ROS::OBJECT_LIST"))

(in-package "ROS")
;;//! \htmlinclude object_list.msg.html


(defclass vision_no_ros::object_list
  :super ros::object
  :slots (_detected_objects ))

(defmethod vision_no_ros::object_list
  (:init
   (&key
    ((:detected_objects __detected_objects) ())
    )
   (send-super :init)
   (setq _detected_objects __detected_objects)
   self)
  (:detected_objects
   (&rest __detected_objects)
   (if (keywordp (car __detected_objects))
       (send* _detected_objects __detected_objects)
     (progn
       (if __detected_objects (setq _detected_objects (car __detected_objects)))
       _detected_objects)))
  (:serialization-length
   ()
   (+
    ;; vision_no_ros/panel_object[] _detected_objects
    (apply #'+ (send-all _detected_objects :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; vision_no_ros/panel_object[] _detected_objects
     (write-long (length _detected_objects) s)
     (dolist (elem _detected_objects)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; vision_no_ros/panel_object[] _detected_objects
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _detected_objects (let (r) (dotimes (i n) (push (instance vision_no_ros::panel_object :init) r)) r))
     (dolist (elem- _detected_objects)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get vision_no_ros::object_list :md5sum-) "93cc90f8ec35aa397138799e59c6bb47")
(setf (get vision_no_ros::object_list :datatype-) "vision_no_ros/object_list")
(setf (get vision_no_ros::object_list :definition-)
      "panel_object[] detected_objects
================================================================================
MSG: vision_no_ros/panel_object
int8 id
int8 reliability
float32 x_pos
float32 y_pos
float32 z_pos
float32 x_rot
float32 y_rot
float32 z_rot
float32 w_quaternion
float32 x_quaternion
float32 y_quaternion
float32 z_quaternion

")



(provide :vision_no_ros/object_list "93cc90f8ec35aa397138799e59c6bb47")


