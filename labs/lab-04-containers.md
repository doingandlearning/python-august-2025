# Lab 4: Analyzing News Headlines

The aim of this lab is to get comfortable working with lists, one of the most common data structures in Python. We'll use a list of BBC News headlines to perform some simple, real-world text analysis.

This lab is made up of 4 steps:
1.  Start with a list of headlines
2.  Count the headlines
3.  Calculate the average headline length
4.  Find the most common topics

## Step 1: Create a New File

For this lab, you should create a new Python file. You can name it `news_analysis.py`.

## Step 2: Start with a list of headlines

Instead of asking the user for input, we'll start with a predefined list of headlines. This lets us focus on the list manipulation itself. Copy this list into your Python file:

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

## Step 3: Count the Headlines and Average Length

First, let's get some basic stats.

### Count the headlines
Use the built-in `len()` function to find the number of items in the `headlines` list. Then, use an f-string to print it out in a readable format, like: `There are 10 headlines in the list.`

### Calculate the average headline length
How long is the typical headline? To figure this out, you'll need to:
1.  Create a variable to keep track of the total word count, let's call it `total_words` and set it to `0`.
2.  Loop through each `headline` in the `headlines` list.
3.  Inside the loop, for each `headline`, use the `.split()` method to turn the headline string into a list of words.
4.  Find the length of that list of words and add it to your `total_words` counter.
5.  After the loop has finished, calculate the average by dividing `total_words` by the number of headlines.
6.  Print the result in a user-friendly sentence.

The `.split()` method is very useful here as it handily turns a string into a list of words.

## Step 4: Find the most common topics

Now for the interesting part. Let's write some code to see how many headlines mention a specific topic.

First, use the `input()` function to ask the user what topic they're interested in and store their answer in a `search_term` variable.

Next, you'll need to:
1.  Create a counter variable, maybe called `matching_headlines`, and initialize it to `0`.
2.  Loop through each `headline` in the `headlines` list.
3.  Inside the loop, use an `if` statement to check if the user's `search_term` is `in` the `headline`.
4.  A good tip is to convert both the headline and the search term to lowercase using the `.lower()` method. This will make your search case-insensitive (so searching for "london" will match "London").
5.  If you find a match, print the headline and add one to your `matching_headlines` counter.
6.  After the loop, print out the final count of how many matching headlines were found.

### Run your program!
Try searching for topics like "election", "new", or "NHS".

This kind of simple script is the foundation of much larger data analysis. You can already see how you could use it to track trends in news coverage over time. 