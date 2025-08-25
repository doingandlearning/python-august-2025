# Lab 9: Step 3 - Enhanced Error Handling with Range Validation
# This adds range validation and better error messages

import random

print("Step 3: Enhanced Error Handling with Range Validation")
print("=" * 50)

secret_channel = random.randint(1, 50)
attempts = 5

print(f"I'm thinking of a BBC channel number between 1 and 50.")
print(f"You have {attempts} attempts to guess it.")
print("=" * 50)

# Enhanced error handling with range validation
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
        break
    elif guess < secret_channel:
        print("📺 Too low! Try a higher channel number.")
    else:
        print("📺 Too high! Try a lower channel number.")
    
    remaining = attempts - (attempt + 1)
    if remaining > 0:
        print(f"Attempts remaining: {remaining}")

print("\n" + "=" * 50)
print("This version now handles both invalid input and out-of-range numbers!")
print("Try entering 'five', '0', or '100' - it handles all cases gracefully.")
print("=" * 50)
