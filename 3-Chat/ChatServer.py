# Ross Nelson CSC376 Assignment 3: Chat
# May 7th, 2019
# ChatServer.py

import sys
import socket
import serverReceive

args = sys.argv
port = int(args[1])

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializes 'serversocket' with a socket
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 
serversocket.bind(('', port)) # Binds 'serversocket' to 'port'
serversocket.listen(5) # Listens for socket connections with a backlog value of '5'

while (True):
	sock, addr = serversocket.accept()
	serverReceive.Receive(sock).start()
	serverReceive.clients.append(sock)