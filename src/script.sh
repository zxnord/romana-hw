#!/bin/bash

export HOME=/home/ubuntu

cd $HOME

source /opt/ros/kilted/setup.bash
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
source /home/ubuntu/romana-hw/install/setup.bash

#nohup /usr/bin/python3 /home/ubuntu/romana-hw/src/romana_controller/romana_controller/romana_serial_node.py >> /var/log/romana_serial.log 2> /var/log/romana_serial_error.log &
#nohup /usr/bin/python3 /home/ubuntu/romana-hw/src/romana_controller/romana_controller/romana_software_node.py >> /var/log/romana_software.log 2> /var/log/romana_software_error.log &

nohup ros2 run romana_controller romana_serial_node >> /var/log/romana_serial.log 2> /var/log/romana_serial_error.log &
nohup ros2 run romana_controller romana_software_node >> /var/log/romana_software.log 2> /var/log/romana_software_error.log &

exit 0

