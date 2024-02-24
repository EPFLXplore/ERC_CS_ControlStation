###########################################
# Xplore Control Station image Build Frontend
###########################################

FROM node:16.14.0 as build-frontend

COPY cs_ws/src/control_station_pkg/control_station_pkg/csApp/frontend .

RUN npm install

RUN npm run build



###########################################
# Xplore Control Station image Build Docker
###########################################
FROM ghcr.io/epflxplore/docker_commons:foxy-desktop as build-cs

ARG DEBIAN_FRONTEND=noninteractive

# Install CS packages
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y --no-install-recommends redis-server python-evdev
RUN apt install -y curl

# Add USB rules
RUN echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="03e7", MODE="0666"' | sudo tee /etc/udev/rules.d/80-movidius.rules
RUN /etc/init.d/udev restart

USER $USERNAME

# Set a diretory to store the project
WORKDIR /home/$USERNAME/dev_ws/src
COPY . .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir install Django==4.1.1

RUN pip install --no-cache-dir channels==3.0.5 \
    pandas==2.0.3 \
    channels-redis==3.4.1 \
    transforms3d==0.4.1 \
    scikit-image \
    autobahn==22.7.1 \
    twisted==17.9.0 \
    redis==4.3.4

RUN pip3 install websocket-client==1.4.1

# Copy the frontend build
COPY --from=build-frontend /build /home/xplore/dev_ws/src/cs_ws/src/control_station_pkg/control_station_pkg/csApp/frontend/build

# Set a directory to build the project
WORKDIR /home/$USERNAME/dev_ws

# Clean up
RUN sudo rm -rf /var/lib/apt/lists/*
