"""

zone.py
Contains definitions of the WorldMap class and the Zone class.
Written by:  Mohsin Rizvi
Last edited: 06/01/17

"""

import npc

# Holds the map of the world.
class WorldMap:

    # Purpose:    Constructs a WorldMap.
    # Parameters: None
    # Return:     Void
    def __init__(self):
        self.initZones()

    # Purpose:    Initializes a basic empty zone map of the world.
    # Parameters: None
    # Return:     Void
    def initZones(self):
        self.zones = [[]]

# Holds data of an individual zone.
class Zone:

    # Purpose:    Constructs a Zone.
    # Parameters: None
    # Return:     Void
    def __init__(self):
        pass
