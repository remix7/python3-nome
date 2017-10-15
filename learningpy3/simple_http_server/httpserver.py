from socket import *

# 注册socket
# 绑定端口 listen accpet

sSocket = socket(AF_INET, SOCK_STREAM)
sSocket.bind(("", 7788))
sSocket.listen(100)

