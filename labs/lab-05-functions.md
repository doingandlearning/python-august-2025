# Lab 5: Building a Headline Analysis Toolkit with Functions

The aim of this lab is to practice writing functions to create a reusable, organized toolkit. We will refactor our previous headline analysis script into a set of functions that can be easily called and tested.

This lab is made up of 4 steps:
1.  Set up your script with the headline data.
2.  Write a function to get the length of a single headline.
3.  Write a function to search for headlines containing a keyword.
4.  Write a main `analyse_all_headlines` function that uses the other functions.

---
## Step 1: Getting Started

Create a new Python file, e.g., `headline_analyzer.py`.

You'll need the same list of headlines from the previous labs:

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

---
## Step 2: A Function to Get Word Count

Let's start with a simple, focused function.

**Your goal:** Create a function `get_word_count(headline_text)` that takes a single headline string as an argument and returns the number of words in it.

**Hints:**
- Define your function using `def get_word_count(headline_text):`.
- Inside the function, use the `.split()` method on `headline_text` to turn it into a list of words.
- Use `len()` to find the length of that list.
- Use the `return` keyword to send this number back as the function's result.
- You can test it by calling `print(get_word_count("This is a test headline"))`. It should print `5`.

---
## Step 3: A Function to Find Headlines with a Keyword

Now, let's create a function that filters our list.

**Your goal:** Create a function `find_headlines_with_keyword(list_of_headlines, keyword)` that takes the full list of headlines and a search term. It should return a *new list* containing only the headlines that match the keyword.

**Hints:**
- Define your function: `def find_headlines_with_keyword(list_of_headlines, keyword):`.
- Inside the function, create an empty list, maybe called `matching_headlines`.
- Loop through each `headline` in the `list_of_headlines`.
- Inside the loop, use an `if` statement to check if the `keyword` (in lowercase) is `in` the `headline` (also in lowercase).
- If it matches, use the `.append()` method to add the headline to your `matching_headlines` list.
- After the loop has finished, `return` the `matching_headlines` list.

---
## Step 4: A Main Analysis Function

Finally, let's create a "main" function that orchestrates our analysis and prints a summary. This is a common pattern in larger scripts.

**Your goal:** Create a function `analyse_all_headlines(list_of_headlines)` that calculates and prints the average headline length.

**Hints:**
- Define your function: `def analyse_all_headlines(list_of_headlines):`.
- Inside it, create a `total_words` counter, initialized to `0`.
- Loop through each `headline` in the `list_of_headlines`.
- In the loop, call your `get_word_count()` function, passing the current `headline` to it. Add the result to `total_words`.
- After the loop, calculate the average and print it in a user-friendly format.

---
## Tying It All Together

After you have defined all your functions, the main part of your script (at the bottom, not indented) is where you call them to produce the final output.

**Example script structure:**

```python
# ... (your list of headlines here) ...

# --- Function Definitions ---
def get_word_count(headline_text):
    # ... your code here ...

def find_headlines_with_keyword(list_of_headlines, keyword):
    # ... your code here ...

def analyse_all_headlines(list_of_headlines):
    # ... your code here ...


# --- Main Script ---
print("--- Headline Analysis ---")
analyse_all_headlines(headlines)

print("\n--- Searching for 'New' ---")
new_headlines = find_headlines_with_keyword(headlines, "new")
for h in new_headlines:
    print(h)

print("\n--- Searching for 'Tax' ---")
tax_headlines = find_headlines_with_keyword(headlines, "tax")
for h in tax_headlines:
    print(h)
```
This structure makes your code clean, readable, and easy to modify. Each function has one clear job. 