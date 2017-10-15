import select
import sys
from socket import *

server = socket(AF_INET,SOCK_STREAM)
server.bind(('',7788))
server.listen()

inputs = [server,sys.stdin]

running = True

while True:
	readable,writeable,excepthonal = select.select(inputs,[],[])

	for sock in readable:
		if sock == server:
			conn,addr = sock.accept()
			inputs.append(conn)
	else if sock == sys.stdin:
		cmd = sys.stdin.readline()
		running = False
		break
	else :
		data = sock.recv(1024)
		if data:
			sock.send(data)
		else:
			inputs.remove(sock)
			