# Step 2: Recursive List Sum
# This demonstrates recursion with a function that returns a value

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

# Test the sum function
print("Step 2: Recursive Sum Function Complete!")
print("=" * 50)

# Test with different lists
test_lists = [
    [1, 2, 3],      # Normal case
    [5],             # Single element
    [],              # Empty list
    [-10, -5, -20], # Negative numbers
    [3, 3, 3, 3]   # All same values
]

for test_list in test_lists:
    result = sum_recursive(test_list)
    print(f"sum_recursive({test_list}) = {result}")

print("\n" + "=" * 50)
print("Sum function is working correctly!")
print("=" * 50)

# Let's trace what happens with sum_recursive([1, 2, 3]):
print("\nTracing sum_recursive([1, 2, 3]):")
print("sum_recursive([1, 2, 3], 0)")
print("  = 1 + sum_recursive([1, 2, 3], 1)")
print("  = 1 + (2 + sum_recursive([1, 2, 3], 2))")
print("  = 1 + (2 + (3 + sum_recursive([1, 2, 3], 3)))")
print("  = 1 + (2 + (3 + 0))  # Base case: index 3 >= len([1,2,3])")
print("  = 1 + (2 + 3)")
print("  = 1 + 5")
print("  = 6")

print("\nKey points:")
print("- Base case: when index >= len(numbers), return 0")
print("- Recursive case: current number + sum of the rest")
print("- Each recursive call moves the index forward")
print("- The function 'unwinds' from the base case back up")
print("=" * 50)
