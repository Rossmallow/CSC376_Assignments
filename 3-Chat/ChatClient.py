# Ross Nelson CSC376 Assignment 3: Chat
# May 7th, 2019
# ChatClient.py

import sys
import socket
import clientSend, clientReceive

args = sys.argv # Stores the command line arguments array in to array 'args'
port = int(args[1])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializes 'sock' with a socket
print("Waiting for request from server...")
sock.connect(('localhost', port)) # Connect to the server over 'port'
print("What is your name?")
name = sys.stdin.readline().replace("\n", "")
print("Sending name to server...")

#RECEIVE THREAD
receiveTherad = clientReceive.Receive(sock)
receiveTherad.start()

#SEND THREAD
sendThread = clientSend.Send(sock, name)
sendThread.start()