# Fourtic
## John Asencio
### Fourtic - A negamax sum algorithm for the game fourtic

# Summary of the game
You can think of fourtic like a 4x4 tic tac toe game, with a twist. The rules are as follows: 
Players alternate turns until the board is completely filled (eight moves by each side). When the game is over, the player with the most points wins.

Point scoring is in two forms:
Every row of three squares owned by a player counts three points for that player. Note that a row of four, which contains a row of three, is thus worth six points.
Every side or corner cell owned by a player is worth one bonus point to that player.

This program is NOT a solver for the fourtic game as of writing this. This program returns the negamax sum of the players turn
which is determined based on the board that is fed into the program at the start.

Future works may include a solver using retrograde analysis.


# Problems and Solutions
The negamax algorithm itself was not hard to implement at all, it was pretty straightforward. Now, the scoring 
algorithm is what took up the bulk of my time. I spent a lot of time trying to get it down and solving it
dynamically you could say but opted for some ways (like the diagonals) to just hard code in the positions.

# How to run and compile
To run the fourtic file simply run: python3 fourtic.py <filename>
So for example in this directory I would run: python3 fourtic.py hw-fourtic/play-7.txt
Then it would output the negamax sum.

To run the tests you would do:
 python -m unittest -k test_negamax  
 or 
 python -m unittest discover

The tests test the displaying the file,
and they also display the negamax output to the expected output.

