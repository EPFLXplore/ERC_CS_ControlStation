# Mode  -> 0: ?, ...
# x     -> position x
# y     -> position y
# theta -> orientation theta

# Check if four arguments are passed
if [ "$#" -ne 4 ]; then
    echo "Usage: $0 <mode integer> <pose x float1> <pose y float2> <theta float3>"
    exit 1
fi

# Check if the first argument is an integer
if ! [[ "$1" =~ ^[0-9]+$ ]]; then
    echo "Error: $1 is not an integer."
    exit 1
fi

# Check if the second argument is a float
if ! [[ "$2" =~ ^[+-]?[0-9]*[.]?[0-9]+$ ]]; then
    echo "Error: $2 is not a float."
    exit 1
fi

# Check if the third argument is a float
if ! [[ "$3" =~ ^[+-]?[0-9]*[.]?[0-9]+$ ]]; then
    echo "Error: $3 is not a float."
    exit 1
fi

# Check if the fourth argument is a float
if ! [[ "$4" =~ ^[+-]?[0-9]*[.]?[0-9]+$ ]]; then
    echo "Error: $4 is not a float."
    exit 1
fi

# Store the parameter in a variable
mode=$1
x=$2
y=$3
theta=$4

ros2 action send_goal -f /Rover/Nav/NavigationReachGoal custom_msg/action/NAVReachGoal "{mode: $mode, goal: {x: $x, y: $y, theta: $theta}}"