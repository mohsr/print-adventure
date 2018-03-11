# Print-Adventure: A text-based adventure
Written by:  Mohsin Rizvi

Last edited: 3/11/18

# *README*

## A. Overview

A randomly-generated text-based RPG with save files! Also, written
in Python. I'm doing this project because it seems like fun, and I love
RPGs! I've also wanted to write a text-based game for a while now.
I originally chose Python over C++ so that I could gain more experience 
using Python. I have a lot of experience using Python now, though, then 
I used to. So some of the older code may not be incredible and/or the 
most Pythonic.

Things yet to be implemented are listed below. I plan on implementing them
starting with item 1, then 2, and so on.

  1. Combat abilities
  3. Combat system
  4. Dungeons
  5. Non-combat NPCs
  6. Towns and cities
  7. Interaction between player and world
  8. Quests
  9. Other things I might think of

## B. Acknowledgments

Stack Overflow assisted me in writing this project. Stack Overflow uses a
cc-by-sa license, meaning all content can be adapted and used for
any purpose (https://creativecommons.org/licenses/by-sa/3.0/).
In particular, it helped me with finding the filepath of the directory
containing the current script that is running (http://stackoverflow.com/
questions/4934806/how-can-i-find-scripts-directory-with-python). The question
was asked by user Jonathan (http://stackoverflow.com/users/348545/jonathan)
and edited by user Martin Thoma
(http://stackoverflow.com/users/562769/martin-thoma). The answer that I used
was by user Czarek Tomczak 
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

## C. Algorithms and Technical Stuff

For world generation, I created my own recursive algorithm to generate biomes
on the world map and to have zones near each other tend to be of the same
specific biome. Here it is:

1. Randomly assign a zone a biome.
2. Mark that zone as "known".
3. For each unknown neighboring zone of that zone, there is a 100% chance
   for the neighbor to inherit the same biome.

    a. If it does inherit the same biome, mark the zone as known and
       recurse from step 3 for the neighbor zone, but with a chance to
       spread the biome equal to the neighbor's chance minus 10%.
       
    b. If it does not inherit the same biome, recurse from step 1 for the
       neighbor zone.

My implementation of the algorithm processes neighbors to the north, then
east, then south, then west. It starts with a 100% chance to spread,
reducing by 15% for each new neighbor "added" to the biome, but these
numbers can be altered to adjust average biome size.

## D. Files and Folders

Here is a brief overview of every file and folder in the project.

  lib

    __pycache__

      The __pycache__ folder contains bytecode used to run the program.

    games

      sample_game

        This is an actual instance of a saved game file, but is mostly used as
        a placeholder for the folder. All saved game files will go in the
        games folder alongside this one.

    abilities

      A directory of combat abilities that can be used in the game.

    ability.py

      Contains the definition of the Ability class for combat abilities.

    basics.py

      Contains definitions of basic functions used for the game.

    battle.py

      Contains the definition of the Battle class for representing combat
      sequences.

    bio.py

      Contains the definition of the Bio class, which generates and stores
      background biographical info on a character.

    damage.py

      Contains the definition of the Damage class, used to enable the player
      and enemies to deal damage during combat.

    enemies

      Contains a list of in-game enemies, sorted by biome. Note that the same
      biome should not appear more than once. To add another enemy to the same
      biome, add its data before the "---" line. To add an enemy, edit the
      list and type in the following, replacing all items in brackets:
        [Biome1]
        [Enemy1_name]
        [Enemy1_type] (e.g. "Beast")
        [Enemy1_desc]
        [Enemy1_maxHP]
        [Enemy1_maxEnergy]
        [Enemy1_regDamage]
        [Enemy1_poisonDamage]
        [Enemy1_fireDamage]
        [Enemy1_coldDamage]
        [Enemy1_electricDamage]
        [Enemy1_earthDamage]
        [Enemy1_defense]
        [Enemy1_poisonResist]
        [Enemy1_fireResist]
        [Enemy1_coldResist]
        [Enemy1_electricResist]
        [Enemy1_earthResist]
        ---
        [Biome2]

    enemy.py

      Contains the definition of the Enemy class.

    game.py

      Contains the definition of the Game class used to run the whole game.

    item.py

      Contains the definition of the Item class.

    items

      Contains a list of in-game items. To add an item, simply edit the list and
      type in the following, replacing all items in brackets:
        For food items:
          [Name]
          [Description]
          Food
          [Integer amount healed per bite]
          [Integer number of bites]
        For armor:
          [Name]
          [Description]
          Armor
          [Profession to be used by (Warrior, Mage, or Ranger)]
          [Integer defense]
          [Integer poison resist]
          [Integer fire resist]
          [Integer cold resist]
          [Integer electricity resist]
          [Integer earth resist]
        For weapons:
          [Name]
          [Description]
          Weapon
          [Profession to be used by (Warrior, Mage, or Ranger)]
          [Integer damage]
          [Integer poison damage]
          [Integer fire damage]
          [Integer cold damage]
          [Integer electricity damage]
          [Integer earth damage]
          [Integer defense]
          [Integer poison resist]
          [Integer fire resist]
          [Integer cold resist]
          [Integer electricity resist]
          [Integer earth resist]
        For rings:
          [Name]
          [Description]
          Ring
          [Strength bonus]
          [Wisdom bonus]
          [Dexterity bonus]
          [Charisma bonus]
          [Luck bonus]
          [Perception bonus]
        For misc items (items that are none of the above):
          [Name]
          [Description]
          Misc

    main.py

      Runs the finished game.

    npc.py

      Contains the definition of the NPC class.

    player.py

      Contains the definition of the Player class.

    savegame.py

      Contains the definition of the SaveGame class, which accesses each
      individual saved game file and all of its informations.

    zone.py

      Contains the definition of the WorldMap class and the Zone class.

  LICENSE

    Contains license information. This project is licensed under the
    MIT license.

  README.md

    You're reading this! Contains information on the overall project.
