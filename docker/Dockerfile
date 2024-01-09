# https://hub.docker.com/_/ros
#FROM ros:galactic

# https://github.com/osrf/docker_images/blob/master/README.md#ros---1
# https://github.com/osrf/docker_images/blob/master/ros/galactic/ubuntu/focal/desktop/Dockerfile
FROM osrf/ros:humble-desktop

# ARG user_id=1000
ARG ros_ws=/home/dev_ws

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3-pip \
    python-is-python3 \
    python3-colcon-clean \
    make

RUN apt-get update && sudo apt install curl -y
RUN apt-get update && apt-get install -y \
    nano \
    lsb-release \
    wget \
    libgflags2.2 \
    libgflags-dev \
    libwebsocketpp-dev \
    nlohmann-json3-dev \
    libasio-dev \
    gnupg

RUN wget https://packages.osrfoundation.org/gazebo.gpg -O /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg

RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null

RUN apt-get update && apt-get install -y gz-garden libsdformat13 

RUN apt-get update && apt-get install -y \
    ros-humble-joint-state-publisher \
    ros-humble-robot-localization \
    ros-humble-plotjuggler-ros \
    ros-humble-robot-state-publisher \
    ros-humble-ros2bag \
    ros-humble-rosbag2-storage-default-plugins \
    ros-humble-rqt-tf-tree \
    ros-humble-rmw-cyclonedds-cpp \
    ros-humble-xacro \
    ros-humble-diagnostic-updater \
    ros-humble-diagnostic-aggregator \
    ros-humble-apriltag-ros \
    ros-humble-actuator-msgs \
    ros-humble-tf-transformations \
    ros-humble-navigation2 \
    ros-humble-nav2-bringup 
    
RUN apt-get update && apt-get install -y \
        ros-humble-rviz2 \
        ros-humble-rviz-common \
        ros-humble-rviz-default-plugins \
        ros-humble-rviz-visual-tools \
        ros-humble-rviz-rendering \
        ros-humble-nav2-rviz-plugins


RUN apt-get install -y \
    nano \
    less \
    xterm \
    byobu \
    python3-pcl \
    python3-opencv 
    
# Install python packages.
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt

RUN apt-get update && apt-get install -y ros-humble-foxglove-bridge

    
#    && rm -rf /var/lib/apt/lists/*

# Switch to a non-root user.
# RUN useradd -m --uid ${user_id} dockeruser
# USER dockeruser

# Working directory
WORKDIR /home

# ENVs
ENV HOME=/home
# ENV PATH="/home/dockeruser/.local/bin:${PATH}"

# Force Python stdout and stderr streams to be unbuffered.
ENV PYTHONUNBUFFERED 1


# Add sourcing to your shell startup script
# https://docs.ros.org/en/galactic/Tutorials/Configuring-ROS2-Environment.html#add-sourcing-to-your-shell-startup-script
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc

RUN echo "source /home/dev_ws/install/setup.bash" >> ~/.bashrc
RUN echo "source /home/ros_gz_ws/install/setup.bash" >> ~/.bashrc

# RUN echo "source /usr/share/gazebo/setup.sh" >> ~/.bashrc
RUN echo "GZ_VERSION=garden" >> ~/.bashrc

# ROS Dependency Management
COPY ./dev_ws/src /home/dev_ws/src

RUN cd /home/ros_gz_ws \
    && rosdep update \
    && rosdep install -y --from-paths src --ignore-src --rosdistro ${ROS_DISTRO}

# Add `colcon_cd` to your shell startup script
# https://docs.ros.org/en/galactic/Tutorials/Configuring-ROS2-Environment.html#add-colcon-cd-to-your-shell-startup-script
RUN echo "source /usr/share/colcon_cd/function/colcon_cd.sh" >> ~/.bashrc \
    && echo "export _colcon_cd_root=${ros_ws}" >> ~/.bashrc

RUN echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc

# This entrypoint is from base image.
# See https://github.com/osrf/docker_images/blob/master/ros/galactic/ubuntu/focal/ros-core/ros_entrypoint.sh

# RUN bash -c "chmod +x /ros_entrypoint.sh"
# COPY ros_entrypoint.sh /ros_entrypoint.sh
ENTRYPOINT ["/ros_entrypoint.sh"]

CMD ["sleep", "infinity"]
