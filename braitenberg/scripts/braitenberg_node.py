#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from cmdMoteur.msg import Cmd


def callback(data):
    rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.axes)
    
def braitenberg():

    rospy.init_node('braitenberg', anonymous=True)

    rospy.Subscriber("joy", Joy, callback)

    rospy.spin()


    pub = rospy.Publisher('cmd', String) #, queue_size=10)
    r = rospy.Rate(10) # 10hz
   

    while not rospy.is_shutdown():


	#Cast des valeurs
	if Vx > 127:
	    Vx = 127
	elif Vx < (-127):
	    Vx = -127
	if Vy > 127:
	    Vy = 127
	elif Vy <(-127):
	    Vy = -127
	
        str = %Vx+"_"+%Vy+"_"+theta
        rospy.loginfo(str)
        pub.publish(str)
        r.sleep()
        
if __name__ == '__main__':
    try:
        braitenberg()
    except rospy.ROSInterruptException: pass
