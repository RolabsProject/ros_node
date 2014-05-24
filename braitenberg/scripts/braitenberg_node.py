#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray, ByteMultiArray


def callback(data):
   # print data

    Vx    = 0
    Vy    = 0
    theta = 0


    Vy = 64 -32*int(data.data[2]) -16*int(data.data[1]) -16*int(data.data[3]) -8*int(data.data[0]) -8*int(data.data[4])


    #Cast des valeurs
    if Vx > 127:
        Vx = 127
    elif Vx < (-127):
        Vx = -127
    if Vy > 127:
        Vy = 127
    elif Vy <(-127):
        Vy = -127
	
    cmdstr = str(Vx) + "_" + str(Vy) + "_" + str(theta)
    rospy.loginfo(cmdstr)
    pub.publish(cmdstr)



    
def braitenberg():

    rospy.init_node('braitenberg', anonymous=True)
    rospy.Subscriber('capteurs', Float32MultiArray, callback)
    rospy.spin()

    pub = rospy.Publisher('cmd', String) #, queue_size=10)
    r = rospy.Rate(10) # 10hz
   

    while not rospy.is_shutdown():
        r.sleep()
        
if __name__ == '__main__':
    try:
        braitenberg()
    except rospy.ROSInterruptException: pass
