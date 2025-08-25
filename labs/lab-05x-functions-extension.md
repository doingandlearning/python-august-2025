# **Lab 5 Extension: Recursive Functions**
### **Objective**
This extension lab builds on **Lab 5: Functions** by exploring **recursive functions** - functions that call themselves to solve problems.

---

## **What is Recursion?**
A **recursive function** is a function that calls itself to solve a smaller version of the same problem. Think of it like a Russian nesting doll - you keep opening smaller dolls until you reach the smallest one.

### **Key Concepts**
- **Base case**: The simplest case that doesn't need recursion
- **Recursive case**: The case where you call the function again with a smaller problem
- **Recursive step**: How you make the problem smaller each time

---

## **Step 1: Understanding Recursion with Counting**
Let's start with a simple example - counting down from a number.

### **Tasks**
1. Write a **`countdown(n)`** function that:
   - Prints numbers from `n` down to 1
   - Uses recursion instead of a loop
   - Stops when it reaches 1

2. Test it with different numbers: 5, 3, and 1

💡 **Hints**
- **Base case**: What happens when `n` is 1?
- **Recursive case**: What do you do when `n` is greater than 1?
- **Recursive step**: How do you make the problem smaller?
- Think about printing the current number, then calling the function with `n-1`

### **Expected Outcomes**
- `countdown(5)` should print: 5, 4, 3, 2, 1
- `countdown(3)` should print: 3, 2, 1
- `countdown(1)` should print: 1

### **Check Your Work**
- Does your function stop when it reaches 1?
- Does it print numbers in descending order?
- Can you trace through what happens step by step?

---

## **Step 2: Recursive List Sum**
Now let's try something more useful - adding up all numbers in a list.

### **Tasks**
1. Write a **`sum_recursive(numbers, index=0)`** function that:
   - Returns the sum of all numbers in the list
   - Uses recursion instead of loops or `sum()`
   - Uses `index` to process one element at a time

2. Test it with different lists: `[1, 2, 3]`, `[5]`, and `[]`

💡 **Hints**
- **Base case**: What happens when `index` reaches the end of the list?
- **Recursive case**: What do you do when there are more numbers to process?
- **Recursive step**: How do you move to the next element?
- Think: current number + sum of the rest of the list

### **Expected Outcomes**
- `sum_recursive([1, 2, 3])` should return `6`
- `sum_recursive([5])` should return `5`
- `sum_recursive([])` should return `0`

### **Check Your Work**
- Does your function work with a single-element list?
- Does it correctly sum multi-element lists?
- Can you trace through the recursive calls?

---

## **Step 3: Finding Maximum Value Recursively**
Let's tackle finding the largest number in a list.

### **Tasks**
1. Write a **`max_recursive(numbers, index=0)`** function that:
   - Returns the largest value in the list
   - Uses recursion instead of loops or `max()`
   - Uses `index` to process one element at a time

2. Test it with different lists: `[3, 7, 2, 9, 1]`, `[5]`, and `[-10, -5, -20]`

💡 **Hints**
- **Base case**: What happens when `index` reaches the end of the list?
- **Recursive case**: What do you do when there are more numbers to process?
- **Recursive step**: How do you move to the next element?
- Think: compare current number with the maximum of the rest

### **Expected Outcomes**
- `max_recursive([3, 7, 2, 9, 1])` should return `9`
- `max_recursive([5])` should return `5`
- `max_recursive([-10, -5, -20])` should return `-5`

### **Check Your Work**
- Does your function work with a single-element list?
- Does it correctly find the maximum in multi-element lists?
- Can you trace through the recursive calls step by step?

---

## **Common Issues to Watch Out For**

### **Infinite Recursion**
- **Missing base case**: Your function must have a stopping condition
- **Wrong recursive step**: Make sure you're making the problem smaller
- **Index errors**: Check that `index` doesn't go beyond list bounds

### **Logic Errors**
- **Forgetting to return**: Make sure your function returns values
- **Wrong comparison**: Double-check your logic for finding maximum
- **Empty list handling**: Think about what happens with `[]`

---

## **Testing Your Solutions**

### **Test Data**
Create these test lists:
```python
test_lists = [
    [1, 2, 3, 4, 5],      # Normal case
    [5],                    # Single element
    [],                     # Empty list
    [-10, -5, -20],        # Negative numbers
    [3, 3, 3, 3]          # All same values
]
```

### **Test Scenarios**
1. **Countdown**: Test with 5, 3, 1, and 0
2. **Sum**: Test with all your test lists
3. **Maximum**: Test with all your test lists

### **Debugging Tips**
- Add print statements to see what's happening
- Start with simple cases (1-2 elements) first
- Draw out the recursive calls on paper

---

## **Extension Ideas (Optional)**

### **More Recursive Functions**
- **`factorial(n)`**: Calculate n! (n × (n-1) × (n-2) × ... × 1)
- **`reverse_string(text)`**: Reverse a string character by character
- **`count_occurrences(numbers, target)`**: Count how many times a number appears

### **Visualizing Recursion**
- Draw a tree of recursive calls
- Use print statements to show the call stack
- Think about the "unwinding" process

---

## **Solutions**

**Complete code examples for all exercises are available in the `solutions/lab-05-extension` folder.**

- `solutions/recursive_functions.py` - All recursive function implementations
- `solutions/step_by_step/` - Individual step solutions

---

## **Why Recursion?**

Recursion is useful because:
- **Elegant solutions**: Some problems are naturally recursive
- **Divide and conquer**: Break big problems into smaller ones
- **Mathematical thinking**: Many algorithms use recursive thinking
- **Tree structures**: Perfect for processing nested data

---

**Remember**: 
- Start simple and build up complexity
- Always have a base case
- Make sure your recursive step makes the problem smaller
- Practice tracing through recursive calls on paper

This extension focuses on one concept (recursion) so you can really understand it before moving to more advanced topics!
