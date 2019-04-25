# Ross Nelson CSC376 Assignment 2: Messenger
# May 7th,s 2019
# serverReceive.py

# Import modules
import os # Import os module
import threading, time  # Import threading and time modules
import socket # Import socket module

global clients
clients = []

# Receive class implements 'threading.Thread' class to receive messages while running in a separate thread
class Receive (threading.Thread): # Creates 'Receive' class that implements the 'threading.Thread' class
	def __init__(self, sock): # Create '__init__' function with arguments 'self' and 'sock'
		threading.Thread.__init__(self) # Calls the threading.Thread constructor passing 'self'
		self.sock = sock # Store 'sock' in the member variable, 'sock'

	# Receives messages until there are no more messages, then exit the process
	def run(self): # Creates 'run' function which takes argument 'self' and is called in the implemented 'start' function
		name = self.sock.recv(1024).decode()
		msg_bytes = self.sock.recv(1024)
		while msg_bytes:
			#SEND TO OTHERS
			message = name + ": " + msg_bytes.decode()
			for client in clients:
				if client != self.sock:
					client.send(message.encode())
			msg_bytes = self.sock.recv(1024) # Receive a message up to 1024 bytes and save bytes to 'msg_bytes'
		clients.remove(self.sock)
		sys.exit()