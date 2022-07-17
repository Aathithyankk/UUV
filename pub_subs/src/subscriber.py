#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry

def Callback(Pose):
 x = Pose.pose.pose.position.x
 y = Pose.pose.pose.position.y
 z = Pose.pose.pose.position.z
 print("x = " + str(x)+" y = "+str(y)+" z = "+str(z))
 

if __name__ =="__main__":
 rospy.init_node("subscriber",anonymous='true')
 rospy.Subscriber('/rexrov/pose_gt',Odometry,Callback)
 rospy.spin()

