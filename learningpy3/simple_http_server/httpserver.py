# coding = utf-8
from socket import *
from multiprocessing import Process

# 注册socket
# 绑定端口 listen accpet

def handle_client(cliSocket):
    """
    处理客户端请求
    :param cliSocket:
    """
    while True:
        data = cliSocket.recv(1024)
        if data:
            print(data)
            response = """Bdpagetype:2
Bdqid:0xf05a9f9600014c29
Bduserid:812878652
Cache-Control:private
Connection:Keep-Alive
Content-Encoding:gzip
Content-Type:text/html;charset=utf-8
Date:Sun, 15 Oct 2017 14:59:44 GMT
Expires:Sun, 15 Oct 2017 14:59:44 GMT
Server:BWS/1.1
Set-Cookie:BDSVRTM=187; path=/
Set-Cookie:BD_HOME=1; path=/
Set-Cookie:H_PS_PSSID=1428_21111_17001_20719; path=/; domain=.baidu.com
Strict-Transport-Security:max-age=172800
Transfer-Encoding:chunked
X-Ua-Compatible:IE=Edge,chrome=1"""
            cliSocket.send(response.encode("gb2312"))
        else:
            cliSocket.close()

if __name__ == '__main__':
    sSocket = socket(AF_INET, SOCK_STREAM)
    sSocket.bind(("", 7789))
    sSocket.listen(100)
    while True:
        cliSocket, cliAddr = sSocket.accept()
        p = Process(target=handle_client, args=(cliSocket,))
        p.start()
        cliSocket.close()



