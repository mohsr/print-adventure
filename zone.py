"""

zone.py
Contains definitions of the WorldMap class and the Zone class.
Written by:  Mohsin Rizvi
Last edited: 06/29/17

"""

import npc
import random

# Holds the map of the world.
class WorldMap:

    # Purpose:    Constructs a 12x12 WorldMap and fills it in.
    # Parameters: None
    # Return:     Void
    def __init__(self):
        self.biomeNames = list()

        # Create zones and biomes on the world map.
        self.initZones()
        self.genZones()

        # TEST CODE used to see how the map generates.
        self.printMap()

    # Purpose:    Initializes a basic empty zone map of the world.
    # Parameters: None
    # Return:     Void
    def initZones(self):
        # Create a 12x12 list of Zones
        self.zones = [[Zone(j, i) for i in range(12)] for j in range(12)]

    # Purpose:    Generates the world's zones.
    # Parameters: None
    # Return:     Void
    def genZones(self):
        # Constructs biomes on the world map.
        self.initBiomes(0, 0)
        self.genRivers(2)

    # Purpose:    Generates the world's biomes from the given x and y
    #             world-map coordinates.
    # Parameters: An int x-coordinate and an int y-coordinate for the
    #             world map to start generating from.
    # Return:     Void
    def initBiomes(self, x, y):
        if x < 0 or y < 0 or x > 11 or y > 11:
            print("ERROR: Invalid biome-gen params.")
            return
        # Biome generation algorithm explained in section C of README.
        self.zones[x][y].assignBiome()
        self.assignBiomeNeighbors(x, y, 100)

    # Purpose:    Gives a Zone's neighbors biomes. Recursive function used
    #             for biome generation.
    # Parameters: An int x-coord for a zone, an int y-coord for a zone, and
    #             an int from 0-100 representing the percent chance of the
    #             Zone's neighbors having the same biome.
    # Return:     Void
    def assignBiomeNeighbors(self, x, y, chance):
        currZone = self.zones[x][y]
        # Biome generation algorithm explained in section C of README.
        # Recurse on each unknown neighbor
        if currZone.hasNeighborNorth():
            if self.zones[x][y - 1].known == False:
                roll = random.randrange(0, 100)
                if roll < chance:
                    self.zones[x][y - 1].setBiome(currZone.biome)
                    self.zones[x][y - 1].setBiomeName(currZone.biomeName)
                    self.assignBiomeNeighbors(x, y - 1, chance - 10)
                else:
                    self.initBiomes(x, y - 1)
        if currZone.hasNeighborEast():
            if self.zones[x + 1][y].known == False:
                roll = random.randrange(0, 100)
                if roll < chance:
                    self.zones[x + 1][y].setBiome(currZone.biome)
                    self.zones[x + 1][y].setBiomeName(currZone.biomeName)
                    self.assignBiomeNeighbors(x + 1, y, chance - 10)
                else:
                    self.initBiomes(x + 1, y)
        if currZone.hasNeighborSouth():
            if self.zones[x][y + 1].known == False:
                roll = random.randrange(0, 100)
                if roll < chance:
                    self.zones[x][y + 1].setBiome(currZone.biome)
                    self.zones[x][y + 1].setBiomeName(currZone.biomeName)
                    self.assignBiomeNeighbors(x, y + 1, chance - 10)
                else:
                    self.initBiomes(x, y + 1)
        if currZone.hasNeighborWest():
            if self.zones[x - 1][y].known == False:
                roll = random.randrange(0, 100)
                if roll < chance:
                    self.zones[x - 1][y].setBiome(currZone.biome)
                    self.zones[x - 1][y].setBiomeName(currZone.biomeName)
                    self.assignBiomeNeighbors(x - 1, y, chance - 10)
                else:
                    self.initBiomes(x - 1, y)

    # Purpose:    Prints a list of zones in the world map, for testing
    #             purposes and for an in-game world map. Code commented out
    #             is used for testing.
    # Parameters: None
    # Return:     Void
    def printMap(self):
        # For each row of zones, print biome of each zone
        for i in self.zones:
            row = " | "
            for j in i:
                # Print coords:
                #row += str(j.x) + " " + str(j.y) + " | "
                # Print biomes:
                #row += str(j.biome)[0:4] + " | "
                # Print rivers:
                if j.river:
                    row += "* | "
                else:
                    row += "  | " 
            print(row)

    # Purpose:    Generates a give number of rivers on the world map.
    # Parameters: An int number of rivers to generate.
    # Return:     Void
    def genRivers(self, numRivers):
        # Place each river.
        for i in range(numRivers):
            # direction is 0 if starting from north side of map, 1 if starting
            # from west side. Start indicates starting coordinate on map.
            direction = random.randrange(0, 2)
            start = random.randrange(0, 12)
            if direction == 0:
                x = 0
                y = start
            elif direction == 1:
                x = start
                y = 0
            # Start a river at the selected point and generate it either
            # moving south or to the east.
            self.zones[x][y].river = True
            if direction == 0:
                self.genRiverSouth(x, y)
            elif direction == 1:
                self.genRiverEast(x, y)

    # Purpose:    Generates a river from the point at the given coordinates
    #             until the river hits the edge of the map heading south. 
    #             Recursive function.
    # Parameters: An int x-coord and int y-coord representing the zone to
    #             spread the river from.
    # Return:     Void
    def genRiverSouth(self, x, y):
        # Either place the next river tile to the southwest (0), the south
        # (1), or the southeast (2).
        nextPos = random.randrange(0, 3)
        if nextPos == 0:
            # Check that next tile is valid. If so, move to it.
            if x + 1 < 12 and y - 1 >= 0:
                self.zones[x + 1][y - 1].river = True
                self.genRiverSouth(x + 1, y - 1)
            else:
                return
        elif nextPos == 1:
            # Check that next tile is valid. If so, move to it.
            if x + 1 < 12:
                self.zones[x + 1][y].river = True
                self.genRiverSouth(x + 1, y)
            else:
                return
        elif nextPos == 2:
            # Check that next tile is valid. If so, move to it.
            if x + 1 < 12 and y + 1 < 12:
                self.zones[x + 1][y + 1].river = True
                self.genRiverSouth(x + 1, y + 1)
            else:
                return

    # Purpose:    Generates a river from the point at the given coordinates
    #             until the river hits the edge of the map heading east.
    #             Recursive function.
    # Parameters: An int x-coord and int y-coord representing the zone to
    #             spread the river from.
    # Return:     Void
    def genRiverEast(self, x, y):
        # Either place the next river tile to the northeast (0), the east (1),
        # or the southeast (2).
        nextPos = random.randrange(0, 3)
        if nextPos == 0:
            # Check that next tile is valid. If so, move to it.
            if x - 1 >= 0 and y + 1 < 12:
                self.zones[x - 1][y + 1].river = True
                self.genRiverEast(x - 1, y + 1)
            else:
                return
        if nextPos == 1:
            # Check that next tile is valid. If so, move to it.
            if y + 1 < 12:
                self.zones[x][y + 1].river = True
                self.genRiverEast(x, y + 1)
            else:
                return
        if nextPos == 2:
            # Check that next tile is valid. If so, move to it.
            if x + 1 < 12 and y + 1 < 12:
                self.zones[x + 1][y + 1].river = True
                self.genRiverEast(x + 1, y + 1)
            else:
                return

    # Purpose:    Generates 8 to 10 villages and towns on the world map.
    # Parameters: None
    # Return:     Void
    def genTowns(self):
        pass

    # Purpose:    Generates 3 to 4 cities on the world map.
    # Parameters: None
    # Return:     Void
    def genCities(self):
        pass

    # Purpose:    Generates 6 to 8 dungeons on the world map.
    # Parameters: None
    # Return:     Void
    def genDungeons(self):
        pass

    # Purpose:    Generates an int number of quests.
    # Parameters: An int number of quests to generate.
    # Return:     Void
    def genQuests(self, numQuests):
        pass

# Holds data of an individual zone.
class Zone:

    # Purpose:    Constructs a Zone.
    # Parameters: An int x-coordinate and an int y-coordinate
    # Return:     Void
    def __init__(self, xCord, yCord):
        self.x = xCord
        self.y = yCord

        self.known = False
        self.river = False

        self.environment = list()

    # Purpose:    Gives the Zone a random biome and a name for the biome
    #             region. Marks the Zone as known.
    # Parameters: None
    # Return:     Void
    def assignBiome(self):
        biomes = ["Plains", "Forest", "Rainforest", "Dunes",
                  "Mountain", "Hills", "Desert", "Steppes",
                  "Snows", "Volcano"]
        # Randomly pick a biome, name the biome, and mark the Zone as known.
        self.biome = random.choice(biomes)
        self.genBiomeName()
        self.known = True

    # Purpose:    Gives the Zone a specified biome. Marks the Zone as known.
    # Parameters: A string biome name.
    # Return:     Void
    def setBiome(self, theBiome):
        # Give the Zone the biome and mark it as known.
        self.biome = theBiome
        self.known = True

    # Purpose:    Gives the Zone a name for its biome region.
    # Parameters: A string biome region name.
    # Return:     Void
    def setBiomeName(self, theBiomeName):
        self.biomeName = theBiomeName

    # Purpose:    Generates a name for a specific biome region.
    # Parameters: None
    # Return:     Void
    def genBiomeName(self):
        adj = ["Iron", "Steady", "Brown", "Lush", "Ferocious", "Quaint",
               "Serene", "Rocky", "Steel", "Peaceful", "Calm", "Stormy",
               "Tumultuous", "Thundering", "Dusty", "Red", "Dark", "Black",
               "Holy", "Unholy", "Ancient", "Young", "New", "Old", "Firey",
               "Infernal", "Demonic", "Unyielding", "Humble", "Primordial",
               "High", "Secret", "Yearning", "Windy", "Wobbley", "Departed",
               "Lightbound", "Unfaltering", "Mesmerizing", "Halting",
               "Broken", "Upside-down", "Great", "Little", "Light's",
               "Dark's", "Shadow", "Craterous", "Windswept", "Bloodied",
               "Raven's", "Nightfall", "Night's", "Sunrise", "Sunset",
               "Middle Moon", "Old Man's", "Craggy", "Red Rock",
               "Roaring", "Timeless", "Alien", "Blackened", "Mythic",
               "Lion Lord's", "Vile", "Bracken", "Toasted"]
        # Picks an adjective to create a name for a specific biome.
        self.biomeName = random.choice(adj) + " " + self.biome

    # Purpose:    Returns true if the Zone has a neighboring Zone north of it,
    #             false otherwise.
    # Parameters: None
    # Return:     True
    def hasNeighborNorth(self):
        # Return False if on north end of map, True otherwise
        if self.y == 0:
            return False
        return True

    # Purpose:    Returns true if the Zone has a neighboring Zone east of it,
    #             false otherwise.
    # Parameters: None
    # Return:     True
    def hasNeighborEast(self):
        # Return False if on east end of map, True otherwise
        if self.x == 11:
            return False
        return True

    # Purpose:    Returns true if the Zone has a neighboring Zone south of it,
    #             false otherwise.
    # Parameters: None
    # Return:     True
    def hasNeighborSouth(self):
        # Return False if on south end of map, True otherwise
        if self.y == 11:
            return False
        return True

    # Purpose:    Returns true if the Zone has a neighboring Zone west of it,
    #             false otherwise.
    # Parameters: None
    # Return:     True
    def hasNeighborWest(self):
        # Return False if on west end of map, True otherwise
        if self.x == 0:
            return False
        return True
