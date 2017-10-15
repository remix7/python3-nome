from socket import *
num = 0
def main():
	udpsocket = socket(AF_INET,SOCK_DGRAM)
	bindAddr = ('',8899)
	udpsocket.bind(bindAddr)
	while True:
		recvData = udpsocket.recvfrom(1024)
		content, destInfo = recvData
		print(content)
		print(content.decode('gb2312'))
		udpsocket.sendto(content,destInfo)

if __name__ == '__main__':
	main()