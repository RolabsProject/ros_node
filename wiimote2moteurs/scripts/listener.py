#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Joy

def callback(data):
    rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.data.axis)
    
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("joy", String, callback)

    rospy.spin()
        
if __name__ == '__main__':
    listener()
