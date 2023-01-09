#!/bin/bash
export ROS1_INSTALL_PATH=/opt/ros/melodic

ROS_DISTRO=melodic source ${ROS1_INSTALL_PATH}/setup.bash

exec "$@"
