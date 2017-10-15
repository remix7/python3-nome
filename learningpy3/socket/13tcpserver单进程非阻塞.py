from socket import *

#1 创建套接字
serSocket = socket(AF_INET,SOCK_STREAM)
#2 绑定ip和端口
serSocket.bind(('',7788))
#3 设置位非阻塞
serSocket.setblocking(False)
#4 将socket变为 被动套接字
serSocket.listen(100)
#5 用来保存已经链接的套接字

clientAddrList = []
while True:
	try:
		clientSocket,clientAddr = serSocket.accept()
	except :
		pass
	else:
		print('一个新的客户端到来 %s'%str(clientAddr))
		clientSocket.setblocking(False)
		clientAddrList.append((clientSocket,clientAddr))
	for clientSocket,clientAddr in clientAddrList:
		try:
			recvData = clientSocket.recv(1024)
		except :
			pass
		else:
			if len(recvData) > 0:
				print("%s:%s"%(str(clientAddr),recvData.decode('gb2312')))
				clientSocket.send("what fuck".encode('gb2312'))
			else:
				clientSocket.close()
				clientAddrList.remove((clientSocket,clientAddr))
				print("%s 已经下线"%str(clientAddr))