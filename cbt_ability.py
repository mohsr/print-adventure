"""

cbt_ability.py
Contains the definition of the CombatAbility class.
Written by:  Mohsin Rizvi
Last edited: 04/27/17

"""

import basics

# An ability to use in combat.
class CombatAbility:

	# Purpose:    Construct a combat ability.
	# Parameters: A string name for the ability.
	# Return:     Void
	def __init__(self, abiName = "Cool Attack"):
		self.name = abiName