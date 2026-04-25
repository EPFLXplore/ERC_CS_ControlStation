#!/bin/bash
# If not working, first do: sudo rm -rf /tmp/.docker.xauth
# If still not working, try running the script as root.
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
if docker ps --format '{{.Names}}' | grep -Fxq cs_humble_desktop; then
    echo "Container cs_humble_desktop is already running. Opening a shell in it..."
    docker exec -it -e RMW_IMPLEMENTATION=rmw_cyclonedds_cpp -e CYCLONEDDS_URI="file:///cyclone.xml" cs_humble_desktop bash
    exit 0
fi
if docker ps -a --format '{{.Names}}' | grep -Fxq cs_humble_desktop; then
    echo "Removing stale container cs_humble_desktop..."
    docker rm cs_humble_desktop >/dev/null
fi
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
    -v /home/mehdi/ERC_CS_ControlStation/docker_humble_desktop/cyclonedds.xml:/cyclone.xml:ro \
    -e CYCLONEDDS_URI="file:///cyclone.xml" \
    -e RMW_IMPLEMENTATION=rmw_cyclonedds_cpp \
    ghcr.io/epflxplore/cs:humble-desktop \
    bash -lc "cd /home/xplore/dev_ws/src; \
              chmod +x ./launch_with_server.sh; \
              ./launch_with_server.sh; \
              exec bash"
