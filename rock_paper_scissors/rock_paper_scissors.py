import random

"""play game function"""


def play_game():

    player_wins = 0
    computer_wins = 0
    computer_choices = ['r', 'p', 's']

    print("Welcome to Rock, Papper, Scissors. \nBest 2 out of 3 wins! Let's play!!\n")

    # while loop for best 2 out of 3
    while (player_wins < 2 and computer_wins < 2):

        # get a valid user input
        while (True):
            player = input(
                "What's your choice? 'r' for rock, 'p' for paper, 's' for scissors: ")
            if player in computer_choices:
                break

        computer = random.choice(computer_choices)

        # check for tie
        if player == computer:
            print(f"\nIt's a tie! Player: {player}, Computer: {computer}")
            print(f"Player Rounds: {player_wins}")
            print(f"Computer Rounds: {computer_wins}")
            print()

        # returns true if player won
        elif who_won(player, computer):
            player_wins += 1
            print(f"\nYou won! Player: {player}, Computer: {computer}")
            print(f"Player Rounds: {player_wins}")
            print(f"Computer Rounds: {computer_wins}")
            print()

        # not a tie, and player didn't win, so computer won
        else:
            computer_wins += 1
            print(f"\nYou lost! Player: {player}, Computer: {computer}")
            print(f"Player Rounds: {player_wins}")
            print(f"Computer Rounds: {computer_wins}")
            print()

    if player_wins > computer_wins:
        print("\nGamer Over, Congratulations,You Won!")
        print(f"Player Rounds: {player_wins}")
        print(f"Computer Rounds: {computer_wins}")
    else:
        print("\nGamer Over, Better Luck Next Time!")
        print(f"Player Rounds: {player_wins}")
        print(f"Computer Rounds: {computer_wins}")


"""determine winner function"""
# r > s, p > r, s > p


def who_won(player, computer):
    """determine if the player won the round"""
    if (player == 'r' and computer == 's') or (player == 'p' and
                                               computer == 'r') or (player == 's' and computer == 'p'):
        return True


print(play_game())
