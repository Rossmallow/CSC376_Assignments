# Ross Nelson CSC376 Assignment 4: Messenger with File Transfers
# May 23rd, 2019
# messenger_with_files.py

# Import modules
import sys # Import sys module
import client, server # Import client and server modules

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
	server.Server(listenPort) # Calls the 'run' function from the server module and passes 'listenPort'
else: # If 'isServer' is not 'True' i.e. 'False'
	print("client")
	client.Client(listenPort, serverPort, serverAddress) # Calls the 'run' function from the client module and passes 'listenPort', 'serverPort', and 'serverAddress'