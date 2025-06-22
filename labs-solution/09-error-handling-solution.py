"""
Solution for Lab 9: Error Handling.

This solution adds a try...except block to the "Channel Guessing Game"
to handle non-numeric user input gracefully.
"""

import random

def guessing_game():
    """The main function for our game."""
    secret_channel = random.randint(1, 50)
    print("I'm thinking of a BBC channel number between 1 and 50.")
    print("You have 5 tries to guess it!")
    print("-" * 20)

    player_won = False

    for guess_attempt in range(5):
        print(f"Attempt {guess_attempt + 1} of 5")

        try:
            # Step 2: Put the risky code in a try block
            guess_str = input("Please guess a channel number: ")
            guess = int(guess_str)
        except ValueError:
            # This block runs if int() fails
            print("That's not a valid number! Wasting a guess.")
            print("-" * 20)
            continue  # Skip to the next attempt

        if guess == secret_channel:
            print(f"Well done! You guessed it. The channel was {secret_channel}.")
            player_won = True
            break
        elif guess < secret_channel:
            print("Too low, try a higher number.")
        else:
            print("Too high, try a lower number.")

        print("-" * 20)


    if not player_won:
        print("Sorry, you've run out of attempts.")
        print(f"The secret channel number was {secret_channel}.")

    print("Game Over.")


if __name__ == "__main__":
    guessing_game() 