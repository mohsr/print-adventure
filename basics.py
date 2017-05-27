"""

basics.py
Contains the definitions of basic functions used for various purposes
in the game.
Written by:  Mohsin Rizvi
Last edited: 05/26/17

"""

import sys

# Purpose:    Prints the keys followed by the values of a given dictionary,
#             where the values are CommVal objects.
# Parameters: A dictionary to print values then Command keys for.
# Return:     Void
def printPairs(comms):
	# Print all key-value pairs in the dictionary
	for i in comms:
		print("  " + i + " - " + comms[i])

# Purpose:    Gets a string input from standard input and checks it against
#             all keys in the given dictionary. Returns key that
#             input matches. Prompts user until input is valid.
# Parameters: A dictionary of commands to look through, where keys are
#             strings and values strings as well.
# Return:     The key that input matches.
def command(comms):
	inv = True
	done = False

	# Get a command from standard input
	entered = input().strip()
	# Checks validity of input against each possible command
	while not done:
		# Check validity of input
		for i in comms:
			if entered.lower() == i.lower():
				return i
		# The rest of the while loop runs if input is invalid
		if inv:
			print("-Invalid command. Please enter a new one. Enter \"$\"" +
				  " for a list of commands.")
		inv = True
		entered = input().strip()
		# Print possible commands if requested
		if entered == "$":
			printPairs(comms)
			inv = False

# Purpose:    Quits the game.
# Parameters: None
# Return:     Void
def quit():
	print("Thanks for playing!")
	sys.exit()

# Purpose:    Prints the given error message and quits the game.
# Parameters: A string error message to print.
# Return:     Void
def error_quit(message):
	sys.exit(message)