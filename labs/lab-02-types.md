# Lab 2: Types

The aim of this lab is to extend our hello world application to make it interactive and to handle different types of data.

This lab is comprised of 5 steps:
1. Make the application interactive
2. Input some numbers
3. Inputting some strings
4. Concatenating numbers and strings
5. Working with / Using the `None` value

---

## Step 1: Make the Application Interactive

**Your Task:** Modify your program to take user input as shown in the lecture slides.

**What to do:**
1. Create a new Python file called `interactive_hello.py`
2. Write a program that prints a welcome message
3. Ask the user for their name using the `input()` function
4. Store the user's input in a variable
5. Greet the user personally using their name

**Expected interaction:**
```
Hello World!
Please enter your name: John
Welcome John
```

**Key concepts to use:**
- `input()` function to get user input
- Variables to store the input
- `print()` function to display messages

**Hints:**
- Remember that `input()` always returns a string
- You can combine strings using the `+` operator
- Think about what message you want to display to the user

**Check your work:** Run the program and test it with different names. Does it work as expected?

---

## Step 2: Input Some Numbers

**Your Task:** Create a program that asks for two numbers and performs calculations.

**What to do:**
1. Create a new file called `number_calculator.py`
2. Ask the user for two numbers using `input()`
3. Convert the input strings to numbers using `int()` or `float()`
4. Add the two numbers together
5. Display the result to the user
6. Show the type of the result variable

**Important concept:** The `input()` function always returns a string, even when the user types numbers. You must convert strings to numbers before doing math.

**Key functions to use:**
- `int()` - converts to integer (whole numbers)
- `float()` - converts to decimal numbers
- `type()` - shows the type of a variable

**Expected output example:**
```
Please enter a number: 2
Please enter another number: 3
The result of 2 + 3 is 5
The type of the value is <class 'int'>
```

**Hints:**
- Use `int(input('prompt'))` to get and convert in one step
- Remember to handle the case where users might enter invalid input
- Think about what happens if you try to add a string and a number

**Check your work:** Test with different numbers. What happens if you enter letters instead of numbers?

---

## Step 3: Input Two Strings

**Your Task:** Create a program that works with string input and concatenation.

**What to do:**
1. Create a file called `string_explorer.py`
2. Ask the user to input two strings (e.g., first name and last name)
3. Use the `+` operator to concatenate the strings together
4. Display the combined result
5. Show the type of the concatenated value

**Key concepts to explore:**
- String concatenation using `+`
- How strings behave differently from numbers
- The `type()` function with strings

**Expected output example:**
```
Please enter a string: Hello
Please enter another string: World
The new value is HelloWorld
The type of the value is <class 'str'>
```

**Hints:**
- Think about spacing when concatenating strings
- Consider what happens if you concatenate multiple strings
- Experiment with different types of text input

**Check your work:** Does the concatenation work as expected? What type is the result?

---

## Step 4: Concatenate a Number and a String

**Your Task:** Explore what happens when you try to combine different data types.

**What to do:**
1. In your `string_explorer.py` file, add code to create a version number
2. Try to concatenate a string with a number directly
3. Use `str()` to convert the number to a string first
4. Compare the results

**Key concept:** Python cannot automatically concatenate strings and numbers. You must convert one type to match the other.

**What to test:**
1. Try: `'Data Processing App Version ' + 1.0` (this will cause an error)
2. Try: `'Data Processing App Version ' + str(1.0)` (this will work)
3. Understand why the first approach fails and the second succeeds

**Expected output:**
```
The title of this app is Data Processing App Version 1.0
```

**Hints:**
- The `str()` function converts numbers to strings
- Think about why Python can't automatically convert types
- Consider what other type conversion functions might be useful

**Check your work:** Does the concatenation work when you convert the number to a string? What error do you get if you don't convert?

---

## Step 5: Using `None`

**Your Task:** Explore the special `None` value and understand its purpose.

**What to do:**
1. In a new file called `none_explorer.py`, create a variable that holds the value `None`
2. Print the variable to see what it displays
3. Test whether the value is `None` using `is None`
4. Test whether the value is not `None` using `is not None`
5. Show the type of the `None` value

**Key concept:** `None` is a special value in Python that represents "nothing" or "no value." It's different from empty strings or zero.

**Expected output:**
```
user: None
user is None: True
user is not None: False
The type of the user: <class 'NoneType'>
```

**Hints:**
- Use `is` and `is not` to compare with `None` (not `==`)
- Think about when you might use `None` in a program
- Consider how `None` is different from other "empty" values

**Check your work:** Does your program correctly identify when a variable is `None`? What type does it show?

---

## Putting It All Together

**Final Challenge:** Create a comprehensive program that demonstrates all the concepts you've learned.

**What to do:**
1. Create a file called `types_demo.py`
2. Combine elements from all previous steps
3. Create an interactive program that:
   - Greets the user
   - Gets their name
   - Asks for two numbers and calculates their sum
   - Combines the name with a version number
   - Demonstrates the `None` value

**Make it your own:**
- Add your own creative touches
- Include helpful error messages
- Make the output look professional
- Test with various inputs

---

## Checks for Understanding

Before moving to the next lab, make sure you can answer these questions:

### Basic Concepts:
- [ ] Can you explain what the `input()` function does?
- [ ] Do you understand the difference between strings and numbers?
- [ ] Can you convert a string to a number using `int()` or `float()`?
- [ ] Do you know how to join strings together?

### Practical Skills:
- [ ] Can you create a program that asks for user input?
- [ ] Can you handle basic type conversion?
- [ ] Can you create a simple interactive program?
- [ ] Do you understand what happens when you try to add a string and a number?

### If you answered "No" to any questions:
- Review the relevant sections above
- Check the solutions folder for complete code examples
- Ask for help if needed

---

## Common Issues and Solutions

### Problem: "TypeError: can only concatenate str (not "int") to str"
**Solution:** Convert the number to a string first using `str(number)`

### Problem: "ValueError: invalid literal for int()"
**Solution:** The user entered something that's not a number. Add error handling.

### Problem: Program crashes when user enters invalid input
**Solution:** Use `try...except` blocks to handle errors gracefully.

---

## What's Next?

In the next lab, you'll learn about:
- Making decisions in your programs (if statements)
- Repeating actions (loops)
- More complex program flow

**Ready to continue?** Move on to Lab 3: Flow Control!

---

## Solutions

**Complete code examples for all exercises are available in the `solutions/` folder.**

- `solutions/interactive_hello.py` - Step 1 solution
- `solutions/number_calculator.py` - Step 2 solution  
- `solutions/string_explorer.py` - Steps 3-4 solution
- `solutions/none_explorer.py` - Step 5 solution
- `solutions/types_demo.py` - Complete combined solution

**Try to solve the exercises yourself first, then check the solutions if you get stuck!**

---

## Questions?

If you get stuck or have questions:
1. Check the error messages carefully
2. Review the concepts in the notes
3. Look at the solutions folder for examples
4. Ask for help from your instructor or classmates
5. Remember: everyone learns at their own pace!