# Lab 9: Step 2 - Add Error Handling
# This adds basic error handling to prevent crashes

import random

print("Step 2: Adding Error Handling to the Guessing Game")
print("=" * 50)

secret_channel = random.randint(1, 50)
attempts = 5

print(f"I'm thinking of a BBC channel number between 1 and 50.")
print(f"You have {attempts} attempts to guess it.")
print("=" * 50)

# This loop now has error handling to prevent crashes
for attempt in range(attempts):
    print(f"\nAttempt {attempt + 1} of {attempts}")
    
    # Try to get valid input from the user
    try:
        guess_str = input("Please guess a channel number: ")
        guess = int(guess_str)
        
    except ValueError:
        # Handle invalid input (non-numeric)
        print("❌ That's not a valid number! Please try again.")
        continue  # Skip to next iteration
    
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
print("This version now handles invalid input gracefully!")
print("Try entering 'five' or 'abc' - it won't crash anymore.")
print("=" * 50)
