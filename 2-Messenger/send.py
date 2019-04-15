# Ross Nelson CSC376 Assignment 2: Messenger
# April 23rd 2019
# send.py

# Import modules
import sys, os # Import sys and os modules
import threading, time # Import threading and time modules
import socket # Import socket module

# Send class implements 'threading.Thread' class to send messages while running in a separate thread
class Send (threading.Thread): # Creates 'Send' class that implements the 'threading.Thread' class
	def __init__(self, sock, message): # Creates '__init__' constructor with arguments 'self', 'sock', and 'message'
		threading.Thread.__init__(self) # Calls the threading.Thread constructor passing 'self'
		self.sock = sock # Store 'sock' in the member variable, 'sock'
		self.message = message # Store 'message' in the member variable, 'sock'
		
	# Sends messages until there are no more messages, then exits the process
	def run(self): # Creates run function that takes argument 'self' and is called in the implemented 'start' function
		while self.message: # Loop while 'message' has a value
			self.sock.send(self.message.encode()) # Encodes and sends 'message'
			self.message = sys.stdin.readline().replace("\n", "") # Saves standard input to 'message' without the newline character
		os._exit(0) # Exit the process