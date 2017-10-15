from threading import Thread
from socket import *
def recvData():
	while True:
		recvInfo = udpsocket.recvfrom(1024)
		print(">> %s %s"%(str(recvInfo[1]),recvInfo[0].decode('gb2312')))

def sendData():
	# while True:
		
	sendInfo = "nihao"
	
	udpsocket.sendto(sendInfo.encode('gb2312'),('192.168.1.109',7788))


udpsocket = None

def main():
	global udpsocket
	udpsocket = socket(AF_INET,SOCK_DGRAM);
	udpsocket.bind(('',8899))
	
	tr = Thread(target=recvData)
	ts = Thread(target=sendData)

	tr.start()
	ts.start()

	tr.join()
	ts.join()

if __name__ == '__main__':
	main()