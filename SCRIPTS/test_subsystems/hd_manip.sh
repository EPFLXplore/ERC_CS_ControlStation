# Check if two arguments are passed
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <task type integer> <task id integer>"
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
task_type=$1
task_id=$2

ros2 action send_goal -f /Rover/HandlingDeviceManipulation custom_msg/action/HDManipulation "{task_type: $task_type, task_id: $task_id}"