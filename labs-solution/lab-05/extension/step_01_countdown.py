# Step 1: Understanding Recursion with Counting
# This demonstrates the basic concept of recursion with a simple countdown function

def countdown(n):
    """
    Count down from n to 1 using recursion.
    
    Args:
        n (int): The starting number
        
    Returns:
        None: Just prints the countdown
    """
    # Base case: stop when we reach 1 or below
    if n <= 0:
        return
    
    # Print current number
    print(n)
    
    # Recursive case: call function with n-1
    countdown(n - 1)

# Test the countdown function
print("Step 1: Countdown Function Complete!")
print("=" * 50)

# Test with different numbers
print("Countdown from 5:")
countdown(5)

print("\nCountdown from 3:")
countdown(3)

print("\nCountdown from 1:")
countdown(1)

print("\nCountdown from 0:")
countdown(0)

print("\n" + "=" * 50)
print("Countdown function is working correctly!")
print("=" * 50)

# Let's trace what happens with countdown(3):
print("\nTracing countdown(3):")
print("countdown(3) calls countdown(2)")
print("countdown(2) calls countdown(1)")
print("countdown(1) calls countdown(0)")
print("countdown(0) returns (base case)")
print("countdown(1) returns")
print("countdown(2) returns")
print("countdown(3) returns")
print("=" * 50)
