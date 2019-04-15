# Ross Nelson CSC376 Assignment 2: Messenger
# April 23rd 2019
# send.py

import sys, os # Import sys and os modules
import threading, time # Import threading and time modules
import socket # Import socket module

class Send (threading.Thread): # Creates 'Send' class that implements the 'threading.Thread' class
	def __init__(self, sock, message): #
		threading.Thread.__init__(self) #
		self.sock = sock #
		self.message = message #
		
	# Sends messages until there are no more messages, then exits the process
	def run(self): # Creates run function that takes argument 'self' and is called in the implemented 'start' function
		while self.message: # Loop while 'message' has a value
			self.sock.send(self.message.encode()) # Encodes and sends 'message'
			self.message = sys.stdin.readline().replace("\n", "") # Saves standard input to 'message' without the newline character
		os._exit(0) # Exit the process