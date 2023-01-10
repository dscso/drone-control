#!/bin/bash

export ROS1_INSTALL_PATH=/opt/ros/melodic
ROS_DISTRO=melodic source ${ROS1_INSTALL_PATH}/setup.bash
source /root/bebop_ws/devel/setup.bash
export LD_LIBRARY_PATH=/opt/ros/melodic/lib/parrot_arsdk:/opt/ros/melodic/lib/:$LD_LIBRARY_PATH
export CATKIN_WS="~/catkin_ws"

exec "$@"