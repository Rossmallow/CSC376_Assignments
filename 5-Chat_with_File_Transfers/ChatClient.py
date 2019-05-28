# Ross Nelson CSC376 Assignment 5: Chat_with_File_Transfers
# June 11th, 2019
# ChatClient.py

# Import modules
import sys # Import sys module
import socket # Import socket module
import clientSend, clientReceive # Import custom clientSend and clientReceive modules

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
		ownername = "o" + sys.stdin.readling().replace("\nl", "")
		print("Which file do you want?") # Prints "Which file do you want?"
		filename = "f" + sys.stdin.readline().replace("\n", "") # Saves standard input to 'filename' without the newline character and an additional "f" at the beginning to denote a file name
		fileServer(port, filename, sock)
	elif option == "X": # Otherwise, if 'option' is equal to "X"
		os._exit(0)
	else: # Otherwise
		print (option + " is not valid.") # Print what is stored in 'option' followed by " is not valid."
	run(sock, port) # Calls 'run' function and passes in 'sock'

# Finds and stores port number from the command line arguments
args = sys.argv # Stores the command line arguments array in to array 'args'
i = 1
while i < len(args): # Loop until the end of the array
	if (args[i] == "-l"): 
		listenPort = args[i + 1] 
	if (arguments[i] == "-p"): 
		serverPort = args[i + 1] 
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
sock.send(str(listenPort).encode())

# Creates and starts a receive thread
receiveTherad = clientReceive.Receive(sock) # Calls 'Receive' function in 'clientReceive.py' and stores the thread in 'receiveThread'
receiveTherad.start() # Starts the thread saved in 'receiveThread'

run (sock, serverPort)