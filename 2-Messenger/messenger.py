# Ross Nelson CSC376 Assignment 2: Messenger
# April 23rd 2019
# messenger.py

# Import modules
import sys # Import sys module
import socket # Import socket module
import send, receive # Import custom send module located in send.py

# Displays how to open the program
def usage (script_name): # Creates 'usage' function and takes in a string that holds the title of the program
	print('Usage: py ' + script_name + ' (-l) <port number>') # Prints 'Usage: py messenger.py (-l) <port number>'

# Runs program as a server
def server (port): # Creates 'server' function and takes in 'port' that holds the port number to connect to
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializes 'serversocket' with a socket
	serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # 
	serversocket.bind(('', port)) # Binds 'serversocket' to 'port'
	serversocket.listen(5) # Listens for socket connections with a backlog value of '5'
	sock, addr = serversocket.accept() # Accept the connection and store it in 'sock' and 'addr'
	serversocket.close() # Close the socket as it is no longer needednd
	receiveThread = receive.Receive(sock) # Create thread to receive messages
	receiveThread.start() # Start thread to receive messages
	message = sys.stdin.readline().replace("\n", "") # Saves standard input to 'message' without the newline character
	sendThread = send.Send(sock, message) # Create thread to send messages
	sendThread.start() # Start thread to send messages

# Runs program as a client
def client (port): # Creates 'client' function and takes in 'port' that holds the port number to connect to
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializes 'sock' with a socket
	sock.connect(('localhost', port)) # Connect to the server over 'port'
	receiveThread = receive.Receive(sock) # Create thread to receive messages
	receiveThread.start() # Start thread to receive messages
	message = sys.stdin.readline().replace("\n", "") # Saves standard input to 'message' without the newline character
	sendThread = send.Send(sock, message) # Create thread to send messages
	sendThread.start() # Start thread to send messages

# Reads command line arguments and determines if program should be run as a client or a server
args = sys.argv # Stores the command line arguments array in to array 'args'
numArgs = len(args) # Store the number of command line arguments in 'numArgs'
if numArgs == 2: # Checks if there are exactly 2 command line arguments
		isServer = False # Sets 'isServer' to be false, since the listen option (-l) was not selected
		portNum = int(args[1]) # Sets 'portNum' to be the 1st argument converted to an integer
elif numArgs == 3: # Checks if there are exactly 3 command line arguments
		isServer = True # Sets 'isServer' to be true
		portNum = int(args[2]) # Sets 'portNum' to be the 2nd argument converted to an integer
else: # If there are not exactly 2 or 3 command line arguments
	usage(args[0]) # Call 'usage' and pass the 0th command line argument, the name of the program
	sys.exit() # Call 'sys.exit()' to end the thread

# Determines which function to run depending on the state of 'isServer'
if (isServer): # Checks if 'isServer' is set to 'True'
	server(portNum) # Calls the 'server' function and passes 'portNum' through
else: # If 'isServer' is not 'True' i.e. 'False'
	client(portNum) # Calls the 'client' function and passes 'portNum' through