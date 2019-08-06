#!/usr/bin/env python
# Refernce: https://hotblackrobotics.github.io/en/blog/2018/01/29/action-client-py/
# Created by: Marwan Taher
# Date: 31/7/2019

import tf
import sys
import rospy
from math import radians
import actionlib
from geometry_msgs.msg import Quaternion
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

rospy.init_node('movebase_client')

client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
client.wait_for_server()

goal = MoveBaseGoal()

if not rospy.is_shutdown():

    goal.target_pose.header.frame_id = "odom"
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.position.x = float(sys.argv[1])
    goal.target_pose.pose.position.y = float(sys.argv[2])#0.25
    goal.target_pose.pose.position.z = 0

    goal_quat = tf.transformations.quaternion_from_euler(0, 0,radians(float(sys.argv[3])))
    goal.target_pose.pose.orientation = Quaternion(*goal_quat)

    rospy.loginfo(goal)
    client.send_goal(goal)
