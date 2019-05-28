# Ross Nelson CSC376 Assignment 5: Chat_with_File_Transfers
# June 11th, 2019
# serverReceive.py

# Import modules
import os # Import os module
import threading # Import threading module
import socket # Import socket module

# Create and initialize global variables 'sockets' and 'clients'
global sockets
sockets = []
global clients
clients = []

# Receive class implements 'threading.Thread' class to receive messages while running in a separate thread
class Receive (threading.Thread): # Creates 'Receive' class that implements the 'threading.Thread' class
	def __init__(self, sock): # Create '__init__' function with arguments 'self' and 'sock'
		threading.Thread.__init__(self) # Calls the threading.Thread constructor passing 'self'
		self.sock = sock # Store 'sock' in the member variable, 'sock'
		self.client = {'Name': '', 'Port': 0}

	def no_file(self, sock, port):
		print ("no file")
		zero_bytes = struct.pack('!L', 0)
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializes 'sock' with a socket
		sock.connect(("localhost", port))
		sock.send(zero_bytes)
		sock.shutdown(socket.SHUT_WR)
		sock.close()

	def checkFile(self, sock, filePort, filename): 
		print(filename)
		try:
			file_stat = os.stat(filename)
			if file_stat.st_size:
				file = open(filename, 'rb')
				self.fileClient(sock, filePort, file_stat.st_size, file)
			else:
				self.no_file(sock, filePort)
		except:
				self.no_file(sock, filePort)

	# Receives messages until there are no more messages, then exit the process
	def run(self): # Creates 'run' function which takes argument 'self' and is called in the implemented 'start' function
		name = self.sock.recv(1024).decode() # Decodes the 1st message and stores it in 'name'
		listenPort = int(self.sock.recv(1024).decode())
		self.client = {'Name': name, 'Port': listenPort} # Creates a dict with the client's name and the port they listen on.
		clients.append(client)
		while True:
			msg_bytes = self.sock.recv(1024) # Stores the next encoded message in 'msg_bytes'
			message = msg_bytes.decode() # Decode the message and store it in 'message'
			if len(message) > 0:
				if message[0] == "m":
					message.replace("m", name + ": ")
					for socket in sockets: # For each 'socket' in global variable 'sockets'
						if socket != self.sock: # If 'socket' is not the same socket as 'self.sock'
							socket.send(message.encode()) # Encode 'message' and send to 'socket'
				elif message[0] == "o":
					filename = self.sock.recv(1024).decode()
					for client in clients:
						if client['Name'] = message[1:]:
							filePort = client['Port']
						else:
							print ("Client not found!")
					print("Requesting File: " + filename + " from: " + message[1:] + " over port: " + filePort)
					self.checkFile(self.sock, filePort, filename)
			else:
				sockets.remove(self.sock) # When msg_bytes is empty, emove 'self.sock' from global variable 'sockets'
				clients.remove(client)
				os._exit(0) # Exit the process