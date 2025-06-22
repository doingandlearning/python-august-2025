# Lab 8: Organizing Your Code with Modules

As your projects grow, putting all your code in one file becomes messy. Modules allow you to organize your code into separate files, making it cleaner, more reusable, and easier to manage.

The aim of this lab is to split our headline analysis tool into two modules: one to define the `Headline` class, and another to run the main analysis.

This lab is made up of 3 steps:
1.  Create a `headline_module.py` to store the `Headline` class.
2.  Create a `main_analysis.py` to import and use the class.
3.  Use the `if __name__ == "__main__"` block to create a safe entry point for the script.

---
## Step 1: Create a `headline_module.py`

This module's only job will be to define our `Headline` class.

**Your goal:** Create a new file named `headline_module.py`. Move the complete `Headline` class definition from your previous lab into this file.

**Hints:**
- Create a new file, `headline_module.py`.
- Copy the `class Headline:` block and all of its methods (`__init__`, `__repr__`, `get_word_count`) into this new file.
- This file should *only* contain the class definition. There should be no code that creates a list of headlines or loops through them. It's just a blueprint.

---
## Step 2: Create a `main_analysis.py`

This will be our main script. It will import the `Headline` class and use it to perform the analysis.

**Your goal:** Create a second new file, `main_analysis.py`. This file will import your `Headline` class and use it.

**Hints:**
- At the very top of `main_analysis.py`, you need to import the class from your other file. The syntax is: `from headline_module import Headline`.
- Now, you can use the `Headline` class as if it were defined in this file.
- Copy the rest of your code from the previous lab here: the part that creates the list of `Headline` objects and the `for` loop that prints the analysis.
- Try running `main_analysis.py`. It should work exactly as before!

---
## Step 3: Using `if __name__ == "__main__"`

It's a very important Python convention to put your main script logic inside a block that checks if the file is being run directly. This prevents code from running automatically when the file is imported by another module.

**Your goal:** In `main_analysis.py`, wrap your script's logic in a `main()` function and call it from within an `if __name__ == "__main__"` block.

**Hints:**
1.  **Define a `main()` function:** Create a function `def main():`.
2.  **Indent your code:** Indent all of your existing script logic (creating the list, looping through it, printing the analysis) so it's inside the `main()` function.
3.  **Add the special block:** At the very bottom of the file (unindented), add the following lines:
    ```python
    if __name__ == "__main__":
        main()
    ```
- This tells Python: "Only call the `main()` function if this file is being executed directly by the user." Your script should still run exactly as before, but now it's structured in a much more professional and reusable way. 