"""

game.py
Contains the definition of the Game class, used to run the main menu and
start the game.
Written by:  Mohsin Rizvi
Last edited: 09/28/17

"""

import basics
import savegame
import pickle
import os

# The Game object.
class Game:

    # Purpose:    Starts the game.
    # Parameters: None
    # Return:     Void
    def __init__(self):
        self.path = os.path.dirname(os.path.realpath(__file__)) + "/games"

        # Introduce the player and open the main menu
        self.intro()
        self.runMenu()

    # Purpose:    Returns a list of filenames in the directory at the given
    #             string path.
    # Parameters: A string path to a directory of files.
    # Return:     A list of filenames in the directory.
    def getFiles(self, dirPath):
        saves = os.listdir(dirPath)
        if ".DS_Store" in saves:
            saves.remove(".DS_Store")
        if "sample_game" in saves:
            saves.remove("sample_game")
        return saves

    # Purpose:    Introduce the player to the game.
    # Parameters: None
    # Return:     Void
    def intro(self):
        print("|-------------------------------------------------------|")
        print("| @~~~               Print-Adventure               ~~~@ |")
        print("|-------------------------------------------------------|")
        print("                  A game by Mohsin Rizvi                 ")

    # Purpose:    Run the main menu
    # Parameters: None
    # Return:     Void
    def runMenu(self):
        mainMenuComms = {"A": "Load Game",
                         "B": "New Game",
                         "C": "Help",
                         "D": "Quit Game"}
        # Print the main menu and process entered input
        while True:
            print("Main menu:")
            print("To use a command, type the letter appearing before it.")
            basics.printPairs(mainMenuComms)
            comm = basics.command(mainMenuComms)
            if comm == "A":
                self.loadGame()
            elif comm == "B":
                self.newGame()
            elif comm == "C":
                self.help()
            elif comm == "D":
                basics.quit()

    # Purpose:    Allow the player to load a saved game file.
    # Parameters: None
    # Return:     Void
    def loadGame(self):
        saves = self.getFiles(self.path)
        # Select a game to load
        if len(saves) == 0:
            print("Sorry, there are no saved games!")
            return
        print("Here are the games to load:")
        for i in saves:
            print(i)
        toLoad = input("Which game would you like to load? Type \"back\" to" +
                       " go to the main menu.\n").strip()
        if toLoad.lower() == "back":
            return
        while toLoad not in saves:
            toLoad = input("Sorry, that is not a valid game name. Which" +
                         " game would you like to load? Type \"back\" to" +
                         " go to the main menu.\n").strip()
            if toLoad.lower() == "back":
                return
        print("Loading game...")
        # Load the game
        # Credit given to Zach Kirsch and Nikhil Shinday from the Tufts
        # University Computer Science Facebook group for suggesting that
        # I use pickle. More info in README.md.
        retrieved = pickle.load(open(self.path + "/" + toLoad, "rb"))
        print("Game loaded!\n")
        # Run the game
        retrieved.play()

    # Purpose:    Start a new game file.
    # Parameters: None
    # Return:     Void
    def newGame(self):
        saves = self.getFiles(self.path)
        invalNames = ["back", "sample_game"]
        lowerSaves = list()
        for i in saves:
            lowerSaves.append(i.lower())
        # Start the save game
        gameName = input("What would you like to call this new game?" + 
                         " Type \"back\" to go to the main" +
                         " menu.\n").strip()
        lowerName = gameName.lower()
        if lowerName == "back":
            return
        while (lowerName in lowerSaves or lowerName in invalNames
        or gameName[0] == "."):
            gameName = input("Sorry, that game name is invalid. What would" +
                             " you like to name this game? Type \"back\" to" +
                             " go to the main menu.\n").strip()
            lowerName = gameName.lower()
            if lowerName == "back":
                return
        save = savegame.SaveGame(gameName, self.path)
        # Run the game
        save.new()

    # Purpose:    "Help" the user.
    # Parameters: None
    # Return:     Void
    def help(self):
        print("To bring up a summary of game controls, type in" +
              " \"help\" while in game. To print current commands," +
              " type in \"$\". To save the game, type \"save\".")
        print("To enter commands, enter them in with the keyboard. To" +
              " submit a command, press [enter]. Commands are" +
              " case-insensitive.")
