# Step 1: Setting up the Game
# This demonstrates the basic setup for the guessing game

import random

# Generate a random secret channel number
secret_channel = random.randint(1, 50)

# Print welcome message
print("Welcome to the BBC Channel Guessing Game!")
print("I'm thinking of a channel number between 1 and 50.")
print("You have 5 tries to guess it!")

# For debugging - remove this in the final game
print(f"Secret number: {secret_channel}")
