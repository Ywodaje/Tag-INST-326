GAME OVERVIEW
Tag & Chase is a text-based tag game built in Python. It was inspired by 
traditional childhood games played across as kids such as Hide and Seek and wanted to bring the game to life. 
The game runs on a 4x4 grid and is played through the terminal.
What makes this version of the game fun and unpredictable:
The tagger is randomly chosen from the list of players at the start of the game it's not always Henry.
All player positions are also randomized at the beginning of each game.
The tagger’s position is hidden during gameplay, so players can’t easily avoid being tagged.
This randomness keeps each round fresh and unpredictable, just like real tag games from childhood.

HOW TO RUN THE PROGRAM (Tested on macOS/Windows)
Make sure Python 3/python  is installed on your system.

Download or clone the repository to your local machine.

Open a terminal window.

Use the cd command to navigate to the folder where demo.py is saved.

Run the program using:
python 3 demo.py/python demo.py
There are no command-line arguments. The game launches and runs on its own.

 
 HOW THE GAME WORKS
The game uses a 4x4 grid.

6 players are placed randomly on the grid.

1 tagger is randomly selected from the group it can be any of the six players.

 Hiding spots are also placed randomly.

The tagger’s identity is known, but their position is hidden on the grid.

The player can move Maya (a non-tagger player) by typing up, down, left, or right.

During gameplay:

The grid is displayed with:

First letters of visible players (e.g., M for Maya)

Hiding spots shown as H

Empty spots as .

The tagger is not shown on the board

The game checks after every move to see if the tagger is right next to Maya (not diagonal).

If Maya is tagged, the game ends with a message.

If not, the game continues and the player moves again.

ANNOTATED BIBLIOGRAPHY
INST 326 Lecture Videos and Slides (UMD)Our class lectures were the foundation
 of this entire project. We based our logic on topics covered in class such as: 
 separating concerns into functions, writing docstrings, handling user input, 
 using random.sample() for sampling, and combining loops with dictionaries. 
These helped us understand not only how to write the game, but how to keep it organized and readable.

W3Schools – Python Basics
Link: https://www.w3schools.com/python/
We used W3Schools as a quick reference for understanding basic syntax, how to 
use dictionaries, and how to work with loops and conditional statements. 
It helped us understand the difference between if, elif, and else, as well as 
how to properly use functions and return values in Python.

Bro Code – Python for Beginners YouTube Series
Link: https://www.youtube.com/c/BroCodez
This channel was used to better understand how to structure beginner-friendly 
programs. Specifically, the videos on loops, user input, and basic game logic 
helped us think through how to break our game into smaller steps and keep our 
functions focused on one task.


TEAM MEMBERS AND GITHUB USERNAMES
Name	                                    GitHub Username
Fatmata                                      @Zara2506
Yalemzewed	                                  @Ywodaje


FUNCTION ATTRIBUTE TABLE
Method/Function	                           Primary Author	                                    Techniques Demonstrated
place_players_and_hiding_spots	              Yalemzewed	                     Lists, Dictionaries, Random Sampling, Sequence unpacking
check_for_tag	                              Fatmata 	                        Conditionals, Iteration, Return values
play_game	                                  Yalemzewed	                         Loops,Input validation, Game flow control