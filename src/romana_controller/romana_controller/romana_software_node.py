#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

import serial

class MyNode(Node):

    def __init__(self):
        super().__init__("romana_serial")
        self._publisher = self.create_publisher(Int64, "/peso_romana", 10)
        #self._port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3.0)
        self._timer = self.create_timer(2.0, self.leer_valores_romana)
        self.get_logger().info("Romana Serial node ha sido creado con exito.")

    def leer_valores_romana(self):
        # val = self._port.readline()
        # parse readline
        data = 50
        self.enviar_peso_romana(data)


    def enviar_peso_romana(self, data):
        val = Int64()
        val.data = data
        self._publisher.publish(val)
        self.get_logger().info("Peso publicado.")

def main(args=None):
    rclpy.init(args=args)

    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()