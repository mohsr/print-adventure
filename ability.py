"""

ability.py
Contains the definition of the Ability class.
Written by:  Mohsin Rizvi
Last edited: 06/29/17

"""

import basics

# An ability to use in-combat.
class Ability:

    # Purpose:    Construct an ability.
    # Parameters: A name for the ability.
    # Return:     Void
    def __init__(self, abiName = "Cool Move"):
        self.name = abiName