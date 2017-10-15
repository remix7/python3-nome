from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

sendAddr = ('192.168.1.109',8899)

sendData = '我不是哦'.encode("gb2312")

udpSocket.sendto(sendData,sendAddr)

udpSocket.close()