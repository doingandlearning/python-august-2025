# Lab 9: Error Handling

### **Objective**
Even a perfect program can crash if it receives unexpected input. **Error handling** is the process of anticipating these situations and dealing with them gracefully instead of letting the program crash.

The aim of this lab is to make our "Channel Guessing Game" more robust by using a `try...except` block to handle invalid user input.

---

## **What is Error Handling?**

**Error handling** is a programming technique that allows your program to continue running even when it encounters problems. Instead of crashing, the program can catch errors, handle them appropriately, and continue with its normal operation.

### **Key Concepts**
- **Exception**: An error that occurs during program execution
- **Try Block**: Code that might cause an error
- **Except Block**: Code that handles the error if it occurs
- **Graceful Degradation**: Program continues running despite errors
- **User Experience**: Better interaction when things go wrong

---

## **Step 1: Find the Bug**

### **Tasks**
1. Get a working copy of your "Channel Guessing Game" from Lab 3
2. Run the script and identify where it can crash
3. Understand what causes the `ValueError` to occur

### **Hints**
- Make sure you have a working guessing game from Lab 3
- Run the script and play the game normally first
- When prompted to "Please guess a channel number:", try entering non-numeric input
- Think about what happens when `int()` tries to convert text to a number
- Consider what types of input could cause problems

### **Expected Outcomes**
- You should be able to identify where the program crashes
- You should see a `ValueError` message when entering invalid input
- The program should stop running when the error occurs
- You should understand why the error happens

### **Check Your Work**
- Does your guessing game run normally with valid numbers?
- Does it crash when you enter text like "five" or "abc"?
- Do you see a `ValueError` message?
- Can you identify which line of code causes the crash?

---

## **Step 2: Implement the `try...except` Block**

### **Tasks**
1. Wrap the risky code in a `try` block
2. Add an `except` block to handle `ValueError`
3. Provide a friendly error message to the user
4. Use `continue` to give the user another chance

### **Hints**
- Find the line that converts user input to an integer
- This line is risky because `input()` could return anything
- Wrap the risky code in a `try` block
- Add an `except ValueError:` block to catch the specific error
- Print a helpful message when the error occurs
- Use `continue` to skip to the next loop iteration
- Think about what should happen when invalid input is entered

### **Expected Outcomes**
- Your program should no longer crash on invalid input
- It should display a friendly error message
- The game should continue running and give another chance
- Users should be able to enter text, symbols, and numbers without crashes

### **Check Your Work**
- Does your program handle text input gracefully?
- Does it show a helpful error message?
- Does the game continue running after invalid input?
- Can you play the game normally with valid numbers?
- Does the error handling work for different types of invalid input?

---

## **Common Issues to Watch Out For**

### **Try-Except Structure**
- **Missing colon**: Don't forget `:` after `try` and `except`
- **Wrong indentation**: Code inside blocks must be properly indented
- **Missing except block**: Every `try` needs at least one `except`
- **Wrong exception type**: Make sure you're catching `ValueError`, not other errors

### **Logic Errors**
- **Wrong placement**: Put only the risky code in the `try` block
- **Missing continue**: Without `continue`, the program might process invalid input
- **Unclear messages**: Error messages should help users understand what went wrong
- **Infinite loops**: Make sure the error handling doesn't create endless loops

### **User Experience**
- **Unhelpful messages**: Error messages should guide users to correct input
- **No recovery**: Program should give users another chance to input correctly
- **Confusing behavior**: Error handling should be predictable and consistent

---

## **Testing Your Solutions**

### **Test Scenarios**
1. **Valid Input**: Test with normal numbers (1, 25, 50)
2. **Text Input**: Test with words ("five", "abc", "hello")
3. **Symbols**: Test with special characters ("@", "#", "!")
4. **Empty Input**: Test with just pressing Enter
5. **Mixed Input**: Test with combinations ("5abc", "abc5")

### **Expected Results**
- Valid numbers should work normally
- Invalid input should show error messages
- Game should continue running after errors
- Users should get multiple chances to input correctly
- No crashes should occur

### **Verification Steps**
1. **Run the game** and test with valid numbers
2. **Test error cases** with various invalid inputs
3. **Check error messages** for clarity and helpfulness
4. **Verify game flow** continues normally after errors
5. **Test edge cases** like empty input or very long text

---

## **Extension Ideas (Optional)**

### **Enhanced Error Handling**
- **Range validation**: Check if numbers are within 1-50 range
- **Multiple error types**: Handle different types of invalid input
- **Input sanitization**: Clean up user input before processing
- **Retry limits**: Limit how many times users can enter invalid input

### **Helper Functions**
- **`get_guess()`**: Create a function to handle input and validation
- **`validate_input()`**: Separate function for input validation
- **`display_error()`**: Function to show user-friendly error messages
- **`get_user_input()`**: Centralized input handling function

### **Custom Exceptions**
- **`ChannelError`**: Create your own exception class
- **`OutOfRangeError`**: Specific exception for invalid ranges
- **`InvalidInputError**`: Exception for malformed input
- **Exception hierarchy**: Build a family of related exceptions

---

## **Solutions**

**Complete code examples for all exercises are available in the `solutions/lab-09` folder.**

- `solutions/error_handling_game.py` - Complete solution with error handling
- `solutions/step_by_step/` - Individual step solutions

---

## **Why Error Handling?**

Error handling is powerful because it:
- **Prevents crashes** - Programs continue running despite problems
- **Improves user experience** - Users get helpful feedback instead of crashes
- **Makes programs robust** - Code can handle unexpected situations
- **Enables debugging** - Better understanding of what went wrong
- **Follows best practices** - Professional programming standards

---

## **Real-World Applications**

Error handling is used everywhere in Python:
- **Web applications**: Handle invalid form submissions gracefully
- **File processing**: Deal with missing or corrupted files
- **API interactions**: Handle network errors and invalid responses
- **User interfaces**: Provide feedback for invalid user actions
- **Data processing**: Handle malformed or unexpected data

---

## **Error Handling Best Practices**

### **Specific Exceptions**
- **Catch specific errors**: Use `except ValueError:` not `except:`
- **Handle different errors**: Different exceptions need different handling
- **Avoid bare except**: Don't catch all errors without knowing what they are
- **Log errors**: Keep track of what went wrong for debugging

### **User Experience**
- **Clear messages**: Tell users exactly what went wrong
- **Helpful guidance**: Suggest how to fix the problem
- **Graceful recovery**: Give users another chance when possible
- **Consistent behavior**: Handle errors the same way throughout

---

**Remember**: 
- Start with simple error handling and build complexity gradually
- Always test your error handling with various types of invalid input
- Make error messages helpful and user-friendly
- Use specific exception types, not generic error catching
- Error handling is essential for professional, user-friendly programs

This lab introduces you to one of Python's most important concepts for building robust, user-friendly applications!
