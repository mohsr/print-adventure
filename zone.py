"""

zone.py
Contains definitions of the WorldMap class, the Zone class, and all
children of the Zone class.
Written by:  Mohsin Rizvi
Last edited: 05/27/17

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
        self.connections = list()
        self.inhabitants = list()

# Holds data on a town.
class Town(Zone):

    # Purpose:    Constructs a Town.
    # Parameters: None
    # Return:     Void
    def __init__(self):
        pass

# Holds data on a city.
class City(Town):

    # Purpose:    Constructs a City.
    # Parameters: None
    # Return:     Void
    def __init__(self):
        pass

# Holds data on a dungeon.
class Dungeon(Zone):

    # Purpose:    Constructs a Dungeon.
    # Parameters: None
    # Return:     Void
    def __init__(self):
        pass
