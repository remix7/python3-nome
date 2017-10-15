from socket import *
import os

udpsocket = socket(AF_INET,SOCK_DGRAM)
# 对这个需要发送广播数据调节在进行修改设置
udpsocket.setsockpt(SOL_SOCKET,SO_BROADCAST,1)
#192.168.1.255 广播地址  broadcast 系统自动寻找广播地址
udpsocket.sendto("Hi",('<broadcast>',7788))