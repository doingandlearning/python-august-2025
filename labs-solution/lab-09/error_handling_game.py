# Lab 9: Error Handling - Complete Solution
# This is the complete guessing game with error handling

import random

def main():
    """
    Main function to run the BBC Channel Guessing Game with error handling.
    """
    print("Welcome to the BBC Channel Guessing Game!")
    print("=" * 50)
    
    # Generate a random secret channel number
    secret_channel = random.randint(1, 50)
    attempts = 5
    player_won = False
    
    print(f"I'm thinking of a BBC channel number between 1 and 50.")
    print(f"You have {attempts} attempts to guess it.")
    print("=" * 50)
    
    # Main game loop with error handling
    for attempt in range(attempts):
        print(f"\nAttempt {attempt + 1} of {attempts}")
        
        # Try to get valid input from the user
        try:
            guess_str = input("Please guess a channel number: ")
            guess = int(guess_str)
            
            # Check if the guess is within valid range
            if guess < 1 or guess > 50:
                print("❌ Please enter a number between 1 and 50!")
                continue
            
        except ValueError:
            # Handle invalid input (non-numeric)
            print("❌ That's not a valid number! Please try again.")
            continue
        
        # Process the valid guess
        if guess == secret_channel:
            print("🎉 Congratulations! You've guessed correctly!")
            print(f"The secret channel was {secret_channel}!")
            player_won = True
            break
        elif guess < secret_channel:
            print("📺 Too low! Try a higher channel number.")
        else:
            print("📺 Too high! Try a lower channel number.")
        
        # Show remaining attempts
        remaining = attempts - (attempt + 1)
        if remaining > 0:
            print(f"Attempts remaining: {remaining}")
    
    # Game over - show result
    print("\n" + "=" * 50)
    if player_won:
        print("🏆 You won! Well done!")
        print(f"You found the secret channel in {attempt + 1} attempts!")
    else:
        print("😔 Game Over! You've run out of attempts.")
        print(f"The secret channel was {secret_channel}.")
    
    print("=" * 50)
    print("Thanks for playing the BBC Channel Guessing Game!")

if __name__ == "__main__":
    main()
