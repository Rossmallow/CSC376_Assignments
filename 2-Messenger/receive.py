# Ross Nelson CSC376 Assignment 2: Messenger
# April 23rd 2019
# receive.py

import os # Import os module
import threading, time  # Import threading and time modules
import socket # Import socket module

class Receive (threading.Thread): # Creates 'Receive' class that implements the 'threading.Thread' class
	def __init__(self, sock): # Create '__init__' function with arguments 'self' and 'sock'
		threading.Thread.__init__(self) # 
		self.sock = sock # 
		
	# Receives messages until there are no more messages, then exit the process
	def run(self): # Creates 'run' function which takes argument 'self' and is called in the implemented 'start' function
		msg_bytes = self.sock.recv(1024) # Receive a message up to 1024 bytes and save bytes to 'msg_bytes'
		while True: # Loop until standard input is closed
			print (msg_bytes.decode()) # Decode the message and print to standard output as a string
			msg_bytes = self.sock.recv(1024) # Receive a message up to 1024 bytes and save bytes to 'msg_bytes'
		os._exit(0) # Exit the process