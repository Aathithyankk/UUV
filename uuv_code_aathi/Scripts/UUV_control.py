#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
import math 
#import numpy as np
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Wrench

prev_x=prev_y=prev_z=pe_x=pe_y=pe_z=pe_yaw=td_x=td_y=td_z=tt=0
ip = Wrench()

def Callback(Odom):
 #print('1')
 global prev_x,prev_y,prev_z,pe_x,pe_y,pe_z,pe_yaw,goal,ip,td_x,td_y,td_z,tt
 orient_quat = Odom.pose.pose.orientation
 orient_quat_list = [orient_quat.x,orient_quat.y,orient_quat.z,orient_quat.w]
 (roll, pitch, yaw) = euler_from_quaternion(orient_quat_list)
 x = Odom.pose.pose.position.x
 y = Odom.pose.pose.position.y
 z = Odom.pose.pose.position.z
 d_x = goal[0]-x
 d_y = goal[1]-y
 d_z = goal[2]-z
 theta = math.atan2(d_y,d_x)-yaw
 ip.force.x = 0.001*d_x + 0.06*(d_x-pe_x)+0.05*td_x
 pe_x = d_x
 td_x+=d_x
 ip.force.y = 0.001*d_y + 0.06*(d_y-pe_y)+0.05*td_y
 pe_y = d_y
 td_y+=d_y
 ip.force.z = 0.004*d_z + 0.06*(d_z-pe_z)+0.01*td_z
 pe_z = d_z
 td_z+=d_z
 #ip.torque.z = 4*theta + 6*(theta-pe_yaw)+0.5*tt
 #pe_yaw = theta
 #tt+=theta
 ip.torque.x = ip.torque.y = ip.torque.z = 0
 pub.publish(ip)
 #print('1') 

#def publisher():
# rate = rospy.Rate(10)
# while(True):
#  ip.force.x = 0
#  ip.force.y = 0
#  ip.force.z = -400
#  ip.torque.x = 0
#  ip.torque.y = 0
#  ip.torque.z = 0
#  pub.publish(ip)
#  rate.sleep()

 if ((goal[0] == x) & (goal[1] == y) & (goal[2] == z)):
  rospy.signal_shutdown('The UUV_reached the goal')
if __name__ =="__main__":
 rospy.init_node('UUV_control',anonymous = True)
 global pub
 pub = rospy.Publisher('/rexrov/thruster_manager/input',Wrench,queue_size=100)
 #publisher() 
 global goal
 goal = []
 goal.append(20)
 goal.append(20)
 goal.append(-20) 
 rospy.Subscriber('/rexrov/pose_gt',Odometry,Callback)
 rospy.spin()
 



