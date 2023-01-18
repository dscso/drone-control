#!/usr/bin/env python
import rospy
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist
import time
import os

global land
global takeoff
global move

# there is some bug with action.angular.z... the program does not stop on ctrl+c
def exit():
    global land
    land.publish()
    time.sleep(2)
    os._exit(0)

def talker():
    global takeoff
    global land
    global move
    takeoff = rospy.Publisher('/bebop/takeoff', Empty, queue_size=1)
    land = rospy.Publisher('/bebop/land', Empty, queue_size=1)
    move = rospy.Publisher('/bebop/cmd_vel', Twist, queue_size=1)
    rospy.init_node('test', anonymous=True)
    rospy.on_shutdown(exit)
    print("Waiting till the drone may be happy...")
    time.sleep(3) # je sais pas pourqui

    print("takeoff")
    takeoff.publish()

    time.sleep(5)

    for i in range(1000):
        action = Twist()
        action.angular.z = 1
        #action.linear.z = 1
        print(action)
        move.publish(action)
        time.sleep(.5)
        action = Twist()
        action.angular.z = -1
        print(action)
        move.publish(action)
        time.sleep(.5)


    print("land")
    land.publish()

if __name__ == '__main__':
    talker()