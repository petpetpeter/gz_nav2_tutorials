# gz_nav2_tutorials

Welcome to the gz_nav2_tutorials wiki!
> gazebo is referred to gz_sim (former ignition)

The content is mainly imported from [Nav2 tutorial](https://navigation.ros.org/index.html)

Table of Content
1. ROS2 gazebo ros_gazebo installation
2. Simple Diff Drive robot with ros2-gazebo
3. Nav2 implementation on the simulation

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

### Task

#### Branch: `1-robot-description/task`

Task is to create a launch file that will show the robot in `rviz2`

Files to create or adjust:
  - `launch/rviz2_display.launch.py` - loading and showing robot in `rviz2` using `robot_state_publisher`, `joint_state_publisher_gui` and `rviz2` nodes

References:
  - Nav2 tutorial: [Sambot description launch file](https://github.com/ros-planning/navigation2_tutorials/blob/master/sam_bot_description/launch/display.launch.py)

Output:
  - `ros2 launch sam_bot_description rviz2_display.launch.py`
  should show the robot in `rviz2`

![task1a](https://github.com/petpetpeter/gz_nav2_tutorials/assets/55285546/66da7466-719c-44a5-8420-3d0940c5661a)

#### Branch: `2-gz-sim/task`

Task is to create a launch file that will show the robot in `gz_sim` and publish the joint states back to `ros2`
Add gz spawn node and gz_bridge to publish joint states instead of `joint_state_publisher_gui`

Pre-requisite:
- `1-robot-description/task` is completed
- ros_gz is installed

Files to create or adjust
- `src/description/sam_bot.xacro` add jointstate publisher plugin in the `sam_bot` model
- `launch/gz_display.launch.py` - loading and showing robot in `gz_sim` using `gzserver` and `gzclient` nodes

References:
- rrbot example: https://github.com/gazebosim/ros_gz/blob/humble/ros_gz_sim_demos/models/rrbot.xacro
- https://github.com/gazebosim/ros_gz/blob/humble/ros_gz_sim_demos/launch/joint_states.launch.py

Output:
- `ros2 launch sam_bot_description gz_display.launch.py`
should show the robot in `gz_sim` and publish joint states back to `ros2`

![image](https://github.com/petpetpeter/gz_nav2_tutorials/assets/55285546/5e1b640e-a7e9-42fb-8d0e-e95b52d8da00)
