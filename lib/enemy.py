"""

enemy.py
Contains the definition of the Enemy class.
Written by:  Mohsin Rizvi
Last edited: 06/29/17

"""

# An enemy to fight.
class Enemy:

    # Purpose:    Constructs an enemy with the given name.
    # Parameters: A name for the enemy.
    # Return:     Void
    def __init__(self, name):
        self.name = name
        self.getData()

    # Purpose:    Get enemy data from a file containing enemy info.
    # Parameters: None
    # Return:     Void
    def getData(self):
        pass