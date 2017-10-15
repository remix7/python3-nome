from socket import *

clientSocket = socket(AF_INET,SOCK_STREAM)

clientSocket.connect(("192.168.226.1",8899))

clientSocket.send("what fuck".encode("utf-8"))

recvData = clientSocket.recv(1024)

print("接受到的数据位%s"%recvData)
clientSocket.close()