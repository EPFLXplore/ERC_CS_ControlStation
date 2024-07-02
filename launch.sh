cd ..
colcon build
source install/setup.bash
ros2 launch rosbridge_server rosbridge_websocket_launch.xml call_services_in_new_thread:=true send_action_goals_in_new_thread:=true & (cd src/frontend && npm start)