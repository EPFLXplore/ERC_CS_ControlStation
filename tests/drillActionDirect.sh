# Actions: auto, start, down, release, up, abort, stop, close, open

# Check if 1 arguments is passed
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <mode string>"
    exit 1
fi

# Function to check if the argument is an integer
is_integer() {
    [[ "$1" =~ ^-?[0-9]+$ ]]
}

# Argument from the command line
ARG="$1"

# Check if the argument is an integer
if is_integer "$ARG"; then
    echo "You need to pass a mode: refer to the one you need in the comments"
else
    cd ../../
    source install/setup.bash

    ros2 action send_goal -f /Rover/DrillTerrain custom_msg/action/DrillCmd "{action: "$ARG"}"
fi