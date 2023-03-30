#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64
def callback(msg):
  print (msg)
rospy.init_node("first_subscriber")
rospy.Subscriber('first_topic',Int64, callback)
rospy.spin() # spin() simply keeps python from exiting until this node is stopped
