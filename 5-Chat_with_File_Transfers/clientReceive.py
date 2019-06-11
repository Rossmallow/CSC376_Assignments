# Ross Nelson CSC376 Assignment 5: Chat_with_File_Transfers
# June 11th, 2019
# clientReceive.py

# Import modules
import os # Import os module
import threading  # Import threading module
import socket # Import socket module
import struct

# Receive class implements 'threading.Thread' class to receive messages while running in a separate thread
class Receive (threading.Thread): # Creates 'Receive' class that implements the 'threading.Thread' class
	def __init__(self, sock, listenPort): # Create '__init__' function with arguments 'self' and 'sock'
		threading.Thread.__init__(self) # Calls the threading.Thread constructor passing 'self'
		self.sock = sock # Store 'sock' in the member variable, 'sock'
		self.listenPort = listenPort
		
	def send_file(self, sock, fileSize, file):
		print('File size is ' + str(fileSize))
		file_size_bytes = struct.pack('!L', fileSize)
		sock.send(file_size_bytes)
		while True:
			file_bytes = file.read(1024)
			if file_bytes:
				sock.send(file_bytes)
			else:
				break
		file.close()
		sock.shutdown(socket.SHUT_WR)
		sock.close()

	def fileClient(self, sock, port, fileSize, file):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializes 'sock' with a socket
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Allows multiple sockets on the same port
		sock.connect(("localhost", port)) # Connect to the server with address 'serverAddress' over port number 'serverPort'
		self.send_file(sock, fileSize, file)
		sock.close()

	def no_file(self, sock, port):
		print ("no file")
		zero_bytes = struct.pack('!L', 0)
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializes 'sock' with a socket
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Allows multiple sockets on the same port
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

	def run(self): # Creates 'run' function which takes argument 'self' and is called in the implemented 'start' function
		while True: # Loop until standard input is closed
			msg_bytes = self.sock.recv(1024) # Receive a message up to 1024 bytes and save bytes to 'msg_bytes'
			message = msg_bytes.decode()
			if len(message) > 0:
				if message[0] == "m":
					print(message[1:])
				elif message[0] == "f":
					filename = message[1:]
					self.checkFile(self.sock, self.listenPort, filename)
		os._exit(0) # Exit the process