# Lab 10: Automated Testing with Pytest

### **Objective**
Writing code is one thing; proving it works is another. **Automated testing** is a crucial skill that helps you verify your code's correctness, prevent future bugs, and make changes with confidence.

The aim of this lab is to introduce automated testing using the `pytest` library. We will write tests for the `Headline` class we created in our `headline_module`.

---

## **What is Automated Testing?**

**Automated testing** is the practice of writing code that automatically verifies your application code works correctly. Instead of manually testing your program every time you make changes, automated tests run automatically and tell you if something is broken.

### **Key Concepts**
- **Test Functions**: Code that verifies your application code
- **Assertions**: Statements that check if conditions are true
- **Test Discovery**: Automatic finding and running of test files
- **Fixtures**: Reusable test data and setup
- **Test Coverage**: How much of your code is tested
- **Regression Testing**: Ensuring new changes don't break existing functionality

---

## **Step 1: Setup**

### **Tasks**
1. Create a test file in the same directory as your headline module
2. Install the pytest library
3. Set up basic imports for testing

### **Hints**
- Test files should be separate from your application code
- Use the standard naming convention: `test_` prefix
- Install pytest using pip from your terminal
- Import the class you want to test from your module
- Think about where test files should be located

### **Expected Outcomes**
- A new test file is created with the correct name
- pytest is successfully installed on your system
- Basic imports are set up correctly
- Test file is in the right location

### **Check Your Work**
- Does your test file start with `test_`?
- Is pytest installed and accessible?
- Can you import your Headline class?
- Is the test file in the same directory as your module?

---

## **Step 2: Write a Basic Test**

### **Tasks**
1. Create a test function for object creation
2. Test that Headline objects are created correctly
3. Verify that attributes are set to the expected values

### **Hints**
- Test functions must start with `test_`
- Create a Headline instance with known test data
- Use assert statements to verify object state
- Test both text and source attributes
- Choose simple, predictable test data

### **Expected Outcomes**
- A test function that creates a Headline object
- Assertions that verify both attributes are correct
- Test passes when run with pytest
- Clear test data that's easy to verify

### **Check Your Work**
- Does your test function start with `test_`?
- Does it create a Headline object with test data?
- Are you testing both text and source attributes?
- Does the test pass when you run pytest?
- Is your test data simple and predictable?

---

## **Step 3: Test a Method**

### **Tasks**
1. Create a test function for the get_word_count method
2. Test the method with known input and expected output
3. Verify the method returns the correct word count

### **Hints**
- Create a new test function for method testing
- Use text where you know the exact word count
- Test with simple, clear examples
- Think about edge cases (empty text, single word, multiple words)
- Use assert to compare expected vs actual results

### **Expected Outcomes**
- A test function that tests the get_word_count method
- Clear test cases with predictable results
- Assertions that verify method behavior
- Tests that pass when run

### **Check Your Work**
- Does your test function have a descriptive name?
- Are you testing with text where you know the word count?
- Does your assertion compare expected vs actual results?
- Does the test pass when you run pytest?
- Is your test case clear and easy to understand?

---

## **Step 4: Refactor with a Fixture**

### **Tasks**
1. Create a pytest fixture for common test data
2. Refactor existing tests to use the fixture
3. Reduce code duplication across tests

### **Hints**
- Import pytest at the top of your file
- Create a fixture function that returns test data
- Use the @pytest.fixture decorator
- Modify test functions to accept the fixture as a parameter
- Remove duplicate object creation code

### **Expected Outcomes**
- A fixture function that provides test data
- Refactored tests that use the fixture
- Reduced code duplication
- Cleaner, more maintainable test code

### **Check Your Work**
- Did you import pytest?
- Is your fixture function decorated with @pytest.fixture?
- Do your tests accept the fixture as a parameter?
- Is there less duplicate code in your tests?
- Do all tests still pass when you run pytest?

---

## **Common Issues to Watch Out For**

### **Test File Setup**
- **Wrong naming**: Test files must start with `test_`
- **Wrong location**: Test files should be discoverable by pytest
- **Missing imports**: Can't test what you can't import
- **Installation issues**: pytest must be installed and accessible

### **Test Function Structure**
- **Wrong naming**: Test functions must start with `test_`
- **Missing assertions**: Tests without assertions don't verify anything
- **Complex test data**: Keep test data simple and predictable
- **Unclear test cases**: Tests should be easy to understand

### **Fixture Usage**
- **Missing decorator**: @pytest.fixture is required
- **Wrong parameter names**: Fixture parameter names must match
- **Fixture not imported**: pytest must be imported to use fixtures
- **Over-complicated fixtures**: Keep fixtures simple and focused

### **Assertion Problems**
- **Wrong comparisons**: Compare the right values
- **Missing assertions**: Every test needs at least one assertion
- **Unclear failure messages**: Assertions should be descriptive
- **Testing wrong things**: Make sure you're testing the right functionality

---

## **Testing Your Solutions**

### **Test Scenarios**
1. **Basic Setup**: Test file creation and pytest installation
2. **Object Creation**: Test Headline object instantiation
3. **Method Testing**: Test get_word_count functionality
4. **Fixture Usage**: Test fixture-based test organization

### **Expected Results**
- All tests pass when run with pytest
- Test discovery works correctly
- Fixtures provide consistent test data
- Code is more maintainable and organized

### **Verification Steps**
1. **Run pytest** and check for test discovery
2. **Verify test results** - all tests should pass
3. **Check test output** for clear pass/fail information
4. **Review code organization** - less duplication, cleaner structure
5. **Test edge cases** - empty strings, single words, etc.

---

## **Extension Ideas (Optional)**

### **Additional Test Cases**
- **Edge cases**: Empty text, very long text, special characters
- **Error conditions**: Invalid input, boundary conditions
- **Method coverage**: Test all methods in your Headline class
- **Property testing**: Test with various text lengths and content

### **Advanced Pytest Features**
- **Parameterized tests**: Test multiple inputs with one test function
- **Test markers**: Categorize and run specific test groups
- **Test coverage**: Measure how much code is tested
- **Test reporting**: Generate detailed test reports

### **Test Organization**
- **Test classes**: Group related tests together
- **Test modules**: Organize tests by functionality
- **Test data files**: External test data for complex scenarios
- **Test utilities**: Helper functions for common test operations

---

## **Running Your Tests**

### **Basic Commands**
- **`pytest`** - Run all tests in current directory
- **`pytest -v`** - Verbose output showing each test
- **`pytest -k "test_name"`** - Run specific tests by name
- **`pytest --tb=short`** - Shorter traceback for failures

### **Test Discovery**
- pytest automatically finds files starting with `test_`
- Test functions must start with `test_`
- Tests can be in subdirectories
- pytest follows Python import rules

---

## **Why Automated Testing?**

Automated testing is powerful because it:
- **Prevents bugs** - Catches problems before they reach users
- **Enables refactoring** - Make changes with confidence
- **Documents behavior** - Tests show how code should work
- **Improves design** - Writing testable code leads to better architecture
- **Saves time** - Automated tests are faster than manual testing
- **Enables CI/CD** - Continuous integration and deployment

---

## **Real-World Applications**

Automated testing is used everywhere in professional development:
- **Web applications**: Test API endpoints, user interactions
- **Data processing**: Verify calculations and transformations
- **Desktop applications**: Test user interface functionality
- **Libraries and packages**: Ensure compatibility and correctness
- **Scientific computing**: Validate algorithms and results
- **DevOps and automation**: Test deployment and configuration

---

## **Testing Best Practices**

### **Test Design**
- **One concept per test**: Each test should verify one thing
- **Descriptive names**: Test names should explain what they test
- **Simple test data**: Use predictable, easy-to-verify data
- **Independent tests**: Tests should not depend on each other

### **Test Organization**
- **Group related tests**: Use classes or modules to organize
- **Consistent structure**: Follow the same pattern across all tests
- **Clear setup**: Make test setup easy to understand
- **Proper teardown**: Clean up after tests if necessary

### **Maintenance**
- **Keep tests simple**: Complex tests are hard to maintain
- **Update tests with code**: Tests should evolve with your code
- **Remove obsolete tests**: Don't keep tests for removed functionality
- **Regular review**: Periodically review and improve your tests

---

## **Solutions**

**Complete code examples for all exercises are available in the `solutions/lab-10` folder.**

- `solutions/test_headline.py` - Complete test file with all exercises
- `solutions/step_by_step/` - Individual step solutions

---

**Remember**: 
- Start with simple tests and build complexity gradually
- Always run your tests after making changes
- Use descriptive names for tests and fixtures
- Keep test data simple and predictable
- Automated testing is a skill that improves with practice

This lab introduces you to one of the most important practices in professional software development - automated testing with pytest! 