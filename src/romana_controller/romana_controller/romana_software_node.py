#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import serial

class MyNode(Node):

    def __init__(self):
        super().__init__("romana_serial")
        self._subscription = self.create_subscription(String, "/peso_romana", self.leer_valores_romana)
        self._port = serial.Serial("/dev/ttyGS0", baudrate=9600, timeout=3.0)
        self._timer = self.create_timer(2.0, self.leer_valores_romana)
        self.get_logger().info("Romana Serial node ha sido creado con exito.")

    def leer_valores_romana(self, valor: String):
        self.enviar_peso_romana(valor.data)

    def enviar_peso_romana(self, data: str):
        self._port.write(bytearray(data, 'utf-8'))
        self.get_logger().info("Peso enviado a USB COM.")

def main(args=None):
    rclpy.init(args=args)

    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()