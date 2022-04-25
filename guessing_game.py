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


def display_menu():
    """Displays game menu with game mode options and returns players pick."""
    # Welcome message.
    print("\nWelcome to The Guessing Game!")
    print('-' * 36)
    print("Pick a game mode:")
    print("1) You vs. The Machine")
    print("2) The Machine vs. You")
    print("3) The Machine vs. The Machine")
    print("4) Quit game")
    print('-' * 36)
    game_mode = input("=> ")
    return game_mode.lower()


def machine_pick_a_number(previous_guesses,
                          same_guesses,
                          lowest_guess,
                          highest_guess):
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


def play_the_machine(machine_number_to_guess, previous_guesses, same_guesses):
    """Keep entering numbers until you guess the number the machine picked."""
    # Variable for determining wining condition to end the game.
    did_i_win = Guess.LOW
    # Loop until the correct number is guessed.
    while did_i_win != Guess.WIN:
        # Get the players guess.
        try:
            player_guess = int(input("\nTake a guess => "))
        except ValueError:
            print("\nYou must enter a number. Try again.")
            continue
        else:
            # Checks if player already guessed this number.
            if player_guess in previous_guesses:
                print("You guessed this already, but ok.")
                same_guesses.append(player_guess)
            # Adds players guess to list of previous guessed.
            previous_guesses.append(player_guess)
            # Checks if the guess is too high or low or correct.
            did_i_win = compare_answer(machine_number_to_guess, player_guess)
            # The number was guessed.
            if did_i_win.value == 0:
                print(f"WINNER!!! Congrats you won! You guessed my number was {player_guess}.")
            # The number was too low.
            elif did_i_win.value == -1:
                print("WRONG!!! Guess higher!")
            # The number was too high.
            elif did_i_win.value == 1:
                print("WRONG!!! Guess lower!")
    return previous_guesses, same_guesses


def machine_plays_you(player_number_to_guess,
                      previous_guesses,
                      same_guesses,
                      lowest_guess,
                      highest_guess):
    """The machine guesses the number you picked."""
    # Variable for determining wining condition to end the game.
    did_i_win = Guess.LOW
    # Loop until the correct number is guessed.
    while did_i_win != Guess.WIN:
        # Gets the computers guess.
        machine_guess = machine_pick_a_number(previous_guesses,
                                              same_guesses,
                                              lowest_guess,
                                              highest_guess)
        # Adds computers guess to list of previous guessed.
        previous_guesses.append(machine_guess)
        print(f"\nTake a guess => {machine_guess}")
        # Checks if the guess is too high or low or correct.
        did_i_win = compare_answer(player_number_to_guess, machine_guess)
        # The number was guessed.
        if did_i_win.value == 0:
            print(f"WINNER!!! Congrats I won! I guessed your number was {machine_guess}.")
        # The number was too low.  Sets the guess as the new low value for next guess.
        elif did_i_win.value == -1:
            print("WRONG!!! Guess higher!")
            lowest_guess = machine_guess
        # The number was too high.  Sets the guess as the new high value for next guess.
        elif did_i_win.value == 1:
            print("WRONG!!! Guess lower!")
            highest_guess = machine_guess
        time.sleep(.1)
    return previous_guesses, same_guesses


def machine_plays_itself(machine_number_to_guess,
                         previous_guesses,
                         same_guesses,
                         lowest_guess,
                         highest_guess):
    """The machine plays against itself."""
    # Variable for determining wining condition to end the game.
    did_i_win = Guess.LOW
    # Loop until the correct number is guessed.
    while did_i_win != Guess.WIN:
        # Gets the computers guess.
        machine_guess = machine_pick_a_number(previous_guesses,
                                              same_guesses,
                                              lowest_guess,
                                              highest_guess)
        # Adds computers guess to list of previous guessed.
        previous_guesses.append(machine_guess)
        print(f"\nTake a guess => {machine_guess}")
        # Checks if the guess is too high or low or correct.
        did_i_win = compare_answer(machine_number_to_guess, machine_guess)
        # The number was guessed.
        if did_i_win.value == 0:
            print(f"WINNER!!! Congrats I won! I guessed your number was {machine_guess}.")
        # The number was too low.  Sets the guess as the new low value for next guess.
        elif did_i_win.value == -1:
            print("WRONG!!! Guess higher!")
            lowest_guess = machine_guess
        # The number was too high.  Sets the guess as the new high value for next guess.
        elif did_i_win.value == 1:
            print("WRONG!!! Guess lower!")
            highest_guess = machine_guess
        time.sleep(.1)
    return previous_guesses, same_guesses


def display_game_stats(previous_guesses, same_guesses):
    """Computes stats from the end of the game and displays them."""
    print(f"\nIt took {len(previous_guesses)} guess(es) to guess the correct number!")
    print(f"There were {len(same_guesses)} number(s) that were guessed more than once.\n")
    if len(same_guesses) > 0:
        print("These are the numbers that were guessed more than once:")
        for guess in same_guesses:
            print(guess)


def main():
    """Main function with the loop, function calls, and game flow logic."""
    # Constants for storing the smallest and biggest possible number.
    max_integer = sys.maxsize
    min_integer = -sys.maxsize

    # Empty lists for storing previous guesses and numbers guessed more than once.
    previous_guesses = []
    same_guesses = []

    while True:
        # Display menu and get desired game mode from player.
        menu_choice = display_menu()
        # Start specified game mode based on input.
        if menu_choice == "1":
            machine_number_to_guess = machine_pick_a_number(previous_guesses,
                                                            same_guesses,
                                                            min_integer,
                                                            max_integer)
            print(f"\nI have chosen a number between {min_integer} & {max_integer}!")
            previous_guesses, same_guesses = play_the_machine(machine_number_to_guess,
                                                              previous_guesses,
                                                              same_guesses)
        elif menu_choice == "2":
            print("\nPick a number and I will guess it.\n")
            while True:
                try:
                    # Number user picks to have guessed.
                    player_number_to_guess = int(input(f"Enter a number between"
                                                       f"{min_integer} & {max_integer} => "))
                except ValueError:
                    print("\nYou must enter a number.  Try again.\n")
                    continue
                else:
                    previous_guesses, same_guesses = machine_plays_you(player_number_to_guess,
                                                                       previous_guesses,
                                                                       same_guesses,
                                                                       min_integer,
                                                                       max_integer)
                    break
        elif menu_choice == "3":
            machine_number_to_guess = machine_pick_a_number(previous_guesses,
                                                            same_guesses,
                                                            min_integer,
                                                            max_integer)
            print(f"\nI have chosen a number between {min_integer} & {max_integer}!")
            previous_guesses, same_guesses = machine_plays_itself(machine_number_to_guess,
                                                                  previous_guesses,
                                                                  same_guesses,
                                                                  min_integer,
                                                                  max_integer)
        elif menu_choice in ("4", "q", "quit"):
            print("\nThanks for playing.  Goodbye!")
            break
        else:
            print("\nInvalid menu option.  Try again.\n")
            continue

        display_game_stats(previous_guesses, same_guesses)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
