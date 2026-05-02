cd ..
source /opt/ros/humble/setup.bash
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
source install/setup.bash

echo "[INFO] Starting rosbridge server..."
ros2 launch rosbridge_server rosbridge_websocket_launch.xml \
  use_compression:=true \
  max_message_size:=70000000 \
  call_services_in_new_thread:=true \
  send_action_goals_in_new_thread:=true \
  delay_between_messages:=0 \
  fragment_timeout:=600 \
  unregister_timeout:=10.0 \
  bson_only_mode:=false \
  default_call_service_timeout:=25.0 &

ROSBRIDGE_PID=$!
echo "[INFO] Rosbridge server PID: $ROSBRIDGE_PID"

# Wait for rosbridge server to be ready (check if port 9090 is listening)
echo "[INFO] Waiting for rosbridge server to be ready on port 9090..."
MAX_ATTEMPTS=30
ATTEMPT=0
while [ $ATTEMPT -lt $MAX_ATTEMPTS ]; do
    if netstat -tuln 2>/dev/null | grep -q ":9090 " || ss -tuln 2>/dev/null | grep -q ":9090 "; then
        echo "[SUCCESS] Rosbridge server is ready!"
        break
    fi
    ATTEMPT=$((ATTEMPT + 1))
    echo "[INFO] Attempt $ATTEMPT/$MAX_ATTEMPTS - waiting for rosbridge..."
    sleep 1
done

if [ $ATTEMPT -eq $MAX_ATTEMPTS ]; then
    echo "[ERROR] Rosbridge server failed to start after ${MAX_ATTEMPTS}s"
    kill $ROSBRIDGE_PID 2>/dev/null || true
    exit 1
fi

echo "[INFO] Starting frontend..."
(cd src/frontend && npm start) &

echo "[INFO] Starting SSH backend..."
(cd src/frontend/ssh_backend && node ssh_server.js) &

# max message size: 350000000 bytes (approximately 333 MB)
# [WARN] if the 'default_call_service_timeout' parameter is  set to 0.0, service calls will block indefinitely if no response is received.

# Wait for all background processes
wait 
