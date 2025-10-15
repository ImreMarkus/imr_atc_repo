from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription()


    lidar_node = Node(
        package='my_obstacle_detector',
        executable='lidar_simulator',
        name='lidar_simulator',
        output='screen',
        emulate_tty=True,
    )


    monitor_node = Node(
        package='my_obstacle_detector',
        executable='obstacle_monitor',
        name='obstacle_monitor',
        output='screen',
        emulate_tty=True,
        parameters=[{'threshold': 0.5}],
    )


    ld.add_action(lidar_node)
    ld.add_action(monitor_node)


    return ld