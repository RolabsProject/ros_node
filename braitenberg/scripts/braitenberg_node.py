#!/usr/bin/env python

import rospy
from numpy import *
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray, ByteMultiArray


def callback(data):
   # print data
    
    Vx    = 0
    Vy    = 0
    theta = 0

    array_coefVy    = array([-8, -20, -32, -20, -8])
    array_coefTheta = array([-1, -5, +2, +5, +1])
    array_capteur = array(data.data)

    array_vy    =  array_coefVy    *  array_capteur
    array_theta =  array_coefTheta *  array_capteur

    Vy    = 64 + array_vy.sum()
    theta = 0  + array_theta.sum()

    #Cast des valeurs
    if Vx > 127:
        Vx = 127
    elif Vx < (-127):
        Vx = -127
    if Vy > 127:
        Vy = 127
    elif Vy <(-127):
        Vy = -127
	
    cmdstr = str(int(Vx)) + " " + str(int(Vy)) + " " + str(int(theta))
    rospy.loginfo(cmdstr)
    
    pub = rospy.Publisher('cmd', String) #, queue_size=10)
    pub.publish(cmdstr)



    
def braitenberg():

    rospy.init_node('braitenberg', anonymous=True)
    rospy.Subscriber('capteurs', Float32MultiArray, callback)
    rospy.spin()

    r = rospy.Rate(10) # 10hz
   

    while not rospy.is_shutdown():
        r.sleep()
        
if __name__ == '__main__':
    try:
        braitenberg()
    except rospy.ROSInterruptException: pass
