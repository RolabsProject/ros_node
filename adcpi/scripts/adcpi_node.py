#!/usr/bin/env python


import rospy
from adcpi import adcpi
from std_msgs.msg import Float32MultiArray


def adcpi_node():
    global adcpiCap

    pub = rospy.Publisher('capteurs', Float32MultiArray )
    pub_dist = rospy.Publisher('distance', Float32MultiArray )
    rospy.init_node('adcpi_node', anonymous=True)
    r = rospy.Rate(10) # 10hz
   
    while not rospy.is_shutdown():

        val_capteurs = []
        val_distance = []
        for i in range(0, 4+1):
		val_capteurs.append( adcpiCap.capteurRead(i) )
		dist_value = 12/adcpiCap.capteurRead(i);
		if(dist_value > 30):
			 val_distance.append( 30 )
         	else:
			val_distance.append( dist_value ) 
	capteurs = Float32MultiArray()
	distance = Float32MultiArray()
        
	capteurs.data = val_capteurs
        distance.data = val_distance
		
	pub.publish(capteurs)
        pub_dist.publish(distance)
		
        r.sleep()
        
if __name__ == '__main__':
    global adcpiCap
    adcpiCap = adcpi()
    try:
        adcpi_node()
    except rospy.ROSInterruptException: pass
