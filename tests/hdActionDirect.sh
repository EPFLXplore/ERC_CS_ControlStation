# Task Type -> name: "Button 1", type: 0, id: 0
#              name: "Button 2", type: 0, id: 0
#              name: "Button 3", type: 0, id: 0
#              name: "Button 4", type: 0, id: 0
#              name: "Button 5", type: 0, id: 0
#              name: "Button 6", type: 0, id: 0
#              name: "Button 7", type: 0, id: 0
#              name: "Button 8", type: 0, id: 0
#              name: "Button 9", type: 0, id: 0
#              name: "Button 10", type: 0, id: 0
#              name: "Voltmeter", type: 0, id: 0
#              name: "Metal Bar", type: 0, id: 0
#              name: "Ethernet Cable", type: 0, id: 0
#              name: "Home Position", type: 0, id: 0
#              name: "Panel A Position", type: 0, id: 0
#              name: "Panel B Position", type: 0, id: 0
#              name: "Panel C Position", type: 0, id: 0
#              name: "Pick Rock", type: 0, id: 0
#              name: "Pick Probe", type: 0, id: 0

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