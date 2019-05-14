# Ross Nelson CSC376 Assignment 4: Messenger with File Transfers
# May 23rd, 2019
# receive.py

# Import modules
import os # Import os module
import threading # Import threading module
import socket # Import socket module

global hasPort
hasPort = False

# Receive class implements 'threading.Thread' class to receive messages while running in a separate thread
class Receive (threading.Thread): # Creates 'Receive' class that implements the 'threading.Thread' class
	def __init__(self, sock): # Create '__init__' function with arguments 'self' and 'sock'
		threading.Thread.__init__(self) # Calls the threading.Thread constructor passing 'self'
		self.sock = sock # Store 'sock' in the member variable, 'sock'
		
	def fileClient (port):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializes 'sock' with a socket
		sock.connect((serverAddress, serverPort)) # Connect to the server with address 'serverAddress' over port number 'serverPort'
		# SEND FILES
		sock.shutdown( socket.SHUT_WR )
		sock.close()

	# Receives messages until there are no more messages, then exit the process
	def run(self): # Creates 'run' function which takes argument 'self' and is called in the implemented 'start' function
		global filePort
		filePort = int(self.sock.recv(1024).decode()) # Receive a message up to 1024 bytes that contains the port number to send files to, decode it, then convert it to an integer, and finally store in 'filePort'
		global hasPort
		hasPort = True
		while True: # Loop until standard input is closed
			msg_bytes = self.sock.recv(1024) # Receive a message up to 1024 bytes and save bytes to 'msg_bytes'
			message = msg_bytes.decode() # Decode the message and store in 'message'
			if message[0] == "m":
				print(message[1:])
			elif message[0] == "f":
				print("Requesting File: " + message[1:] + " over port: " + str(filePort))
				fileClient(filePort)
		os._exit(0) # Exit the process