#!/bin/bash

# Check if the container 'cs_humble_desktop' is running
if [ -z "$(docker ps -q -f name=cs_humble_desktop)" ]; then
    # Container is not running, execute the commands
    echo "Container cs_humble_desktop is not running."

    # Change directory and run the script
    cd docker_humble_desktop
    ./run_cs.sh

    # Wait for 10 seconds
    sleep 10

    # Execute further commands inside the running container
    docker exec cs_humble_desktop bash -c "cd src && ./launch.sh"
else
    # Container is running, run it interactively
    echo "Container cs_humble_desktop is running."
    
    # Start the container in interactive mode
    docker exec -it cs_humble_desktop bash

    # After starting, change directory and execute the script
    docker exec cs_humble_desktop bash -c "cd src && ./launch.sh"
fi
