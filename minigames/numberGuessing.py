import random
import sys
import os
import time
from minigames.creature_reactions import get_creature_reaction


def play_guessing_minigame():
    low, high, max_attempts = difficulty()
    secret_number = random.randint(low, high)
    creature_name = random.choice(["Fizzletail", "Glimwisp", "Snork", "Zilbo", "Wub"])

    print(f"You encounter a strange creature named {creature_name}... It wants you to guess the number it’s thinking of!")
    print(f"'Make a guess between {low} and {high}. You have {max_attempts} tries.' said {creature_name}...")

    guess = get_valid_guess(low, high)
    attempts = 1
    previous_diff = None

    while guess != secret_number:
        if attempts == (max_attempts - 3):
            print("You have 3 guesses left!")
        elif attempts == (max_attempts - 2):
            print("You have 2 guesses left")
        elif attempts == (max_attempts - 1):
            print("LAST CHANCE!")
        elif attempts == max_attempts:
            print("GAME OVER! YOU RAN OUT OF GUESSES.")
            print(f"The secret number was {secret_number}")
            return False

        current_diff = abs(secret_number - guess)
        time.sleep(0.5)
        print(get_creature_reaction(current_diff, previous_diff))
        previous_diff = current_diff
        guess = get_valid_guess(low, high)
        attempts += 1
        
    print("You guessed it!")
    return True

        
def get_valid_guess(low, high):
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if low <= guess <= high:
                return guess    
            else:
                print(f"Please enter a number between {low}-{high}.")
        except ValueError:
            print("Please enter a valid number.")


def difficulty():
    difficulty = random.randint(1, 4)

    if difficulty == 1:
        return 1, 10, 4
    elif difficulty == 2:
        return 1, 50, 20
    elif difficulty == 3:
        return 1, 100, 30
    else:
        return 1, 500, 40






