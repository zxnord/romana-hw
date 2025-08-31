#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

import serial

class MyNode(Node):

    def __init__(self):
        super().__init__("romana_serial")
        self._port = serial.Serial("/dev/ttyGS0", baudrate=9600, timeout=0.001)
        self.get_logger().info("Romana Serial node ha sido creado con exito.")


    def enviar_peso_romana(self, data: bytearray):
        self._port.write(data)
        self.get_logger().info("Traza: <" + str(data, 'utf-8') + "> enviada a USB COM.")

def main(args=None):
    rclpy.init(args=args)

    node = MyNode()
    port = serial.Serial("/dev/ttySC1", baudrate=9600, timeout=0.0001)
    data = bytearray()
    while(1):
        node.get_logger().info("Antes de leer la romana")
        data = port.read(port.in_waiting or 1)
        node.get_logger().info("Despues de leer la romana")
        if data :
            node.get_logger().info("Antes de enviar a USB")
            node.enviar_peso_romana(data)
            data = bytearray()
    rclpy.shutdown()

if __name__ == '__main__':
    main()