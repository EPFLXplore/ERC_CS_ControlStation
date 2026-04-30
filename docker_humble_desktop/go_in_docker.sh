#!/bin/bash
# If not working, first do: sudo rm -rf /tmp/.docker.xauth
# If still not working, try running the script as root.

# --- CycloneDDS config from host ---
if [ -z "$CYCLONEDDS_URI" ]; then
    echo "[ERROR] CYCLONEDDS_URI is not set on the host. Please set it in your ~/.bashrc:"
    echo "  export CYCLONEDDS_URI=file:///path/to/your/cyclone.xml"
    exit 1
fi
CYCLONE_FILE="${CYCLONEDDS_URI#file://}"
if [ ! -f "$CYCLONE_FILE" ]; then
    echo "[ERROR] CycloneDDS config file not found: $CYCLONE_FILE"
    exit 1
fi
echo "[INFO] Using CycloneDDS config: $CYCLONE_FILE"

echo "Launching Chrome at http://localhost:3000/ ..."
google-chrome --new-window "http://localhost:3000/" >/dev/null 2>&1 &
sleep 1

XAUTH=/tmp/.docker.xauth
echo "Preparing Xauthority data..."
xauth_list=$(xauth nlist :0 | tail -n 1 | sed -e 's/^..../ffff/')
if [ ! -f $XAUTH ]; then
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

current_dir=$(pwd)
parent_dir=$(dirname "$current_dir")

docker run -it \
    --name cs_humble_desktop \
    --rm \
    --privileged \
    --net=host \
    -e DISPLAY=unix$DISPLAY \
    -e QT_X11_NO_MITSHM=1 \
    -e XAUTHORITY=$XAUTH \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -v $XAUTH:$XAUTH \
    -v /run/user/1000/at-spi:/run/user/1000/at-spi \
    -v /dev:/dev \
    -v $parent_dir:/home/xplore/dev_ws/src \
    -v cs_humble_desktop_home_volume:/home/xplore \
    -v "$CYCLONE_FILE":"$CYCLONE_FILE":ro \
    -e CYCLONEDDS_URI="$CYCLONEDDS_URI" \
    -e RMW_IMPLEMENTATION=rmw_cyclonedds_cpp \
    ghcr.io/epflxplore/cs:humble-desktop \
    bash -lc "cd /home/xplore/dev_ws/src; \
              chmod +x ./launch_with_server.sh; \
              exec bash"