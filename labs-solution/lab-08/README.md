# Lab 8: Organizing Your Code with Modules - Solutions

This folder contains complete solutions for Lab 8: Organizing Your Code with Modules. These solutions demonstrate how to split code into separate modules and use imports to organize your Python projects.

## Files Overview

### Module File

1. **`headline_module.py`** - Module containing the Headline class
   - Contains only the class definition and methods
   - No headline data or analysis code
   - Designed to be imported by other files

### Main Script

2. **`main_analysis.py`** - Main script that imports and uses the Headline class
   - Imports the Headline class from headline_module
   - Creates headlines and performs analysis
   - Uses the `if __name__ == "__main__"` block

## How to Use These Solutions

### For Learning
1. **Try the lab exercises yourself first** - don't peek at solutions until you're stuck!
2. **Compare your code** with the solutions to see different approaches
3. **Experiment** with the code - modify imports, add new modules
4. **Run both files** to see how modules work together

### For Reference
- Use these as templates for similar module organization
- Study the import syntax and module structure
- Note the separation of concerns between files
- See how the `if __name__ == "__main__"` block works

## Running the Programs

### Running the Main Script
```bash
python main_analysis.py
```

### Testing the Module Import
```bash
python -c "from headline_module import Headline; h = Headline('Test', 'Test Source'); print(h)"
```

### Running Both Files Together
Make sure both files are in the same directory, then run:
```bash
python main_analysis.py
```

## Key Concepts Demonstrated

### **Module Organization**
- **Separation of Concerns**: Class definition vs. analysis logic
- **Reusability**: Class can be imported by multiple scripts
- **Maintainability**: Easier to modify class or analysis independently
- **Professional Structure**: Following Python best practices

### **Import System**
- **Module Import**: `from headline_module import Headline`
- **Class Usage**: Using imported class as if defined locally
- **Method Access**: All class methods work through import
- **Namespace Management**: Clear separation of module contents

### **Main Block Pattern**
- **`if __name__ == "__main__"`**: Safe entry point for scripts
- **Function Wrapping**: Main logic wrapped in `main()` function
- **Import Safety**: Code doesn't run when imported
- **Professional Structure**: Industry-standard Python pattern

## Concepts Used (Lab 8 Appropriate)

These solutions use concepts appropriate for Lab 8:
- Module creation and organization
- Import statements and syntax
- Class definition and usage
- Function definition and calling
- The `if __name__ == "__main__"` pattern
- Basic string operations and methods
- List operations and loops

## Sample Output

When you run the main script, you'll see:

```
Lab 8: Organizing Your Code with Modules
==================================================

Creating headlines using imported Headline class:
Created 10 headline objects using imported class
Type of first headline: <class 'headline_module.Headline'>
Class name: Headline

Processing all headlines:
----------------------------------------
 1. ( 8 words,  58 chars) [BBC News] General election: Labour and Tories clash over tax
 2. ( 4 words,  35 chars) [Sky Sports] England crowned T20 world champions
 3. ( 8 words,  58 chars) [The Guardian] Summer travel chaos feared as airline strikes loom
...

Demonstrating imported class functionality:
----------------------------------------
String representation:
  Headline(text='General election: Labour and Tories clash over tax', source='BBC News')
  Headline(text='England crowned T20 world champions', source='Sky Sports')

Word counting:
  Headline 1: 8 words
  Headline 2: 4 words
  Headline 3: 8 words

Import Verification:
----------------------------------------
✓ Successfully imported Headline class from headline_module
✓ All class methods work correctly
✓ Analysis produces the same results as before
✓ Code is now organized into separate modules
```

## Module Examples

### Module File Structure (headline_module.py)
```python
# Module containing only the class definition
class Headline:
    def __init__(self, text, source):
        self.text = text
        self.source = source
    
    def get_word_count(self):
        return len(self.text.split())
    # ... other methods
```

### Main Script Structure (main_analysis.py)
```python
# Import the class from the module
from headline_module import Headline

def main():
    # Use the imported class
    headlines = [
        Headline("Some text", "Some source"),
        Headline("More text", "Another source")
    ]
    # ... analysis code

if __name__ == "__main__":
    main()
```

## Understanding Modules

### **The Module Structure**
Modules follow this basic pattern:
```python
# filename: my_module.py
class MyClass:
    def __init__(self, param):
        self.param = param
    
    def my_method(self):
        return self.param

# No main execution code here
```

### **Import and Usage**
```python
# In another file
from my_module import MyClass

# Use the imported class
obj = MyClass("value")
result = obj.my_method()
```

### **Main Block Pattern**
```python
def main():
    # Main program logic here
    pass

if __name__ == "__main__":
    main()
```

## Common Module Patterns

### **Class Modules**
```python
# person_module.py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def is_adult(self):
        return self.age >= 18
```

### **Utility Modules**
```python
# math_utils.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

### **Data Modules**
```python
# constants.py
PI = 3.14159
GRAVITY = 9.81
MAX_RETRIES = 3

# config.py
DATABASE_URL = "localhost:5432"
API_KEY = "your_api_key_here"
DEBUG_MODE = True
```

## Debugging Modules

### **Common Issues**
1. **Import errors**: File not found or wrong path
2. **Name errors**: Class not imported correctly
3. **Indentation errors**: Wrong indentation in module files
4. **Main block issues**: Code running when imported

### **Debugging Tips**
1. **Check file locations**: Ensure files are in the same directory
2. **Verify import syntax**: Use correct `from module import class` syntax
3. **Test imports**: Try importing in Python interactive mode
4. **Check file names**: Ensure exact spelling and case matching

## Extension Ideas

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

## Next Steps

After completing this lab, you should be comfortable with:
- Creating modules to organize code
- Importing classes and functions from modules
- Using the `if __name__ == "__main__"` pattern
- Separating concerns between different files
- Following Python module best practices

Move on to more advanced topics like:
- **Lab 9: Error Handling** for robust programs
- **Lab 10: Testing** for code quality
- **Package Development** for distributing code
- **Advanced Import Techniques** for complex projects

---

## **Remember**: 
- Modules help organize and structure your code
- Always use the `if __name__ == "__main__"` pattern for scripts
- Keep modules focused on a single responsibility
- Test imports and functionality after creating modules
- Modules are the foundation of professional Python development

This lab introduces you to one of Python's most important concepts for organizing and scaling your code!
