cd ..
source install/setup.bash
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
export CYCLONEDDS_URI="${CYCLONEDDS_URI:-file:///etc/cyclonedds.xml}"
ros2 daemon stop 2>/dev/null || true
ros2 launch rosbridge_server rosbridge_websocket_launch.xml use_compression:=true call_services_in_new_thread:=true send_action_goals_in_new_thread:=true & (cd src/frontend && npm start)