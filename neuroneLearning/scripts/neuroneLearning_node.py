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
#!/usr/bin/env python

import rospy
from cmdMoteur import cmdMoteur
from std_msgs.msg import String

def callback(data):
    global myCmdMoteur
    #rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.data)
    cmd = data.data.split(' ')
    Vx = int(cmd[0])
    Vy = int(cmd[1])
    theta = int(cmd[2])
    rospy.loginfo("Vx : %d\tVy : %d\tTheta : %d "%(Vx, Vy, theta) )
    myCmdMoteur.envoiCommande(Vx,Vy,theta)

def cmdMoteur_node():
    global myCmdMoteur
    myCmdMoteur = cmdMoteur()
    rospy.init_node('cmdMoteur_node', anonymous=True)
    rospy.Subscriber("cmd", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
        
if __name__ == '__main__':
    cmdMoteur_node()
