#!/usr/bin/env python


import rospy
from adcpi import adcpi
from std_msgs.msg import Float32


def adcpi_node():
    global capteurs

   
    pub_capteurs = []
    for i in range(0, 4+1):
        pub_capteurs.append( rospy.Publisher('capteurs/capteur%d'%i, Float32) )
 

    rospy.init_node('adcpi_node', anonymous=True)
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():

	for i in range(0, 4+1):
        	pub_capteurs[i].publish( capteurs.capteurRead(i) )
	
        #rospy.loginfo("Capteurs: " + str(val_capteurs))
        r.sleep()
        
if __name__ == '__main__':
    global capteurs
    capteurs = adcpi()
    try:
        adcpi_node()
    except rospy.ROSInterruptException: pass
