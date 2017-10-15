from socket import * 
import struct

sendData = struct.pack("!H5sb5sb",1,"1.flv".encode("utf-8"),0,"octet".encode('utf-8'),0)
print(sendData)

udpsocket = None

def requert(data,addr):
	udpsocket.sendto(data,addr);

num = 0
def response():
	global num
	recvFile = open('abc.flv','bw')
	while True:
		recvinfo = udpsocket.recvfrom(1024)
		recvData,recvIpPort = recvinfo
		# print(recvinfo)
		cmdTuple = struct.unpack("!HH",recvData[:4])
		print(cmdTuple)
		cmd = cmdTuple[0]
		currentPackNum = cmdTuple[1]
		# print(cmdTuple)
		if cmd == 3:
			num = num + 1
			if num == 65536:
				num = 0
			if num == currentPackNum:
				recvFile.write(recvData[4:])
				num = currentPackNum
			ackData = struct.pack("!HH",4,currentPackNum)
			requert(ackData,recvIpPort)
		elif cmd == 5:
			print("sorry")
			break
		if len(recvData) < 516:
			break

if __name__ == '__main__':
	udpsocket = socket(AF_INET,SOCK_DGRAM)
	udpsocket.bind(('',8899))
	requert(sendData,('192.168.1.109',69));
	response()