cd ..
source /opt/ros/humble/setup.bash
source install/setup.bash
# After workspace setup: force Cyclone + URI (local_setup can override RMW_IMPLEMENTATION).
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
export CYCLONEDDS_URI="${CYCLONEDDS_URI:-file:///etc/cyclonedds.xml}"
# Daemon caches the RMW stack; restart so it picks up CYCLONEDDS_URI (critical in Docker).
ros2 daemon stop 2>/dev/null || true
ros2 launch rosbridge_server rosbridge_websocket_launch.xml use_compression:=true max_message_size:=50000000 call_services_in_new_thread:=true send_action_goals_in_new_thread:=true & (cd src/frontend && npm start) & (cd src/frontend/ssh_backend && node ssh_server.js)