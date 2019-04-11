# Ross Nelson CSC376 Assignment 2: Messenger
# April 23rd 2019
# send.py

import sys
import threading, time
import socket

class Send (threading.Thread):
	def __init__(self, sock, message, delay):
		threading.Thread.__init__(self)
		self.sock = sock
		self.message = message
		self.delay = delay
		
	def run(self):
		self.wait_for_it(self.delay)
		while self.message: # Loop while 'message' has a value
			self.sock.send(self.message.encode()) # Encodes and sends 'message'
			self.wait_for_it(2) # Calls 'wait_for_it' with a value of '2'
			self.message = sys.stdin.readline().replace("\n", "") # Saves standard input to 'message' without the newline character
			self.sock.close() # Closes the socket

	def wait_for_it(self, wait_time):
		time.sleep(wait_time)