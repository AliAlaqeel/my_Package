from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='demos_nodes_cpp',
            executable='talker'
        )
    ])