# Lab 9: Testing Error Handling Scenarios
# This script demonstrates various error handling scenarios

import random
from io import StringIO
import sys

def test_error_handling():
    """
    Test function to demonstrate error handling without user input.
    """
    print("Testing Error Handling Scenarios")
    print("=" * 50)
    
    # Test data for different scenarios
    test_inputs = [
        "25",      # Valid number
        "five",    # Text input
        "abc",     # More text
        "0",       # Out of range (too low)
        "100",     # Out of range (too high)
        "25abc",   # Mixed input
        "@#$",     # Special characters
        "",        # Empty input
        "12.5",    # Decimal number
        " 25 ",    # Number with spaces
    ]
    
    secret_channel = 25
    attempts = 3
    
    print(f"Secret channel: {secret_channel}")
    print(f"Test inputs: {test_inputs}")
    print("=" * 50)
    
    for i, test_input in enumerate(test_inputs):
        print(f"\nTest {i+1}: Input = '{test_input}'")
        
        try:
            # Try to convert input to integer
            guess = int(test_input)
            
            # Check range
            if guess < 1 or guess > 50:
                print(f"❌ Range Error: {guess} is outside 1-50")
                continue
            
            # Process valid guess
            if guess == secret_channel:
                print(f"🎉 Correct! {guess} matches the secret channel")
                break
            elif guess < secret_channel:
                print(f"📺 Too low: {guess} < {secret_channel}")
            else:
                print(f"📺 Too high: {guess} > {secret_channel}")
                
        except ValueError:
            print(f"❌ ValueError: '{test_input}' cannot be converted to a number")
        except Exception as e:
            print(f"❌ Unexpected error: {type(e).__name__}: {e}")
    
    print("\n" + "=" * 50)
    print("Error handling test completed!")
    print("This demonstrates how different types of input are handled.")

def demonstrate_try_except_structure():
    """
    Demonstrate the basic try-except structure.
    """
    print("\n" + "=" * 50)
    print("Try-Except Structure Examples")
    print("=" * 50)
    
    # Example 1: Basic try-except
    print("\n1. Basic try-except:")
    try:
        result = int("abc")
        print(f"Result: {result}")
    except ValueError:
        print("Caught ValueError: 'abc' is not a valid number")
    
    # Example 2: Multiple except blocks
    print("\n2. Multiple except blocks:")
    try:
        result = int("abc")
        print(f"Result: {result}")
    except ValueError:
        print("Caught ValueError: Invalid number format")
    except TypeError:
        print("Caught TypeError: Wrong type")
    except Exception as e:
        print(f"Caught general exception: {e}")
    
    # Example 3: Try-except with else and finally
    print("\n3. Try-except with else and finally:")
    try:
        result = int("25")
        print(f"Result: {result}")
    except ValueError:
        print("Caught ValueError")
    else:
        print("No exception occurred - this runs on success")
    finally:
        print("Finally block always runs")
    
    # Example 4: Raising exceptions
    print("\n4. Raising custom exceptions:")
    try:
        age = int("150")
        if age > 120:
            raise ValueError("Age seems unrealistic")
        print(f"Age: {age}")
    except ValueError as e:
        print(f"Caught ValueError: {e}")

if __name__ == "__main__":
    test_error_handling()
    demonstrate_try_except_structure()
    
    print("\n" + "=" * 50)
    print("Key Points About Error Handling:")
    print("- Always catch specific exceptions when possible")
    print("- Use try-except to prevent crashes")
    print("- Provide helpful error messages to users")
    print("- Use continue to skip invalid input in loops")
    print("- Test your error handling with various inputs")
    print("=" * 50)
