cd ..
colcon build
source install/setup.bash
ros2 launch rosbridge_server rosbridge_websocket_launch.xml & (cd src/frontend && npm start)