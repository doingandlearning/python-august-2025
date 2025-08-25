# Lab 4: Extended Exploration of Containers

## **Objective**
This lab extends the concepts covered in Lab 4 by exploring additional list operations, introducing basic data structures, and building more complex analysis tools. This extension is designed for students who want to explore further after completing the basic lab.

This lab consists of **four sections**:
1. **List & String Processing Extensions**
2. **Introducing Data Structures**
3. **Logic and Searching**
4. **Stretch Challenge**

---

## **Section 1: List & String Processing Extensions**

### **Extension 1: Sort headlines by length**

**Your Task:** Organize your headlines by their length to find patterns.

**What to do:**
1. Create a way to sort your headlines by the number of words they contain
2. Display the top 3 longest headlines
3. Display the top 3 shortest headlines

**Hints:**
- Think about how to get the length of each headline
- You might need to create a new list with length information
- Consider using the `sorted()` function or `.sort()` method
- Remember that you can sort by different criteria

**Expected outcome:**
- Your program should show the longest and shortest headlines
- The output should be clearly organized and easy to read

**Check your work:**
- Are the headlines actually sorted by length?
- Do you have exactly 3 longest and 3 shortest?
- Is the output clear and readable?

---

### **Extension 2: Count total characters**

**Your Task:** Calculate the total number of characters across all headlines.

**What to do:**
1. Count the total characters (including spaces and punctuation) in all headlines
2. Display this information alongside your word count
3. Calculate the average characters per headline

**Hints:**
- Think about how to count characters in a string
- You'll need to loop through each headline
- Consider what the difference is between characters and words

**Expected outcome:**
- Total character count for all headlines
- Average characters per headline
- Comparison with your word count statistics

---

### **Extension 3: Find headlines that are questions**

**Your Task:** Identify headlines that end with question marks.

**What to do:**
1. Look through all headlines to find ones that end with `?`
2. Count how many question headlines you have
3. Display all the question headlines

**Hints:**
- Think about how to check if a string ends with a specific character
- You might want to create a separate list for question headlines
- Consider what to do if there are no question headlines

**Expected outcome:**
- List of all headlines that are questions
- Count of question headlines
- Clear indication if there are no questions

---

### **Extension 4: Capitalize all headlines uniformly**

**Your Task:** Apply consistent formatting to all headlines.

**What to do:**
1. Convert all headlines to title case (first letter of each word capitalized)
2. Display both the original and formatted versions
3. Consider if this changes the meaning of any headlines

**Hints:**
- Look up the `.title()` method for strings
- Think about whether you want to modify the original list or create a new one
- Consider what happens to acronyms like "NHS" or "AI"

**Expected outcome:**
- All headlines in consistent title case format
- Comparison between original and formatted versions
- Understanding of how formatting affects readability

---

## **Section 2: Introducing Data Structures**

### **Extension 5: Create a dictionary of headline lengths**

**Your Task:** Build a dictionary that maps headlines to their word counts.

**What to do:**
1. Create a dictionary where each headline is a key
2. The value should be the number of words in that headline
3. Display the dictionary in a readable format

**Hints:**
- Think about how dictionaries work (key-value pairs)
- You'll need to loop through your headlines list
- Consider how to make the output readable

**Expected outcome:**
- Dictionary with headlines as keys and word counts as values
- Clear display of the dictionary contents
- Understanding of how dictionaries organize data

**Check your work:**
- Does each headline have a corresponding word count?
- Are the word counts correct?
- Is the output easy to understand?

---

### **Extension 6: Group headlines by first word**

**Your Task:** Organize headlines by their first word to see topic patterns.

**What to do:**
1. Look at the first word of each headline
2. Group headlines that start with the same word
3. Display the groups in an organized way

**Hints:**
- Think about how to get the first word of a headline
- You might want to use a dictionary to group them
- Consider what to do with headlines that start with the same word

**Expected outcome:**
- Headlines grouped by their first word
- Clear organization showing each group
- Understanding of how headlines are structured

---

## **Section 3: Logic and Searching**

### **Extension 7: Support multiple search terms**

**Your Task:** Allow users to search for multiple topics at once.

**What to do:**
1. Ask the user to enter multiple search terms separated by commas
2. Split their input into individual search terms
3. Search for each term and display results

**Hints:**
- Think about how to split a string into multiple parts
- You'll need to handle each search term separately
- Consider how to organize the results clearly

**Expected outcome:**
- Users can enter multiple search terms
- Results are organized by search term
- Clear indication of which terms found matches

---

### **Extension 8: Highlight the search term in the headline**

**Your Task:** Make search results more visual by highlighting matches.

**What to do:**
1. When displaying matching headlines, highlight the search term
2. You could use ALL CAPS, asterisks, or other highlighting
3. Make sure the highlighting is clear and readable

**Hints:**
- Think about how to replace or modify text in a string
- Consider different ways to highlight text
- Make sure the highlighting doesn't make text hard to read

**Expected outcome:**
- Search terms are clearly highlighted in results
- Highlighting makes it easy to see matches
- Output remains readable and professional

---

## **Section 4: Stretch Challenge**

### **Extension 9: Build a simple frequency counter**

**Your Task:** Count how often each word appears across all headlines.

**What to do:**
1. Count the frequency of every word in all headlines
2. Store the results in a dictionary
3. Display the top 5 most frequent words

**Hints:**
- You'll need to split each headline into words
- Think about how to handle capitalization and punctuation
- Consider what to do with very common words like "the" or "and"

**Expected outcome:**
- Dictionary showing word frequencies
- Top 5 most common words displayed
- Understanding of which words appear most often

---

## **What You've Learned**

By completing these extensions, you've practiced:
- Advanced list operations and sorting
- Working with dictionaries and data organization
- Complex string processing and manipulation
- Building more sophisticated search tools
- Data analysis and pattern recognition

## **Is This Extension Necessary?**

This extension is **completely optional** and designed for students who want to explore more after completing the basic lab. The concepts here will be covered more thoroughly in later labs, so don't worry if some parts seem challenging.

**Focus on the basic lab first** - make sure you're comfortable with:
- Creating and working with lists
- Basic loops and string operations
- Simple search functionality
- Basic statistics calculations

Only attempt these extensions if you've completed the main lab successfully and want to explore further!

---

## **Tips for Success**

1. **Start simple** - don't try to implement everything at once
2. **Test each extension** individually before moving to the next
3. **Experiment** with different approaches
4. **Ask for help** if you get stuck on any particular concept
5. **Remember** - these are advanced concepts, so don't get discouraged!

---

## **Next Steps**

After completing these extensions, you'll be ready for:
- More advanced data structures (sets, tuples)
- List comprehensions and advanced list operations
- File handling and data persistence
- More complex data analysis projects

**Ready to continue?** Move on to Lab 5: Advanced Container Operations!
