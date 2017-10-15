from socket import *
udpsocket = socket(AF_INET,SOCK_DGRAM)

udpsocket.sendto('hhh'.encode('utf-8'),("192.168.1.104",7788))

udpsocket.close()