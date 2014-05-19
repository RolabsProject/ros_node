#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talkerCmd():
    pub = rospy.Publisher('cmd', String) #, queue_size=10)
    rospy.init_node('talkerCmd', anonymous=True)
    r = rospy.Rate(10) # 10hz
    i = 0
    sens = 1
    while not rospy.is_shutdown():
	
	if  ( ( i>= -100) and (i<=100) ):
	    if (sens == 1):
		i+=1
            else:
                i-=1

	if ( (i>=100) and (sens == 1) ):
	    sens = 0

	if ( (i<= -100) and (sens == 0) ):
            sens = 1
	
        str = "0 0 %d"%i
        rospy.loginfo(str)
        pub.publish(str)
        r.sleep()
        
if __name__ == '__main__':
    try:
        talkerCmd()
    except rospy.ROSInterruptException: pass
