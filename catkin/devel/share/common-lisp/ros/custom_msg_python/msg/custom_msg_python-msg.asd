
(cl:in-package :asdf)

(defsystem "custom_msg_python-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "move_base_action_goal" :depends-on ("_package_move_base_action_goal"))
    (:file "_package_move_base_action_goal" :depends-on ("_package"))
    (:file "move_base_goal" :depends-on ("_package_move_base_goal"))
    (:file "_package_move_base_goal" :depends-on ("_package"))
  ))