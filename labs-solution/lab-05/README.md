# Lab 5: Building a Headline Analysis Toolkit with Functions - Solutions

This folder contains complete solutions for all exercises in Lab 5: Building a Headline Analysis Toolkit with Functions.

## Files Overview

### Complete Solution

1. **`headline_analyzer.py`** - Complete working headline analyzer program
   - Demonstrates all functions from the lab
   - Includes additional helper functions and main program
   - Ready to run and analyze headlines

### Step-by-Step Solutions

2. **`step_01_setup.py`** - Step 1: Basic setup and headlines data
   - Shows how to set up the workspace
   - Demonstrates loading and verifying headline data
   - Basic file structure

3. **`step_02_word_count.py`** - Step 2: Implementing the word count function
   - Shows basic function definition with parameters
   - Demonstrates return values
   - Includes function testing

4. **`step_03_search.py`** - Step 3: Implementing the search function
   - Shows function with multiple parameters
   - Demonstrates returning lists
   - Shows case-insensitive searching

5. **`step_04_analysis.py`** - Step 4: Implementing the main analysis function
   - Shows calling functions from within other functions
   - Demonstrates function integration
   - Shows how to orchestrate multiple functions

## How to Use These Solutions

### For Learning
1. **Try the lab exercises yourself first** - don't peek at solutions until you're stuck!
2. **Compare your code** with the solutions to see different approaches
3. **Experiment** with the code - modify functions, add new parameters
4. **Run each step file** to see how functions build up gradually

### For Reference
- Use these as templates for similar function-writing problems
- Study the function structure and parameter usage
- Note the docstring documentation and commenting
- See how functions can work together

## Running the Programs

All programs can be run from the command line:

```bash
python headline_analyzer.py
python step_01_setup.py
python step_02_word_count.py
python step_03_search.py
python step_04_analysis.py
```

## Key Concepts Demonstrated

- **Function Definition**: Using `def` to create functions
- **Parameters**: Functions that take input arguments
- **Return Values**: Functions that send data back
- **Function Calls**: Using functions from within other functions
- **Documentation**: Docstrings explaining function purpose
- **Code Organization**: Breaking programs into logical functions

## Concepts Used (Lab 5 Appropriate)

These solutions use concepts covered in Lab 5:
- Function definition with `def`
- Function parameters and arguments
- Return statements
- Calling functions
- Basic string operations (`.split()`, `.lower()`)
- List operations and loops
- Basic arithmetic and calculations

## Sample Output

When you run the complete program, you'll see:

```
Welcome to the Headline Analysis Toolkit!
This program demonstrates functions for analyzing news headlines.
==================================================
HEADLINE ANALYSIS RESULTS
==================================================
Total headlines analyzed: 10
Total words across all headlines: 82
Average words per headline: 8.2
==================================================

Searching for 'new':
------------------------------
Found 1 headline(s):
  • New David Hockney exhibition opens in London
```

## Function Examples

### Basic Function (Step 2)
```python
def get_word_count(headline_text):
    words = headline_text.split()
    return len(words)
```

### Function with Multiple Parameters (Step 3)
```python
def find_headlines_with_keyword(list_of_headlines, keyword):
    matching_headlines = []
    for headline in list_of_headlines:
        if keyword.lower() in headline.lower():
            matching_headlines.append(headline)
    return matching_headlines
```

### Function Calling Other Functions (Step 4)
```python
def analyse_all_headlines(list_of_headlines):
    total_words = 0
    for headline in list_of_headlines:
        word_count = get_word_count(headline)  # Calling another function
        total_words += word_count
    # ... rest of function
```

## Next Steps

After completing this lab, you should be comfortable with:
- Writing functions that take parameters
- Writing functions that return values
- Calling functions from within other functions
- Organizing code into logical, reusable pieces
- Documenting functions with docstrings

Move on to Lab 6: Advanced Functions to learn about more complex function features!

---

**Remember**: These solutions are for learning and reference. Always try to solve problems yourself first!
