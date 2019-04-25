# Ross Nelson CSC376 Assignment 3: Chat
# May 7th, 2019
# ChatServer.py

# Import modules
import sys # Import sys module
import socket # Import socket module
import serverReceive # Import custom serverReceive module

# Finds and stores port number from the command line arguments
args = sys.argv # Stores the command line arguments array in to array 'args'
port = int(args[1]) # Stores the 1st command line argument in 'port' (where 0th is the name of the program)

# Creates a socket, binds it to port 'port' and listens for connections
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializes 'serversocket' with a socket
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Allows multiple sockets on the same port
serversocket.bind(('', port)) # Binds 'serversocket' to 'port'
serversocket.listen(5) # Listens for socket connections with a backlog value of '5'

# Accepts connections and adds them to global array 'serverReceive.clients'
while (True): # Loop forever
	sock, addr = serversocket.accept() # Accepts connection and stores socket in 'sock' and 'addr'
	serverReceive.Receive(sock).start() # Creates new thread by calling 'Receive' in 'serverReceive.py' and passes 'sock' to receive from, then starts the thread
	serverReceive.clients.append(sock) # Appends 'sock' to the end of gloabl array 'serverReceive.clients'