# Lab 5 Extension: Recursive Functions - Solutions

This folder contains complete solutions for the Lab 5 Extension: Recursive Functions. These solutions demonstrate how to implement recursive functions that call themselves to solve problems.

## Files Overview

### Complete Solution

1. **`recursive_functions.py`** - Complete working program with all recursive functions
   - Demonstrates all recursive functions from the extension
   - Includes comprehensive testing and tracing
   - Ready to run and explore recursion

### Step-by-Step Solutions

2. **`step_01_countdown.py`** - Step 1: Basic countdown recursion
   - Shows the simplest form of recursion
   - Demonstrates base case and recursive case
   - Includes tracing of recursive calls

3. **`step_02_sum.py`** - Step 2: Recursive list summation
   - Shows recursion with return values
   - Demonstrates processing lists recursively
   - Includes step-by-step tracing

4. **`step_03_maximum.py`** - Step 3: Recursive maximum finding
   - Shows recursion with comparison logic
   - Demonstrates multiple base cases
   - Includes alternative implementation approach

## How to Use These Solutions

### For Learning
1. **Try the extension exercises yourself first** - don't peek at solutions until you're stuck!
2. **Compare your code** with the solutions to see different approaches
3. **Experiment** with the code - modify functions, add new parameters
4. **Run each step file** to see how recursion builds up gradually

### For Reference
- Use these as templates for similar recursive problems
- Study the recursive structure and base case handling
- Note the docstring documentation and commenting
- See how different recursive patterns work

## Running the Programs

All programs can be run from the command line:

```bash
python recursive_functions.py
python step_01_countdown.py
python step_02_sum.py
python step_03_maximum.py
```

## Key Concepts Demonstrated

### **Recursion Fundamentals**
- **Base Case**: The stopping condition that prevents infinite recursion
- **Recursive Case**: The case where the function calls itself
- **Recursive Step**: How the problem gets smaller with each call
- **Function Unwinding**: How results flow back up the call stack

### **Recursive Patterns**
- **Tail Recursion**: Functions that make recursive calls at the end
- **Index-based Processing**: Using an index parameter to track position
- **Return Value Accumulation**: Building results through recursive calls
- **Multiple Base Cases**: Handling different stopping conditions

## Concepts Used (Extension Level)

These solutions use concepts appropriate for the extension:
- Function definition with `def`
- Function parameters and arguments
- Return statements
- Recursive function calls
- Basic list operations and indexing
- Comparison operations (`max()`, `min()`)
- Edge case handling

## Sample Output

When you run the complete program, you'll see:

```
Lab 5 Extension: Recursive Functions Demo
==================================================

1. COUNTDOWN FUNCTION
------------------------------
Countdown from 5:
5
4
3
2
1

2. RECURSIVE SUM FUNCTION
------------------------------
sum_recursive([1, 2, 3, 4, 5]) = 15
sum_recursive([5]) = 5
sum_recursive([]) = 0
sum_recursive([-10, -5, -20]) = -35
sum_recursive([3, 3, 3, 3]) = 12

3. RECURSIVE MAXIMUM FUNCTION
------------------------------
max_recursive([3, 7, 2, 9, 1]) = 9
max_recursive([5]) = 5
max_recursive([-10, -5, -20]) = -5
max_recursive([3, 3, 3, 3]) = 3
max_recursive([100, 50, 200, 75]) = 200
```

## Function Examples

### Basic Recursion (Step 1)
```python
def countdown(n):
    if n <= 0:  # Base case
        return
    print(n)    # Process current value
    countdown(n - 1)  # Recursive call
```

### Recursion with Return Values (Step 2)
```python
def sum_recursive(numbers, index=0):
    if index >= len(numbers):  # Base case
        return 0
    return numbers[index] + sum_recursive(numbers, index + 1)  # Recursive case
```

### Recursion with Comparison (Step 3)
```python
def max_recursive(numbers, index=0):
    if index >= len(numbers):  # Base case 1
        return float('-inf')
    if index == len(numbers) - 1:  # Base case 2
        return numbers[index]
    return max(numbers[index], max_recursive(numbers, index + 1))  # Recursive case
```

## Understanding Recursion

### **The Call Stack**
Recursive functions create a "call stack" where each recursive call waits for the next one to complete:

```
countdown(3) calls countdown(2)
  countdown(2) calls countdown(1)
    countdown(1) calls countdown(0)
      countdown(0) returns (base case)
    countdown(1) returns
  countdown(2) returns
countdown(3) returns
```

### **Base Cases**
Every recursive function needs at least one base case:
- **Countdown**: Stop when `n <= 0`
- **Sum**: Stop when `index >= len(numbers)`
- **Maximum**: Stop when `index >= len(numbers)` or at last element

### **Recursive Steps**
Each recursive call should make the problem smaller:
- **Countdown**: `n - 1` (closer to base case)
- **Sum**: `index + 1` (closer to end of list)
- **Maximum**: `index + 1` (closer to end of list)

## Common Recursion Patterns

### **List Processing**
```python
def process_list(items, index=0):
    if index >= len(items):  # Base case
        return result
    # Process current item
    # Make recursive call with next index
    return process_list(items, index + 1)
```

### **Tree-like Processing**
```python
def process_tree(node):
    if node is None:  # Base case
        return result
    # Process current node
    # Process left subtree
    # Process right subtree
    return combine_results(...)
```

## Debugging Recursive Functions

### **Common Issues**
1. **Missing base case**: Function never stops calling itself
2. **Wrong recursive step**: Problem doesn't get smaller
3. **Index errors**: Going beyond list boundaries
4. **Logic errors**: Wrong comparison or calculation

### **Debugging Tips**
1. **Add print statements** to see the call flow
2. **Start with simple cases** (1-2 elements)
3. **Draw the call stack** on paper
4. **Check base cases** first
5. **Verify recursive steps** make the problem smaller

## Extension Ideas

### **More Recursive Functions**
- **`factorial(n)`**: Calculate n! recursively
- **`fibonacci(n)`**: Generate Fibonacci sequence
- **`reverse_string(text)`**: Reverse a string character by character
- **`binary_search(numbers, target, low, high)`**: Binary search algorithm

### **Advanced Recursion**
- **Tree traversal**: Process hierarchical data structures
- **Backtracking**: Solve puzzles like Sudoku or maze navigation
- **Divide and conquer**: Merge sort, quick sort algorithms
- **Dynamic programming**: Optimize recursive solutions with memoization

## Next Steps

After completing this extension, you should be comfortable with:
- Writing recursive functions with proper base cases
- Understanding how recursive calls work
- Debugging recursive function issues
- Applying recursion to list processing problems

Move on to more advanced topics like:
- **Lab 6: Advanced Functions** for decorators and closures
- **Lab 7: Classes** for object-oriented programming
- **Algorithm Design** for more complex recursive algorithms

---

**Remember**: 
- Recursion is a powerful problem-solving tool
- Always start with the base case
- Make sure your recursive step makes the problem smaller
- Practice tracing recursive calls to understand the flow
- Don't be afraid to draw diagrams to visualize recursion

This extension provides a solid foundation in recursion that you can build upon in future labs!
