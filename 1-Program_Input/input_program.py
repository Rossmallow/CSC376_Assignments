# Ross Nelsson CSC 376 Assignment 1: Program Input
import sys # Import sys 

# Echo standard input
print ("Standard Input:") # Prints 'Standard Input:'
text = sys.stdin.readline().replace("\n", "") # Saves standard input to 'text' without the newline character
while text: # Loop while 'text' has a value
	print (text) # Print the value of 'text'
	text = sys.stdin.readline().replace("\n", "") # Saves standard input to 'text' without the newline character

# Get the command line arguments
options = ["", "", False] # Instantiate options array

arguments = sys.argv # Store command line arguments in 'arguments'
#print (arguments) # Print contents of 'arguments'
i = 1 # Instantiate i to 1 because the 0th argument can be ignored
while i < len(arguments): # Loop until the end of the array
	if (arguments[i] == "-o"): # Check for option 1
		options[0] = arguments[i + 1] # Set the 0th index of 'options' to be the command line argument following '-o'
	if (arguments[i] == "-t"): # Check for option 2
		options[1] = arguments[i + 1] # Set the 1st index of 'options' to be the command line argument following '-t'
	if (arguments[i] == "-h"): # Check for option 3
		options[2] = True # Set the 3rd index of 'options' to be true
	i += 1 # Increment i by 1

# Print the command line arguments
print ("Command line arguments:") # Prints 'Command line arguments:'
if (options[0] != ""): # Check for an argument for the first option
	print ("option 1: " + options[0]) # Prints 'option 1:' followed by the command line argument
if (options[1] != ""): # Check for an argument for the second option
	print ("option 2: " + options[1]) # Prints 'option 2:' followed by the command line argument
if (options[2] != False): # Check for an argument for the third option
	print("option 3") # Prints 'option 3'