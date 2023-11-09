###########################################
# Xplore Control Station image
###########################################
FROM ghcr.io/epflxplore/docker_commons:foxy-desktop

ARG DEBIAN_FRONTEND=noninteractive

# Install ROS 2 Nav packages
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y --no-install-recommends \
    redis-server \
    python-evdev

RUN python3 -m pip install Django==4.1.1

RUN pip install channels==3.0.5 \
    channels-redis \
    transforms3d \
    scikit-image \
    autobahn \
    twisted==17.9.0 \
    redis==4.3.4

RUN pip3 install websocket-client==1.4.1

# Add USB rules
RUN echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="03e7", MODE="0666"' | sudo tee /etc/udev/rules.d/80-movidius.rules
RUN /etc/init.d/udev restart

USER $USERNAME

# Set a diretory to store the project
WORKDIR /home/$USERNAME/dev_ws/src
COPY . .

# Set a directory to build the project
WORKDIR /home/$USERNAME/dev_ws

# Install ROS 2 Nav dependencies
RUN rosdep update \
    && rosdep install -i --from-path src --rosdistro $ROS_DISTRO -y --skip-keys "libg2o g2o"

# Clean up
RUN sudo rm -rf /var/lib/apt/lists/*