# Step 3: Finding Maximum Value Recursively
# This demonstrates recursion with comparison logic

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

# Test the maximum function
print("Step 3: Recursive Maximum Function Complete!")
print("=" * 50)

# Test with different lists
test_lists = [
    [3, 7, 2, 9, 1],    # Normal case with positive numbers
    [5],                  # Single element
    [-10, -5, -20],      # Negative numbers
    [3, 3, 3, 3],       # All same values
    [100, 50, 200, 75]  # Larger numbers
]

for test_list in test_lists:
    result = max_recursive(test_list)
    print(f"max_recursive({test_list}) = {result}")

# Test edge case: empty list
print(f"\nmax_recursive([]) = {max_recursive([])}")

print("\n" + "=" * 50)
print("Maximum function is working correctly!")
print("=" * 50)

# Let's trace what happens with max_recursive([3, 7, 2]):
print("\nTracing max_recursive([3, 7, 2]):")
print("max_recursive([3, 7, 2], 0)")
print("  = max(3, max_recursive([3, 7, 2], 1))")
print("  = max(3, max(7, max_recursive([3, 7, 2], 2)))")
print("  = max(3, max(7, 2))  # Base case: index 2 == len([3,7,2])-1")
print("  = max(3, 7)")
print("  = 7")

print("\nKey points:")
print("- Base case 1: when index >= len(numbers), return -inf")
print("- Base case 2: when index == len(numbers)-1, return the element")
print("- Recursive case: compare current with max of the rest")
print("- Use max() function to compare two values")
print("- The function finds the maximum by comparing pairs of values")
print("=" * 50)

# Alternative approach: using a helper function
print("\nAlternative approach - helper function:")
def max_recursive_helper(numbers, index=0, current_max=None):
    """
    Alternative recursive max function using a helper parameter.
    """
    # Base case: if we've reached the end
    if index >= len(numbers):
        return current_max
    
    # If this is the first element, set it as current max
    if current_max is None:
        current_max = numbers[index]
    else:
        # Update current max if we find a larger value
        current_max = max(current_max, numbers[index])
    
    # Recursive call with next index
    return max_recursive_helper(numbers, index + 1, current_max)

# Test the alternative approach
print("Alternative max function:")
for test_list in test_lists:
    result = max_recursive_helper(test_list)
    print(f"max_recursive_helper({test_list}) = {result}")

print("=" * 50)
