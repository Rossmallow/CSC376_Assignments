# Ross Nelson CSC376 Assignment 5: Chat_with_File_Transfers
# June 11th, 2019
# serverReceive.py

# Import modules
import os, sys # Import os andd sys modules
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
					for socket in sockets: # For each 'socket' in global variable 'sockets'
						if socket != self.sock: # If 'socket' is not the same socket as 'self.sock'
							socket.send(("m" + message).encode()) # Encode 'message' and send to 'socket'
				elif message[0] == "f":
					ownername = message[1:]
					filename = self.sock.recv(1024).decode()
					for client in clients:
						if client['Name'] == ownername:
							ownerPort = client['Port']
							ownerSocket = client['Socket']
							print("Requesting File: " + filename + " from: " + ownername + " over port: " + str(ownerPort))
							ownerSocket.send(("f" + message).encode())
						else:
							print ("Client not found!")
				elif message == "eXit":
					sockets.remove(self.sock) # When msg_bytes is empty, emove 'self.sock' from global variable 'sockets'
					clients.remove(self.client)
					sys.exit() # Exit