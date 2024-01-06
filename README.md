# gz_nav2_tutorials

Welcome to the gz_nav2_tutorials wiki!
> gazebo is referred to gz_sim (former ignition)

The content is mainly imported from [Nav2 tutorial](https://navigation.ros.org/index.html)

## Structure of this repositor
The structure of the repository follows the flow of integrating robots with NAV2 and these are the following steps:

1. Setting up the robot's URDF using XACRO
2. Spawning the robot in Gazebo
3. Simulating diff drive robot in Gazebo using diff_drive_controller plugin
4. Publishing gz topic to ROS2 topic via ros_gz_bridge
4. Navigation2 setup
5. Writing Navigation2 configuration files and plugins

## Pre-Installation
1. [ROS2 (humbel)](https://docs.ros.org/en/humble/Installation.html)
2. [gz_sim](https://gazebosim.org/docs/garden/install_ubuntu)
3. [ros_gz](https://gazebosim.org/docs/garden/ros_installation](https://github.com/gazebosim/ros_gz)https://github.com/gazebosim/ros_gz)  (required to install from src)

## Test Installation
1. Launch sam-bot example from this repo
```
git clone https://github.com/petpetpeter/gz_nav2_tutorials.git
colcon build
ros2 launch sam_bot_description gz_display.launch.py
```




