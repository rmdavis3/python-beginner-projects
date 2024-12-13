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
            print("Invalid move attempt")
    # place the player's move on the board
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if move == board[i][j]:
                board[i][j] = 'O'
                free_moves[int(move)-1] = 'O'


def draw_move(board):
    """Updates the board with the computer's move and the list of free moves"""
    # don't implement any form of artificial intelligence − a random
    # field choice made by the computer is good enough for the game.
    computer_move = 0
    while computer_move not in free_moves:
        computer_move = str(randrange(1, 10))
    print("computer is attempting to move to position", computer_move)
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if computer_move == board[i][j]:
                board[i][j] = 'X'
                free_moves[int(computer_move)-1] = 'X'


def check_victory(board):
    """Returns true if 3 in a row or stalemate"""
    print("checking for victory")
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
    for num in range(1, 10):
        if str(num) in board:
            print("checking for if any valid moves are left, at least postion",
                  num, "is left")
            return False
    print("STALEMATE!")
    return True


###################################################################################################

# temp = ['x', 'o', 'x', 'o', 'x', 'x', 'o', 'x', 'o']
# print(temp)
# for num in range(1, 10):
#     print("hi", type(num))
#     if str(num) in temp:
#         print(temp)
#         print(num, "is in temp")


print("Welcome to my Tic Tac Toe game!")
time.sleep(1)
print("The computer will be X's and you will be O's.")
time.sleep(1)
print("The computer will go first!")
time.sleep(1)
print("LET'S BEGIN!")

while True:
    draw_move(board)  # computer turn
    time.sleep(3)
    display_board(board)
    if check_victory(free_moves):
        break
    print(free_moves)
    print("\n", "\n", "\n", "-"*50)
    enter_move(board)  # player turn
    display_board(board)
    if check_victory(free_moves):
        break
    time.sleep(2)
    print(free_moves)
    print("\n", "\n", "\n", "-"*50)

print("GAME OVER")

# display_board(board)
# draw_move(board)  # computer turn
# print("victory?", check_victory(free_moves))
# display_board(board)

# enter_move(board)  # player turn
# print("victory?", check_victory(free_moves))
# display_board(board)

# draw_move(board)  # computer turn
# print("victory?", check_victory(free_moves))
# display_board(board)

# enter_move(board)  # player turn
# print("victory?", check_victory(free_moves))
# display_board(board)

# draw_move(board)  # computer turn
# print("victory?", check_victory(free_moves))
# display_board(board)

# enter_move(board)  # player turn
# print("victory?", check_victory(free_moves))
# display_board(board)

# print(free_moves)
# print("victory?", check_victory(free_moves))


# def draw_move(board):
#     """Updates the board with the computer's move"""
#     # don't implement any form of artificial intelligence − a random
#     # field choice made by the computer is good enough for the game.
#     valid = False
#     while not valid:
#         # first get random value for computer's move
#         computer_move = str(randrange(1, 9))
#         print("attempting move", computer_move)
#         for i, row in enumerate(board):
#             for j, column in enumerate(row):
#                 if computer_move == board[i][j]:
#                     print(i, j)
#                     board[i][j] = 'x'
#                     valid = True
