"""
To create a beginner Python project for a Tic Tac Toe game, follow these steps:

1. **Design the Game Logic**:
   - Understand the rules: Youll need to check if either player (X or O) wins or if the game ends
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
   check if the move is valid (i.e., the cell isnt already taken and is within the bounds of the
   board).

6. **Game Loop**:
   - Use a loop to keep the game running until theres a winner or the game ends in a draw.
   - After each move, check for a win or a draw, then ask the next player to make a move.

7. **Additional Features** (optional for beginners):
   - You could add a way to restart the game or keep track of the score.
   - You could even extend the project to allow two players to play on the same computer or add a
   simple AI opponent.

By following these steps, youll create a simple, interactive Tic Tac Toe game that covers the
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
import time


free_moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

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
    """Updates the board with the player's move and the list of free moves"""
    move = 0
    while move not in free_moves:
        move = input("Please enter your move: ")
        if move not in free_moves:
            print("Invalid move attempt, please try again.")
    # loop through the board
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if move == board[i][j]:
                # place the player's move on the board
                board[i][j] = 'O'
                # update the list of free available moves
                free_moves[int(move)-1] = 'O'


def draw_move(board):
    """Updates the board with the computer's move and the list of free moves"""
    # don't implement any form of artificial intelligence − a random
    # field choice made by the computer is good enough for the game.
    computer_move = 0
    # get a random valid move for the computer
    while computer_move not in free_moves:
        computer_move = str(randrange(1, 10))
    # loop through the board
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if computer_move == board[i][j]:
                # place the computer's move on the board
                board[i][j] = 'X'
                # update the list of free available moves
                free_moves[int(computer_move)-1] = 'X'
                print(f"Computer moved to postion {computer_move}")


def check_victory(board):
    """Returns true if 3 in a row or stalemate"""
    if board[0] == board[1] == board[2] \
            or board[3] == board[4] == board[5] \
            or board[6] == board[7] == board[8] \
            or board[0] == board[3] == board[6] \
            or board[1] == board[4] == board[7] \
            or board[2] == board[5] == board[8] \
            or board[0] == board[4] == board[8] \
            or board[2] == board[4] == board[6]:
        print("Congrats, there's 3 in a row!")
        return True
    # checks for stalemate condition
    for num in range(1, 10):
        if str(num) in board:
            return False
    print("STALEMATE!")
    return True


###################################################################################################


print("Welcome to my Tic Tac Toe game!")
time.sleep(1)
print("The computer will be X's and you will be O's.")
time.sleep(1)
print("The computer will go first!")
time.sleep(1)
print("LET'S BEGIN!")

while True:
    draw_move(board)  # computer turn
    time.sleep(1)
    display_board(board)
    if check_victory(free_moves):
        break
    print("\n", "\n")
    enter_move(board)  # player turn
    display_board(board)
    if check_victory(free_moves):
        break
    time.sleep(1)
    print("\n", "\n")

print("GAME OVER")
