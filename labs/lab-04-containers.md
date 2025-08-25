# Lab 4: Analyzing News Headlines

The aim of this lab is to get comfortable working with lists, one of the most common data structures in Python. We'll use a list of BBC News headlines to perform some simple, real-world text analysis.

This lab is made up of 4 steps:
1. Start with a list of headlines
2. Count the headlines
3. Calculate the average headline length
4. Find the most common topics

---

## Step 1: Create a New File

**Your Task:** Set up your workspace for the news analysis lab.

**What to do:**
1. Create a new Python file called `news_analysis.py`
2. Think about what you'll need to import (hint: you probably don't need any special imports for this lab)

**Expected outcome:**
- You should have an empty Python file ready to work with
- The file should be named appropriately for this lab

---

## Step 2: Start with a list of headlines

**Your Task:** Create a list of news headlines to work with.

**What to do:**
1. Create a variable called `headlines`
2. Add at least 8-10 news headlines to your list
3. Make sure each headline is a string (enclosed in quotes)
4. Use headlines about different topics (politics, sports, technology, etc.)

**Hints:**
- Remember that lists use square brackets `[]`
- Each headline should be a separate string
- You can copy headlines from real news sources or make them up
- Include a variety of topics to make your analysis interesting

**Expected outcome:**
- You should have a list with multiple news headlines
- Each headline should be a realistic news title
- The list should contain different types of news

**Check your work:**
- Does your list have the right number of headlines?
- Are all the headlines properly formatted as strings?
- Do you have a good variety of topics?

<details>
<summary>Possible list</summary>

```python
headlines = [
    "General election: Labour and Tories clash over tax",
    "England crowned T20 world champions",
    "Summer travel chaos feared as airline strikes loom",
    "UK inflation rate falls to lowest level in three years",
    "New David Hockney exhibition opens in London",
    "Science discovers new way to tackle plastic waste",
    "Government announces new funding for NHS",
    "Stock market hits record high on tech boom",
    "Debate rages over future of Artificial Intelligence",
    "Classic Doctor Who episodes to be released in colour"
]
```
</details>

---

## Step 3: Count the Headlines and Average Length

**Your Task:** Analyze basic statistics about your headlines.

**What to do:**
1. Count how many headlines you have in your list
2. Calculate the average number of words per headline
3. Display both results in a user-friendly format

**Hints:**
- Think about what function tells you how many items are in a list
- To count words, you'll need to loop through each headline
- The `.split()` method can help you break a string into words
- Remember to initialize a counter variable before your loop

**Expected outcome:**
- Your program should tell you how many headlines there are
- It should calculate and display the average word count
- The output should be clear and readable

**Check your work:**
- Does the headline count match what you expect?
- Is the average word count reasonable?
- Are your results displayed clearly?

---

## Step 4: Find the most common topics

**Your Task:** Create a search function to find headlines about specific topics.

**What to do:**
1. Ask the user what topic they want to search for
2. Look through all headlines to find matches
3. Count how many headlines mention that topic
4. Display the matching headlines and the final count

**Hints:**
- Use the `input()` function to get the search term from the user
- You'll need another loop to check each headline
- Think about how to check if one string contains another
- Consider making your search case-insensitive for better results
- Keep track of how many matches you find

**Expected outcome:**
- Users should be able to search for any topic
- The program should find and display matching headlines
- It should show the total count of matches
- The search should work regardless of capitalization

**Check your work:**
- Try searching for different topics (some common, some rare)
- Does the search find the right headlines?
- Does it handle capitalization correctly?
- Are the results displayed clearly?

---

## Putting It All Together

**Final Challenge:** Make sure all parts work together smoothly.

**What to do:**
1. Test your complete program with different search terms
2. Make sure all the statistics are calculated correctly
3. Verify that the output is clear and professional
4. Consider adding some formatting to make results easier to read

**Hints:**
- Test with topics you know are in your headlines
- Test with topics that aren't in your headlines
- Make sure your average calculation is mathematically correct
- Consider adding some visual separation between different sections

---

## Checks for Understanding

Before moving to the next lab, make sure you can answer these questions:

### Basic Concepts:
- [ ] Can you explain how lists work in Python?
- [ ] Do you understand how to loop through a list?
- [ ] Can you explain what the `.split()` method does?
- [ ] Do you know how to check if one string contains another?

### Practical Skills:
- [ ] Can you create and populate a list with data?
- [ ] Can you calculate statistics from list data?
- [ ] Can you search through a list for specific content?
- [ ] Can you handle user input and provide meaningful output?

### If you answered "No" to any questions:
- Review the relevant sections above
- Check the solutions folder for complete code examples
- Ask for help if needed

---

## Common Issues and Solutions

### Problem: "NameError: name 'headlines' is not defined"
**Solution:** Make sure you've created your headlines list before trying to use it.

### Problem: Average calculation gives 0 or wrong results
**Solution:** Check that you're initializing your counter variable to 0 before the loop.

### Problem: Search doesn't find obvious matches
**Solution:** Make sure you're using `.lower()` on both the headline and search term.

### Problem: Program crashes when searching
**Solution:** Make sure you're properly handling the case where no matches are found.

---

## What's Next?

In the next lab, you'll learn about:
- More advanced list operations
- Working with other container types (tuples, sets)
- List comprehensions and advanced data processing

**Ready to continue?** Move on to Lab 5: Advanced Container Operations!

---

## Solutions

**Complete code examples for all exercises are available in the `solutions/` folder.**

- `solutions/news_analysis.py` - Complete news analysis solution
- `solutions/step_by_step/` - Individual step solutions

**Try to solve the exercises yourself first, then check the solutions if you get stuck!**

---

## Questions?

If you get stuck or have questions:
1. Check the error messages carefully
2. Review the concepts in the notes
3. Look at the solutions folder for examples
4. Ask for help from your instructor or classmates
5. Remember: everyone learns at their own pace! 