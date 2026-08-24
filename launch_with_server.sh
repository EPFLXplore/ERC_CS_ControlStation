cd ..
source /opt/ros/humble/setup.bash
source install/setup.bash
# After workspace setup: force Cyclone + URI (local_setup can override RMW_IMPLEMENTATION).
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
export CYCLONEDDS_URI="${CYCLONEDDS_URI:-file:///etc/cyclonedds.xml}"
# Daemon caches the RMW stack; restart so it picks up CYCLONEDDS_URI (critical in Docker).
ros2 daemon stop 2>/dev/null || true
# use_compression is off on purpose: permessage-deflate runs on the single Tornado ioloop thread
# and gains ~nothing on already-compressed JPEG, so it just slows the websocket sink down until
# frames back up and camera latency drifts.
# default_call_service_timeout must be > 0: the launch default is 0.0, which means "wait forever",
# and roslib never sends a per-call timeout. A call that is never answered then parks its
# ServiceCaller thread permanently and never reaches destroy_client(), so every dropped call
# leaks a DDS service-client endpoint for the life of the process.
ros2 launch rosbridge_server rosbridge_websocket_launch.xml use_compression:=false max_message_size:=50000000 call_services_in_new_thread:=true send_action_goals_in_new_thread:=true default_call_service_timeout:=6.0 & (cd src/frontend && WATCHPACK_POLLING=true CHOKIDAR_USEPOLLING=true npm start 2>&1 | cat) & (cd src/frontend/ssh_backend && node ssh_server.js)
