### **Lab Extension: Advanced Error Handling**

This **extension lab** builds on **Lab: Errors and Exceptions** by introducing:
1. **Logging errors instead of printing them**
2. **Handling multiple exceptions in a single block**
3. **Using `else` and `finally` in try-except blocks**
4. **Retrying a function after an exception**

---

## **Task 3: Logging Errors Instead of Printing Them**
So far, we've been **printing errors**. A better approach is to **log them** so we can track issues in real applications.

### **Step 1: Use the `logging` module**
Modify the `process_input()` function to log errors instead of printing them.

```python
import logging

# Configure logging
logging.basicConfig(filename="errors.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

class InvalidInputError(Exception):
    """Raised when an invalid input is provided."""
    def __init__(self, value, message="Invalid input provided"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.value}"

def process_input(value):
    try:
        if not isinstance(value, int) or value <= 0:
            raise InvalidInputError(value, "Input must be a positive integer")
        print(f"Processing value: {value}")
    except InvalidInputError as e:
        logging.error(e)
        print("An error occurred. Check `errors.log` for details.")

# Test
process_input(-5)  # Logs error instead of printing it
```

🔹 **Why this is useful?**  
- Instead of **cluttering the console**, errors go to **`errors.log`**, making debugging easier.

---

## **Task 4: Handle Multiple Exceptions**
Sometimes, functions raise **different types of errors**. Let’s extend our function to handle multiple exceptions **in a single block**.

### **Step 1: Expand the `process_input()` function**
Modify it to handle **more than just invalid numbers**:
- If the input is **None**, raise a `TypeError`.
- If the input is **too large**, raise a `ValueError`.

```python
def process_input(value):
    try:
        if value is None:
            raise TypeError("Input cannot be None")
        if not isinstance(value, int):
            raise InvalidInputError(value, "Input must be an integer")
        if value <= 0:
            raise InvalidInputError(value, "Input must be positive")
        if value > 1000:
            raise ValueError("Input is too large to process")
        
        print(f"Processing value: {value}")

    except (InvalidInputError, TypeError, ValueError) as e:
        logging.error(e)
        print(f"Error: {e}")

# Test with multiple invalid inputs
process_input(None)   # TypeError
process_input("ten")  # InvalidInputError (not an integer)
process_input(-10)    # InvalidInputError (negative)
process_input(5000)   # ValueError (too large)
```

🔹 **Why this is useful?**  
- **Groups multiple exceptions** in one block.
- **Provides specific error messages** for different cases.

---

## **Task 5: Using `else` and `finally` in Try-Except Blocks**
Python lets us add:
- **`else`** (runs if there’s **no exception**).
- **`finally`** (always runs, even if an error occurs).

### **Step 1: Add `else` and `finally`**
Modify `process_input()` to:
- Print success messages using `else`.
- Always run cleanup code using `finally`.

```python
def process_input(value):
    try:
        if not isinstance(value, int) or value <= 0:
            raise InvalidInputError(value, "Input must be a positive integer")
        
        print(f"Processing value: {value}")

    except InvalidInputError as e:
        logging.error(e)
        print(f"Error: {e}")
    
    else:
        print("Successfully processed input!")  # Runs if no error

    finally:
        print("Cleaning up resources...\n")  # Always runs

# Test cases
process_input(10)  # Works normally
process_input(-5)  # Triggers exception
```

🔹 **Why this is useful?**  
- **`else`** ensures code **only runs if no error occurs**.
- **`finally`** guarantees cleanup happens **no matter what**.

---

## **Task 6: Retrying a Function on Exception**
Sometimes, we need to **retry** when an error occurs.

### **Step 1: Implement retry logic**
Let’s modify `process_input()` to **retry input three times** before failing.

```python
def process_input():
    attempts = 3
    while attempts > 0:
        try:
            value = int(input("Enter a positive number: "))
            if value <= 0:
                raise InvalidInputError(value, "Input must be a positive integer")
            print(f"Processing value: {value}")
            return  # Exit function if successful
        except (InvalidInputError, ValueError) as e:
            print(f"Error: {e}. Attempts left: {attempts - 1}")
            attempts -= 1

    print("Too many failed attempts. Exiting.")
```

🔹 **Why this is useful?**  
- Instead of **failing immediately**, the function allows **three tries**.


