#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import serial

class MyNode(Node):

    def __init__(self):
        super().__init__("romana_serial")
        self._publisher = self.create_publisher(String, "/peso_romana", 10)
        self._port = serial.Serial("/dev/serial0", baudrate=9600, timeout=0.0001)
        self._timer = self.create_timer(0.00005, self.leer_valores_romana)
        self.get_logger().info("Romana Serial node ha sido creado con exito.")

    def leer_valores_romana(self):
        val = bytearray()
        while 1:
            val += self._port.read(self._port.in_waiting or 1)
            if val :
                self.enviar_peso_romana(val)
                break


    def enviar_peso_romana(self, data):
        val = String()
        val.data = str(data, 'utf-8')
        self._publisher.publish(val)
        self.get_logger().info("Peso publicado.")

def main(args=None):
    rclpy.init(args=args)

    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()