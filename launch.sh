cd ..
source install/setup.bash
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
export CYCLONEDDS_URI="${CYCLONEDDS_URI:-file:///etc/cyclonedds.xml}"
ros2 daemon stop 2>/dev/null || true
# use_compression is off on purpose: permessage-deflate runs on the single Tornado ioloop thread
# and gains ~nothing on already-compressed JPEG, so it just slows the websocket sink down until
# frames back up and camera latency drifts.
# max_message_size matches launch_with_server.sh: the launch file defaults to 10MB, which is
# under the size of a full-resolution frame and silently truncates it.
# default_call_service_timeout must be > 0: the launch default is 0.0, which means "wait forever",
# and roslib never sends a per-call timeout. A call that is never answered then parks its
# ServiceCaller thread permanently and never reaches destroy_client(), so every dropped call
# leaks a DDS service-client endpoint for the life of the process.
ros2 launch rosbridge_server rosbridge_websocket_launch.xml use_compression:=false max_message_size:=50000000 call_services_in_new_thread:=true send_action_goals_in_new_thread:=true default_call_service_timeout:=6.0 & (cd src/frontend && WATCHPACK_POLLING=true CHOKIDAR_USEPOLLING=true npm start 2>&1 | cat)
