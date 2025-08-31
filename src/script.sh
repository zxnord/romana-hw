#!/bin/bash

export HOME=/home/ubuntu

cd $HOME

source /opt/ros/kilted/setup.bash
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
source /home/ubuntu/romana-hw/install/setup.bash

nohup ros2 run romana_controller romana_serial_node >> /var/log/romana_serial.log 2> /var/log/romana_serial_error.log &

exit 0