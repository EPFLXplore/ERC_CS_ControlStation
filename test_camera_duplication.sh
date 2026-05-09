#!/bin/bash
# Test script to verify camera subscriptions are not duplicated
# This checks that only one ROS subscription exists per camera topic
# even when multiple clients connect

set -e

echo "=== Camera Stream Duplication Test ==="
echo ""
echo "This script monitors ROS subscriptions to verify that multiple"
echo "clients connecting to the same camera topics don't create duplicate"
echo "subscriptions from rosbridge to the rover."
echo ""

# Source ROS setup
cd "$(dirname "$0")"
source /opt/ros/humble/setup.bash
source install/setup.bash

# Define camera topics
CAMERA_TOPICS=(
    "/ROVER/feed_camera_hd_0"
    "/NAV/feed_camera_nav_0" 
    "/NAV/feed_camera_nav_1"
    "/CS/feed_camera_cs_0"
)

echo "Step 1: Check current ROS subscriptions before starting lanch_with_server"
echo "==========================================================================="
echo "Active subscribers to camera topics:"
for topic in "${CAMERA_TOPICS[@]}"; do
    count=$(ros2 node info /rosbridge_websocket 2>/dev/null | grep -c "$topic" || echo "0")
    echo "  $topic: $count subscriber(s)"
done
echo ""

echo "Step 2: After launching with 1 client, verify subscription count"
echo "=================================================================="
echo "Expected: Each topic should have exactly 1 ROS subscription"
echo "If you're seeing multiple counts per topic, streams are being duplicated."
echo ""

echo "Step 3: Connect second client and verify subscription count hasn't increased"
echo "=========================================================================="
echo "Expected: Subscription count should remain the same (1 per topic)"
echo "If count increases, duplicate subscriptions are being created."
echo ""

echo "To run this test manually:"
echo "1. Terminal 1: Run: cd docker_humble_desktop && ./go_in_docker.sh"
echo "2. In Docker: ./launch_with_server.sh"
echo "3. Terminal 2: Connect first browser to localhost:8080"
echo "4. Terminal 3: Connect second browser to localhost:8080"
echo "5. Terminal 2 (host): Run this script to check subscription counts"
echo ""
echo "Subscription info can be checked with:"
echo "  ros2 node info /rosbridge_websocket"
echo "  ros2 topic info /ROVER/feed_camera_hd_0 --verbose"
echo ""
