import guess_number

ryans_game = guess_number

game_type = int(input(
    "Enter 1 if you want to guess, enter 2 if you want the computer to guess: "))
if game_type == 1:
    # ryans_game.user_guess()
    ryans_game.user_guess2(10)
elif game_type == 2:
    # ryans_game.computer_guess()
    ryans_game.computer_guess2(10)
else:
    print("Invalid entry")
