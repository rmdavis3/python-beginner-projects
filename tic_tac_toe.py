"""
To create a beginner Python project for a Tic Tac Toe game, follow these steps:

1. **Design the Game Logic**:
   - Understand the rules: You’ll need to check if either player (X or O) wins or if the game ends
   in a draw.
   - Represent the board: Use a 3x3 grid (which can be a list of lists) to store the moves.
   - Develop functions to display the board, check for win conditions, and handle player moves.

2. **Create the Game Board**:
   - Use a list of lists to represent the 3x3 grid. Each cell in the grid will be initially empty.
   - You will need a function to print the grid after each move, so players can see the current
   state.

3. **Turn-based System**:
   - Implement a way to alternate turns between the two players.
   - Ensure each player can place their marker (X or O) on an empty cell, and check after each move
   if someone has won.

4. **Win Condition**:
   - After every move, check whether a player has won by having three of their markers in a row
   (horizontally, vertically, or diagonally).
   - If the board is full and no one has won, declare a draw.

5. **Input Validation**:
   - Allow players to input their move (usually a number corresponding to a cell on the grid) and
   check if the move is valid (i.e., the cell isn’t already taken and is within the bounds of the
   board).

6. **Game Loop**:
   - Use a loop to keep the game running until there’s a winner or the game ends in a draw.
   - After each move, check for a win or a draw, then ask the next player to make a move.

7. **Additional Features** (optional for beginners):
   - You could add a way to restart the game or keep track of the score.
   - You could even extend the project to allow two players to play on the same computer or add a
   simple AI opponent.

By following these steps, you’ll create a simple, interactive Tic Tac Toe game that covers the
basics of Python programming, such as loops, conditionals, functions, and lists.
+-------+-------+-------+
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   4   |   X   |   6   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
+-------+-------+-------+
"""

from random import randrange


board = [
    ['+', '-'*7, '+', '-'*7, '+', '-'*7, '+'],
    ['|', ' '*7, '|', ' '*7, '|', ' '*7, '|'],
    ['|   ', '1', '   |   ', '2', '   |   ', '3', '   |'],
    ['|', ' '*7, '|', ' '*7, '|', ' '*7, '|'],
    ['+', '-'*7, '+', '-'*7, '+', '-'*7, '+'],
    ['|', ' '*7, '|', ' '*7, '|', ' '*7, '|'],
    ['|   ', '4', '   |   ', '5', '   |   ', '6', '   |'],
    ['|', ' '*7, '|', ' '*7, '|', ' '*7, '|'],
    ['+', '-'*7, '+', '-'*7, '+', '-'*7, '+'],
    ['|', ' '*7, '|', ' '*7, '|', ' '*7, '|'],
    ['|   ', '7', '   |   ', '8', '   |   ', '9', '   |'],
    ['|', ' '*7, '|', ' '*7, '|', ' '*7, '|'],
    ['+', '-'*7, '+', '-'*7, '+', '-'*7, '+'],]


def display_board(board):
    """Prints current board"""
    for row in board:
        full_row = ''
        for column in row:
            full_row += column
        print(full_row)


def enter_move(board):
    """Updates the board with the player's move"""
    move = input("Please enter your move: ")
    # update the board
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if move == board[i][j]:
                board[i][j] = 'o'


def draw_move(board):
    """Updates the board with the computer's move"""
    # don't implement any form of artificial intelligence − a random
    # field choice made by the computer is good enough for the game.
    valid = False
    while not valid:
        # first get random value for computer's move
        computer_move = str(randrange(1, 9))
        print("attempting move", computer_move)
        for i, row in enumerate(board):
            for j, column in enumerate(row):
                if computer_move == board[i][j]:
                    board[i][j] = 'x'
                    valid = True


display_board(board)
print(enter_move(board))
display_board(board)
draw_move(board)
display_board(board)
