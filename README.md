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


### 1. 📑 Setting up the hardware description for *ros2_control*
##### GOAL
  - learn how to setup the URDF of a robot using XACRO macros

##### 🗒 Setting up URDF using XACRO for a robot

For any robot that is used with ROS/ROS2 an URDF description is needed.
This description holds information about kinematics, visualization (e.g., for Rviz2) and collision data.
This description is also used by popular ROS2 high-level libraries like, MoveIt2, Nav2 and Simulators.

In this excercise we will focus on setting up the description using the XACRO format which is highly configurable and parameterizable and generally better to use than the static URDF format.

##### Task

Branch: `1-robot-description/task`

Task is to create a launch file that will show the robot in `rviz2`

Files to create or adjust:
  - `launch/rviz2_display.launch.py` - loading and showing robot in `rviz2` using `robot_state_publisher`, `joint_state_publisher_gui` and `rviz2` nodes

References:
  - Nav2 tutorail: [Sambot description launch file](https://github.com/ros-planning/navigation2_tutorials/blob/master/sam_bot_description/launch/display.launch.py)

Output:
  - `ros2 launch gz_nav2_tutorials rviz2_display.launch.py`
  should show the robot in `rviz2`

![task1a](https://github.com/petpetpeter/gz_nav2_tutorials/assets/55285546/66da7466-719c-44a5-8420-3d0940c5661a)


  

