# **Lab 2: Extended Exploration of Types**

## **Objective**
This lab extends the concepts covered in Lab 2 by exploring additional built-in methods for strings and numbers, and introducing some practical applications of what you've learned.

This lab consists of **three steps**:
1. **Exploring Basic String Methods**
2. **Exploring Number Properties**
3. **Practical Type Applications**

---

## **Step 1: Exploring Basic String Methods**

**Your Task:** Create a program that gets a string from the user and explores different ways to work with it.

**What to do:**
1. Ask the user to enter a sentence or word
2. Store their input in a variable
3. Try to display the string in different ways:
   - Show the original string
   - Convert it to uppercase
   - Convert it to lowercase
   - Find out how many characters it has
   - Show the first character
   - Show the last character

**Hints:**
- Remember that strings can be accessed by position using square brackets
- The first character is at position 0
- You can use negative numbers to count from the end (-1 is the last character)
- Look up the `.upper()` and `.lower()` methods in your notes

**Expected output example:**
```
Enter a sentence: Hello World
Original string: Hello World
Uppercase: HELLO WORLD
Lowercase: hello world
Length: 11
First character: H
Last character: d
```

**Check your work:**
- Try different types of input (short words, long sentences)
- What happens if you try to access position 5 in a short word?
- Experiment with accessing characters using different positions

---

## **Step 2: Exploring Number Properties**

**Your Task:** Extend your number calculator to explore more number properties.

**What to do:**
1. Ask the user for a decimal number
2. Store it as a float
3. Try these operations:
   - Round the number to 2 decimal places
   - Check if it's a whole number
   - Multiply it by 2
   - Divide it by 2

**Hints:**
- Use the `round()` function to round numbers
- Think about how to check if a number is whole (compare it to its integer version)
- Remember that division always gives you a float result

**Expected output example:**
```
Enter a decimal number: 5.7
Original number: 5.7
Rounded to 2 decimal places: 5.7
Is it a whole number? False
Number multiplied by 2: 11.4
Number divided by 2: 2.85
```

**Check your work:**
- Try whole numbers (like 5) and decimal numbers (like 5.7)
- What happens when you divide by zero?
- Try very large numbers and very small numbers

---

## **Step 3: Practical Type Applications**

**Your Task:** Create a program that collects user information and performs calculations.

**What to do:**
1. Ask the user for their first name, last name, and age
2. Store each piece of information in separate variables
3. Convert the age to a number
4. Calculate:
   - Their full name (combine first and last)
   - Approximate birth year (assume current year is 2024)
   - Age in months
5. Display all the information in a nice format

**Hints:**
- Remember to convert the age input to an integer
- You can combine strings using the `+` operator
- Think about the math: if someone is 25 in 2024, they were born around 1999
- There are 12 months in a year

**Expected output example:**
```
Enter your first name: John
Enter your last name: Smith
Enter your age: 25
Hello John Smith!
You are 25 years old.
You were born around 1999.
You are approximately 300 months old.
```

**Check your work:**
- Test with different ages
- What happens if you enter a very large age?
- Try entering the age as text instead of numbers

---

## **Optional Challenge**

If you're feeling confident, try this:
- Ask the user for a word
- Check if it's a palindrome (reads the same forwards and backwards)
- Use string indexing and comparison to check this

**Hints:**
- Think about how to compare the first and last characters
- You might need to check multiple positions
- Remember that "racecar" is a palindrome

---

## **What You've Learned**

By completing this extension, you've practiced:
- Basic string methods and indexing
- Number operations and properties
- Combining multiple input types
- Creating practical applications
- Basic conditional logic (if statements)

## **Is This Extension Necessary?**

This extension is **optional** and designed for students who want to explore more after completing the basic lab. The concepts here will be covered more thoroughly in later labs, so don't worry if some parts seem challenging.

**Focus on the basic lab first** - make sure you're comfortable with:
- Getting user input
- Converting between types
- Basic string operations
- Understanding the `None` value

Only attempt this extension if you've completed the main lab successfully and want to explore further!
