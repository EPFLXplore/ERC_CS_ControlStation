cd ..
source /opt/ros/humble/setup.bash
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
source install/setup.bash
# ros2 launch rosbridge_server rosbridge_websocket_launch.xml use_compression:=true max_message_size:=70000000 call_services_in_new_thread:=true send_action_goals_in_new_thread:=true & (cd src/frontend && npm start) & (cd src/frontend/ssh_backend && node ssh_server.js)

ros2 launch rosbridge_server rosbridge_websocket_launch.xml \
  use_compression:=true \
  max_message_size:=70000000 \
  call_services_in_new_thread:=true \
  send_action_goals_in_new_thread:=true \
  delay_between_messages:=0 \
  fragment_timeout:=600 \
  unregister_timeout:=10.0 \
  bson_only_mode:=false \
  default_call_service_timeout:=5.0 & \
(cd src/frontend && npm start) & \
(cd src/frontend/ssh_backend && node ssh_server.js)

# max message size: 350000000 bytes (approximately 333 MB)
# [WARN] if the 'default_call_service_timeout' parameter is  set to 0.0, service calls will block indefinitely if no response is received. 
