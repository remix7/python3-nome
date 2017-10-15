from socket import *
import select
# 创建套接字
s = socket(AF_INET,SOCK_STREAM)
# 设置套接字可以重复使用绑定信息
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(("",7788))
s.listen(100)
# 创建一个epoll对象
epoll = select.epoll()
# 将创建的套接字添加到epoll事件监听中
epoll.register(s.fileno(),select.EPOLLIN | select.EPOLLET)

connections = {}
addresses = {}

while True:
	# epoll 进行fd扫描 未指定超时时间则为阻塞
	epoll_list = epoll.poll()

	for fd,events in epoll_list:
		# 如果是socket创建的套接字被激活
		if fd == s.fileno():
			conn,addr = s.accept()
			connections[conn.fileno()] = conn
			addresses[conn.fileno()] = addr
			# 向epoll中注册 连接socket 的可读事件
			epoll.register(conn.fileno(),select.EPOLLIN|select.EPOLLET)
		else:
			if events == select.EPOLLIN:
				# 从激活 fd 上收取数据
				recvData = connections[fd].recv(1024)

				if recvData:
					print("recvData %s"%recvData)
				else:
					# 从epoll 中取消注册链接
					epoll.unregister(fd)
					connections[fd].close()
					print("%s -- offline ---"%str(addresses[fd]))

