# Lab 6: Supercharging Analysis with List Comprehensions

### **Objective**
The aim of this lab is to use **list comprehensions** to perform powerful data manipulation on the headlines list in a single, readable line of code. This is a very common and powerful technique in Python.

---

## **What are List Comprehensions?**
A **list comprehension** is a concise way to create lists by applying operations to existing data. Think of it as a "for loop in one line" that's both readable and efficient.

### **Key Concepts**
- **Mapping**: Transform each item in a list
- **Filtering**: Select only items that meet certain criteria
- **Combining**: Map and filter in a single expression
- **Readability**: Write complex operations in clear, single lines

---

## **Step 1: Getting Started**

### **Tasks**
1. Create a new Python file, e.g., `comprehensions_analysis.py`
2. Set up your workspace with the headlines data
3. Verify that your data is loaded correctly

### **Expected Outcomes**
- You should have a working Python file
- The headlines list should be loaded and accessible
- You should be able to print the headlines to verify they're loaded

### **Check Your Work**
- Can you print the headlines list?
- Does it contain all 10 headlines?
- Is your file ready for the next steps?

---

## **Step 2: Mapping with List Comprehensions**

A list comprehension is a great way to create a new list by applying an operation to every item in an existing list.

### **Tasks**
1. Create a new list called `headline_lengths` that contains the word count for each headline
2. Use a list comprehension to transform the data
3. Print the result to verify your work

### **Hints**
- The basic syntax is `[expression for item in list]`
- Your `expression` will involve calling `.split()` and `len()` on each `item`
- The `item` in your case is each `headline` in the `headlines` list
- Think about what operation you want to apply to each headline
- Consider how to count words in a string

### **Expected Outcomes**
- `headline_lengths` should be a list of numbers
- Each number should represent the word count of the corresponding headline
- The list should have the same length as your headlines list
- First headline should have 8 words, second should have 4 words, etc.

### **Check Your Work**
- Does your list have 10 numbers?
- Is the first number 8 (for "General election: Labour and Tories clash over tax")?
- Is the second number 4 (for "England crowned T20 world champions")?
- Can you verify a few more word counts manually?

---

## **Step 3: Filtering with List Comprehensions**

Now, let's use a list comprehension to select only the items that meet a certain criteria.

### **Tasks**
1. Create a new list called `short_headlines` that contains only the headlines with 7 words or fewer
2. Use a list comprehension with a condition to filter the data
3. Print the result to verify your work

### **Hints**
- The syntax for filtering is `[item for item in list if condition]`
- Your `condition` will check the word count of each `headline`
- Remember to use `.split()` and `len()` as part of your `if condition`
- Think about what makes a headline "short" (7 words or fewer)
- Consider how to combine the word counting with the filtering condition

### **Expected Outcomes**
- `short_headlines` should be a list of strings (the actual headlines)
- Only headlines with 7 words or fewer should be included
- The list should be shorter than your original headlines list
- You should see headlines like "England crowned T20 world champions" (4 words)

### **Check Your Work**
- Is your filtered list shorter than the original?
- Do all headlines in the result have 7 words or fewer?
- Can you manually count words to verify the filtering worked?
- Are you getting the expected headlines?

---

## **Step 4: Combining Mapping and Filtering**

This is where list comprehensions really shine. You can filter a list and transform the results in a single, elegant line.

### **Tasks**
1. Create a list called `specific_headline_lengths` that contains the word counts of only those headlines that include the word "new"
2. Combine filtering and mapping in a single list comprehension
3. Print the result to verify your work

### **Hints**
- You'll use the combined syntax: `[expression for item in list if condition]`
- Your `expression` will get the word count of the `item` (the headline)
- Your `if condition` will check if the word "new" is in the `item`
- Remember to use `.lower()` to make your check case-insensitive
- Think about the order: filter first, then map the results

### **Expected Outcomes**
- `specific_headline_lengths` should be a list of numbers (word counts)
- Only headlines containing "new" should contribute to this list
- The list should be shorter than your original headlines list
- You should get word counts for headlines like "New David Hockney exhibition opens in London"

### **Check Your Work**
- Is your result list shorter than the original headlines?
- Do all the word counts correspond to headlines with "new"?
- Can you manually verify which headlines contain "new"?
- Are you getting the expected word counts?

---

## **Common Issues to Watch Out For**

### **Syntax Errors**
- **Missing brackets**: List comprehensions must be enclosed in `[]`
- **Wrong order**: Remember it's `[expression for item in list if condition]`
- **Missing colons**: Don't forget the `:` after `for` and `if`
- **Indentation**: List comprehensions should be on one line or properly indented

### **Logic Errors**
- **Case sensitivity**: Remember to use `.lower()` for case-insensitive searches
- **Word counting**: Make sure you're splitting on whitespace correctly
- **Filtering conditions**: Double-check your comparison operators
- **Empty results**: If you get an empty list, check your filtering condition

### **Performance Considerations**
- **Large lists**: List comprehensions are efficient but can use memory
- **Complex expressions**: Keep expressions readable and simple
- **Nested comprehensions**: Avoid going too deep for readability

---

## **Testing Your Solutions**

### **Test Data Verification**
Make sure your headlines list contains exactly these 10 headlines:
1. "General election: Labour and Tories clash over tax" (8 words)
2. "England crowned T20 world champions" (4 words)
3. "Summer travel chaos feared as airline strikes loom" (8 words)
4. "UK inflation rate falls to lowest level in three years" (10 words)
5. "New David Hockney exhibition opens in London" (7 words)
6. "Science discovers new way to tackle plastic waste" (8 words)
7. "Government announces new funding for NHS" (6 words)
8. "Stock market hits record high on tech boom" (8 words)
9. "Debate rages over future of Artificial Intelligence" (7 words)
10. "Classic Doctor Who episodes to be released in colour" (9 words)

### **Expected Results**
- **Step 2**: `[8, 4, 8, 10, 7, 8, 6, 8, 7, 9]`
- **Step 3**: Headlines with ≤7 words: 4, 7, 6, 7
- **Step 4**: Word counts of headlines with "new": 7, 8, 6

---

## **Extension Ideas (Optional)**

### **More Complex Comprehensions**
- Find headlines that start with specific letters
- Create a list of headline lengths for headlines containing multiple keywords
- Filter by word count ranges (e.g., 5-8 words)

### **Advanced Filtering**
- Find headlines that contain numbers
- Select headlines that end with specific punctuation
- Filter by multiple conditions (e.g., contains "new" AND has ≤8 words)

### **Data Analysis**
- Calculate the average word count of filtered headlines
- Find the longest and shortest headlines
- Create a frequency count of headline lengths

---

## **Solutions**

**Complete code examples for all exercises are available in the `solutions/lab-06` folder.**

- `solutions/comprehensions_analysis.py` - Complete solution with all steps

---

## **Why List Comprehensions?**

List comprehensions are powerful because they:
- **Improve readability** - Complex operations in single lines
- **Boost performance** - Often faster than equivalent loops
- **Reduce code** - Less verbose than traditional for loops
- **Express intent** - Clear what you're trying to accomplish
- **Follow Python style** - Considered "Pythonic" code

---

**Remember**: 
- Start with simple comprehensions and build complexity
- Always test with small examples first
- Keep expressions readable and simple
- Practice combining mapping and filtering
- List comprehensions are a fundamental Python skill

This lab introduces you to one of Python's most powerful and commonly used features! 