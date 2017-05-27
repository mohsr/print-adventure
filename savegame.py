"""

savegame.py
Contains the definition of the SaveGame class which holds an instance of the
game.
Written by:  Mohsin Rizvi
Last edited: 05/27/17

"""

import os
import basics
import player
import pickle
import time

# An instance of the interactive game.
class SaveGame:

    # Purpose:    Creates a SaveGame.
    # Parameters: A string name for the SaveGame and a string filepath to the
    #             directory containing the save file.
    # Return:     Void
    def __init__(self, filename, path):
        # Create a save games folder if it doesn't exist, then move to it
        # Credit given to Stack Overflow for helping me figure out how to get
        # the filepath of the current script. More info in README.md.
        gamesPath = os.path.dirname(os.path.realpath(__file__)) + "/games"
        if not os.path.isdir(gamesPath):
            os.mkdir(gamesPath)
        os.chdir(gamesPath)

        self.gameName = filename
        self.path = path + "/" + filename

    # Purpose:    Starts a new game from scratch.
    # Parameters: None
    # Return:     Void
    def new(self):
        print("Starting a new game. Have fun!\n")
        self.printControls()
        self.createCharacter()
        self.start()
        self.play()

    # Purpose:    Plays the game.
    # Parameters: None
    # Return:     Void
    def play(self):
        pass

    # Purpose:    Saves the game.
    # Parameters: None
    # Return:     Void
    def save(self):
        print("\nSaving game...")

        # Save the game
        # Credit given to Zach Kirsch and Nikhil Shinday from the Tufts
        # University Computer Science Facebook group for suggesting that
        # I use pickle. More info in README.md.
        pickle.dump(self, open(self.path, "wb"))

        print("Game saved!\n")

    # Purpose:    Begin character creation and create the Player.
    # Parameters: None
    # Return:     Void
    def createCharacter(self):
        raceComms = {"Human": "A jack-of-all-trades human",
                     "Dwarf": "A hardy denizen of the mountains",
                     "Elf": "A nimble inhabitant of the woodlands"}
        jobComms = {"Warrior": "A muscular, powerful armsman",
                    "Mage": "A wise user of arcane magic",
                    "Ranger": "A quick and dextrous wielder of bows and guns"}
        # Collect basic character info from the player
        name = input("Hello young hero. What is your name?\n").strip()
        # Collect player race
        time.sleep(1)
        print(("Ah, %s then. You've been asleep quite some time." +
              " I am an old inhabitant of this world. I can't quite see" +
              " you too well. Tell me, are you a human, a dwarf, or an elf?")
              % name)
        race = basics.command(raceComms)
        # Collect player profession
        time.sleep(1)
        print(("Ah, good. So, %s, how do you plan on defending yourself" +
              " in these vast lands? Are you a warrior, a mage, or a" +
              " ranger?") % name)
        prof = basics.command(jobComms)
        time.sleep(1)
        # Create the player
        self.player = player.Player(name, race, prof)
        print("Very good then. Are you ready? Your adventure is about to" +
              " begin...\n")
        time.sleep(3)

    # Purpose:    Prints the controls.
    # Parameters: None
    # Return:     Void
    def printControls(self):
        print("Print-Adventure is a text-based adventure game, so all of\n" +
              " the actions you do are entered into the game through the\n" +
              " keyboard. To print all of the possible commands at any\n" +
              " time, just type in \"$\". To save the game (when not in\n" +
              " a talking sequence or in combat), type in \"save\".\n")

    # Purpose:    Introduces the player to the actual game.
    # Parameters: None
    # Return:     Void
    def start(self):
        print("You wake up on a beach.")
        time.sleep(2)
        print("You don't remember much, only your name and some facts about" +
              " your life and where you come from.")
        time.sleep(2)
        print("What will you do next?\n")
