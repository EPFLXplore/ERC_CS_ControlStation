# Mode -> hd: {0: off, 1: manual direct, 2: manual inverse, 3: auto}


# Check if two arguments are passed
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <system integer> <mode integer>"
    exit 1
fi

# Check if the first argument is an integer
if ! [[ "$1" =~ ^[0-9]+$ ]]; then
    echo "Error: $1 is not an integer."
    exit 1
fi

# Store the parameter in a variable
mode=$1
cd ../../
source install/setup.bash
ros2 service call /HD/fsm/mode custom_msg/srv/HDMode "{mode: $mode}"
