# Ross Nelson CSC376 Assignment 2: Messenger
# April 23rd 2019
# send.py

import sys # Import sys module
import threading, time, os # Import threading and time modules
import socket # Import socket module

class Send (threading.Thread): # Create class 'Send' that implements the 'threading.Thread' class
	def __init__(self, sock, message, delay): #
		threading.Thread.__init__(self) #
		self.sock = sock #
		self.message = message #
		self.delay = delay #
		
	def run(self): # 
		self.wait_for_it(self.delay) #
		while self.message: # Loop while 'message' has a value
			self.sock.send(self.message.encode()) # Encodes and sends 'message'
			self.message = sys.stdin.readline().replace("\n", "") # Saves standard input to 'message' without the newline character
		os._exit(0)

	def wait_for_it(self, wait_time): #
		time.sleep(wait_time) #