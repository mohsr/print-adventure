"""

basics.py
Contains the definitions of basic functions used for various purposes
in the game.
Written by:  Mohsin Rizvi
Last edited: 07/12/17

"""

import sys
import os

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
#             strings and values describe the keys as well.
# Return:     The key that input matches.
def command(comms):
    # Get a command from standard input
    # Checks validity of input against each possible command
    while not done:
        
        # Read the input
        # Querying the user is done by the caller
        entered = input().strip().lower()
        # Check validity of input
        for i in comms:
            if entered == i.lower():
                return i
        # The execute reaches here if and only if the command is not found
        # Print possible commands if requested
        if entered == "$":
            printPairs(comms)
        else:
            print("-Invalid command. Please try again. Enter \"$\"" +
                  " for a list of commands.")

# Purpose:    Appends a new line to the end of the file with the given
#             filename if one is not already present.
# Parameters: A filename of a file in this script's directory to append
#             a new line onto.
# Return:     Void
def fixData(filename):
    # Credit given to Stack Overflow for helping me figure out how to get
    # the filepath of the current script's directory. More info in 
    # README.md.
    # Get the path of the current script's directory
    path = os.path.dirname(os.path.realpath(__file__))
    # Change the working directory to this script's directory
    os.chdir(path)

    # Open the  file for reading and writing.
    with open(filename, "r+") as fixer:
        x = fixer.read()
        # Check last character, add a new line char if one is not present
        if len(x) > 0:
            if x[len(x) - 1] != "\n":
                fixer.write("\n")
        else:
            fixer.write("\n")

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
