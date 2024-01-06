import launch
from launch.substitutions import Command, LaunchConfiguration
import launch_ros
import os

def generate_launch_description():
    pkg_share = launch_ros.substitutions.FindPackageShare(package='sam_bot_description').find('sam_bot_description')
    default_model_path = os.path.join(pkg_share, 'src/description/sam_bot.xacro')
    default_rviz_config_path = os.path.join(pkg_share, 'rviz/urdf_config.rviz')
    world_path=os.path.join(pkg_share, 'world/my_world.sdf')
    
    robot_state_publisher_node = launch_ros.actions.Node(
        #robot state publisher should be run with the robot description from xacro file
        ### your code from here ###

        ### your code ends here ###
    )
    joint_state_publisher_node = launch_ros.actions.Node(
        #using joint state publisher gui to rotate the joints of the robot in rviz
        ### your code from here ###

        ### your code ends here ###
    )
    rviz_node = launch_ros.actions.Node(
        #rviz should be run with the config file from rviz folder
        ### your code from here ###

        ### your code ends here ###
    )

    return launch.LaunchDescription([
        ### your code from here ###

        ### your code ends here ###
    ])
