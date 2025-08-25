# Lab 9: Step 1 - Find the Bug
# This demonstrates the bug in the guessing game that causes a crash

import random

print("Step 1: Finding the Bug in the Guessing Game")
print("=" * 50)

# This is the buggy version from Lab 3
secret_channel = random.randint(1, 50)
attempts = 5

print(f"I'm thinking of a BBC channel number between 1 and 50.")
print(f"You have {attempts} attempts to guess it.")
print("=" * 50)

# This loop has a bug - it will crash on invalid input
for attempt in range(attempts):
    print(f"\nAttempt {attempt + 1} of {attempts}")
    
    # BUG: This line will crash if user enters non-numeric input
    # Try entering "five" or "abc" to see the crash!
    guess = int(input("Please guess a channel number: "))
    
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
print("This version will crash if you enter invalid input!")
print("Try running it and entering 'five' instead of 5 to see the error.")
print("=" * 50)
