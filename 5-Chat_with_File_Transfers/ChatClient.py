# Ross Nelson CSC376 Assignment 5: Chat_with_File_Transfers
# June 11th, 2019
# ChatClient.py

# Import modules
import sys # Import sys module
import socket # Import socket module
import clientReceive # Import custom clientReceive module
import time
import os
import struct

def receive_file(sock, filename):
	file = open(filename, 'wb')
	while True:
		file_bytes = sock.recv(1024)
		if file_bytes:
			file.write(file_bytes)
		else:
			break
	file.close()

def fileServer(port, filename, mainSock):
	print ("Starting server on " + str(port))
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializes 'serversocket' with a socket
	serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Allows multiple sockets on the same port
	serversocket.bind(('', port)) # Binds 'serversocket' to 'port'
	serversocket.listen(5) # Listens for socket connections with a backlog value of '5'
	mainSock.send(filename.encode()) # Encodes and sends 'fileName' over 'sock'
	sock, addr = serversocket.accept() # Accept the connection and store it in 'sock' and 'addr'
	serversocket.close() # Close the socket as it is no longer needed
	file_size_bytes= sock.recv( 4 )
	if file_size_bytes:
		file_size = struct.unpack( '!L', file_size_bytes[:4] )[0]
		if file_size:
			receive_file(sock, filename)
		else:
			print('File does not exist or is empty')
	else:
		print('File does not exist or is empty')
	sock.close()

# Runs program
def run (sock, port): # Creates 'run' function that takes in socket 'sock' and that asks users to select from a list of options until the program is closed
	optionsMessage = "Enter an option ('m', 'f', 'x'):\n (M)essage (send)\n (F)ile (request)\ne(X)it" # Stores sting "Enter an option ('m', 'f', 'x'):\n (M)essage (send)\n (F)ile (request)\ne(X)it" in 'optionsMessage'
	print(optionsMessage) # Prints what is stored in 'optionsMessage'
	option = sys.stdin.readline().replace("\n", "").upper() # Stores standard input in 'option' after removing the newline character, and converting the input to all uppercase
	if option == "M": # If 'option' is equal to "M"
		print("Enter your message:") # Prints "Enter your message:"
		message = "m" + sys.stdin.readline().replace("\n", "") # Saves standard input to 'message' without the newline character and an additional "m" at the beginning to denote a message
		sock.send(message.encode()) # encodes and sends 'message' over 'sock'
	elif option == "F": # Otherwise, if 'option' is equal to "F"
		print("Who owns the file?")
		ownername = "f" + sys.stdin.readline().replace("\n", "")
		sock.send(ownername.encode())
		print("Which file do you want?") # Prints "Which file do you want?"
		filename = sys.stdin.readline().replace("\n", "") # Saves standard input to 'filename' without the newline character and an additional "f" at the beginning to denote a file name
		fileServer(port, filename, sock)
	elif option == "X": # Otherwise, if 'option' is equal to "X"
		sock.send("eXit".encode())
		os._exit(0) # Exit the process
	else: # Otherwise
		print (option + " is not valid.") # Print what is stored in 'option' followed by " is not valid."
	run(sock, port) # Calls 'run' function and passes in 'sock'

# Finds and stores port number from the command line arguments
args = sys.argv # Stores the command line arguments array in to array 'args'
i = 1
while i < len(args): # Loop until the end of the array
	if (args[i] == "-l"): 
		listenPort = int(args[i + 1])
	if (args[i] == "-p"): 
		serverPort = int(args[i + 1])
	i += 1 # Increment i by 1

# Creates a socket, connects on the provided port, and gets user name from standard input
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializes 'sock' with a socket
print("Waiting for request from server...") # Prints "Waiting for request from server..." to standard output
sock.connect(('localhost', serverPort)) # Connect to the server over 'port'
print("What is your name?") # Prints "What is your name?" to standard output
name = sys.stdin.readline().replace("\n", "") # Reads standard input and replaces the newline character with an empty character, then stores the edited string in 'name'
print("Sending name to server...") # Prints "Sending name to server..." to standard output

# Send client's name and listen port
sock.send(name.encode())
time.sleep(.5)
sock.send(str(listenPort).encode())

# Creates and starts a receive thread
receiveTherad = clientReceive.Receive(sock, listenPort) # Calls 'Receive' function in 'clientReceive.py' and stores the thread in 'receiveThread'
receiveTherad.start() # Starts the thread saved in 'receiveThread'

run (sock, listenPort)