# Lab 10: Automated Testing with Pytest

Writing code is one thing; proving it works is another. Automated testing is a crucial skill that helps you verify your code's correctness, prevent future bugs, and make changes with confidence.

The aim of this lab is to introduce automated testing using the `pytest` library. We will write tests for the `Headline` class we created in our `headline_module`.

This lab is made up of 4 steps:
1.  Set up a test file and install `pytest`.
2.  Write a basic test to check object creation.
3.  Write a test for a class method.
4.  Refactor tests to use a `pytest` fixture to reduce code duplication.

---
## Step 1: Setup

Testing code should live in separate files from your application code. `pytest` has a standard naming convention for test files and functions.

**Your goal:** Create a test file and install `pytest`.

**Hints:**
- In the same directory as `headline_module.py` and `main_analysis.py`, create a new file named `test_headline.py`. `pytest` automatically discovers files that start with `test_`.
- You'll need to install `pytest`. From your terminal, run: `pip install pytest`.
- In `test_headline.py`, you'll need to import the class you want to test: `from headline_module import Headline`.

---
## Step 2: Write a Basic Test

Let's test the most basic functionality: creating a `Headline` object.

**Your goal:** Write a test function that creates a `Headline` and asserts its attributes are set correctly.

**Hints:**
- Test functions must also start with `test_`. Define a function, for example: `def test_headline_creation():`.
- Inside the function, create an instance of your `Headline` class with some sample text and a sample source.
- Use the `assert` keyword to check if the `text` attribute of your new object is equal to the sample text you provided.
- Do the same to verify the `source` attribute.
- If your assertions are true, the test passes. If not, `pytest` will report a failure.

---
## Step 3: Test a Method

Now let's test the behavior of our class by testing its `get_word_count` method.

**Your goal:** Write a test to verify the `get_word_count` method works correctly.

**Hints:**
- Define another test function, like `def test_get_word_count():`.
- Inside, create a `Headline` object with text where you know the exact word count (e.g., "This has four words").
- Use `assert` to check if calling the `.get_word_count()` method on your object returns the number you expect (e.g., `4`).

---
## Step 4: Refactor with a Fixture

You might notice we're creating `Headline` objects in multiple tests. We can avoid this repetition using a `pytest` fixture. A fixture is a function that provides a consistent baseline or data for your tests.

**Your goal:** Create a fixture that provides a sample `Headline` object and use it in your tests.

**Hints:**
1.  Import `pytest` at the top of your file.
2.  Define a new function for your fixture, for example `def sample_headline():`.
3.  Add the `@pytest.fixture` decorator on the line directly above the function definition.
4.  Inside the fixture function, create and `return` a standard `Headline` object. This will be the baseline object used in your tests.
5.  Now, refactor one of your previous tests. Change its signature to accept `sample_headline` as an argument (the same name as your fixture function).
6.  Inside this refactored test, you can remove the line where you create the `Headline` object yourself. You can now directly use the `sample_headline` object that `pytest` passes in.
7.  Update your `assert` statements to check the attributes of the `sample_headline` object against the values you defined inside your fixture.
---
## Running Your Tests

Once your test file is saved, navigate to its directory in your terminal and simply run the command:
`pytest`

`pytest` will automatically find and run your tests, giving you a report of what passed and what failed. 