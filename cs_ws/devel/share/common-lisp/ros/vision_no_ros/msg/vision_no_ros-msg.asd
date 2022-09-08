
(cl:in-package :asdf)

(defsystem "vision_no_ros-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "object_list" :depends-on ("_package_object_list"))
    (:file "_package_object_list" :depends-on ("_package"))
    (:file "panel_object" :depends-on ("_package_panel_object"))
    (:file "_package_panel_object" :depends-on ("_package"))
  ))