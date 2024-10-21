from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['gzserver', '~/ros2_ws/src/drone_sim/worlds/myworld.world', '--verbose'],
            output='screen'),
        ExecuteProcess(
            cmd=['gzclient'],
            output='screen'),
    ])
