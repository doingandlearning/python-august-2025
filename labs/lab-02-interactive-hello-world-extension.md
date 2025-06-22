# **Lab 2: Extended Exploration of Types**

## **Objective**
This lab extends the concepts covered in Lab 2 by exploring built-in methods for strings and numbers, working with type conversion, and improving string formatting. 

This lab consists of **four steps**:
1. **Exploring String Methods**
2. **Exploring Number Methods**
3. **Advanced String Formatting**

---

## **Step 1: Exploring String Methods**

Modify your program to **input a string** and apply various string methods to manipulate and analyze the input.

Example:
```python
user_string = input("Enter a sentence: ")

print(f"Uppercase: {user_string.upper()}")
print(f"Lowercase: {user_string.lower()}")
print(f"Title Case: {user_string.title()}")
print(f"Stripped: {user_string.strip()}")
print(f"Words in string: {user_string.split()}")
print(f"Replaced spaces with underscores: {user_string.replace(' ', '_')}")
print(f"Starts with 'Hello'? {user_string.startswith('Hello')}")
print(f"Ends with a question mark? {user_string.endswith('?')}")
print(f"Number of occurrences of 'e': {user_string.count('e')}")
print(f"First occurrence of 'e': {user_string.find('e')}")
```

### **Tasks**
1. Experiment with different string methods by using `help(str)`.
2. Modify the program to check if the input is **alphabetic (`isalpha()`), alphanumeric (`isalnum()`), or numeric (`isnumeric()`)**.

---

## **Step 2: Exploring Number Methods**
Modify the number input from **Step 2 of the original lab** to include numeric method explorations.

```python
num = float(input("Enter a decimal number: "))

print(f"Rounded: {round(num, 2)}")
print(f"Is it an integer? {num.is_integer()}")
print(f"Hexadecimal representation: {num.hex()}")
print(f"As an integer ratio: {num.as_integer_ratio()}")
```

### **Tasks**
1. Try entering whole numbers and decimal numbers. Observe how `is_integer()` behaves.
2. Convert a float to an integer and explore potential data loss.

---

## **Step 3: Advanced String Formatting**
Instead of simple concatenation, **use f-strings with formatting options**.

```python
app_version = 1.234567

# Aligning text
print(f"Left aligned: {'Hello':<20} World")
print(f"Right aligned: {'Hello':>20} World")
print(f"Centered: {'Hello':^20}")

# Formatting numbers
print(f"Version number rounded: {app_version:.2f}")
print(f"Binary representation: {42:08b}")
print(f"Percentage: {0.75:.1%}")
```

### **Tasks**
1. Modify the code to print **currency format (e.g., £123.45)**.
2. Print numbers in **scientific notation** (`:.2e`).

---
