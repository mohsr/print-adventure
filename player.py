"""

player.py
Contains the definition of the Player class.
Written by:  Mohsin Rizvi
Last edited: 05/23/17

"""

import ability
import cbt_ability
import random
import bio

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
		self.inv = list()
	
	# Purpose:    Gives the Player a current zone.
	# Parameters: Two ints representing the x and y coordinates of the
	#             player's current zone.
	# Return:     Void
	def setZone(self, zone_x, zone_y):
		self.x_coord = zone_x
		self.y_coord = zone_y