#coding:utf-8
#!/usr/bin/env python
from channels.routing import route
from channels_example import consumers  #导入处理函数

channel_routing = [
    #route("http.request", consumers.http_consumer), #这个表项比较特殊，他响应的是http.request，也就是说有HTTP请求时就会响应，同时urls.py里面的表单会失效


   # route("websocket.connect", consumers.ws_connect),        #当WebSocket请求连接上时调用consumers.ws_connect函数
    route("websocket.receive", consumers.ws_message),        #当WebSocket请求发来消息时。。。
    #route("websocket.disconnect", consumers.ws_disconnect),    #当WebSocket请求断开连接时。。。
]