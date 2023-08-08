"""This is a number guessing game, the computer will guess the number you are thinking of
https://www.youtube.com/watch?v=8ext9G7xspg&t=100s"""

import random


def user_guess():
    """method to begin the user number guessing game, this \
    is my implementation before looking at the answer"""
    guess = 0
    computer_number = int(random.randint(1, 20))
    print("Computer is thinking...Computer has picked a number between 1 and 20!")
    print("Let's play!")
    while guess != computer_number:
        guess = int(input("Guess a number between 1 and 20: "))
        if guess < computer_number:
            print("Sorry, too low, try again!")
        elif guess > computer_number:
            print("Sorry, too high, try again!")
    print(
        f"You guessed correctly, the computer's number was {computer_number}!")


"""Actual Solution"""


def user_guess2(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(
        f'Yay, congrats. You have guessed the number {random_number} correctly!!')


def computer_guess():
    """method to begin the computer number guessing game """
    guessed = False
    upper = 1000
    lower = 1
    number = random.randint(lower, upper)
    print("Think of a number between 1 and 1000!")
    print("Let's play!")
    while not guessed:
        hint = input(
            f"Is {number} too high (H), too low (L), or correct (C)??")
        if hint == "H":
            print("Entered H")
            upper = number - 1
            number = int((upper+lower)/2)
        elif hint == "L":
            lower = number + 1
            number = int((upper+lower)/2)
        elif hint == "C":
            print(f"Yay! The computer guess your number, {number}, correctly!")
            guessed = True
        else:
            print("Invalid entry")


"""Actual Solution"""


def computer_guess2(x):
    low = 1
    high = x
    feedback = ""
    print(f"Think of a number between {low} and {high}! - Let's play!")
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(
            f"Is {guess} too high (H), too low (L), or correct (C)??").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yay! The computer guessed your number, {guess}, correctly!")
