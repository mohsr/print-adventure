"""

npc.py
Contains the definition of the NPC class and all of its children, including
the Enemy class.
Written by:  Mohsin Rizvi
Last edited: 04/27/17

"""

import cbt_ability

# A basic NPC to interact with.
class NPC:

	# Purpose:    Construct an NPC with the given name.
	# Parameters: A name for the NPC.
	# Return:     Void
	def __init__(self, theName = "NPC"):
		self.name = theName

# An enemy to fight in combat with.
class Enemy(NPC):

	# Purpose:    Constructs an enemy with the given name.
	# Parameters: None
	# Return:     Void
	def __init__(self):
		pass