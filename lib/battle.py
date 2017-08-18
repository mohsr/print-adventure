"""

battle.py

Contains the definition of the Battle class for combat between a player
and one or more enemies.
Written by:  Mohsin Rizvi
Last edited: 07/25/17

"""

# The Battle class
class Battle:

    # Purpose:    Begin a battle.
    # Parameters: A player and a list of enemies to fight against.
    # Return:     True if battle is won, false otherwise.
    def __init__(self, player, *enemies):
        # Assign turns to go in battle based on current energy.
        #tempTurns = [player]
        #for i in enemies:
        #    turns.append(i);
        #for i in range(len(tempTurns)):
            #append to self.turns