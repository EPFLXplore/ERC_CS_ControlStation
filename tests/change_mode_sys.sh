# Check if two arguments are passed
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <system integer> <mode integer>"
    exit 1
fi

# Check if the first argument is an integer
if ! [[ "$1" =~ ^[0-9]+$ ]]; then
    echo "Error: $1 is not an integer."
    exit 1
fi

# Check if the second argument is an integer
if ! [[ "$2" =~ ^[0-9]+$ ]]; then
    echo "Error: $2 is not an integer."
    exit 1
fi

# Store the parameter in a variable
system=$1
mode=$2
cd ../../
source install/setup.bash
ros2 service call /Rover/ChangeModeSystem custom_msg/srv/ChangeModeSystem "{system: $system, mode: $mode}"
