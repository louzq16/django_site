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

def gen():
    while True:
        frame=aimg.q.get()
        cv_image = cvB.imgmsg_to_cv2(frame, "bgr8")
        img=cv2.imencode('.jpg',cv_image)
        
        print("okok ")
        yield (b'--frame\r\n'+b'Content-Type: image/jpeg\r\n\r\n' + img[1].tostring() + b'\r\n')
def video_feed(request):
    print("ok")
    return StreamingHttpResponse(gen(),content_type='multipart/x-mixed-replace; boundary=frame')