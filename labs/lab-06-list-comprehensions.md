# Lab 6: Supercharging Analysis with List Comprehensions

The aim of this lab is to use list comprehensions to perform powerful data manipulation on the headlines list in a single, readable line of code. This is a very common and powerful technique in Python.

This lab is made up of 3 steps:
1.  Use a list comprehension to "map" data to a new list.
2.  Use a list comprehension with a condition to "filter" data.
3.  Combine mapping and filtering in a single list comprehension.

---
## Step 1: Getting Started

Create a new Python file, e.g., `comprehensions_analysis.py`.

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
## Step 2: Mapping with List Comprehensions

A list comprehension is a great way to create a new list by applying an operation to every item in an existing list.

**Your goal:** Create a new list called `headline_lengths` that contains the word count for each headline.

**Hints:**
- The basic syntax is `[expression for item in list]`.
- Your `expression` will involve calling `.split()` and `len()` on each `item`.
- The `item` in your case is each `headline` in the `headlines` list.
- After creating the list, print it to see the result.

---
## Step 3: Filtering with List Comprehensions

Now, let's use a list comprehension to select only the items that meet a certain criteria.

**Your goal:** Create a new list called `short_headlines` that contains only the headlines with 7 words or fewer.

**Hints:**
- The syntax for filtering is `[item for item in list if condition]`.
- Your `condition` will check the word count of each `headline`.
- Remember to use `.split()` and `len()` as part of your `if condition`.
- Print the `short_headlines` list to check your work.

---
## Step 4: Combining Mapping and Filtering

This is where list comprehensions really shine. You can filter a list and transform the results in a single, elegant line.

**Your goal:** Create a list called `specific_headline_lengths` that contains the word counts of only those headlines that include the word "new".

**Hints:**
- You'll use the combined syntax: `[expression for item in list if condition]`.
- Your `expression` will get the word count of the `item` (the headline).
- Your `if condition` will check if the word "new" is in the `item`. Remember to use `.lower()` to make your check case-insensitive.
- Print the final list to see the word counts of just the matching headlines. 