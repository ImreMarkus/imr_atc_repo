import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String


class ObstacleMonitor(Node):
    def __init__(self):
        super().__init__('obstacle_monitor')
        self.declare_parameter('threshold', 0.5)
        self.threshold = float(self.get_parameter('threshold').get_parameter_value().double_value)
        self.sub = self.create_subscription(Float32, 'distance', self.distance_callback, 10)
        self.alert_pub = self.create_publisher(String, 'alert', 10)
        self.get_logger().info(f'ObstacleMonitor started, threshold = {self.threshold:.2f} m')


    def distance_callback(self, msg: Float32):
        dist = float(msg.data)
        self.get_logger().debug(f'Received distance: {dist:.2f}')
        if dist < self.threshold:
            alert = String()
            alert.data = f'Obstacle detected at {dist:.2f} m'
            self.alert_pub.publish(alert)
            self.get_logger().warn(f'** ALERT: Obstacle at {dist:.2f} m **')




def main(args=None):
    rclpy.init(args=args)
    node = ObstacleMonitor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('ObstacleMonitor: shutdown requested')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()