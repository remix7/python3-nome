from socket import *
# 如果想要使用tcpsocket 创建socket的第二个参数一定要是SOCK_STREAM
serversSocket = socket(AF_INET,SOCK_STREAM)
# 绑定本机的任意一个ip和端口号
serversSocket.bind(("",8899))
# 此处的5没有实际含义
serversSocket.listen(5)
# 返回值位客户端套接字 和客户端ip port元祖
clientSocket,clientInfo = serversSocket.accept()
# 直接谁用recv
recvData = clientSocket.recv(1024)
print("%s:%s"%(str(clientInfo),recvData))


clientSocket.send("thenk you".encode("utf-8"));

clientSocket.close()
serversSocket.close()