"""

damage.py
Contains the definition of the Damage class, used for showing damage dealt in
combat.
Written by:  Mohsin Rizvi
Last edited: 09/27/17

"""

class Damage:

    # Purpose:    Initialize a Damage object.
    # Parameters: An int for regular damage, an optional int for elemental
    #             damage, and an optional string for elemental type.
    # Return:     Void
    def __init__(self, reg_damage, ele_damage, ele_type):
        self.reg_damage = reg_damage
        self.ele_damage = ele_damage
        self.ele_type = ele_type