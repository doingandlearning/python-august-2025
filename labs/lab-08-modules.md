# Lab 8: Organizing Your Code with Modules

### **Objective**
As your projects grow, putting all your code in one file becomes messy. **Modules** allow you to organize your code into separate files, making it cleaner, more reusable, and easier to manage.

The aim of this lab is to split our headline analysis tool into two modules: one to define the `Headline` class, and another to run the main analysis.

---

## **What are Modules?**

A **module** is a Python file that can be imported and used in other Python files. Think of modules as building blocks that you can combine to create larger programs.

### **Key Concepts**
- **Module**: A Python file containing code that can be imported
- **Import**: Bringing code from one module into another
- **Separation of Concerns**: Different files handle different responsibilities
- **Reusability**: Code can be used in multiple programs
- **Maintainability**: Easier to find and fix issues in smaller files

---

## **Step 1: Create a `headline_module.py`**

### **Tasks**
1. Create a new file named `headline_module.py`
2. Move the complete `Headline` class definition from your previous lab into this file
3. Ensure the file contains only the class definition

### **Hints**
- Create a new file, `headline_module.py`
- Copy the `class Headline:` block and all of its methods
- Include `__init__`, `__str__`, and `get_word_count` methods
- This file should *only* contain the class definition
- There should be no code that creates headlines or runs analysis
- It's just a blueprint for creating `Headline` objects

### **Expected Outcomes**
- You should have a new file called `headline_module.py`
- The file should contain only the `Headline` class definition
- All methods should be properly indented inside the class
- The file should not contain any headline data or analysis code

### **Check Your Work**
- Does `headline_module.py` exist in your workspace?
- Does it contain the complete `Headline` class?
- Are there any headline objects or analysis code in this file?
- Can you see all the methods (`__init__`, `__str__`, `get_word_count`)?

---

## **Step 2: Create a `main_analysis.py`**

### **Tasks**
1. Create a second new file, `main_analysis.py`
2. Import the `Headline` class from your module
3. Use the imported class to perform the analysis
4. Copy the headline data and analysis logic from your previous lab

### **Hints**
- At the very top of `main_analysis.py`, import the class
- Use the syntax: `from headline_module import Headline`
- Now you can use the `Headline` class as if it were defined in this file
- Copy the headline creation and analysis code from your previous lab
- Include the list of `Headline` objects and the analysis loop

### **Expected Outcomes**
- You should have a new file called `main_analysis.py`
- The file should import the `Headline` class successfully
- It should create a list of `Headline` objects
- It should run the analysis and display results
- The output should be identical to your previous lab

### **Check Your Work**
- Does `main_analysis.py` exist in your workspace?
- Does it import the `Headline` class without errors?
- Can you run the file and see the analysis results?
- Are the results the same as your previous lab?
- Does the import statement appear at the top of the file?

---

## **Step 3: Using `if __name__ == "__main__"`**

### **Tasks**
1. Wrap your script's logic in a `main()` function
2. Add the `if __name__ == "__main__"` block
3. Call the `main()` function from within this block

### **Hints**
1. **Define a `main()` function:** Create a function `def main():`
2. **Indent your code:** Move all your existing script logic inside the `main()` function
3. **Add the special block:** At the bottom of the file, add the `if __name__ == "__main__"` check
4. **Call main():** Inside the block, call `main()`
5. **Keep it unindented:** The `if` statement should be at the leftmost margin

### **Expected Outcomes**
- Your script logic should be wrapped in a `main()` function
- The `if __name__ == "__main__"` block should be at the bottom
- The script should still run exactly as before
- The code should be more professional and reusable
- Importing the file should not run the analysis automatically

### **Check Your Work**
- Is your code wrapped in a `main()` function?
- Is the `if __name__ == "__main__"` block at the bottom?
- Does the script still run and show results?
- Can you import the file without running the analysis?
- Is the code structure cleaner and more organized?

---

## **Common Issues to Watch Out For**

### **Import Errors**
- **File not found**: Make sure both files are in the same directory
- **Import syntax**: Use `from headline_module import Headline`
- **File names**: Check that file names match exactly (including case)
- **Python path**: Ensure you're running from the correct directory

### **Code Organization**
- **Wrong indentation**: The `if __name__ == "__main__"` should not be indented
- **Missing main() call**: Don't forget to call `main()` inside the block
- **Mixed responsibilities**: Keep class definition separate from analysis code
- **Circular imports**: Avoid importing files that import each other

### **Function Structure**
- **Missing function definition**: Make sure `def main():` is defined
- **Wrong indentation**: All analysis code should be inside the `main()` function
- **Missing colon**: Don't forget `:` after `def main()`
- **Function call**: Remember to call `main()` in the special block

---

## **Testing Your Solutions**

### **Test Scenarios**
1. **Module Creation**: Verify `headline_module.py` contains only the class
2. **Import Testing**: Check that `main_analysis.py` can import the class
3. **Functionality**: Ensure the analysis still works correctly
4. **Main Block**: Verify the `if __name__ == "__main__"` works properly

### **Expected Results**
- Both files should exist and be properly structured
- Import should work without errors
- Analysis should produce the same results as before
- Running `main_analysis.py` should work normally
- Importing `main_analysis.py` should not run the analysis

### **Verification Steps**
1. **Check file structure**: Verify both files exist and contain the right code
2. **Test import**: Try importing the module in Python
3. **Run analysis**: Execute `main_analysis.py` to see results
4. **Test import behavior**: Import the file to ensure analysis doesn't run

---

## **Extension Ideas (Optional)**

### **Additional Modules**
- **`data_module.py`**: Store headline data separately
- **`analysis_module.py`**: Move analysis functions to their own module
- **`utils_module.py`**: Create utility functions for common operations
- **`config_module.py`**: Store configuration settings

### **Enhanced Organization**
- **Package structure**: Create a folder with `__init__.py` files
- **Relative imports**: Use relative imports within packages
- **Module aliases**: Import modules with different names
- **Selective imports**: Import only specific functions or classes

### **Advanced Module Features**
- **Module documentation**: Add docstrings to modules
- **Module variables**: Define constants or configuration in modules
- **Module functions**: Create functions that work at the module level
- **Module testing**: Test individual modules independently

---

## **Solutions**

**Complete code examples for all exercises are available in the `solutions/lab-08` folder.**

- `solutions/headline_module.py` - Module containing the Headline class
- `solutions/main_analysis.py` - Main script that imports and uses the class

---

## **Why Modules?**

Modules are powerful because they:
- **Organize code** - Break large programs into manageable pieces
- **Enable reuse** - Use the same code in multiple programs
- **Improve maintainability** - Easier to find and fix issues
- **Support collaboration** - Different people can work on different modules
- **Follow best practices** - Professional Python development standards

---

## **Real-World Applications**

Modules are used everywhere in Python:
- **Standard library**: Built-in modules like `os`, `sys`, `datetime`
- **Third-party packages**: Libraries like `pandas`, `requests`, `flask`
- **Your own projects**: Organizing code into logical components
- **Team development**: Multiple developers working on different modules
- **Package distribution**: Sharing code with the Python community

---

## **Module Best Practices**

### **File Organization**
- **One class per module**: Keep modules focused on a single responsibility
- **Descriptive names**: Use clear, descriptive file names
- **Consistent structure**: Follow the same pattern across all modules
- **Documentation**: Include docstrings and comments

### **Import Guidelines**
- **Import at the top**: Put all imports at the beginning of files
- **Specific imports**: Import only what you need
- **Avoid wildcards**: Don't use `from module import *`
- **Clear naming**: Use descriptive names for imported items

---

**Remember**: 
- Start with simple module organization and build complexity gradually
- Always test imports and functionality after creating modules
- Use descriptive file names that reflect the module's purpose
- Keep modules focused on a single responsibility
- Modules are the foundation of professional Python development

This lab introduces you to one of Python's most important concepts for organizing and scaling your code! 