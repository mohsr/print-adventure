"""

npc.py
Contains the definition of the NPC class.
Written by:  Mohsin Rizvi
Last edited: 06/29/17

"""

import bio

# A basic NPC to interact with.
class NPC:

    # Purpose:    Construct a random NPC.
    # Parameters: A string NPC name.
    # Return:     Void
    def __init__(self, name):
        self.name = name