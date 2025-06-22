# Lab 3: Iteration and Control Flow

The aim of this lab is to create a simple guessing game. This will give you practice with `while` or `for` loops, `if/elif/else` statements, and handling user input.

The logic of the game is:
- The program randomly selects a secret "channel number" between 1 and 50.
- The player has a fixed number of attempts to guess it.
- After each guess, the program tells the player if their guess was too high, too low, or correct.
- The game ends when the player guesses the number or runs out of attempts.

---
## Step 1: Setting up the Game

First, you need to get your Python script ready.

**Hints:**
- To generate a random number, you must first `import` the `random` module at the top of your file.
- Create a variable, for example `secret_channel`, and assign it a random integer. The `random.randint(1, 50)` function is perfect for picking a number between 1 and 50.
- It's good practice to print a welcome message to the player, explaining the rules. For example: "I'm thinking of a BBC channel number between 1 and 50. You have 5 tries to guess it!".

---
## Step 2: The Game Loop

You need to give the player a fixed number of attempts. A `for` loop is a great choice for this.

**Hints:**
- You can create a loop that runs 5 times using `for guess_attempt in range(5):`.
- All the logic for getting and checking the user's guess will go inside this loop.

---
## Step 3: Getting and Checking the User's Guess

This is where the main logic of your game will be.

**Hints:**
- Inside your loop, use the `input()` function to ask the user for their guess.
- `input()` returns a string, but you need a number to compare with your `secret_channel`. Use `int()` to convert the user's input into an integer.
- Use an `if/elif/else` block to compare the user's guess to the `secret_channel`:
    - `if` the guess is correct: print a "Well done!" message. The game should then end. The `break` statement is what you need to exit the loop early.
    - `elif` the guess is less than the secret number: print a hint like "Too low, try a higher number."
    - `else` (meaning the guess must be too high): print a hint like "Too high, try a lower number."

---
## Step 4: Handling a Win or Loss

What happens when the loop finishes? The player has either won (by guessing correctly and using `break`) or lost (by running out of attempts). Your program needs to know the difference.

**Hints:**
- A "flag" variable is a good way to track whether the player has won. Before the loop starts, create a variable `player_won = False`.
- If the player guesses correctly, as well as breaking the loop, set `player_won = True`.
- **After** the loop has finished, you can check the flag: `if player_won:`
    - If it's true, you've already congratulated them. You could print a "Game over!" message.
    - If it's false, it means the loop finished naturally without a correct guess. In this case, you should tell them they've lost and reveal the `secret_channel`. 