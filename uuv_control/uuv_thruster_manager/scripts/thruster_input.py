#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Wrench

if __name__=="__main__":
 pub = rospy.Publisher("/rexrov/thruster_manager/input",Wrench,queue_size=100)
 #pub1 = rospy.Publisher("/rexrov_1/thruster_manager/input",Wrench,queue_size=10)
 #rospy.Subscriber("/rexrov/pose_gt",nav_msgs/Odometry,rexrov_callback)
 #rospy.Subscriber("/rexrov1/pose_gt",nav_msgs/Odometry,rexrov_callback)
 rospy.init_node("thruster_input",anonymous=True)
 rate=rospy.Rate(10)
 input = Wrench()
 while(True):
  input.force.x = 0
  input.force.y = 0
  input.force.z = -400
  input.torque.x = 0
  input.torque.y = 0
  input.torque.z = 0
  pub.publish(input)
  #pub1.publish(input)
  rate.sleep()
 
