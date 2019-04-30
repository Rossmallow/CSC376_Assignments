# Ross Nelson CSC376 Assignment 3: Chat
# May 7th,s 2019
# serverReceive.py

# Import modules
import os # Import os module
import threading # Import threading module
import socket # Import socket module

# Create and initialize global variable 'clients'
global clients # Creats global variale 'clients'
clients = [] # Initializes 'clients' with an empty array

# Receive class implements 'threading.Thread' class to receive messages while running in a separate thread
class Receive (threading.Thread): # Creates 'Receive' class that implements the 'threading.Thread' class
	def __init__(self, sock): # Create '__init__' function with arguments 'self' and 'sock'
		threading.Thread.__init__(self) # Calls the threading.Thread constructor passing 'self'
		self.sock = sock # Store 'sock' in the member variable, 'sock'

	# Receives messages until there are no more messages, then exit the process
	def run(self): # Creates 'run' function which takes argument 'self' and is called in the implemented 'start' function
		name = self.sock.recv(1024).decode() # Decodes the 1st message and stores it in 'name'
		msg_bytes = self.sock.recv(1024) # Stores the next encoded message in 'msg_bytes'
		while msg_bytes: # While msg_bytes is not empty
			message = name + ": " + msg_bytes.decode() # Decode the message and prepend 'name' and the string ": " to the message and store it in 'message'
			for client in clients: # For each 'client' in global variable 'clients'
				if client != self.sock: # If 'client' is not the same socket as 'self.sock'
					client.send(message.encode()) # Encode 'message' and send to 'client'
			msg_bytes = self.sock.recv(1024) # Receive a message up to 1024 bytes and save bytes to 'msg_bytes'
		clients.remove(self.sock) # When msg_bytes is empty, emove 'self.sock' from global variable 'clients'