# Lab 7: Structuring Data with Classes - Solutions

This folder contains complete solutions for Lab 7: Structuring Data with Classes. These solutions demonstrate how to create and use classes in Python for object-oriented programming.

## Files Overview

### Complete Solution

1. **`headline_objects.py`** - Complete working program with all class features
   - Demonstrates all steps from the lab
   - Includes additional methods and functionality
   - Ready to run and explore classes

### Step-by-Step Solutions

2. **`step_01_class_definition.py`** - Step 1: Basic class definition and constructor
   - Shows how to define a class with `__init__` method
   - Demonstrates creating objects and accessing attributes
   - Basic class structure and object creation

3. **`step_02_string_representation.py`** - Step 2: Adding the `__str__` method
   - Shows how to add string representation to objects
   - Demonstrates the `__str__` method for readable output
   - Testing string representation in different contexts

4. **`step_03_adding_methods.py`** - Step 3: Adding custom methods
   - Shows how to add behavior to classes
   - Demonstrates the `get_word_count()` method
   - Testing methods and edge cases

5. **`step_04_using_classes.py`** - Step 4: Using classes in practice
   - Shows how to work with lists of objects
   - Demonstrates object-oriented vs. functional approaches
   - Advanced functionality and statistics

## How to Use These Solutions

### For Learning
1. **Try the lab exercises yourself first** - don't peek at solutions until you're stuck!
2. **Compare your code** with the solutions to see different approaches
3. **Experiment** with the code - add new methods, modify attributes
4. **Run each step file** to see how classes build up gradually

### For Reference
- Use these as templates for similar class designs
- Study the class structure and method implementation
- Note the docstring documentation and commenting
- See how different object-oriented patterns work

## Running the Programs

All programs can be run from the command line:

```bash
python headline_objects.py
python step_01_class_definition.py
python step_02_string_representation.py
python step_03_adding_methods.py
python step_04_using_classes.py
```

## Key Concepts Demonstrated

### **Class Fundamentals**
- **Class Definition**: Using `class` keyword to create blueprints
- **Constructor**: `__init__` method for object initialization
- **Attributes**: Storing data in objects with `self.attribute`
- **Methods**: Functions that belong to objects
- **Objects**: Instances created from classes

### **Special Methods**
- **`__init__`**: Constructor method for object initialization
- **`__str__`**: String representation method for readable output
- **`self`**: Reference to the current object instance
- **Method calls**: Using `object.method()` syntax

### **Object-Oriented Programming**
- **Encapsulation**: Bundling data and behavior together
- **Data access**: Using `object.attribute` to access data
- **Method calls**: Using `object.method()` to call functions
- **Object creation**: Using `ClassName()` to create instances

## Concepts Used (Lab 7 Appropriate)

These solutions use concepts appropriate for Lab 7:
- Class definition with `class` keyword
- Constructor method with `__init__`
- Special methods like `__str__`
- Object creation and instantiation
- Attribute access and method calls
- Basic string operations and methods
- List operations and loops

## Sample Output

When you run the complete program, you'll see:

```
Lab 7: Structuring Data with Classes
==================================================

Step 1: Creating Headline Objects
----------------------------------------
Created headline objects:
1. Headline(text='General election: Labour and Tories clash over tax', source='BBC News')
2. Headline(text='England crowned T20 world champions', source='Sky Sports')
3. Headline(text='Summer travel chaos feared as airline strikes loom', source='The Guardian')

Step 2: String Representation
----------------------------
Printing headline objects:
Headline(text='General election: Labour and Tories clash over tax', source='BBC News')
Headline(text='England crowned T20 world champions', source='Sky Sports')
Headline(text='Summer travel chaos feared as airline strikes loom', source='The Guardian')

Step 3: Testing Methods
-----------------------
Word counts:
Headline 1: 8 words
Headline 2: 4 words
Headline 3: 8 words

Step 4: Working with a List of Headline Objects
-----------------------------------------------
Processing all headlines:
 1. ( 8 words) [BBC News] General election: Labour and Tories clash over tax
 2. ( 4 words) [Sky Sports] England crowned T20 world champions
 3. ( 8 words) [The Guardian] Summer travel chaos feared as airline strikes loom
...
```

## Class Examples

### Basic Class Definition (Step 1)
```python
class Headline:
    def __init__(self, text, source):
        self.text = text
        self.source = source
```

### String Representation (Step 2)
```python
def __str__(self):
    return f"Headline(text='{self.text}', source='{self.source}')"
```

### Custom Methods (Step 3)
```python
def get_word_count(self):
    return len(self.text.split())
```

### Using Objects (Step 4)
```python
headlines = [
    Headline("Some text", "Some source"),
    Headline("More text", "Another source")
]

for headline in headlines:
    count = headline.get_word_count()
    print(f"{headline.text}: {count} words")
```

## Understanding Classes

### **The Class Structure**
Classes follow this basic pattern:
```python
class ClassName:
    def __init__(self, param1, param2):
        self.attribute1 = param1
        self.attribute2 = param2
    
    def method_name(self):
        # Method implementation
        return result
```

### **Object Creation and Usage**
```python
# Create an object
my_object = ClassName("value1", "value2")

# Access attributes
print(my_object.attribute1)

# Call methods
result = my_object.method_name()
```

### **Key Benefits of Classes**
- **Organization**: Group related data and functions together
- **Reusability**: Create multiple objects from the same template
- **Maintainability**: Easier to modify and extend code
- **Readability**: Code is more self-documenting
- **Encapsulation**: Data and behavior are bundled together

## Common Class Patterns

### **Data Classes**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def is_adult(self):
        return self.age >= 18
```

### **Utility Classes**
```python
class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
```

### **Collection Classes**
```python
class HeadlineCollection:
    def __init__(self):
        self.headlines = []
    
    def add_headline(self, headline):
        self.headlines.append(headline)
    
    def get_total_words(self):
        return sum(h.get_word_count() for h in self.headlines)
```

## Debugging Classes

### **Common Issues**
1. **Missing `self`**: Don't forget `self` as the first parameter
2. **Indentation errors**: Methods must be indented inside the class
3. **Attribute errors**: Make sure attributes are defined in `__init__`
4. **Method calls**: Remember to call methods on objects, not the class

### **Debugging Tips**
1. **Print objects**: Use `print(object)` to see the string representation
2. **Check attributes**: Verify `object.attribute` works
3. **Test methods**: Call methods individually to isolate issues
4. **Use `dir()`**: See all available attributes and methods

## Extension Ideas

### **Additional Methods**
- **`get_character_count()`**: Return total character count
- **`is_long_headline()`**: Check if headline is long
- **`contains_keyword(keyword)`**: Search for specific words
- **`get_source()`**: Return just the source information

### **Enhanced Functionality**
- **Data validation**: Check that text is not empty
- **Source categories**: Group by source type
- **Statistics methods**: Calculate averages and totals
- **Export methods**: Save to files or databases

### **Advanced Features**
- **Inheritance**: Create specialized headline types
- **Class methods**: Methods that work on the class itself
- **Static methods**: Utility functions that don't need object data
- **Properties**: Controlled attribute access

## Next Steps

After completing this lab, you should be comfortable with:
- Defining classes with constructors
- Adding methods to classes
- Creating and using objects
- Understanding the object-oriented approach
- Choosing when to use classes vs. functions

Move on to more advanced topics like:
- **Lab 8: Modules** for code organization
- **Lab 9: Error Handling** for robust programs
- **Advanced OOP** for inheritance and polymorphism
- **Design Patterns** for common programming solutions

---

**Remember**: 
- Classes are templates for creating objects
- Always define `__init__` to set up object attributes
- Use `self` to refer to the current object
- Methods belong to objects, not the class itself
- Classes help organize related data and behavior

This lab introduces you to one of Python's most important concepts for organizing and structuring code!
