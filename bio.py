"""

bio.py
Contains the definition of the Bio class.
Written by:  Mohsin Rizvi
Last edited: 05/27/17

"""

import basics
import random

# The Bio (Biography) class, used to hold biographical info about a
# character (not including name, race, and class--only background info).
class Bio:

	# Purpose:    Constructs a Bio object.
	# Parameters: A charRace string indicating the race of the character.
	# Return:     Void
	def __init__(self, charRace):
		self.generateBio(charRace)

	# Purpose:    Generates a random biography with the given charRace string.
	# Parameters: A charRace string indicating the race of the character.
	# Return:     Void
	def generateBio(self, charRace):
		races = ["Human", "Dwarf", "Elf"]
		humanHomes = ["Arakas", "Arcpoint", "Baldwater", "Bandura",
		              "Cloud City", "Coramar", "Dale", "Fenbrun",
		              "Milheim", "Maanil", "Outerland", "Roth", "Saab",
		              "Urhall", "Zaab ar Duul"]
		dwarfHomes = ["Anheil", "Baldwater", "Bd-ran", "Bd-darak",
					  "Cloud City", "Dale", "Fenbrun", "Gaal", "Hirad",
					  "Milheim", "Nevron", "Urhall", "Zald", "Zanar"]
		elfHomes = ["Arcpoint," "Bandura", "Belfinar", "Cloud City",
					"Dale", "Dif an Eil", "Enhreim", "Fenbrun", "Hirad",
					"Iiliac", "Janis", "Milheim", "Outerland", "Saab",
					"Uil", "Vaar", "Vaan an Set", "Zaab ar Duul", "Zanar"]
		jobs = ["Cook", "Warrior", "Mage", "Archmage", "Thief", "Beggar",
				"King", "Queen", "Paladin", "Ranger", "Actor", "Actress",
				"Soldier", "Merchant", "Blacksmith", "Silversmith", "Tailor",
				"Fisher", "Farmer", "Grand Wizard", "Clown", "Fool", "Hunter",
				"Pirate", "Mathematician", "Philosopher", "Alchemist",
				"Shaman", "Engineer", "Architect", "Carpenter", "Priest",
				"Reverand", "Warlock", "Necromancer", "Peasant", "Lumberjack",
				"Outlaw", "Professor", "Arcanomancer", "Pyromancer", "Monk",
				"Prince", "Princess", "Duke", "Duchess", "Assasssin"]
		# Randomly pick a homeland
		if charRace not in races:
			basics.error_quit("ERROR: Invalid character race.")
		if charRace == "Human":
			self.home = random.choice(humanHomes)
		elif charRace == "Dwarf":
			self.home = random.choice(dwarfHomes)
		elif charRace == "Elf":
			self.home = random.choice(elfHomes)
		# Randomly pick jobs of parents
		self.parent1 = random.choice(jobs)
		self.parent2 = random.choice(jobs)