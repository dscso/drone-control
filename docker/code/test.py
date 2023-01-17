#!/usr/bin/env python
import rospy
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
import time
import os

def talker():
    takeoff = rospy.Publisher('/bebop/takeoff', Empty, queue_size=1)
    land = rospy.Publisher('/bebop/land', Empty, queue_size=1)
    move = rospy.Publisher('/bebop/cmd_vel', Twist, queue_size=1)
    rospy.init_node('test', anonymous=True)
    rospy.on_shutdown(land.publish)
    print("Waiting till the drone may be happy...")
    time.sleep(3) # je sais pas pourqui

    print("takeoff")
    takeoff.publish()

    time.sleep(3)

    for i in range(5):
        action = Twist()
        action.linear.x = 10
        move.publish(action)
        time.sleep(2)
        action = Twist()
        action.linear.y = 10
        move.publish(action)
        time.sleep(2)
        action = Twist()
        action.linear.y = -10
        action.linear.x = -10
        move.publish(action)

    print("land")
    land.publish()

def move_left(move, amount):
    action = Twist()
    action.linear.x = amount
    move.publish(action)

if __name__ == '__main__':
    talker()