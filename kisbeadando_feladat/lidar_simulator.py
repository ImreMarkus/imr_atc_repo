import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random


class LidarSimulator(Node):
    def __init__(self):
        super().__init__('lidar_simulator')
        self.pub = self.create_publisher(Float32, 'distance', 10)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('LidarSimulator node started, publishing on "distance" topic')


    def timer_callback(self):
        dist = random.uniform(0.2, 2.0)
        msg = Float32()
        msg.data = float(dist)
        self.pub.publish(msg)
        if random.random() < 0.2:
            self.get_logger().info(f"Simulated distance: {dist:.2f} m")




def main(args=None):
    rclpy.init(args=args)
    node = LidarSimulator()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('LidarSimulator: shutdown requested')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()