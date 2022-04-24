"""Guessing Game"""
import sys
import random
import time
from enum import Enum


class Guess(Enum):
    """Enum for guess result types (high, low, win)."""
    LOW = -1
    WIN = 0
    HIGH = 1


def guess_a_number(previous_guesses, same_guesses, lowest_guess, highest_guess):
    """Returns the computers guess.  Takes in the computers previous guesses, a list of guesses
    the computer guessed more than once, and the high and low range to make a guess within."""
    # Gets a random integer within the specified range.
    random_guess = random.randint(lowest_guess, highest_guess)
    # If that number has been previously guessed, add it to list of same guesses and guess again.
    while random_guess in previous_guesses:
        same_guesses.append(random_guess)
        random_guess = random.randint(lowest_guess, highest_guess)
    # Return the new guess.
    return random_guess


def compare_answer(number_to_guess, user_guess):
    """Returns if the guess is too high, too low, or just right.  Takes in the number to
    guess and the users guess."""
    if user_guess < number_to_guess:
        return Guess.LOW
    if user_guess > number_to_guess:
        return Guess.HIGH
    return Guess.WIN


def main():
    """Main function with the loop, function calls, and game flow logic."""
    # Constants for storing the smallest and biggest possible number.
    max_integer = sys.maxsize
    min_integer = -sys.maxsize

    # Initializations for lowest and highest possible guess.
    lowest_guess = min_integer
    highest_guess = max_integer
    # Variable for determining wining condition to end the game.
    did_i_win = Guess.LOW
    # Empty lists for storing previous guesses and numbers guessed more than once.
    previous_guesses = []
    same_guesses = []

    # Welcome message.
    print("\nWelcome to The Guessing Game!")
    print("Pick a number and I will guess it.\n")
    # Number user picks to have guessed.
    number_to_guess = int(input(f"Enter a number between {min_integer} & {max_integer} => "))
    # Loop until the correct number is guessed.
    while did_i_win != Guess.WIN:
        # Gets the computers guess.
        guess = guess_a_number(previous_guesses, same_guesses, lowest_guess, highest_guess)
        # Adds computers guess to list of previous guessed.
        previous_guesses.append(guess)
        print(f"\nTake a guess => {guess}")
        # Checks if the guess is too high or low or correct.
        did_i_win = compare_answer(number_to_guess, guess)
        # The number was guessed.
        if did_i_win.value == 0:
            print(f"WINNER!!! Congrats I won! I guessed your number was {guess}.")
        # The number was too low.  Sets the guess as the new low value for next guess.
        elif did_i_win.value == -1:
            print("WRONG!!! Guess higher!")
            lowest_guess = guess
        # The number was too high.  Sets the guess as the new high value for next guess.
        elif did_i_win.value == 1:
            print("WRONG!!! Guess lower!")
            highest_guess = guess
        time.sleep(.1)

    # Displays stats at the end of the game.
    print(f"\nIt took me {len(previous_guesses)} guess(es)!")
    print(f"I tried to guess {len(same_guesses)} number(s) the same time.\n")
    if len(same_guesses) > 0:
        print("These are the numbers I tried to guess more than once:")
        for guess in same_guesses:
            print(guess)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
