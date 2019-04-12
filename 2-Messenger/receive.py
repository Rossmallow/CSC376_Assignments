# Ross Nelson CSC376 Assignment 2: Messenger
# April 23rd 2019
# receive.py

import sys # Import sys module
import threading, time # Import threading and time modules
import socket # Import socket module

class Receive (threading.Thread): # Create class 'Send' that implements the 'threading.Thread' class
	def __init__(self, sock, talkingTo, delay): #
		threading.Thread.__init__(self) #
		self.sock = sock #
		self.talkingTo = talkingTo #
		self.delay = delay #
		
	def run(self): # 
		self.wait_for_it(self.delay) #
		msg_bytes = self.sock.recv(1024)
		while msg_bytes: # Loop while 'message' has a value	
#			print (self.talkingTo + ' said: ' + msg_bytes.decode())
			print (msg_bytes.decode())
			msg_bytes = self.sock.recv(1024)
		self.sock.close() # Closes the socket

	def wait_for_it(self, wait_time): #
		time.sleep(wait_time) #