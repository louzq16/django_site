#coding:utf-8
#!/usr/bin/env python
from django.shortcuts import render,HttpResponse
from django.http import StreamingHttpResponse
import os
import time
import json

from mymulti import aimg
import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError

cvB=CvBridge()
aimg.prostart() 


def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)

def getnewstr(request):
    #print "one"
    #st=smm.smmread()
    #result = {"data":str,}
    #json返回为中文
    #return HttpResponse(json.dumps(result))
    #return HttpResponse(st)
    pass

def add(request):
    c=5
    return HttpResponse(str(c))

def gen_1():
    while True:
        frame=aimg.q.get()
        cv_image = cvB.imgmsg_to_cv2(frame, "bgr8")
        img=cv2.imencode('.jpg',cv_image)
        yield (b'--frame\r\n'+b'Content-Type: image/jpeg\r\n\r\n' + img[1].tostring() + b'\r\n')
def video_feed_1(request):
    return StreamingHttpResponse(gen_1(),content_type='multipart/x-mixed-replace; boundary=frame')
def gen_2():
    while True:
        frame=aimg.q.get()
        cv_image = cvB.imgmsg_to_cv2(frame, "bgr8")
        img=cv2.imencode('.jpg',cv_image)
        yield (b'--frame\r\n'+b'Content-Type: image/jpeg\r\n\r\n' + img[1].tostring() + b'\r\n')
def video_feed_2(request):
    return StreamingHttpResponse(gen_2(),content_type='multipart/x-mixed-replace; boundary=frame')
def gen_3():
    while True:
        frame=aimg.q.get()
        cv_image = cvB.imgmsg_to_cv2(frame, "bgr8")
        img=cv2.imencode('.jpg',cv_image)
        yield (b'--frame\r\n'+b'Content-Type: image/jpeg\r\n\r\n' + img[1].tostring() + b'\r\n')
def video_feed_3(request):
    return StreamingHttpResponse(gen_3(),content_type='multipart/x-mixed-replace; boundary=frame')
def gen_4():
    while True:
        frame=aimg.q.get()
        cv_image = cvB.imgmsg_to_cv2(frame, "bgr8")
        img=cv2.imencode('.jpg',cv_image)
        yield (b'--frame\r\n'+b'Content-Type: image/jpeg\r\n\r\n' + img[1].tostring() + b'\r\n')
def video_feed_4(request):
    return StreamingHttpResponse(gen_4(),content_type='multipart/x-mixed-replace; boundary=frame')
