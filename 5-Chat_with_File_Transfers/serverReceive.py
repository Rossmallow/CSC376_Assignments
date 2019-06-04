# Ross Nelson CSC376 Assignment 5: Chat_with_File_Transfers
# June 11th, 2019
# serverReceive.py

# Import modules
import os, sys # Import os andd sys modules
import threading # Import threading module
import socket # Import socket module
import struct

global clients
clients = []

# Receive class implements 'threading.Thread' class to receive messages while running in a separate thread
class Receive (threading.Thread): # Creates 'Receive' class that implements the 'threading.Thread' class
	def __init__(self, sock): # Create '__init__' function with arguments 'self' and 'sock'
		threading.Thread.__init__(self) # Calls the threading.Thread constructor passing 'self'
		self.sock = sock # Store 'sock' in the member variable, 'sock'
		self.client = {'Name': '', 'Port': 0, 'Socket': None}

	def receive_file(self, ownerSock, filename, fileSize):
		##SEND BYTES TO REQUESTER
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializes 'sock' with a socket
		sock.connect(('localhost', self.client['Port'])) # Connect to the server over 'port'
		file_size_bytes = struct.pack('!L', fileSize)
		sock.send(file_size_bytes)
		while True:
			file_bytes = ownerSock.recv(1024)
			if file_bytes:
				sock.send(file_bytes)
			else:
				break

	def sendZeroBytes(self):
		zero_bytes = struct.pack('!L', 0)
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializes 'sock' with a socket
		sock.connect(('localhost', self.client['Port'])) # Connect to the server over 'port'
		sock.send(zero_bytes)

	def fileServer(self, port, filename, mainSock):
		print ("Starting server on " + str(port))
		serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializes 'serversocket' with a socket
		serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Allows multiple sockets on the same port
		serversocket.bind(('', port)) # Binds 'serversocket' to 'port'
		serversocket.listen(5) # Listens for socket connections with a backlog value of '5'
		mainSock.send(("f" + filename).encode()) # Encodes and sends 'fileName' over 'sock'
		sock, addr = serversocket.accept() # Accept the connection and store it in 'sock' and 'addr'
		serversocket.close() # Close the socket as it is no longer needed
		file_size_bytes= sock.recv( 4 )
		if file_size_bytes:
			file_size = struct.unpack( '!L', file_size_bytes[:4] )[0]
			if file_size:
				self.receive_file(sock, filename, file_size)
			else:
				print('File does not exist or is empty')
				self.sendZeroBytes()
		else:
			print('File does not exist or is empty')
			self.sendZeroBytes()
		sock.close()	

	# Receives messages until there are no more messages, then exit the process
	def run(self): # Creates 'run' function which takes argument 'self' and is called in the implemented 'start' function
		name = self.sock.recv(1024).decode() # Decodes the 1st message and stores it in 'name'
		listenPort = int(self.sock.recv(1024).decode())
		self.client = {'Name': name, 'Port': listenPort, 'Socket' : self.sock} # Creates a dict with the client's name and the port they listen on.
		clients.append(self.client)
		while True:
			msg_bytes = self.sock.recv(1024) # Stores the next encoded message in 'msg_bytes'
			message = msg_bytes.decode() # Decode the message and store it in 'message'
			if len(message) > 0:
				if message[0] == "m":
					message = name + ": " + message[1:]
					for client in clients: # For each 'socket' in global variable 'sockets'
						if client['Socket'] != self.sock: # If 'socket' is not the same socket as 'self.sock'
							client['Socket'].send(("m" + message).encode()) # Encode 'message' and send to 'socket'
				elif message[0] == "f":
					ownername = message[1:]
					filename = self.sock.recv(1024).decode()
					for client in clients:
						if client['Name'] == ownername:
							ownerPort = client['Port']
							ownerSocket = client['Socket']
							print("Requesting File: " + filename + " from: " + ownername + " over port: " + str(ownerPort))
							##START SERVER ON OWNER PORT
							self.fileServer(ownerPort, filename, ownerSocket)
				elif message == "eXit":
					clients.remove(self.client)
					sys.exit() # Exit