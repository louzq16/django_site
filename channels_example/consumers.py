#coding:utf-8
#!/usr/bin/env python
from django.http import HttpResponse
from channels.handler import AsgiHandler
import json
from mymulti import atry
from uwb.msg import Uwb_msgs,Point
#message.reply_channel    一个客户端通道的对象
#message.reply_channel.send(chunk)  用来唯一返回这个客户端
atry.prostart()
#一个管道大概会持续30s

#当连接上时，发回去一个connect字符串
def ws_connect(message):
    message.reply_channel.send({"accept":True})
    

#将发来的信息原样返回
def dataprocess(qdata):
    temdict=dict()
    temlist=[0.0]*8
    for i in range(4):
        temlist[i*2]=qdata.quaposi[i].x
        temlist[i*2+1]=qdata.quaposi[i].y
    temdict["quaposi"]=temlist
    temdict["perposi"]=[qdata.perposi.x,qdata.perposi.y]
    return temdict
def ws_message(message):
    q=atry.q.get()
    dictq=dataprocess(q)
    message.reply_channel.send({"text":json.dumps(dictq)})#json.dumps(dataprocess(q))})
#断开连接时发送一个disconnect字符串，当然，他已经收不到了
def ws_disconnect(message):
    message.reply_channel.send({"close":True,})

