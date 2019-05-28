# Ross Nelson CSC376 Assignment 5: Chat_with_File_Transfers
# June 11th, 2019
# clientReceive.py

# Import modules
import os # Import os module
import threading  # Import threading module
import socket # Import socket module

# Receive class implements 'threading.Thread' class to receive messages while running in a separate thread
class Receive (threading.Thread): # Creates 'Receive' class that implements the 'threading.Thread' class
	def __init__(self, sock): # Create '__init__' function with arguments 'self' and 'sock'
		threading.Thread.__init__(self) # Calls the threading.Thread constructor passing 'self'
		self.sock = sock # Store 'sock' in the member variable, 'sock'
		
	# Receives messages until there are no more messages, then exit the process
	def run(self): # Creates 'run' function which takes argument 'self' and is called in the implemented 'start' function
		msg_bytes = self.sock.recv(1024) # Receive a message up to 1024 bytes and save bytes to 'msg_bytes'
		while True: # Loop until standard input is closed
			print (msg_bytes.decode()) # Decode the message and print to standard output as a string
			msg_bytes = self.sock.recv(1024) # Receive a message up to 1024 bytes and save bytes to 'msg_bytes'
		os._exit(0) # Exit the process