"""

enemy.py
Contains the definition of the Enemy class.
Written by:  Mohsin Rizvi
Last edited: 09/28/17

"""

import damage

# An enemy to fight.
class Enemy:

    # Purpose:    Constructs an enemy with the given name.
    # Parameters: A name for the enemy.
    # Return:     Void
    def __init__(self, name):
        self.name = name
        basics.fixData("enemies")
        self.openData()

    # Purpose:    Get enemy data from a file containing enemy info.
    # Parameters: None
    # Return:     Void
    def openData(self):
        # Open enemy directory file for reading.
        with open("enemies", "r") as self.reader:
            # Find the correct enemy in the file
            # Read one line, seeing if it is the empty string
            x = self.reader.readline()
            if x == "":
                print("ERROR: Enemy not found.")
                return
            # While enemy is not found, search until empty string
            while x.lower() != self.name.lower() + "\n":
                x = self.reader.readline()
                if x == "":
                    print("ERROR: Enemy not found.")
                    return
            # Set enemy name to name in directory to fix capitalization errors
            self.name = x[0:len(x) - 1]
            # Read the data into the Item object.
            self.readData()

    # Purpose:    Read in enemy data from an open file (self.reader).
    # Parameters: None
    # Return:     Void
    def readData(self):
        # Read the enemy type and description
        x = self.reader.readline()
        self.type = x[0:len(x) - 1]
        x = self.reader.readline()
        self.desc = x[0:len(x) - 1]
        # Read enemy combat data
        self.max_hp = int(self.reader.readline())
        self.curr_hp = self.max_hp
        self.max_energy = int(self.reader.readline())
        self.curr_energy = self.max_energy
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

    # Purpose:    Print enemy data.
    # Parameters: None
    # Return:     Void
    def printData(self):
        print("Enemy: " + self.name)
        print("    " + self.type)
        print("    " + self.desc)
        print("    Max HP: " + str(self.max_hp))
        print("    Max Energy: " + str(self.max_energy))
        print("    Damage: " + str(self.damage))
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

    # Purpose:    Take the given Damage.
    # Parameters: A Damage instance and a double protection modifier, which
    #             defaults to .075.
    # Return:     Amount of damage dealt.
    def takeDamage(self, damage_received):
        # Check if the attack misses
        miss_chance = int(self.lck + (self.dex * 0.5))
        miss = random.randrange(0, 101)
        if (miss <= miss_chance):
            return 0

        # Calculate whether or not modifier is negative
        negative = random.randrange(0,2)
        # Calculate a modifier for damage taken
        modifier = random.randrange(0, self.defense * mult_modifier)
        if (negative != 0):
            modifier *= -1

        # Check for elemental resistances
        if damage_received.ele_type == "Electric":
            damage_received.ele_dmg -= self.electric_resist
        elif damage_received.ele_type == "Fire":
            damage_received.ele_dmg -= self.fire_resist
        elif damage_received.ele_type == "Cold":
            damage_received.ele_dmg -= self.cold_resist
        elif damage_received.ele_type == "Earth":
            damage_received.ele_dmg -= self.earth_resist
        elif damage_received.ele_type == "Poison":
            damage_received.ele_dmg -= self.poison_resist

        # Check for regular defense and get total, and check for death
        total_dmg = ((damage_received.reg_damage - self.defense) +
                    damage_received.ele_dmg) * modifier
        self.curr_hp -= total_dmg
        if self.curr_hp <= 0:
            die()

        return total_dmg

    # Purpose:    "Kills" the enemy upon death.
    # Parameters: None
    # Return:     Void
    def die(self):
        pass

    # Purpose:    Get damage done for an attack, stored in a Damage instance.
    # Parameters: A string elemental damage type and a double modifier to
    #             add/subtract from, which defaults to .25.
    # Return:     A Damage instance to pass to the target.
    def doDamage(self, ele_type, mult_modifier = 0.25):
        # Calculate whether or not the modifier will be negative
        negative = random.randrange(0, 2)

        # Calculate the damage done with a modifier.
        modifier = random.randrange(0, self.damage * mult_modifier)
        if negative != 0:
            modifier *= -1;
        damage_dealt = self.damage + modifier

        # Return the damage to deal.
        if ele_type == "Electric":
            return damage.Damage(damage_dealt, self.electric_dmg, ele_type)
        elif ele_type == "Fire":
            return damage.Damage(damage_dealt, self.fire_dmg, ele_type)
        elif ele_type == "Cold":
            return damage.Damage(damage_dealt, self.cold_dmg, ele_type)
        elif ele_type == "Earth":
            return damage.Damage(damage_dealt, self.earth_dmg, ele_type)
        elif ele_type == "Poison":
            return damage.Damage(damage_dealt, self.poison_dmg, ele_type)
