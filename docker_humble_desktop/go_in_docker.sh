#!/usr/bin/env bash
# If not working, first do: sudo rm -rf /tmp/.docker.xauth
# If still not working, try running the script as root.
#
# Off-rover use: CycloneDDS config is **cyclonedds_outside_rover.xml** (next to this script).
# For developers testing on a laptop **not** joined to the rover LAN (home, office, etc.).
# Expected layout:
#   docker_humble_desktop/
#     cyclonedds_outside_rover.xml  run_outside_rover.sh  ...

echo "Opening http://localhost:3000/ in Chrome (new tab if Chrome is already running) ..."
# Omit --new-window so the existing Chrome process opens a tab instead of another window.
google-chrome "http://localhost:3000/" >/dev/null 2>&1 &
sleep 1

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

CYCLONEDDS_HOST="$SCRIPT_DIR/cyclonedds_outside_rover.xml"
if command -v realpath >/dev/null 2>&1; then
	CYCLONEDDS_HOST="$(realpath "$CYCLONEDDS_HOST")"
fi

CYCLONEDDS_CONTAINER="/etc/cyclonedds.xml"
CYCLONEDDS_URI="file://${CYCLONEDDS_CONTAINER}"
# The container always sees the file at /etc/cyclonedds.xml, so the URI cannot tell you which
# profile is mounted. Pass the host file name through for the CS "Data Path" panel to show.
CYCLONEDDS_FILE="$(basename "$CYCLONEDDS_HOST")"

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

CONTAINER_NAME=cs_humble_desktop

if docker container inspect "$CONTAINER_NAME" >/dev/null 2>&1; then
	echo "Reusing existing container $CONTAINER_NAME (docker exec — Cyclone XML is from container create, not remounted)."
	echo "To remount cyclonedds_outside_rover.xml:  docker rm -f $CONTAINER_NAME  then run this script again."
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

echo "Running docker (off-rover CycloneDDS profile) — new container"

if [ ! -f "$CYCLONEDDS_HOST" ]; then
	echo "Error: Cyclone DDS off-rover config not found: $CYCLONEDDS_HOST" >&2
	echo "Place cyclonedds_outside_rover.xml next to run_outside_rover.sh under: $SCRIPT_DIR" >&2
	exit 1
fi

echo "CycloneDDS: mounting off-rover host file"
echo "  $CYCLONEDDS_HOST"
echo "  -> ${CYCLONEDDS_CONTAINER} (read-only)"
echo "  CYCLONEDDS_URI=${CYCLONEDDS_URI}"
echo ""
echo "Container start: rosbridge + frontend (npm) + ssh_backend (see launch_with_server.sh)"
echo ""
echo "Sanity checks inside the container:"
echo "  sed -n '1,20p' /etc/cyclonedds.xml   # should match host cyclonedds_outside_rover.xml"
echo "  env | grep -E 'CYCLONEDDS_URI|RMW_IMPLEMENTATION'"
echo "  ros2 daemon stop && ros2 topic list | head"
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
	-e REACT_APP_DDS_PROFILE=outside \
	-e REACT_APP_ROS_DOMAIN_ID=0 \
	-e REACT_APP_RMW_IMPLEMENTATION=rmw_cyclonedds_cpp \
	-e REACT_APP_CYCLONEDDS_URI="$CYCLONEDDS_URI" \
	-e REACT_APP_CYCLONEDDS_FILE="$CYCLONEDDS_FILE" \
	-v /tmp/.X11-unix:/tmp/.X11-unix:rw \
	-v $XAUTH:$XAUTH \
	-v /run/user/1000/at-spi:/run/user/1000/at-spi \
	-v /dev:/dev \
	-v cs_humble_desktop_home_volume:/home/xplore \
	-v "$REPO_ROOT:/home/xplore/dev_ws/src" \
	-v "$CYCLONEDDS_HOST:$CYCLONEDDS_CONTAINER:ro" \
	-w /home/xplore/dev_ws/src \
	ghcr.io/epflxplore/cs:humble-desktop \
	/bin/bash
