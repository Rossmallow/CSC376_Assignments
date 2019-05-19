# Ross Nelson CSC376 Assignment 4: Messenger with File Transfers
# May 23rd, 2019
# client.py

# Import modules
import sys # Import sys module
import socket # Import socket module
import receive # Import custom receive module
import os

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
	receive_file(sock, filename[1:])
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
		print("Which file do you want?") # Prints "Which file do you want?"
		filename = "f" + sys.stdin.readline().replace("\n", "") # Saves standard input to 'filename' without the newline character and an additional "f" at the beginning to denote a file name
		fileServer(port, filename, sock)
	elif option == "X": # Otherwise, if 'option' is equal to "X"
		os._exit(0)
	else: # Otherwise
		print (option + " is not valid.") # Print what is stored in 'option' followed by " is not valid."
	run(sock, port) # Calls 'run' function and passes in 'sock'
	
# Runs program as a client
def Client (listenPort, serverPort, serverAddress): # Creates 'Client' function and takes in 'listenPort' that holds the port number to connect to, 'serverPort' that holds the server's port number, and 'serverAddress', that hods the address of the server to connect to
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializes 'sock' with a socket
	sock.connect((serverAddress, serverPort)) # Connect to the server with address 'serverAddress' over port number 'serverPort'
	receiveThread = receive.Receive(sock) # Create thread to receive messages
	receiveThread.start() # Start thread to receive messages
	sock.send(str(listenPort).encode())
	while (receive.hasPort == False):
		i = 1
	receive.filePort = listenPort
	run(sock, listenPort) # Calls 'run' function