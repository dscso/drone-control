#!/bin/bash
export ROS1_INSTALL_PATH=/opt/ros/noetic
export ROS1_PATH=/opt/ros/noetic

ROS_DISTRO=noetic source ${ROS1_INSTALL_PATH}/setup.bash

roscore