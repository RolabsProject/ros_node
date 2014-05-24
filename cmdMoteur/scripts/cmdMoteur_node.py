#!/usr/bin/env python

import rospy
from cmdMoteur import cmdMoteur
from std_msgs.msg import String
from cmdMoteur.msg import Cmd

def callback(data):
    global myCmdMoteur
    print data
    #rospy.loginfo(rospy.get_caller_id()+"I heard %s",data.data)
    #cmd = data.data.split(' ')
    msg = Cmd(vx=int(cmd[0]),
              vy=int(cmd[1]),
              theta=int(cmd[2]))
    print vx
    print vy
    print theta
    rospy.loginfo("Vx : %d\tVy : %d\tTheta : %d "%(msg.vx, msg.vy, msg.theta) )
    myCmdMoteur.envoiCommande(msg)

def cmdMoteur_node():
    global myCmdMoteur
    myCmdMoteur = cmdMoteur()
    rospy.init_node('cmdMoteur_node', anonymous=True)
    rospy.Subscriber("cmd", Cmd, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
        
if __name__ == '__main__':
    cmdMoteur_node()
