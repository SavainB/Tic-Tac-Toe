# Tic-Tac-Toe
I see a mission on upwork is to do an basic tic tac toe on python so i decide to try to do it 
write a simple tic-tac-toe game that allows two players to play tic-tac-toe against one another. 
You will be asked to:
1.	Implement a program that tracks the state of an ongoing tic-tac-toe game.
2.	Allow each player to choose the position they want to place their pieces.
3.	Check and end the game when either a win or a tie occurs.
Assignment Requirements
Your program must meet the following requirements, since it will be marked electronically, failing to meet these requirements means your program or its ouptut will not be found and cannot be graded.
1.	Your program MUST be called tictactoe.py. You CANNOT submit a Jupyter notebook .ipynb file.
2.	You MUST use the identifiers A1, A2 and so on to refer to squares on the board exactly as we have specified.
Basic Game Loop
The game loop for a tic-tac-toe game is fairly simple.
1.	Initialize the board to be empty.
2.	X starts, and chooses a position to place their marker.
3.	O positions their marker in any empty position.
4.	After each marker is placed, a check is made to see whether either player has won.
5.	Placement alternates until a player wins or the board is full, at which point the game is called for a tie.
The reason you would break down the game like this isn't because you don't know tic-tac-toe, but because this gives you a fairly good idea of what you need to do to program Python to play a tic-tac-toe game. This is a common strategy for larger programs, take each problem and break it down into a sequence of sub-problems until you feel comfortable that you understand how to write code to solve each sub-problem. If our breakdown above is still too high level, keep decomposing it until to get to a point where you feel like you understand how to convert each description into a corresponding block of code.
Interface
Board Positions.<br />  Because we'll be marking your programs electronically, there is a very specific way that positions on the board are labeled, and in how your program should accept the positions as input to update your tic-tac-toe board.<br />
Positions on the board are labeled with the numbers 1, 2, and 3, used for the three rows, top to bottom, and the letters A, B, and C, used for the three columns, left to right. So, for example, the top-left position is A1, and the bottom-left position is C3. The entire board has positions labeled like this.<br />
A1	B1	C1
A2	B2	C2<br />
A3	B3	C3<br />
User Input.  When a user enters a position, they must use the above format exactly. You are required to check any position a user provides to ensure it properly defines a valid position. If it does not, you should tell the user the position is invalid, and ask them to enter a new, correct position.
Even if the position provided by the user is in the correct format, it may still be invalid (e.g., if the position is already taken). After confirming the position's format is correct, you must then check to ensure the position itself is available. If not, you would again report the issue to the user and ask them to provide a new, valid position.<br />
Input from the keyboard can be requested using Python's input() function.
position = input( "Choose a position: " )
print( position )
input() allows a user to enter characters from the keyboard, then returns the result as a string. This can be assigned to a variable for further processing.
Wins and Ties
At some point, one of the players will win the game, or the game will end in a tie. When this happens, your program should print the result of the game, and exit the program.

