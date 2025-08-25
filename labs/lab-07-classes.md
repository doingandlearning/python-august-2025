# Lab 7: Structuring Data with Classes

### **Objective**
So far, we've been working with headlines as simple strings. This is fine, but as our data gets more complex, it's better to structure it. **Classes** are the perfect tool for this.

The aim of this lab is to create a `Headline` class to hold not just the text of a headline, but also its source. We will then add behavior to this class.

---

## **What are Classes?**

A **class** is a blueprint for creating objects that bundle data (attributes) with functions (methods) that act on that data. Think of it as a template that defines what an object should look like and what it can do.

### **Key Concepts**
- **Class**: The blueprint/template for objects
- **Object**: An instance created from a class
- **Attributes**: Data stored in the object
- **Methods**: Functions that belong to the object
- **Constructor**: Special method that initializes new objects

---

## **Step 1: Defining the `Headline` Class**

### **Tasks**
1. Create a new Python file, e.g., `headline_objects.py`
2. Define a class named `Headline`
3. Create a constructor (`__init__` method) that accepts two arguments
4. Store the arguments as attributes of the object

### **Hints**
- Start with `class Headline:`
- Define the constructor: `def __init__(self, text, source):`
- Inside the constructor, store the arguments as attributes
- The standard way is `self.text = text` and `self.source = source`
- Remember that `self` refers to the object being created

### **Expected Outcomes**
- You should have a working `Headline` class
- The class should accept `text` and `source` parameters
- Objects should store both pieces of information
- You should be able to create `Headline` objects

### **Check Your Work**
- Can you create a `Headline` object with `Headline("Some text", "Some source")`?
- Does the object store both the text and source?
- Can you access the attributes with `object.text` and `object.source`?

---

## **Step 2: Adding a String Representation**

### **Tasks**
1. Add a `__str__` method to your `Headline` class
2. Make the method return a clear, readable string representation
3. Test that printing the object shows useful information

### **Hints**
- Define a new method inside the class: `def __str__(self):`
- This method must `return` a string
- A good representation shows the class name and its attributes
- Consider using an f-string to format the output clearly
- Think about what information would be most helpful when debugging

### **Expected Outcomes**
- Printing a `Headline` object should show readable information
- The output should include both the text and source
- The representation should be clear and unambiguous
- You should no longer see `<__main__.Headline object at 0x...>`

### **Check Your Work**
- Does `print(your_headline_object)` show readable text?
- Can you see both the headline text and source in the output?
- Is the output format clear and helpful?
- Try printing multiple objects to see the difference

---

## **Step 3: Adding Behavior with a Method**

### **Tasks**
1. Create a method `get_word_count()` inside the `Headline` class
2. Make the method return the number of words in the headline's text
3. Test that the method works correctly

### **Hints**
- Define a new method: `def get_word_count(self):`
- The logic is the same as our old standalone function
- Now it uses the object's own data: `self.text`
- The method should `return len(self.text.split())`
- Think about how this method relates to the object's data

### **Expected Outcomes**
- The method should return the correct word count
- It should work with any `Headline` object
- The method should be easy to call on any object
- Results should match manual word counting

### **Check Your Work**
- Does `your_headline.get_word_count()` return the right number?
- Does it work with different headlines (short and long)?
- Can you verify the word count manually?
- Does the method use the object's own text data?

---

## **Step 4: Refactoring Your Code to Use the Class**

### **Tasks**
1. Create a list of `Headline` objects instead of strings
2. Loop through the list and use object methods
3. Print each headline's text and word count
4. Notice how much cleaner the object-oriented approach is

### **Hints**
- Replace your old list of strings with `Headline` objects
- Each object should have text and source information
- Use a loop to process all headlines
- Call methods directly on objects: `h.get_word_count()`
- Think about how this compares to the functional approach

### **Expected Outcomes**
- You should have a list of `Headline` objects
- Each object should have both text and source
- The loop should work with object methods
- Output should show both headline text and word counts
- Code should be cleaner and more organized

### **Check Your Work**
- Do you have a list of `Headline` objects?
- Does each object have text and source attributes?
- Does the loop work correctly with all objects?
- Is the output clear and informative?
- Does the code feel more organized?

---

## **Common Issues to Watch Out For**

### **Class Definition**
- **Missing colon**: Don't forget `:` after `class Headline`
- **Wrong method names**: `__init__` and `__str__` are special names
- **Indentation**: Methods must be indented inside the class
- **Self parameter**: Don't forget `self` as the first parameter

### **Constructor Issues**
- **Missing attributes**: Make sure you store the parameters
- **Wrong attribute names**: Use `self.text` and `self.source`
- **Parameter order**: Check that you're passing arguments in the right order
- **Object creation**: Test creating objects with different values

### **Method Problems**
- **Missing return**: `__str__` must return a string
- **Wrong data access**: Use `self.text` to access the object's text
- **Method calls**: Remember to call methods on objects, not the class
- **Attribute access**: Use `object.attribute` to access data

---

## **Testing Your Solutions**

### **Test Data**
Create test headlines with different sources:
- "General election: Labour and Tories clash over tax" from "BBC News"
- "England crowned T20 world champions" from "Sky Sports"
- "Summer travel chaos feared as airline strikes loom" from "The Guardian"

### **Test Scenarios**
1. **Object Creation**: Test creating `Headline` objects
2. **Attribute Access**: Verify text and source are stored correctly
3. **String Representation**: Check that printing shows useful information
4. **Method Functionality**: Test `get_word_count()` with different headlines
5. **List Processing**: Verify the loop works with multiple objects

### **Expected Results**
- Objects should store both text and source
- `print(headline)` should show clear information
- `headline.get_word_count()` should return correct numbers
- Loop should process all objects correctly

---

## **Extension Ideas (Optional)**

### **Additional Methods**
- **`get_character_count()`**: Return the total character count
- **`get_source()`**: Return just the source information
- **`is_long_headline()`**: Return True if word count > 8
- **`contains_keyword(keyword)`**: Check if headline contains a specific word

### **Enhanced Functionality**
- **Multiple sources**: Add more news sources to your list
- **Data validation**: Check that text is not empty
- **Source categories**: Group headlines by source type
- **Statistics**: Calculate average word count by source

### **Advanced Features**
- **Date attributes**: Add publication date to headlines
- **Category classification**: Add topic categories
- **Comparison methods**: Compare headlines by length or content
- **Export functionality**: Save headlines to a file

---

## **Solutions**

**Complete code examples for all exercises are available in the `solutions/lab-07` folder.**

- `solutions/headline_objects.py` - Complete solution with all class features

---

## **Why Classes?**

Classes are powerful because they:
- **Organize code** - Group related data and functions together
- **Reduce duplication** - Create reusable templates for objects
- **Improve readability** - Code is more self-documenting
- **Enable inheritance** - Build new classes from existing ones
- **Follow OOP principles** - Encapsulation, inheritance, polymorphism

---

## **Real-World Applications**

Classes are used everywhere in Python:
- **Data structures**: Lists, dictionaries, sets are all classes
- **File handling**: File objects are class instances
- **Web frameworks**: Django, Flask use classes extensively
- **Data science**: Pandas DataFrames are class instances
- **GUI programming**: Tkinter widgets are class objects

---

**Remember**: 
- Start with simple classes and build complexity gradually
- Always test object creation and method calls
- Use meaningful attribute and method names
- Think about what data and behavior belong together
- Classes are the foundation of object-oriented programming

This lab introduces you to one of Python's most important concepts for organizing and structuring code!
