# Lab 5 Extension: Recursive Functions - Complete Solution
# This program demonstrates recursive functions that call themselves

def countdown(n):
    """
    Count down from n to 1 using recursion.
    
    Args:
        n (int): The starting number
        
    Returns:
        None: Just prints the countdown
    """
    # Base case: stop when we reach 1
    if n <= 0:
        return
    
    # Print current number
    print(n)
    
    # Recursive case: call function with n-1
    countdown(n - 1)

def sum_recursive(numbers, index=0):
    """
    Calculate the sum of a list using recursion.
    
    Args:
        numbers (list): List of numbers to sum
        index (int): Current position in the list
        
    Returns:
        int/float: Sum of all numbers in the list
    """
    # Base case: if we've reached the end of the list
    if index >= len(numbers):
        return 0
    
    # Recursive case: current number + sum of the rest
    return numbers[index] + sum_recursive(numbers, index + 1)

def max_recursive(numbers, index=0):
    """
    Find the maximum value in a list using recursion.
    
    Args:
        numbers (list): List of numbers to search
        index (int): Current position in the list
        
    Returns:
        int/float: Maximum value in the list
    """
    # Base case: if we've reached the end of the list
    if index >= len(numbers):
        return float('-inf')  # Return negative infinity as base case
    
    # Base case: if this is the last element
    if index == len(numbers) - 1:
        return numbers[index]
    
    # Recursive case: compare current with maximum of the rest
    current = numbers[index]
    max_of_rest = max_recursive(numbers, index + 1)
    
    return max(current, max_of_rest)

def min_recursive(numbers, index=0):
    """
    Find the minimum value in a list using recursion.
    
    Args:
        numbers (list): List of numbers to search
        index (int): Current position in the list
        
    Returns:
        int/float: Minimum value in the list
    """
    # Base case: if we've reached the end of the list
    if index >= len(numbers):
        return float('inf')  # Return positive infinity as base case
    
    # Base case: if this is the last element
    if index == len(numbers) - 1:
        return numbers[index]
    
    # Recursive case: compare current with minimum of the rest
    current = numbers[index]
    min_of_rest = min_recursive(numbers, index + 1)
    
    return min(current, min_of_rest)

def main():
    """
    Main function to demonstrate all recursive functions.
    """
    print("Lab 5 Extension: Recursive Functions Demo")
    print("=" * 50)
    
    # Test countdown function
    print("\n1. COUNTDOWN FUNCTION")
    print("-" * 30)
    print("Countdown from 5:")
    countdown(5)
    
    print("\nCountdown from 3:")
    countdown(3)
    
    print("\nCountdown from 1:")
    countdown(1)
    
    # Test sum function
    print("\n\n2. RECURSIVE SUM FUNCTION")
    print("-" * 30)
    test_lists = [
        [1, 2, 3, 4, 5],
        [5],
        [],
        [-10, -5, -20],
        [3, 3, 3, 3]
    ]
    
    for test_list in test_lists:
        result = sum_recursive(test_list)
        print(f"sum_recursive({test_list}) = {result}")
    
    # Test max function
    print("\n\n3. RECURSIVE MAXIMUM FUNCTION")
    print("-" * 30)
    for test_list in test_lists:
        if test_list:  # Skip empty list for max
            result = max_recursive(test_list)
            print(f"max_recursive({test_list}) = {result}")
        else:
            print(f"max_recursive({test_list}) = Cannot find max of empty list")
    
    # Test min function
    print("\n\n4. RECURSIVE MINIMUM FUNCTION")
    print("-" * 30)
    for test_list in test_lists:
        if test_list:  # Skip empty list for min
            result = min_recursive(test_list)
            print(f"min_recursive({test_list}) = {result}")
        else:
            print(f"min_recursive({test_list}) = Cannot find min of empty list")
    
    # Demonstrate recursion step by step
    print("\n\n5. RECURSION STEP-BY-STEP")
    print("-" * 30)
    print("Let's trace sum_recursive([1, 2, 3]):")
    print("sum_recursive([1, 2, 3], 0)")
    print("  = 1 + sum_recursive([1, 2, 3], 1)")
    print("  = 1 + (2 + sum_recursive([1, 2, 3], 2))")
    print("  = 1 + (2 + (3 + sum_recursive([1, 2, 3], 3)))")
    print("  = 1 + (2 + (3 + 0))")
    print("  = 1 + (2 + 3)")
    print("  = 1 + 5")
    print("  = 6")
    
    print("\n" + "=" * 50)
    print("Recursion demonstration complete!")
    print("=" * 50)

if __name__ == "__main__":
    main()
