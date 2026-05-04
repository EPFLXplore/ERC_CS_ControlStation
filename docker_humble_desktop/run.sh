#!/usr/bin/env bash
# If not working, first do: sudo rm -rf /tmp/.docker.xauth
# If still not working, try running the script as root.
#
# Expected layout (repo stays as-is; cyclonedds lives next to this script):
#   docker_humble_desktop/
#     attach.sh  build.sh  compose.yaml  cyclonedds.xml  Dockerfile  run_cs.sh  run.sh

echo "Launching Chrome at http://localhost:3000/ ..."
google-chrome --new-window "http://localhost:3000/" >/dev/null 2>&1 &
sleep 1

# Use $0 so the script still works if invoked as `sh run.sh` (dash has no BASH_SOURCE).
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

CYCLONEDDS_HOST="$SCRIPT_DIR/cyclonedds.xml"
if command -v realpath >/dev/null 2>&1; then
	CYCLONEDDS_HOST="$(realpath "$CYCLONEDDS_HOST")"
fi

# Inside the container: bind-mount host cyclonedds.xml here (not under /home/xplore,
# or the named volume on /home/xplore could hide it).
CYCLONEDDS_CONTAINER="/etc/cyclonedds.xml"
# CYCLONEDDS_URI must match CYCLONEDDS_CONTAINER (three slashes after file:).
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
echo "Running docker..."

if [ ! -f "$CYCLONEDDS_HOST" ]; then
	echo "Error: Cyclone DDS config not found: $CYCLONEDDS_HOST" >&2
	echo "Place cyclonedds.xml next to run.sh under: $SCRIPT_DIR" >&2
	exit 1
fi

echo "CycloneDDS: mounting host file"
echo "  $CYCLONEDDS_HOST"
echo "  -> ${CYCLONEDDS_CONTAINER} (read-only)"
echo "  CYCLONEDDS_URI=${CYCLONEDDS_URI}"
echo ""
echo "Container start: rosbridge + frontend (npm) + ssh_backend (see launch_with_server.sh)"
echo ""

docker run -it \
	--name cs_humble_desktop \
	--rm \
	--privileged \
	--net=host \
	-e DISPLAY=unix$DISPLAY \
	-e QT_X11_NO_MITSHM=1 \
	-e XAUTHORITY=$XAUTH \
	-e CYCLONEDDS_URI="$CYCLONEDDS_URI" \
	-e RMW_IMPLEMENTATION=rmw_cyclonedds_cpp \
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
