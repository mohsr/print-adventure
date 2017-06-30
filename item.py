"""

item.py
Contains the definition of the Item class.
Written by:  Mohsin Rizvi
Last edited: 06/29/17

"""

# An Item.
class Item:

    # Purpose:    Initialize an item with the given name.
    # Parameters: A string name for the item.
    # Return:     Void
    def __init__(self, name):
        self.name = name
        self.getData()

    # Purpose:    Gives the item data according to its name using a database
    #             of items stored in a file.
    # Parameters: None
    # Return:     Void
    def getData(self):
        pass