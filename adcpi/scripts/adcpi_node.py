#!/usr/bin/env python


import rospy
from adcpi import adcpi
from std_msgs.msg import String


def adcpi_node():
    global capteurs
    pub = rospy.Publisher('capteurs', String)
    rospy.init_node('adcpi_node', anonymous=True)
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        str = "%f %f %f %f %f"%(	capteurs.capteurRead(0), 
									capteurs.capteurRead(1), 
									capteurs.capteurRead(2), 
									capteurs.capteurRead(3), 
									capteurs.capteurRead(4) ) 
        rospy.loginfo(str)
        pub.publish(str)
        r.sleep()
        
if __name__ == '__main__':
    global capteurs
    capteurs = adcpi()
    try:
        adcpi_node()
    except rospy.ROSInterruptException: pass
