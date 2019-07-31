#!/usr/bin/env python
from multiprocessing import Process,Queue
import os,random,time,sys
import rospy 
from uwb.msg import Point
from uwb.msg import Uwb_msgs
import cv2
from sensor_msgs.msg import Image
class mymulti:    
    def prostart(self):
        self.p.start()
    def __init__(self):
        self.q=Queue(10)
        self.p=Process(target=self.listener,args=(self.q,))
    def __del__(self):
        pass#self.p.join()
    def callback(self,data,args):
        q=args[0]
        #rospy.loginfo(rospy.get_caller_id() + "I heard ")
        #rospy.loginfo(data.quaposi[0].x)
        #q.put(data)
        if q.full():
            q.get()
            q.put(data)
          #  rospy.loginfo("put ok,but the queue is full!!!")
        else:
            q.put(data)
           # rospy.loginfo("put ok,but the queue is still not full")
       # rospy.loginfo(data.perposi)
    def listener(self,q):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("chatter", Uwb_msgs, self.callback,(q,))
        rospy.spin()

class mygetimg:
    def prostart(self):
        self.p.start()
    def __init__(self):
        self.q=Queue(10)
        self.p=Process(target=self.listener,args=(self.q,))
    def __del__(self):
        pass#self.p.join()
    def callback(self,data,args):
        q=args[0]
        #rospy.loginfo(rospy.get_caller_id() + "I heard ")
        #rospy.loginfo(data.quaposi[0].x)
        #q.put(data)
        if q.full():
            q.get()
            q.put(data)
          #  rospy.loginfo("put ok,but the queue is full!!!")
        else:
            q.put(data)
           # rospy.loginfo("put ok,but the queue is still not full")
       # rospy.loginfo(data.perposi)
    def listener(self,q):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber("test_cam_video", Image, self.callback,(q,))
        rospy.spin()

atry = mymulti()
aimg=mygetimg()

