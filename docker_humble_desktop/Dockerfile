###########################################
# Xplore Control Station image Build Docker
###########################################
FROM ghcr.io/epflxplore/docker_commons:humble-desktop

ARG DEBIAN_FRONTEND=noninteractive

# Install CS packages
RUN echo "Install packages ROS"
RUN apt-get update && apt-get upgrade -y
# RUN apt-get install -y ros-${ROS_DISTRO}-rosbridge-server  --> To add when they release the version with ros2 actions
RUN apt-get install curl

# nvm environment variables
WORKDIR /usr/local/nvm
ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 20.14.0

# install nvm
# https://github.com/creationix/nvm#install-script
RUN curl --silent -o- https://raw.githubusercontent.com/creationix/nvm/v0.39.7/install.sh | bash

# add node and npm to path so the commands are available
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

RUN ls $NVM_DIR

# Add USB rules
RUN echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="03e7", MODE="0666"' | sudo tee /etc/udev/rules.d/80-movidius.rules
RUN /etc/init.d/udev restart

USER $USERNAME

# install node and npm
SHELL ["/bin/bash", "-c", "source $NVM_DIR/nvm.sh"]
RUN nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" \
    && [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" \
    && nvm use default

# Set a diretory to store the project
WORKDIR /home/$USERNAME/dev_ws/src
COPY . .

# Set a directory to build the project
WORKDIR /home/$USERNAME/dev_ws

# Clean up
RUN sudo rm -rf /var/lib/apt/lists/*
