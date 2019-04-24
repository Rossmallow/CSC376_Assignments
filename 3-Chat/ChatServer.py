# Ross Nelson CSC376 Assignment 3: Chat
# May 7th, 2019
# ChatServer.py

import sys
import socket

args = sys.argv
port = int(args[1])

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializes 'serversocket' with a socket
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 
serversocket.bind(('', port)) # Binds 'serversocket' to 'port'
serversocket.listen(5) # Listens for socket connections with a backlog value of '5'
#addClientThread = addClient.AddClient (serversocket)
#addClientThread.start()
#sock1, addr1 = serversocket.accept() # Accept the connection and store it in 'sock1' and 'addr1'
#sock2, addr2 = serversocket.accept() # Accept the connection and store it in 'sock2' and 'addr2'

global sockets
sockets = []
while (True):
	sockets.append(serversocket.accept)
	# Start new thread

#RECIEVE THREAD
#SEND THREAD

os._exit(0) # Exit the process

#serverSendReceiveThread = ServerSendReceive.ServerSendReceive(sockets)
#serverSendReceiveThread.start()

#msg_bytes1= sock1.recv(1024)
#print ('client1 said: ' + msg_bytes1.decode())
#sock1.send(msg_bytes1) # send the message back

#msg_bytes2= sock2.recv(1024)
#print ('client2 said: ' + msg_bytes2.decode())
#sock2.send(msg_bytes2) # send the message back