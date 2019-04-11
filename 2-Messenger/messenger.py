# Ross Nelson CSC376 Assignment 2: Messenger
# April 23rd 2019

import sys # Import sys module
import socket # Import socket module

# Displays how to open the program
def usage (script_name): # Creates 'usage' function and takes in a string that holds the title of the program
	print('Usage: py ' + script_name + ' (-l) <port number>') # Prints 'Usage: py messenger.py (-l) <port number>'

# Reads command line arguments and determines if program should be run as a client or a server
isServer = False # Initializes 'isServer' to be False
portNum = 0 # Initializes the port number, 'portNum' to be 0
args = sys.argv # Stores the command line arguments array in to array 'args'
numArgs = len(args) # Store the number of command line arguments in 'numArgs'
if numArgs == 2: # Checks if there are exactly 2 command line arguments
		isServer = False # Sets 'isServer' to be false, since the listen option (-l) was not selected
		portNum = args[1] # Sets 'portNum' to be the 1st argument
elif numArgs == 3: # Checks if there are exactly 3 command line arguments
		isServer = True # Sets 'isServer' to be true
		portNum = args[2] # Sets 'portNum' to be the 2nd argument
else: # If there are not exactly 2 or 3 command line arguments
	usage(args[0]) # Call 'usage' and pass the 0th command line argument, the name of the program
	sys.exit() # Call 'sys.exit()' to close the program

# Determines which function to run depending on the state of 'isServer'
if (isServer): # Checks if 'isServer' is set to 'True'
	server() # Calls the 'server' function
else: # If 'isServer' is not 'True' i.e. 'False'
	client() # Calls the 'client' function


def server ():

def client ():