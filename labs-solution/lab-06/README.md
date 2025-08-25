# Lab 6: Supercharging Analysis with List Comprehensions - Solutions

This folder contains complete solutions for Lab 6: Supercharging Analysis with List Comprehensions. These solutions demonstrate how to use list comprehensions for powerful data manipulation.

## Files Overview

### Complete Solution

1. **`comprehensions_analysis.py`** - Complete working program with all list comprehension techniques
   - Demonstrates all steps from the lab
   - Includes additional analysis and examples
   - Ready to run and explore list comprehensions

### Step-by-Step Solutions

2. **`step_01_setup.py`** - Step 1: Basic setup and headlines data
   - Shows how to set up the workspace
   - Demonstrates loading and verifying headline data
   - Basic file structure and data access

3. **`step_02_mapping.py`** - Step 2: Mapping with list comprehensions
   - Shows how to transform data using list comprehensions
   - Demonstrates word counting for headlines
   - Includes verification and breakdown of the syntax

4. **`step_03_filtering.py`** - Step 3: Filtering with list comprehensions
   - Shows how to select data using list comprehensions
   - Demonstrates filtering headlines by word count
   - Includes additional filtering examples

5. **`step_04_combining.py`** - Step 4: Combining mapping and filtering
   - Shows how to combine both operations in one comprehension
   - Demonstrates complex data transformations
   - Includes statistics and additional examples

## How to Use These Solutions

### For Learning
1. **Try the lab exercises yourself first** - don't peek at solutions until you're stuck!
2. **Compare your code** with the solutions to see different approaches
3. **Experiment** with the code - modify comprehensions, add new conditions
4. **Run each step file** to see how list comprehensions build up gradually

### For Reference
- Use these as templates for similar list comprehension problems
- Study the syntax structure and pattern usage
- Note the docstring documentation and commenting
- See how different types of comprehensions work

## Running the Programs

All programs can be run from the command line:

```bash
python comprehensions_analysis.py
python step_01_setup.py
python step_02_mapping.py
python step_03_filtering.py
python step_04_combining.py
```

## Key Concepts Demonstrated

### **List Comprehension Fundamentals**
- **Mapping**: Transform each item in a list
- **Filtering**: Select only items that meet criteria
- **Combining**: Map and filter in a single expression
- **Syntax**: Understanding the structure and components

### **List Comprehension Patterns**
- **Basic mapping**: `[expression for item in list]`
- **Basic filtering**: `[item for item in list if condition]`
- **Combined operations**: `[expression for item in list if condition]`
- **Complex expressions**: Multiple operations in the expression part

### **Data Processing Techniques**
- **String operations**: `.split()`, `.lower()`, `.startswith()`, `.endswith()`
- **Conditional logic**: `if` statements within comprehensions
- **Nested operations**: Combining multiple string methods
- **Data transformation**: Converting between data types

## Concepts Used (Lab 6 Appropriate)

These solutions use concepts appropriate for Lab 6:
- List comprehensions (the main focus)
- String methods and operations
- Basic list operations and indexing
- Conditional statements (`if`)
- Function calls (`len()`, `split()`)
- Basic arithmetic and comparisons

## Sample Output

When you run the complete program, you'll see:

```
Lab 6: List Comprehensions Analysis
==================================================

Step 2: Mapping with List Comprehensions
----------------------------------------
Headline lengths (word counts):
 1. ( 8 words) General election: Labour and Tories clash over tax
 2. ( 4 words) England crowned T20 world champions
 3. ( 8 words) Summer travel chaos feared as airline strikes loom
...

All headline lengths: [8, 4, 8, 10, 7, 8, 6, 8, 7, 9]

Step 3: Filtering with List Comprehensions
------------------------------------------
Headlines with 7 words or fewer:
1. (4 words) England crowned T20 world champions
2. (7 words) New David Hockney exhibition opens in London
3. (6 words) Government announces new funding for NHS
4. (7 words) Debate rages over future of Artificial Intelligence

Step 4: Combining Mapping and Filtering
---------------------------------------
Word counts of headlines containing 'new':
• 'New David Hockney exhibition opens in London' -> 7 words
• 'Science discovers new way to tackle plastic waste' -> 8 words
• 'Government announces new funding for NHS' -> 6 words

All word counts for 'new' headlines: [7, 8, 6]
```

## List Comprehension Examples

### Basic Mapping (Step 2)
```python
headline_lengths = [len(headline.split()) for headline in headlines]
```

### Basic Filtering (Step 3)
```python
short_headlines = [headline for headline in headlines if len(headline.split()) <= 7]
```

### Combined Operations (Step 4)
```python
specific_headline_lengths = [len(headline.split()) for headline in headlines if "new" in headline.lower()]
```

## Understanding List Comprehensions

### **The Syntax Structure**
List comprehensions follow this pattern:
```python
[expression for item in iterable if condition]
```

- **Expression**: What you want to create/transform
- **For loop**: Iterate through the data
- **Condition**: Optional filter (only if needed)

### **When to Use List Comprehensions**
- **Simple transformations** of list items
- **Filtering** lists based on conditions
- **Combining** filtering and transformation
- **Creating new lists** from existing data
- **Replacing simple for loops** for readability

### **When NOT to Use List Comprehensions**
- **Complex logic** that's hard to read in one line
- **Multiple operations** that make the line too long
- **Nested comprehensions** that become confusing
- **Side effects** (like printing or modifying variables)

## Common List Comprehension Patterns

### **String Processing**
```python
# Convert to uppercase
upper_words = [word.upper() for word in words]

# Filter by length
long_words = [word for word in words if len(word) > 5]

# Transform and filter
long_upper_words = [word.upper() for word in words if len(word) > 5]
```

### **Number Processing**
```python
# Square numbers
squares = [x**2 for x in numbers]

# Filter even numbers
evens = [x for x in numbers if x % 2 == 0]

# Square only even numbers
even_squares = [x**2 for x in numbers if x % 2 == 0]
```

### **List Processing**
```python
# Get lengths
lengths = [len(item) for item in items]

# Filter by condition
valid_items = [item for item in items if item is not None]

# Transform and filter
valid_lengths = [len(item) for item in items if item is not None]
```

## Debugging List Comprehensions

### **Common Issues**
1. **Syntax errors**: Missing brackets, colons, or parentheses
2. **Logic errors**: Wrong conditions or expressions
3. **Empty results**: Overly restrictive filtering
4. **Performance issues**: Complex expressions or large data

### **Debugging Tips**
1. **Break it down**: Write the equivalent for loop first
2. **Test parts separately**: Test the expression and condition independently
3. **Use print statements**: Add debugging output to see what's happening
4. **Start simple**: Begin with basic comprehensions and add complexity

## Extension Ideas

### **More Complex Comprehensions**
- **Nested comprehensions**: Process nested data structures
- **Multiple conditions**: Use `and`/`or` in filtering
- **Complex expressions**: Combine multiple operations
- **Dictionary comprehensions**: Create dictionaries from data

### **Advanced Applications**
- **Data analysis**: Process CSV data, JSON responses
- **Text processing**: Analyze documents, extract information
- **API responses**: Transform API data into usable formats
- **Database results**: Process query results efficiently

## Next Steps

After completing this lab, you should be comfortable with:
- Writing basic list comprehensions for mapping
- Using list comprehensions for filtering
- Combining mapping and filtering in single comprehensions
- Choosing when to use comprehensions vs. loops
- Reading and understanding complex comprehensions

Move on to more advanced topics like:
- **Lab 7: Classes** for object-oriented programming
- **Lab 8: Modules** for code organization
- **Advanced Python** for more complex data processing
- **Data Science** for large-scale data manipulation

---

**Remember**: 
- List comprehensions are powerful but should remain readable
- Start simple and build complexity gradually
- Always test with small examples first
- Practice combining different operations
- List comprehensions are a fundamental Python skill

This lab introduces you to one of Python's most powerful and commonly used features for data manipulation!
