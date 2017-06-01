# Print-Adventure: A text-based adventure
Written by:  Mohsin Rizvi

Last edited: 05/27/17

# *README*

## A. Overview

A procedurally-generated text-based RPG with save files! Also, written
in Python. I'm doing this project because it's fun! And also because
I want to get more experience using Python (which is why I'm not
writing it in C++, my language of choice).

## B. Acknowledgments

Stack Overflow assisted me in writing this project. Stack Overflow uses a
cc-by-sa license, meaning all content can be adapted and used for
any purpose (https://creativecommons.org/licenses/by-sa/3.0/).
In particular, it helped me on the following occasions:
  Finding the filepath of the directory containing the current script that
  is running (http://stackoverflow.com/questions/4934806/
  how-can-i-find-scripts-directory-with-python). The question was asked by
  user Jonathan (http://stackoverflow.com/users/348545/jonathan) and edited
  by user Martin Thoma (http://stackoverflow.com/users/562769/martin-thoma).
  The answer that I used was by user Czarek Tomczak
  (http://stackoverflow.com/users/623622/czarek-tomczak).

Zach Kirsch and Nikhil Shinday from the Tufts University Computer
Science Facebook group suggested that I use pickle for saving/loading objects
easily as files. I used this to save game files so that games can be loaded
and picked up again later. Here is a link to the Facebook group:
https://www.facebook.com/groups/TuftsCS/?fref=ts

Further acknowledgments will be added here as the project goes on.

Thanks to everyone who has played a part in my computer science
education so far! And many thanks to my terrific girlfriend for
listening to me talk about this stuff all the time. <3

## C. Files and Folders

Here is a brief overview of every file and folder in the project.

  ### Files

  README.md

    You're reading this! Contains information on the overall project.

  basics.py

    Contains definitions of basic functions used for the game.

  game.py
  
    Contains the definition of the Game class used to run the whole game.

  savegame.py

    Contains the definition of the SaveGame class, which holds each individual
    saved game file and all of its information.

  runner.py

    Runs the finished game.

  player.py
  
    Contains the definition of the Player class.
    
  zone.py
  
    Contains the definition of the WorldMap class and the Zone class.
    
  npc.py
  
    Contains the definition of the NPC class.
    
  ability.py
  
    Contains the definition of the Ability class for out-of-combat
    
    abilities.
    
  cbt_ability.py
  
    Contains the definition of the CombatAbility class for in-combat
    
    abilities.

  bio.py

    Contains the definition of the Bio class, which generates and stores
    background biographical info for a character.

  sample_game

    Contained in the games folder. This is an actual instance of a saved game
    file, but is mostly used as a placeholder for the folder. All saved game
    files will go in the games folder alongside this one.

  ### Folders

  games

    Contains saved game files.
