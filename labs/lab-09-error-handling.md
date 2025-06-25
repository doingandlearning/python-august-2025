# Lab 9: Error Handling

Even a perfect program can crash if it receives unexpected input. Error handling is the process of anticipating these situations and dealing with them gracefully instead of letting the program crash.

The aim of this lab is to make our "Channel Guessing Game" more robust by using a `try...except` block to handle invalid user input.

This lab is made up of 2 steps:

1.  Identify the problem by running the guessing game and causing a `ValueError`.
2.  Add a `try...except` block to catch the error and print a friendly message.

---

## Step 1: Find the Bug

First, we need to understand the problem.

**Your goal:** Run your "Channel Guessing Game" from Lab 3 and make it crash.

**Hints:**

- Get a working copy of your guessing game solution.
- Run the script.
- When it prompts you to "Please guess a channel number:", type a word like "five" instead of the number `5`, and press Enter.
- Observe the error. You should see a `ValueError` message, and the program will stop. This happens because the `int()` function doesn't know how to convert the string "five" into a number.

---

## Step 2: Implement the `try...except` Block

Now we will fix the bug. We will "try" to convert the user's input to an integer, and if it fails, we will "except" the `ValueError` and handle it.

**Your goal:** Wrap the risky code in a `try` block and add an `except` block to handle the `ValueError`.

**Hints:**

- In your guessing game's `for` loop, find this line:
  `guess = int(input("Please guess a channel number: "))`
- This line is risky because `input()` could be anything. Put it inside a `try` block:
  ```python
  try:
      guess_str = input("Please guess a channel number: ")
      guess = int(guess_str)
  except ValueError:
      # This code runs ONLY if a ValueError occurs
      print("That's not a valid number! Please try again.")
      continue # This keyword skips to the next iteration of the loop
  ```
- Notice the use of the `continue` keyword. When we catch an error, we don't want to proceed to the `if/elif/else` block that checks if the guess is too high or low. `continue` tells the `for` loop to immediately end the current iteration and start the next one.
- Now, run your game again. Try entering words, symbols, and numbers. The game should no longer crash. It should print your helpful message and then continue the loop, giving the user another chance.

## Stretch tasks (optional)

1. Handle range errors
   Raise your own ValueError if a user enters a number outside 1-50.

2. Create a helper function
   Move the prompting code into def get_guess(): …

3. Custom exception
   Define class ChannelError(Exception): pass and raise ChannelError("Out of range") to practise user-defined exceptions.
