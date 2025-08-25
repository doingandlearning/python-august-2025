# Lab 4: Analyzing News Headlines - Solutions

This folder contains complete solutions for all exercises in Lab 4: Analyzing News Headlines.

## Files Overview

### Complete Solution

1. **`news_analysis.py`** - Complete working news analysis program
   - Demonstrates all concepts from the lab
   - Includes polished output and user interaction
   - Ready to run and analyze headlines

### Step-by-Step Solutions

2. **`step_01_setup.py`** - Step 1: Setting up the file and headlines list
   - Shows how to create and populate a list
   - Demonstrates basic list operations
   - Basic verification that data is loaded

3. **`step_02_count.py`** - Step 2: Counting headlines and calculating averages
   - Shows how to loop through lists
   - Demonstrates using `.split()` method
   - Shows basic statistics calculations

4. **`step_03_search.py`** - Step 3: Implementing search functionality
   - Shows how to search through lists
   - Demonstrates case-insensitive string matching
   - Shows user input handling

5. **`step_04_complete.py`** - Step 4: Complete program with functions
   - Shows how to organize code into functions
   - Demonstrates putting all concepts together
   - More advanced structure (optional for this lab level)

## How to Use These Solutions

### For Learning
1. **Try the lab exercises yourself first** - don't peek at solutions until you're stuck!
2. **Compare your code** with the solutions to see different approaches
3. **Experiment** with the code - modify headlines, add new features
4. **Run each step file** to see how the program builds up gradually

### For Reference
- Use these as templates for similar problems
- Study the code organization and commenting
- Note the variable naming and structure
- See how concepts build upon each other

## Running the Programs

All programs can be run from the command line:

```bash
python news_analysis.py
python step_01_setup.py
python step_02_count.py
python step_03_search.py
python step_04_complete.py
```

## Key Concepts Demonstrated

- **Lists**: Creating, populating, and accessing list elements
- **Loops**: Using `for` loops to iterate through lists
- **String Methods**: Using `.split()` and `.lower()` methods
- **User Input**: Getting and processing user search terms
- **Conditional Logic**: Using `if` statements for searching
- **String Operations**: Case-insensitive matching and string containment
- **Basic Statistics**: Counting and calculating averages

## Concepts Used (Lab 4 Appropriate)

These solutions use concepts covered in Lab 4:
- List creation and manipulation
- `for` loops with lists
- String methods (`.split()`, `.lower()`)
- `in` operator for string containment
- Basic arithmetic operations
- User input with `input()`
- String formatting with f-strings

## Sample Output

When you run the complete program, you'll see:

```
============================================================
BBC NEWS HEADLINES ANALYSIS
============================================================
There are 10 headlines in the list.
The average headline length is 8.2 words.

----------------------------------------
What topic would you like to search for? NHS

Headlines containing 'NHS':
----------------------------------------
• Government announces new funding for NHS

Found 1 headline(s) containing 'NHS'.
```

## Next Steps

After completing this lab, you should be comfortable with:
- Creating and working with lists of data
- Looping through collections to perform operations
- Processing text data with string methods
- Building interactive programs that search through data
- Calculating basic statistics from collections

Move on to Lab 5: Advanced Container Operations to learn about more complex data structures!

---

**Remember**: These solutions are for learning and reference. Always try to solve problems yourself first!
