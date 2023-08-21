"""this is my implementation before looking at the answer
https://www.youtube.com/watch?v=8ext9G7xspg&t=1465s

***inital thoughts***
-six lives
-will need to pick a random word to use
-store the word as letters in an array (answer array)
-create a second arrary same length, but filled with dashes (guess arrary)
-loop while still alive
-user will guess a letter (need to keep track of guessed letters)
-check if the user guess is in the answer array
-if the user guess is in the answer arrary, copy the answer arrary at index to same index is guess array)
-if the user guess is not in the answer arrary, add letter to guessed letters, subtract 1 life

https://www.w3schools.com/python/python_arrays.asp
Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
"""

import random
from words import words


def play_hangman():

    word = list(random.choice(words).upper())
    current_word = []
    guessed_letters = []
    lives = 6

    # create inital current_word filled with dashes using a list comprehension
    current_word = ["-" for letters in enumerate(word)]

    # begin game loop
    while lives > 0:
        print(f"You have {lives} lives left and you have used these letters: ", ' '.join(
            guessed_letters))
        print("Current word: ", ' '.join(current_word))

        # get a valid guess from the user
        while True:
            guess = input("\nGuess a letter: ").upper()
            if guess not in guessed_letters and guess.isalpha() and len(guess) == 1:
                break
            print(
                "Invalid guess, you've already guessed that letter or you entered an invalid character.")

        # if the letter is not in the word
        if guess not in word:
            print(f"\nSorry, your guess {guess} was not in the word!")
            guessed_letters.append(guess)
            lives -= 1
        else:
            # letter is in the word so update current_word
            for x, letter in enumerate(word):
                if guess == letter:
                    current_word[x] = guess
                    print(f"\nNice, your guess {guess} was in the word!")

        # if guess == word then you won, game over
        if current_word == word:
            print("\nCongratulations, you guessed the word,",
                  "".join(word), "!!")
            return

    print("\nGAME OVER")
    print("Sorry, you lost. The word was ", end="")
    print("".join(word))
    return


# start the game
play_hangman()
