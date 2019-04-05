# Ross Nelsson CSC 376 Assignment 1: Program Input
import sys

# Get the command line arguments
options = ["", "", False]

arguments = sys.argv
print (arguments)
i = 1
while i < len(arguments):
	if (arguments[i] == "-o"):
		options[0] = arguments[i + 1]
	if (arguments[i] == "-t"):
		options[1] = arguments[i + 1]
	if (arguments[i] == "-h"):
		options[2] = True
	i = i + 1