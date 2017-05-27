"""

npc.py
Contains the definition of the NPC class.
Written by:  Mohsin Rizvi
Last edited: 05/27/17

"""

import bio
import cbt_ability

# A basic NPC to interact with.
class NPC:

    # Purpose:    Construct a random NPC.
    # Parameters: A string charType. It can be one of several strings to
    #             specify a certain type of NPC to construct. If it is not
    #             one of those, construct a random NPC. A string charRace
    #             is also given.
    # Return:     Void
    def __init__(self, charType, charRace):
        if charType.lower() == "mob":
            self.genMob(charRace)
        elif charType.lower() == "vendor":
            self.genVendor(charRace)

    # Purpose:    Make the NPC a mob (generic enemy).
    # Parameters: A string charRace indicating the race of the mob.
    # Return:     Void
    def genMob(self, charRace):
        pass

    # Purpose:    Make the NPC a vendor.
    # Parameters: A string charRace indicating the race of the vendor.
    # Return:     Void
    def genVendor(self, charRace):
        pass