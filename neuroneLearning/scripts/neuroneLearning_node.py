#!/usr/bin/env python
#alpha: un nombre reel auquel on donne le nom de taux d apprentissage
#x : input
#y : output exemples
#s : output recalculer
#w : coef

import rospy
import message_filters
from numpy import *
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray, ByteMultiArray


###################################################################################
def callback(data):
    global i

    global errStaticiVx 
    global errStaticiVy 
    global errStaticiTheta

    global coefVy
    global coefVx
    global coefTheta 

    global d_coefVy
    global d_coefVx
    global d_coefTheta 

    #"""""""""""""""""""""""""""""""""""""""
    alpha = 0.01

    #"""""""""""""""""""""""""""""""""""""""
    xk       = data.data[0:5] #valeurs capteurs par exemple
    yk_vx    = data.data[5]   #valeurs Vitesse x par exemple
    yk_vy    = data.data[6]   #valeurs Vitesse y par exemple
    yk_theta = data.data[7]

    #"""""""""""""""""""""""""""""""""""""""
    sk = calculeOut(xk)

    #"""""""""""""""""""""""""""""""""""""""
    #print "Xk : ", xk, "\t Vy : ", yk_vy, "\t Vx : ", yk_vx, "\t Theta : ", yk_theta, 
 
    #"""""""""""""""""""""""""""""""""""""""
    for i in range(0, 5): #5 capteurs
        d_coefVy[i]    =  d_coefVy[i]    + alpha*(yk_vy    - sk['Vy']    ) *xk[i]
        d_coefVx[i]    =  d_coefVx[i]    + alpha*(yk_vx    - sk['Vx']    ) *xk[i]
        d_coefTheta[i] =  d_coefTheta[i] + alpha*(yk_theta - sk['Theta'] ) *xk[i]

    print "\tcoefVy : ", coefVy + d_coefVy, "\tcoefVx : ", coefVx + d_coefVx, "\tcoefTheta : ", coefTheta + d_coefTheta
    i+=1

###################################################################################
def calculeOut(array_capteurs):
    #"""""""""""""""""""""""""""""""""""""""
    global coefVy
    global coefVx
    global coefTheta 

    global d_coefVy
    global d_coefVx
    global d_coefTheta

    #"""""""""""""""""""""""""""""""""""""""
    vy    =  (coefVy+d_coefVy)	     *  array_capteurs
    vx    =  (coefVx+d_coefVx)	     *  array_capteurs
    theta =  (coefTheta+d_coefTheta) *  array_capteurs

    #"""""""""""""""""""""""""""""""""""""""
    Vy    = 64 + vy.sum()
    Vx    = 0  + vx.sum()
    theta = 0  + theta.sum()

    #"""""""""""""""""""""""""""""""""""""""
    #Cast des valeurs
    if Vx > 127:
        Vx = 127
    elif Vx < (-127):
        Vx = -127
    if Vy > 127:
        Vy = 127
    elif Vy <(-127):
        Vy = -127

    return {'Vy':Vy, 'Vx':Vx ,'Theta':theta }

###################################################################################
def neuroneLearning():
    global i

    #"""""""""""""""""""""""""""""""""""""""
    rospy.init_node('neuroneLearning', anonymous=True)
    rospy.Subscriber('cmdCapteurs', Float32MultiArray, callback)
    rospy.spin()

    r = rospy.Rate(10) # 10hz
   
    while not rospy.is_shutdown():
       r.sleep()

    
    coefVy    = coefVy    + d_coefVy
    coefTheta = coefTheta + d_coefTheta

    print "coefVy : ", coefVy
    print "coefTheta : ", coefTheta
    print "i : ", i


###################################################################################
if __name__ == '__main__':
    #"""""""""""""""""""""""""""""""""""""""
    global i 
    global coefVy
    global coefVx
    global coefTheta 

    global d_coefVy
    global d_coefVx
    global d_coefTheta 

    global errStaticiVx 
    global errStaticiVy 
    global errStaticiTheta

    #"""""""""""""""""""""""""""""""""""""""
    #coefVy    = array([-8, -20, -32, -20,  -8])
    #coefTheta = array([-1,  -5,  +2,  +5,  +1])
    #coefVy    = array([-1, -10, -23, -10,  -1])
    coefVx    = array([ 0,   0,   0,   0,   0])
    coefVy    = array([ 0,   0,   0,   0,   0])
    #coefTheta = array([-0,  -1,  +1,  +2,  +0])
    coefTheta    = array([ 0,   0,   0,  0,   0])
    d_coefVy    = array([0., 0., 0., 0., 0.])
    d_coefVx    = array([0., 0., 0., 0., 0.])
    d_coefTheta = array([0., 0., 0., 0., 0.])

    errStaticiVx = 0
    errStaticiVy = 0
    errStaticiTheta = 0
    i = 0

    #"""""""""""""""""""""""""""""""""""""""
    neuroneLearning()
