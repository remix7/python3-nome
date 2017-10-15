from socket import * 

sSocket = socket(AF_INET,SOCK_STREAM)
sSocket.bind(("",8899))
sSocket.listen(5)

while True:
	cSocket,cAddr = sSocket.accept()
	while True:
		recvData = cSocket.recv(1024)
		print(cAddr)
		print(recvData.decode("gb2312"))
		# 这里数据长度小于0时 说明对方已经断了链接
		if len(recvData) > 0:
			print("data is %s"%str(recvData))
		else:
			break
		cSocket.send("what fuck".encode("gb2312"))
	cSocket.close()

sSocket.close()