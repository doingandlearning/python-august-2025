# Lab 9: Step 5 - Custom Exceptions for Error Handling
# This demonstrates how to create and use custom exception classes

import random

# Custom exception classes
class ChannelError(Exception):
    """Base exception for channel-related errors."""
    pass

class OutOfRangeError(ChannelError):
    """Exception raised when a channel number is out of valid range."""
    pass

class InvalidInputError(ChannelError):
    """Exception raised when input cannot be converted to a number."""
    pass

def get_valid_guess(attempt_number, max_attempts):
    """
    Helper function that raises custom exceptions for different error types.
    """
    print(f"\nAttempt {attempt_number} of {max_attempts}")
    
    try:
        guess_str = input("Please guess a channel number: ")
        guess = int(guess_str)
        
        # Check if the guess is within valid range
        if guess < 1 or guess > 50:
            raise OutOfRangeError(f"Channel {guess} is outside the valid range (1-50)")
        
        return guess
        
    except ValueError:
        # Handle invalid input (non-numeric)
        raise InvalidInputError("Input must be a valid number")
    except OutOfRangeError:
        # Re-raise our custom exception
        raise

def main():
    """
    Main function demonstrating custom exception handling.
    """
    print("Step 5: Custom Exceptions for Error Handling")
    print("=" * 50)
    
    secret_channel = random.randint(1, 50)
    attempts = 5
    
    print(f"I'm thinking of a BBC channel number between 1 and 50.")
    print(f"You have {attempts} attempts to guess it.")
    print("=" * 50)
    
    # Main game loop with custom exception handling
    for attempt in range(attempts):
        try:
            guess = get_valid_guess(attempt + 1, attempts)
            
        except OutOfRangeError as e:
            print(f"❌ Range Error: {e}")
            continue
        except InvalidInputError as e:
            print(f"❌ Input Error: {e}")
            continue
        except ChannelError as e:
            print(f"❌ Channel Error: {e}")
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
    print("This version uses custom exceptions for more specific error handling!")
    print("Different types of errors are handled with different exception classes.")
    print("=" * 50)

if __name__ == "__main__":
    main()
