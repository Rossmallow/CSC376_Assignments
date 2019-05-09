# Ross Nelson CSC376 Assignment 4: Messenger with File Transfers
# May 23rd, 2019
# messenger_with_files.py

# Import modules
import sys # Import sys module
import socket # Import socket module
import receive # Imoprt custom receive module

# Reads command line arguments and determines if program should be run as a client or a server
args = sys.argv # Stores the command line arguments array in to array 'args'
numArgs = len(args) # Store the number of command line arguments in 'numArgs'
serverAddress = 'localhost' # Initializes 'serverAddress' with 'localhost' as the default server address
isServer = True # Initializes 'isServer' to be true
i = 0 # Initializes i to be 0
while i < numArgs: # Iterate through each of the arguments
	if args[i] == '-l': # If the current argument is equal to '-l'
		listenPort = int(args[i + 1]) # Set 'listenPort' to be equal to the value following '-l' converted to an integer
	if args[i] == '-p': # If the current argument is equal to '-p'
		serverPort = int(args[i + 1]) # Set 'serverPort' to be equal to the value following '-p' converted to an integer
		isServer = False # Set 'isServer' to be False, since only the client takes these arguments
	if args[i] == '-s': # If the current argument is equal to '-s'
		serverAddress = int(args[i + 1]) # Set 'serverAddress' to be equal to the value following '-s' converted to an integer
		isServer = False # Set 'isServer' to be False, since only the client takes these arguments
	i += 1 # Increment i

# Determines which function to run depending on the state of 'isServer'
if (isServer): # Checks if 'isServer' is set to 'True'
	Server(listenPort) # Calls the 'run' function from the server module and passes 'listenPort'
else: # If 'isServer' is not 'True' i.e. 'False'
	Client(listenPort, serverPort, serverAddress) # Calls the 'run' function from the client module and passes 'listenPort', 'serverPort', and 'serverAddress'

	# Runs program
def run (sock): # Creates 'run' function that takes in socket 'sock' and that asks users to select from a list of options until the program is closed
	optionsMessage = "Enter an option ('m', 'f', 'x'):\n (M)essage (send)\n (F)ile (request)\ne(X)it" # Stores sting "Enter an option ('m', 'f', 'x'):\n (M)essage (send)\n (F)ile (request)\ne(X)it" in 'optionsMessage'
	print(optionsMessage) # Prints what is stored in 'optionsMessage'
	option = sys.stdin.readline().replace("\n", "").upper() # Stores standard input in 'option' after removing the newline character, and converting the input to all uppercase
	if option == "M": # If 'option' is equal to "M"
		print("Enter your message:") # Prints "Enter your message:"
		message = sys.stdin.readline().replace("\n", "") # Saves standard input to 'message' without the newline character
		sock.send(message.encode()) # encodes and sends 'message' over 'sock'
	elif option == "F": # Otherwise, if 'option' is equal to "F"
		print("Which file do you want?") # Prints "Which file do you want?"
		filename = sys.stdin.readline().replace("\n", "") # Saves standard input to 'filename' without the newline character
		#CALL RECEIVE FUNCTION
		print("RECEIVE")
	elif option == "X": # Otherwise, if 'option' is equal to "X"
		sys.exit() # Call 'sys.exit()' to end the thread
	else: # Otherwise
		print (option + " is not valid.") # Print what is stored in 'option' followed by " is not valid."
	run(sock) # Calls 'run' function and passes in 'sock'

# Starts program as a server
def Server (port): # Creates 'Server' function and takes in 'port' that holds the port number to connect to
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializes 'serversocket' with a socket
	serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Allows multiple sockets on the same port
	serversocket.bind(('', port)) # Binds 'serversocket' to 'port'
	serversocket.listen(5) # Listens for socket connections with a backlog value of '5'
	sock, addr = serversocket.accept() # Accept the connection and store it in 'sock' and 'addr'
	serversocket.close() # Close the socket as it is no longer needed
	receiveThread = receive.Receive(sock) # Create thread to receive messages
	receiveThread.start() # Start thread to receive messages
	run(sock) # Call 'run' function and passes in 'sock'

	# Runs program as a client
def Client (listenPort, serverPort, serverAddress): # Creates 'Client' function and takes in 'listenPort' that holds the port number to connect to, 'serverPort' that holds the server's port number, and 'serverAddress', that hods the address of the server to connect to
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Initializes 'sock' with a socket
	sock.connect((serverAddress, listenPort)) # Connect to the server with address 'serverAddress' over port number 'listenPort'
	receiveThread = receive.Receive(sock) # Create thread to receive messages
	receiveThread.start() # Start thread to receive messages
	run(sock) # Calls 'run' function