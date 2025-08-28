# Lab 9: Step 4 - Using Helper Functions for Input Validation
# This demonstrates how to organize error handling into helper functions

import random

def get_valid_guess(attempt_number, max_attempts):
    """
    Helper function to get and validate user input.
    Returns a valid guess and reprompts the user if it's not.
    """
    print(f"\nAttempt {attempt_number} of {max_attempts}")
    
    try:
        guess_str = input("Please guess a channel number: ")
        guess = int(guess_str)
        
        # Check if the guess is within valid range
        if guess < 1 or guess > 50:
            print("❌ Please enter a number between 1 and 50!")
            return get_valid_guess(attempt_number, max_attempts)
        
        return guess
        
    except ValueError:
        # Handle invalid input (non-numeric)
        print("❌ That's not a valid number! Please try again.")
        return get_valid_guess(attempt_number, max_attempts) 

def main():
    """
    Main function using helper functions for cleaner code.
    """
    print("Step 4: Using Helper Functions for Input Validation")
    print("=" * 50)
    
    secret_channel = random.randint(1, 50)
    attempts = 5
    
    print(f"I'm thinking of a BBC channel number between 1 and 50.")
    print(f"You have {attempts} attempts to guess it.")
    print("=" * 50)
    
    # Main game loop using helper function
    for attempt in range(attempts):
        guess = get_valid_guess(attempt + 1, attempts)
        
        # If input was invalid, continue to next attempt
        if guess is None:
            continue
        
        # Process the valid guess
        if guess == secret_channel:
            print("🎉 Congratulations! You've guessed correctly!")
            break
        elif guess < secret_channel:
            print("📺 Too low! Try a higher channel number.")
        else:
            print("📺 Too high! Try a lower channel number.")
        
        remaining = attempts - (attempt + 1)
        if remaining > 0:
            print(f"Attempts remaining: {remaining}")
    
    print("\n" + "=" * 50)
    print("This version uses helper functions for cleaner, more organized code!")
    print("The error handling is now separated into its own function.")
    print("=" * 50)

if __name__ == "__main__":
    main()
