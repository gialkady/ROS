#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64
rospy.init_node("first_publisher") #initiate a node
pub=rospy.Publisher('first_topic',Int64,queue_size=1) #publish parameters
while not rospy.is_shutdown():
    pub.publish(5) #publish integer number “5”
    rospy.sleep(1)
