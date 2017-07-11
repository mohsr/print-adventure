"""

player.py
Contains the definition of the Player class.
Written by:  Mohsin Rizvi
Last edited: 07/11/17

"""

import ability
import item
import bio
import zone

# The Player character.
class Player:

    # Purpose:    Constructor for the Player class.
    # Parameters: A name for the Player, which defaults to "Hero", a character
    #             profession (class), and the character's race (human, alien,
    #             etc.
    # Return:     Void
    def __init__(self, myName, myRace, myProf):
        self.name = myName
        self.race = myRace
        self.prof = myProf
        self.biography = bio.Bio(self.race)
        # Initialize and assign player stats and XP.
        self.assignStats()
        self.xp = 0
        self.lvl = 1
        # Generate a world map.
        self.map = zone.WorldMap()
        # Initialize inventory slots and abilities.
        self.gold = 10
        self.inv = []
        self.abilities = []
        # Initialize gear slots and give player basic gear.
        self.initGear()
        self.assignStarterGear()
        # Initialize combat abilities.
        self.initAbilities()

    # Purpose:    Assigns the player stats based on race and profession.
    # Parameters: None
    # Return:     Void
    def assignStats(self):
        # Initialize all player stats to default values.
        self.initStats()
        # Adjust player stats according to race and profession.
        self.adjustStatsRace()
        self.adjustStatsProf()

    # Purpose:    Initializes player stats to default values.
    # Parameters: None
    # Return:     Void
    def initStats(self):
        self.initBasicStats()
        self.initResistStats()
        self.initAttackStats()

    # Purpose:    Assigns the player default stats.
    # Parameters: None
    # Return:     Void
    def initBasicStats(self):
        # Initialize and declare health and power
        self.max_hp = 20
        self.curr_hp = 20
        self.max_energy = 20
        self.curr_energy = 20
        self.defense = 0
        self.damage = 0
        # Initialize and declare strength, wisdom, dexterity, charisma,
        # luck, and perception stats.
        self.str = 5
        self.wis = 5
        self.dex = 5
        self.cha = 5
        self.lck = 5
        self.per = 5

    # Purpose:    Assigns the player damage-resist default stats.
    # Parameters: None
    # Return:     Void
    def initResistStats(self):
        self.poison_resist = 0
        self.fire_resist = 0
        self.cold_resist = 0
        self.electric_resist = 0
        self.earth_resist = 0

    # Purpose:    Assigns the player special attack stats.
    # Parameters: None
    # Return:     Void
    def initAttackStats(self):
        self.poison_dmg = 0
        self.cold_dmg = 0
        self.fire_dmg = 0
        self.electric_dmg = 0
        self.earth_dmg = 0

    # Purpose:    Adjusts player stats according to character race.
    # Parameters: None
    # Return:     Void  
    def adjustStatsRace(self):
        # Assign stats for each race.
        if self.race == "Human":
            self.max_hp += 3
            self.curr_hp += 3
            self.max_energy += 3
            self.curr_energy += 3
            self.str += 1
            self.wis += 1
            self.cha += 1
            self.fire_resist += 1
        elif self.race == "Dwarf":
            self.max_hp += 6
            self.curr_hp += 6
            self.str += 1
            self.dex += 1
            self.lck += 1
            self.electric_resist += 1
        elif self.race == "Elf":
            self.max_energy += 6
            self.curr_energy += 6
            self.dex += 1
            self.wis += 1
            self.per += 1
            self.poison_resist += 1

    # Purpose:    Adjusts player stats according to character profession.
    # Parameters: None
    # Return:     Void
    def adjustStatsProf(self):
        # Assign warrior prof stats.
        if self.prof == "Warrior":
            self.str += 1
            self.lck += 1
            self.earth_resist += 1
            self.electric_resist -= 1
        # Assign mage prof stats.
        elif self.prof == "Mage":
            self.wis += 1
            self.cha += 1
            self.fire_resist += 1
            self.earth_resist -= 1
        # Assign ranger prof stats.
        elif self.prof == "Ranger":
            self.dex += 1
            self.per += 1
            self.poison_resist += 1
            self.cold_resist -= 1

    # Purpose:    Initializes player gear slots.
    # Parameters: None
    # Return:     Void
    def initGear(self):
        self.armor = None
        self.weapon = None
        self.ring = None

    # Purpose:    Gives the player default gear according to profession.
    # Parameters: None
    # Return:     Void
    def assignStarterGear(self):
        pass
        self.addItem("Apple", 3)
        self.calcDamage()

    # Purpose:    Equip a piece of armor.
    # Parameters: The index of the piece of armor in the inventory.
    # Return:     Void
    def equipArmor(self, index):
        if inv[index].type != "Armor" or inv[index].prof != self.prof:
            print("You can't wear that!")
            return
        # Equip the armor.
        self.armor = self.inv.pop(index)
        # Give the player the armor stats.
        self.defense += self.armor.defense
        self.poison_resist += self.armor.poison_resist
        self.fire_resist += self.armor.fire_resist
        self.cold_resist += self.armor.cold_resist
        self.electric_resist += self.armor.electric_resist
        self.earth_resist += self.armor.earth_resist

    # Purpose:    Unequip a piece of armor.
    # Parameters: None
    # Return:     Void
    def unequipArmor(self):
        if self.armor == None:
            print("You have no armor to unequip!")
            return
        # Adjust player stats accordingly.
        self.defense -= self.armor.defense
        self.poison_resist -= self.armor.poison_resist
        self.fire_resist -= self.armor.fire_resist
        self.cold_resist -= self.armor.cold_resist
        self.electric_resist -= self.armor.electric_resist
        self.earth_resist -= self.armor.earth_resist
        # Finish taking the armor off.
        self.inv.append(self.armor)
        self.armor = None

    # Purpose:    Equip a weapon.
    # Parameters: The inventory index of the weapon to equip.
    # Return:     Void
    def equipWeapon(self, index):
        if inv[index].type != "Weapon" or inv[index].prof != self.prof:
            print("That's not a weapon!")
            return
        # Equip the weapon.
        self.weapon = self.inv.pop(index)
        # Give the player the weapon stats.
        self.poison_dmg += self.weapon.poison_dmg
        self.fire_dmg += self.weapon.fire_dmg
        self.cold_dmg += self.weapon.cold_dmg
        self.electric_dmg += self.weapon.electric_dmg
        self.earth_dmg += self.weapon.earth_dmg
        self.defense += self.weapon.defense
        self.poison_resist += self.weapon.poison_resist
        self.fire_resist += self.weapon.fire_resist
        self.cold_resist += self.weapon.cold_resist
        self.electric_resist += self.weapon.electric_resist
        self.earth_resist += self.weapon.earth_resist
        self.calcDamage()

    # Purpose:    Unequip a weapon.
    # Parameters: None
    # Return:     Void
    def unequipWeapon(self):
        if self.weapon == None:
            print("You have no weapon to unequip!")
            return
        # Adjust player stats accordingly.
        self.poison_dmg -= self.weapon.poison_dmg
        self.fire_dmg -= self.weapon.fire_dmg
        self.cold_dmg -= self.weapon.cold_dmg
        self.electric_dmg -= self.weapon.electric_dmg
        self.earth_dmg -= self.weapon.earth_dmg
        self.defense -= self.weapon.defense
        self.poison_resist -= self.weapon.poison_resist
        self.fire_resist -= self.weapon.fire_resist
        self.cold_resist -= self.weapon.cold_resist
        self.electric_resist -= self.weapon.electric_resist
        self.earth_resist -= self.weapon.earth_resist
        # Take the weapon off and recalculate damage.
        self.inv.append(self.weapon)
        self.weapon = None
        self.calcDamage()

    # Purpose:    Equip a ring.
    # Parameters: The inventory index of the ring to equip.
    # Return:     Void
    def equipRing(self, index):
        if inv[index].type != "Ring":
            print("That's not a ring!")
            return
        # Equip the ring.
        self.ring = self.inv.pop(index)
        # Give the player ring stats.
        self.str += self.ring.str
        self.wis += self.ring.wis
        self.dex += self.ring.dex
        self.cha += self.ring.cha
        self.lck += self.ring.lck
        self.per += self.ring.per
        # Recalculate damage.
        self.calcDamage()

    # Purpose:    Unequip a ring.
    # Parameters: None
    # Return:     Void
    def unequipRing(self):
        if self.ring == None:
            print("You have no ring to unequip!")
            return
        # Adjust player stats accordingly.
        self.str -= self.ring.str
        self.wis -= self.ring.wis
        self.dex -= self.ring.dex
        self.cha -= self.ring.cha
        self.lck -= self.ring.lck
        self.per -= self.ring.per
        # Take the ring off and recalculate damage.
        self.inv.append(self.ring)
        self.ring = None
        self.calcDamage()

    # Purpose:    Calculate player damage (without elemental damage).
    # Parameters: None
    # Return:     Void
    def calcDamage(self):
        # If the player has no weapon:
        if self.weapon == None:
            self.damage = 1 * (self.str/2)
            return
        # Calculate damage according to weapons for each profession.
        self.damage = self.weapon.damage
        if self.prof == "Warrior":
            self.damage += self.str
        elif self.prof == "Mage":
            self.damage += self.wis
        elif self.prof == "Ranger":
            self.damage += self.dex

    # Purpose:    Take the given amount of damage of the given attack type.
    # Parameters: An int amount of damage, an optional int attack type.
    # Return:     Void
    def takeDamage(damage_dealt, attack_type = "Default"):
        pass

    # Purpose:    Initialize player's abilities according to class. Abilities
    #             are "given" to the player at start and unlocked over time.
    # Parameters: None
    # Return:     Void
    def initAbilities(self):
        pass

    # Purpose:    Gives the player a certain amount of the given item.
    # Parameters: A string item to give the player, and an optional amount of
    #             items to give.
    # Return:     Void
    def addItem(self, itemName, amt = 1):
        for i in range(amt):
            newItem = item.Item(itemName)
            self.inv.append(newItem)

    # Purpose:    Returns true if the player has an item with the given string
    #             name, false otherwise.
    # Parameters: A string name of an item to search for
    # Return:     True if the player has an item with the given name, false
    #             otherwise.
    def hasItem(self, item):
        for i in self.inv:
            if self.inv[i].name == item:
                return True
        # Return false if item not found
        return False

    # Purpose:    Removes the item with the given name from the player.
    # Parameters: A string item name to take from the player.
    # Return:     Void
    def takeItem(self, item):
        for i in self.inv:
            if self.inv[i].name == item:
                self.inv.pop(i)
                return
        print("ERROR: Item not found")

    # Purpose:    Give the player the given amount of gold.
    # Parameters: An int amount of gold to add.
    # Return:     Void
    def addGold(self, amtGold):
        self.gold += amtGold

    # Purpose:    Returns true if the player has the given amount of gold,
    #             false otherwise.
    # Parameters: An int amount of gold to check for.
    # Return:     True if the player has the given amount of gold, false
    #             otherwise.
    def hasGold(self, amtGold):
        if self.gold < amtGold:
            return False
        return True

    # Purpose:    Remove the given amount of gold from the player.
    # Parameters: An int amount of gold to take from the player.
    # Return:     None
    def takeGold(self, amtGold):
        if self.gold < amtGold:
            print("ERROR: Not enough gold")
            return
        self.gold -= amtGold

    # Purpose:    Gives the Player a current zone.
    # Parameters: Two ints representing the x and y coordinates of the
    #             player's current zone.
    # Return:     Void
    def setZone(self, zone_x, zone_y):
        self.x_coord = zone_x
        self.y_coord = zone_y
        self.loc = self.map.zones[x_coord][y_coord]

    # Purpose:    Moves the player north.
    # Parameters: None
    # Return:     Void
    def moveNorth(self):
        pass

    # Purpose:    Moves the player east.
    # Parameters: None
    # Return:     Void
    def moveEast(self):
        pass

    # Purpose:    Moves the player south.
    # Parameters: None
    # Return:     Void
    def moveSouth(self):
        pass

    # Purpose:    Moves the player west.
    # Parameters: None
    # Return:     Void
    def moveWest(self):
        pass
