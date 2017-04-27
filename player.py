"""

player.py
Contains the definition of the Player class.
Written by:  Mohsin Rizvi
Last edited: 04/27/17

"""

import zone
import ability
import cbt_ability

# The Player character.
class Player:

	# Purpose: 	  Constructor for the Player class.
	# Parameters: A name for the Player, which defaults to "Hero", a player
	#             profession (class), and the player's race (human, elf, etc).
	# Return:     Void
	def __init__(self, myName = "Hero", myProfession, myRace):
		self.name = myName
		self.profession = myProfession
		self.race = myRace
	
	# Purpose:    Gives the Player a currZone.
	# Parameters: A Zone to place the player in.
	# Return:     Void
	def setZone(self, theZone):
		self.currZone = theZone