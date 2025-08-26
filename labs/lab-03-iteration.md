# Lab 3: Iteration and Control Flow

The aim of this lab is to create a simple guessing game. This will give you practice with `while` or `for` loops, `if/elif/else` statements, and handling user input.

The logic of the game is:

- The program randomly selects a secret "channel number" between 1 and 50.
- The player has a fixed number of attempts to guess it.
- After each guess, the program tells the player if their guess was too high, too low, or correct.
- The game ends when the player guesses the number or runs out of attempts.

---

## Step 1: Setting up the Game

**Your Task:** Set up the basic structure for your guessing game.

**What to do:**

1. Create a new Python file for your game
2. Import the module you need for generating random numbers (`import random`)
3. Create a variable to store the secret channel number
4. Print a welcome message explaining the game rules

**Hints:**

- Look up how to generate a random integer between 1 and 50
- Make your welcome message clear and friendly
- Tell the player how many attempts they have

**Expected outcome:**

- Your program should generate a random number when it runs
- It should display a welcome message explaining the rules
- The secret number should be different each time you run the program

**Check your work:**

- Run the program multiple times - does the secret number change?
- Is your welcome message clear and helpful?
- Does the program run without errors?

---

## Step 2: The Game Loop

**Your Task:** Create a loop that gives the player multiple attempts to guess.

**What to do:**

1. Decide how many attempts the player should have
2. Create a loop that runs that many times
3. Think about what type of loop would work best for this

**Hints:**

- You know exactly how many attempts the player gets, so what type of loop makes sense?
- Remember that `range(5)` gives you numbers 0, 1, 2, 3, 4
- All the game logic will go inside this loop

**Expected outcome:**

- Your program should loop the correct number of times
- The loop should be ready to contain the guessing logic

**Check your work:**

- Does your loop run the right number of times?
- Is the loop structure clear and readable?

---

## Step 3: Getting and Checking the User's Guess

**Your Task:** Add the core game logic inside your loop.

**What to do:**

1. Ask the user for their guess inside the loop
2. Convert their input to a number
3. Compare their guess to the secret number
4. Give them appropriate feedback
5. Handle the case when they guess correctly

**Hints:**

- Remember that `input()` gives you a string - you need to convert it
- Think about the three possible outcomes: too low, too high, or correct
- What should happen when they guess correctly? How do you exit the loop early?
- Make your feedback messages helpful and encouraging

**Expected outcome:**

- Players should be able to input their guesses
- They should get clear feedback after each guess
- The game should end immediately if they guess correctly

**Check your work:**

- Try guessing too low, too high, and correctly
- Are your feedback messages clear and helpful?
- Does the game end when you guess correctly?

---

## Step 4: Handling a Win or Loss

**Your Task:** Determine the final outcome and display appropriate messages.

**What to do:**

1. Figure out how to tell if the player won or lost
2. Display different messages for winning vs. losing
3. If they lost, show them what the secret number was

**Hints:**

- Think about how you can track whether the player has won
- What happens if the loop finishes without a correct guess?
- How can you tell the difference between winning and losing?

**Expected outcome:**

- Winners should get a congratulatory message
- Losers should see what the secret number was
- The game should clearly indicate the final result

**Check your work:**

- Test both winning and losing scenarios
- Are the final messages clear and appropriate?
- Does the program handle both outcomes correctly?

---

## Putting It All Together

**Final Challenge:** Make sure all parts work together smoothly.

**What to do:**

1. Test your complete game multiple times
2. Try different strategies (guessing high, low, or in the middle)
3. Make sure the game works whether you win or lose
4. Add any finishing touches to make it more polished

**Hints:**

- Test edge cases (guessing 1, guessing 50, etc.)
- Make sure your messages are consistent and helpful
- Consider adding some personality to your game

---

## Checks for Understanding

Before moving to the next lab, make sure you can answer these questions:

### Basic Concepts:

- [ ] Can you explain how a `for` loop works?
- [ ] Do you understand the difference between `if`, `elif`, and `else`?
- [ ] Can you explain what the `break` statement does?
- [ ] Do you know how to generate random numbers?

### Practical Skills:

- [ ] Can you create a program that loops a specific number of times?
- [ ] Can you handle different user inputs and give appropriate responses?
- [ ] Can you create a program that tracks game state?
- [ ] Do you understand how to exit a loop early?

### If you answered "No" to any questions:

- Review the relevant sections above
- Check the solutions folder for complete code examples
- Ask for help if needed

---

## Common Issues and Solutions

### Problem: "NameError: name 'random' is not defined"

**Solution:** Make sure you've imported the random module at the top of your file.

### Problem: "ValueError: invalid literal for int()"

**Solution:** The user entered something that's not a number. Think about how to handle this gracefully.

### Problem: Game doesn't end when guessing correctly

**Solution:** Make sure you're using `break` when the guess is correct.

### Problem: Loop runs too many or too few times

**Solution:** Check your `range()` function - remember it starts at 0.

---

## What's Next?

In the next lab, you'll learn about:

- Working with lists and other container types
- More complex data structures
- Processing collections of data

**Ready to continue?** Move on to Lab 4: Container Types!

---

## Solutions

**Complete code examples for all exercises are available in the `solutions/` folder.**

- `solutions/guessing_game.py` - Complete game solution
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
