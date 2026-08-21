cd ..
source install/setup.bash
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
export CYCLONEDDS_URI="${CYCLONEDDS_URI:-file:///etc/cyclonedds.xml}"
ros2 daemon stop 2>/dev/null || true
# use_compression is off on purpose: permessage-deflate runs on the single Tornado ioloop thread
# and gains ~nothing on already-compressed JPEG, so it just slows the websocket sink down until
# frames back up and camera latency drifts.
ros2 launch rosbridge_server rosbridge_websocket_launch.xml use_compression:=false call_services_in_new_thread:=true send_action_goals_in_new_thread:=true & (cd src/frontend && WATCHPACK_POLLING=true CHOKIDAR_USEPOLLING=true npm start 2>&1 | cat)
