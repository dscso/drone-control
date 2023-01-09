#!/bin/bash
echo "setting variables..."
export ROS1_INSTALL_PATH=/opt/ros/noetic
export ROS1_PATH=/opt/ros/noetic
export ROS2_INSTALL_PATH=/opt/ros/foxy
export ROS2_PATH=/opt/ros/foxy


ROS_DISTRO=noetic source ${ROS1_INSTALL_PATH}/setup.bash
ROS_DISTRO=foxy source ${ROS2_INSTALL_PATH}/setup.bash


echo "done!"
exec "$@"
