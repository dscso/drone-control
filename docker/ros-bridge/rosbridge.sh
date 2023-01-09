#!/bin/bash
export ROS2_INSTALL_PATH=/opt/ros/foxy
export ROS2_PATH=/opt/ros/foxy

ROS_DISTRO=foxy source ${ROS2_INSTALL_PATH}/setup.bash

ros2 run ros1_bridge dynamic_bridge