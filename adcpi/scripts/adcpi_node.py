#!/usr/bin/env python


import rospy
from adcpi import adcpi
from std_msgs.msg import Float32MultiArray


def adcpi_node():
    global capteurs

    
    capteurs = rospy.Publisher('capteurs', Float32MultiArray)

    rospy.init_node('adcpi_node', anonymous=True)
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():

	val_capteurs = []
	
	for i range(0, 4+1):	
            val_capteurs.append( capteurs.capteurRead(i)
        
	rospy.loginfo("Capteurs: " + val_capteurs)
        pub.publish(val_capteurs)
        r.sleep()
        
if __name__ == '__main__':
    global capteurs
    capteurs = adcpi()
    try:
        adcpi_node()
    except rospy.ROSInterruptException: pass
