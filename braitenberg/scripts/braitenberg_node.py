#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32
#from cmdMoteur.msg import Cmd


def callback(data):
    rospy.loginfo(rospy.get_caller_id()+"I heard %f",data.data)
    
def braitenberg():

    rospy.init_node('braitenberg', anonymous=True)

    for i in range(0, 4+1):
    	rospy.Subscriber("capteurs/capteur%d"%i, Float32, callback)

    #rospy.Subscriber("capteurs/capteur0", Float32, callback)
    rospy.spin()


    pub = rospy.Publisher('cmd', String) #, queue_size=10)
    r = rospy.Rate(10) # 10hz
   

    while not rospy.is_shutdown():
        Vx    = 0
        Vy    = 0
        theta = 0


	#Cast des valeurs
	if Vx > 127:
	    Vx = 127
	elif Vx < (-127):
	    Vx = -127
	if Vy > 127:
	    Vy = 127
	elif Vy <(-127):
	    Vy = -127
	
        str = Vx+"_"+Vy+"_"+theta
        rospy.loginfo(str)
        pub.publish(str)
        r.sleep()
        
if __name__ == '__main__':
    try:
        braitenberg()
    except rospy.ROSInterruptException: pass
