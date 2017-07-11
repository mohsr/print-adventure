"""

item.py
Contains the definition of the Item class.
Written by:  Mohsin Rizvi
Last edited: 07/11/17

"""

import os

# An Item.
class Item:

    # Purpose:    Create an item with the given name.
    # Parameters: A string name for the item.
    # Return:     Void
    def __init__(self, name):
        self.name = name
        self.fixData()
        self.openData()

    # Purpose:    Appends a new line to the end of the item directory if one
    #             is not already present.
    # Parameters: None
    # Return:     Void
    def fixData(self):
        # Credit given to Stack Overflow for helping me figure out how to get
        # the filepath of the current script's directory. More info in 
        # README.md.
        path = os.path.dirname(os.path.realpath(__file__))
        if not os.path.isdir(path):
            os.mkdir(path)
        os.chdir(path)

        # Open the item directory file for reading and writing.
        with open("items", "r+") as fixer:
            x = fixer.read()
            # Check last character, add a new line char if one is not present
            if len(x) > 0:
                if x[len(x) - 1] != "\n":
                    fixer.write("\n")
            else:
                fixer.write("\n")

    # Purpose:    Gives the item data according to its name using a database
    #             of items stored in a file.
    # Parameters: None
    # Return:     Void
    def openData(self):
        # Open item directory file for reading.
        with open("items", "r") as self.reader:
            # Find the correct item in the file
            x = self.reader.readline()
            if x == "":
                print("ERROR: Item not found.")
                return
            while x != self.name + "\n":
                x = self.reader.readline()
                if x == "":
                    print("ERROR: Item not found.")
                    return
            # Read the data into the Item object.
            self.readData()

    # Purpose:    Retrieves and stores the Item data from an opened
    #             directory of items ("items").
    # Parameters: None
    # Return:     Void
    def readData(self):
        # Get data common to all items.
        self.getCommonData()
        # Gets item data according to whichever item type is read from file.
        # First, retrieve item type.
        x = self.reader.readline()
        self.type = x[0:len(x) - 1]
        types = ["Food", "Armor", "Weapon", "Ring", "Misc"]
        if self.type not in types:
            print("ERROR: Item type invalid.")
            return
        # Now, retrieve item data according to type.
        self.getFoodData()
        self.getArmorData()
        self.getWeaponData()
        self.getRingData()
        self.getMiscData()

    # Purpose:    Retrieves and stores data used for all items.
    # Parameters: None
    # Return:     Void
    def getCommonData(self):
        # Get data common to all items.
        x = self.reader.readline()
        self.desc = x[0:len(x) - 1]

    # Purpose:    Retrieves and stores food data for food items.
    # Parameters: None
    # Return:     Void
    def getFoodData(self):
        if self.type != "Food":
            return
        # Get HP restored per bite and amount of bites in a food Item.
        self.hp_per_bite = int(self.reader.readline())
        self.bites = int(self.reader.readline())

    # Purpose:    Retrieves and stores armor data for armor items.
    # Parameters: None
    # Return:     Void
    def getArmorData(self):
        if self.type != "Armor":
            return
        # Get profession data.
        x = self.reader.readline()
        self.prof = x[0:len(x) - 1]
        # Get defense and resist data.
        self.defense = int(self.reader.readline())
        self.poison_resist = int(self.reader.readline())
        self.fire_resist = int(self.reader.readline())
        self.cold_resist = int(self.reader.readline())
        self.electric_resist = int(self.reader.readline())
        self.earth_resist = int(self.reader.readline())

    # Purpose:    Retrieves and stores weapon data for weapon items.
    # Parameters: None
    # Return:     Void
    def getWeaponData(self):
        if self.type != "Weapon":
            return
        # Get profession data.
        x = self.reader.readline()
        self.prof = x[0:len(x) - 1]
        # Get weapon data.
        self.damage = int(self.reader.readline())
        self.poison_dmg = int(self.reader.readline())
        self.fire_dmg = int(self.reader.readline())
        self.cold_dmg = int(self.reader.readline())
        self.electric_dmg = int(self.reader.readline())
        self.earth_dmg = int(self.reader.readline())
        self.defense = int(self.reader.readline())
        self.poison_resist = int(self.reader.readline())
        self.fire_resist = int(self.reader.readline())
        self.cold_resist = int(self.reader.readline())
        self.electric_resist = int(self.reader.readline())
        self.earth_resist = int(self.reader.readline())

    # Purpose:    Retrieves and stores ring data for ring items.
    # Parameters: None
    # Return:     Void
    def getRingData(self):
        if self.type != "Ring":
            return
        # Get ring data.
        self.str = int(self.reader.readline())
        self.wis = int(self.reader.readline())
        self.dex = int(self.reader.readline())
        self.cha = int(self.reader.readline())
        self.lck = int(self.reader.readline())
        self.per = int(self.reader.readline())

    # Purpose:    Retrieves and stores misc data for misc items.
    # Parameters: None
    # Return:     Void
    def getMiscData(self):
        if self.type != "Misc":
            return

    # Purpose:    Prints item data.
    # Parameters: None
    # Return:     Void
    def printData(self):
        if self.type == "Weapon" or self.type == "Armor":
            print("Item: " + self.name + ". " + self.prof + " " +
                  self.type + ". " + self.desc)
        else:
            print("Item: " + self.name + ". " + self.type + ". " + self.desc)
        if self.type == "Food":
            self.printFood()
        elif self.type == "Armor":
            self.printArmor()
        elif self.type == "Weapon":
            self.printWeapon()
        elif self.type == "Ring":
            self.printRing()
        elif self.type == "Misc":
            self.printMisc()

    # Purpose:    Prints food item data.
    # Parameters: None
    # Return:     Void
    def printFood(self):
        print("    HP per bite: " + str(self.hp_per_bite))
        print("    No. of bites: " + str(self.bites))

    # Purpose:    Prints armor item data.
    # Parameters: None
    # Return:     Void
    def printArmor(self):
        print("    Defense: " + str(self.defense))
        if self.poison_resist != 0:
            print("    Poison resist: " + str(self.poison_resist))
        if self.fire_resist != 0:
            print("    Fire resist: " + str(self.fire_resist))
        if self.cold_resist != 0:
            print("    Cold resist: " + str(self.cold_resist))
        if self.electric_resist != 0:
            print("    Electric resist: " + str(self.electric_resist))
        if self.earth_resist != 0:
            print("    Earth resist: " + str(self.earth_resist))

    # Purpose:    Prints weapon item data.
    # Parameters: None
    # Return:     Void
    def printWeapon(self):
        print("    Base damage: " + str(self.damage))
        if self.poison_dmg != 0:
            print("    Poison damage: " + str(self.poison_dmg))
        if self.fire_dmg != 0:
            print("    Fire damage: " + str(self.fire_dmg))
        if self.cold_dmg != 0:
            print("    Cold damage: " + str(self.cold_dmg))
        if self.electric_dmg != 0:
            print("    Electric damage: " + str(self.electric_dmg))
        if self.earth_dmg != 0:
            print("    Earth damage: " + str(self.earth_dmg))
        if self.defense != 0:
            print("    Defense: " + str(self.defense))
        if self.poison_resist != 0:
            print("    Poison resist: " + str(self.poison_resist))
        if self.fire_resist != 0:
            print("    Fire resist: " + str(self.fire_resist))
        if self.cold_resist != 0:
            print("    Cold resist: " + str(self.cold_resist))
        if self.electric_resist != 0:
            print("    Electric resist: " + str(self.electric_resist))
        if self.earth_resist != 0:
            print("    Earth resist: " + str(self.earth_resist))

    # Purpose:    Prints ring item data.
    # Parameters: None
    # Return:     Void
    def printRing(self):
        if self.str != 0:
            print("    Strength bonus: " + str(self.str))
        if self.wis != 0:
            print("    Wisdom bonus: " + str(self.wis))
        if self.dex != 0:
            print("    Dexterity bonus: " + str(self.dex))
        if self.cha != 0:
            print("    Charisma bonus: " + str(self.cha))
        if self.lck != 0:
            print("    Luck bonus: " + str(self.lck))
        if self.per != 0:
            print("    Perception bonus: " + str(self.per))

    # Purpose:    Prints misc item data.
    # Parameters: None
    # Return:     Void
    def printMisc(self):
        pass
