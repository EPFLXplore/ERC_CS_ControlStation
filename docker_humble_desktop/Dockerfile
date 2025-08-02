###########################################
# Xplore Control Station image Build Docker
###########################################
FROM ghcr.io/epflxplore/docker_commons:humble-desktop

ARG DEBIAN_FRONTEND=noninteractive

RUN rm /usr/share/keyrings/ros-archive-keyring.gpg
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
RUN apt update && apt install ros2-apt-source  
RUN rm /etc/apt/sources.list.d/ros2.list
RUN rm /usr/share/keyrings/ros-archive-keyring.gpg

# Install CS packages
RUN echo "Install packages ROS"
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y ros-${ROS_DISTRO}-rosbridge-server
RUN apt install ros-humble-rmw-cyclonedds-cpp -y
RUN apt install net-tools iputils-ping -y

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

USER $USERNAME

# install node and npm
SHELL ["/bin/bash", "-c", "source $NVM_DIR/nvm.sh"]
RUN nvm install $NODE_VERSION \
    && nvm alias default $NODE_VERSION \
    && [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" \
    && [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" \
    && nvm use default

# Add rosbridge dependencies
RUN pip install pymongo tornado

# Set a diretory to store the project
WORKDIR /home/$USERNAME/dev_ws/src
COPY . .

# Set a directory to build the project
WORKDIR /home/$USERNAME/dev_ws

# Clean up
RUN sudo rm -rf /var/lib/apt/lists/*

# Remove all the confidential Xplore source code from the image
RUN sudo rm -rf /home/$USERNAME/dev_ws/src/*
