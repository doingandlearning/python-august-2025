# Lab 7: Structuring Data with Classes

So far, we've been working with headlines as simple strings. This is fine, but as our data gets more complex, it's better to structure it. Classes are the perfect tool for this.

The aim of this lab is to create a `Headline` class to hold not just the text of a headline, but also its source. We will then add behavior to this class.

This lab is made up of 4 steps:

1.  Define a basic `Headline` class with an `__init__` method.
2.  Add a `__str__` method for a clean string representation.
3.  Add a `get_word_count()` method to the class.
4.  Refactor the main script to use a list of `Headline` objects.

---

## Step 1: Defining the `Headline` Class

Create a new Python file, e.g., `headline_objects.py`.

**Your goal:** Define a class named `Headline`. The "constructor" (`__init__` method) should accept two arguments: the `text` of the headline and its `source` (e.g., "BBC News").

**Hints:**

- Start with `class Headline:`.
- Define the constructor: `def __init__(self, text, source):`.
- Inside the constructor, you need to store the arguments as attributes of the object. The standard way is `self.text = text` and `self.source = source`.

---

## Step 2: Adding a String Representation

If you try to print a `Headline` object right now, you'll get something unhelpful like `<__main__.Headline object at 0x10d6d6a90>`. We can fix this with the `__str__` method.

**Your goal:** Add a `__str__` method to your `Headline` class that returns a clear, unambiguous string representation of the object.

**Hints:**

- Define a new method inside the class: `def __str__(self):`.
- This method must `return` a string.
- A good representation shows the class name and its attributes, like: `f"Headline(text='{self.text}', source='{self.source}')"`.

---

## Step 3: Adding Behavior with a Method

The real power of classes is bundling data (attributes) with the functions (methods) that act on that data.

**Your goal:** Create a method `get_word_count()` inside the `Headline` class that returns the number of words in the headline's text.

**Hints:**

- Define a new method: `def get_word_count(self):`.
- The logic is the same as our old standalone function, but now it uses the object's own data: `self.text`.
- The method should `return len(self.text.split())`.

---

## Step 4: Refactoring Your Code to Use the Class

Now it's time to use our new class.

**Your goal:** Instead of a list of strings, create a list of `Headline` objects. Then, loop through this new list and use the object's method to print the word count for each.

**Hints:**

- Your old list of strings: `["General election: ...", ...]`
- Your new list of objects:
  ```python
  headlines = [
      Headline("General election: Labour and Tories clash over tax", "BBC News"),
      Headline("England crowned T20 world champions", "Sky Sports"),
      # ... and so on for the rest
  ]
  ```
- Now, loop through this list: `for h in headlines:`.
- Inside the loop, you no longer need a separate function to get the word count. You can call the method directly on the object: `count = h.get_word_count()`.
- Print out the headline's text and its word count. Notice how much cleaner `h.get_word_count()` is than `get_word_count(h)`. It reads "tell the headline to get its own word count."
