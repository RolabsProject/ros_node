#!/usr/bin/env python

import rospy
import message_filters
from numpy import *
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray, ByteMultiArray


def callback(data):
    global i
    print data
    i+=1
    # array_capteur = array(data.data)
	# cmd = data.data.split(' ')
    # Vx = int(cmd[0])
    # Vy = int(cmd[1])
    # theta = int(cmd[2])

def callback2(data):
    global i2
    print data
    i2+=1
	
def neuroneLearning():
    global i
    global i2
    rospy.init_node('neuroneLearning', anonymous=True)
    rospy.Subscriber('capteursVal', Float32MultiArray, callback)
    rospy.Subscriber("cmd", String, callback2)
	
    ts = message_filters.TimeSynchronizer([image_sub, info_sub], 10)
    ts.registerCallback(callback)
	
    rospy.spin()
    r = rospy.Rate(10) # 10hz
   
    while not rospy.is_shutdown():
       r.sleep()
    print i
    print i2	
if __name__ == '__main__':
    global i 
    global i2
    i = 0
    i2=0
    neuroneLearning()
