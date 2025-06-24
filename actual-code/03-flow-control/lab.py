"""
Solution for the Iteration and Control Flow Lab (Channel Guessing Game).
"""

import random

# Step 1: Setting up the Game
secret_channel = random.randint(1, 50)
print("I'm thinking of a BBC channel number between 1 and 50.")
print("You have 5 tries to guess it!")
print("-" * 20)

# Step 4: Handling a Win or Loss (Setup the flag)
player_won = False

# Step 2: The Game Loop
for guess_attempt in range(5):
    # The number of the current attempt
    print(f"Attempt {guess_attempt + 1} of 5")

    # Step 3: Getting and Checking the User's Guess
    guess_str = input("Please guess a channel number: ")
    guess = int(guess_str)

    if guess == secret_channel:
        print(f"Well done! You guessed it. The channel was {secret_channel}.")
        player_won = True
        break  # Exit the loop on a correct guess
    elif guess < secret_channel:
        print("Too low, try a higher number.")
    else:
        print("Too high, try a lower number.")

    print("-" * 20)


# After the loop, check the flag to see if the player won
print("-" * 20)
if not player_won:
    print("Sorry, you've run out of attempts.")
    print(f"The secret channel number was {secret_channel}.")

print("Game Over.") 