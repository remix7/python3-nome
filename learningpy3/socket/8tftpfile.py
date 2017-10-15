from socket import *
import struct

sendData = struct.pack("!H11sb5sb",1,"tftpd32.chm".encode("utf-8"),0,"octet".encode('utf-8'),0)
print(sendData)
udpsocket = socket(AF_INET,SOCK_DGRAM)
udpsocket.sendto(sendData,('192.168.1.109',69))
udpsocket.close()