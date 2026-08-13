#!/usr/bin/env bash
# If not working, first do: sudo rm -rf /tmp/.docker.xauth
# If still not working, try running the script as root.
#
# Rover / field use: CycloneDDS config is **cyclonedds_with_rover.xml** (next to this script).
# Expected layout:
#   docker_humble_desktop/
#     cyclonedds_with_rover.xml  run_on_rover.sh  ...

echo "Opening http://localhost:3000/ in Chrome (new tab if Chrome is already running) ..."
# Omit --new-window so the existing Chrome process opens a tab instead of another window.
google-chrome "http://localhost:3000/" >/dev/null 2>&1 &
sleep 1

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

CYCLONEDDS_HOST="$SCRIPT_DIR/cyclonedds_with_rover.xml"
if command -v realpath >/dev/null 2>&1; then
	CYCLONEDDS_HOST="$(realpath "$CYCLONEDDS_HOST")"
fi

# Bind-mount rover Cyclone config here (not under /home/xplore — named volume would hide it).
CYCLONEDDS_CONTAINER="/etc/cyclonedds.xml"
CYCLONEDDS_URI="file://${CYCLONEDDS_CONTAINER}"

XAUTH=/tmp/.docker.xauth

echo "Preparing Xauthority data..."
xauth_list=$(xauth nlist :0 | tail -n 1 | sed -e 's/^..../ffff/')
if [ ! -f "$XAUTH" ]; then
	if [ ! -z "$xauth_list" ]; then
		echo $xauth_list | xauth -f $XAUTH nmerge -
	else
		touch $XAUTH
	fi
	chmod a+r $XAUTH
fi

echo "Done."
echo ""
echo "Verifying file contents:"
file $XAUTH
echo "--> It should say \"X11 Xauthority data\"."
echo ""
echo "Permissions:"
ls -FAlh $XAUTH
echo ""


sudo sysctl -w net.core.rmem_max=2147483647         # 2 GiB
# CycloneDDS requests >= 1 MiB. Give it plenty of headroom.
sudo sysctl -w net.core.wmem_max=33554432
# Reasonable defaults for sockets that do not explicitly request a size.
sudo sysctl -w net.core.rmem_default=8388608
sudo sysctl -w net.core.wmem_default=8388608


CONTAINER_NAME=cs_humble_desktop

# Reuse first: bind-mounts only apply to docker run, so don't print "mounting" when we only exec.
if docker container inspect "$CONTAINER_NAME" >/dev/null 2>&1; then
	echo "Reusing existing container $CONTAINER_NAME (docker exec — Cyclone XML is from container create, not remounted)."
	echo "To remount cyclonedds_with_rover.xml:  docker rm -f $CONTAINER_NAME  then run this script again."
	echo ""
	if [ "$(docker container inspect -f '{{.State.Running}}' "$CONTAINER_NAME")" = "true" ]; then
		echo "Already running — opening an interactive shell..."
		exec docker exec -it "$CONTAINER_NAME" /bin/bash
	else
		echo "Starting stopped container, then opening a shell..."
		docker start "$CONTAINER_NAME" || exit 1
		exec docker exec -it "$CONTAINER_NAME" /bin/bash
	fi
fi

echo "Running docker (rover CycloneDDS profile) — new container"

if [ ! -f "$CYCLONEDDS_HOST" ]; then
	echo "Error: Cyclone DDS rover config not found: $CYCLONEDDS_HOST" >&2
	echo "Place cyclonedds_with_rover.xml next to run_on_rover.sh under: $SCRIPT_DIR" >&2
	exit 1
fi

echo "CycloneDDS: mounting rover host file"
echo "  $CYCLONEDDS_HOST"
echo "  -> ${CYCLONEDDS_CONTAINER} (read-only)"
echo "  CYCLONEDDS_URI=${CYCLONEDDS_URI}"
echo ""
echo "Container start: rosbridge + frontend (npm) + ssh_backend (see launch_with_server.sh)"
echo ""
echo "Sanity checks inside the container:"
echo "  sed -n '1,15p' /etc/cyclonedds.xml   # should match host cyclonedds_with_rover.xml"
echo "  env | grep -E 'CYCLONEDDS_URI|RMW_IMPLEMENTATION|ROS_DOMAIN_ID'"
echo "  ros2 daemon stop && ros2 topic list | grep -E 'NAV/State|State' || true"
echo "  # If Nav2 topics exist but not /NAV/State → NAV interface node not publishing (not DDS)."
echo ""

# ROS_DOMAIN_ID is pinned to 0 rather than inherited from the host: both cyclonedds_*.xml
# are scoped to a single domain, so a host override would silently disable the peers list
# and buffer settings without any error.
docker run -it \
	--name "$CONTAINER_NAME" \
	--rm \
	--privileged \
	--net=host \
	-e DISPLAY=unix$DISPLAY \
	-e QT_X11_NO_MITSHM=1 \
	-e XAUTHORITY=$XAUTH \
	-e CYCLONEDDS_URI="$CYCLONEDDS_URI" \
	-e RMW_IMPLEMENTATION=rmw_cyclonedds_cpp \
	-e COLCON_DEFAULTS_FILE=/home/xplore/dev_ws/src/colcon_defaults.yaml \
	-e ROS_DOMAIN_ID=0 \
	-e REACT_APP_DDS_PROFILE=rover \
	-e REACT_APP_ROS_DOMAIN_ID=0 \
	-e REACT_APP_RMW_IMPLEMENTATION=rmw_cyclonedds_cpp \
	-e REACT_APP_CYCLONEDDS_URI="$CYCLONEDDS_URI" \
	-v /tmp/.X11-unix:/tmp/.X11-unix:rw \
	-v $XAUTH:$XAUTH \
	-v /run/user/1000/at-spi:/run/user/1000/at-spi \
	-v /dev:/dev \
	-v cs_humble_desktop_home_volume:/home/xplore \
	-v "$REPO_ROOT:/home/xplore/dev_ws/src" \
	-v "$CYCLONEDDS_HOST:$CYCLONEDDS_CONTAINER:ro" \
	-w /home/xplore/dev_ws/src \
	ghcr.io/epflxplore/cs:humble-desktop \
	/bin/bash ./launch_with_server.sh
