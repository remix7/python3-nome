from socket import *
# 创建套接字
udpSocket = socket(AF_INET,SOCK_DGRAM)
# 绑定本地相关信息 如果一个网络程序不绑定 则系统会所及分配
bindAddr = ('',7788) #ip 地址和端口地址 ip一般不用写 表示本机的ip
udpSocket.bind(bindAddr)

# 等待接受对方发送的数据 1024 表示本次接受最大字节数
recvData = udpSocket.recvfrom(1024)
# 显示接受到的数据
print(recvData)

udpSocket.close()