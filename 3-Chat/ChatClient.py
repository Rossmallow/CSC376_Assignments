# Ross Nelson CSC376 Assignment 3: Chat
# May 7th, 2019
# ChatClient.py

# Import modules
import sys # Import sys module
import socket # Import socket module
import clientSend, clientReceive # Import custom clientSend and clientReceive modules

# Finds and stores port number from the command line arguments
args = sys.argv # Stores the command line arguments array in to array 'args'
port = int(args[1]) # Stores the 1st command line argument in 'port' (where 0th is the name of the program)

# Creates a socket, connects on the provided port, and gets user name from standard input
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializes 'sock' with a socket
print("Waiting for request from server...") # Prints "Waiting for request from server..." to standard output
sock.connect(('localhost', port)) # Connect to the server over 'port'
print("What is your name?") # Prints "What is your name?" to standard output
name = sys.stdin.readline().replace("\n", "") # Reads standard input and replaces the newline character with an empty character, then stores the edited string in 'name'
print("Sending name to server...") # Prints "Sending name to server..." to standard output

# Creates and starts a receive thread
receiveTherad = clientReceive.Receive(sock) # Calls 'Receive' function in 'clientReceive.py' and stores the thread in 'receiveThread'
receiveTherad.start() # Starts the thread saved in 'receiveThread'

# Creats and starts a send thread
sendThread = clientSend.Send(sock, name) # Calls 'Send' function in 'clientSend.py' and stores the thread in 'sendThread'
sendThread.start() # Starts the thread saved in 'sendThread'