# Lab 11: Reading Data From a File

### **Objective**
Our program is great, but having the data hard-coded inside the script is inflexible. Real-world programs almost always load their data from external files.

The aim of this lab is to modify our program to read headlines from the `headlines.csv` file using Python's built-in `csv` module.

---

## **What is File I/O?**

**File I/O (Input/Output)** is the process of reading data from files and writing data to files. This is essential for real-world applications because it allows programs to work with external data sources and persist information between program runs.

### **Key Concepts**
- **File Operations**: Opening, reading, writing, and closing files
- **CSV Format**: Comma-separated values for structured data
- **Data Loading**: Reading external data into your program
- **Separation of Concerns**: Data storage separate from program logic
- **Error Handling**: Managing file operations safely
- **Resource Management**: Properly closing files after use

---

## **Step 1: Getting Started**

### **Tasks**
1. Import the csv module in your script
2. Prepare an empty list for storing headlines
3. Remove or comment out the hard-coded headlines list
4. Ensure the CSV file is accessible

### **Hints**
- You'll be modifying the `main_analysis.py` script from the modules lab
- Look for the `import` statement section at the top of your file
- Find the hard-coded `headlines` list in your `main()` function
- Think about where to place the empty list declaration
- Make sure `headlines.csv` is in the same directory as your Python script

### **Expected Outcomes**
- The csv module is imported at the top of your script
- The hard-coded headlines list is removed or commented out
- An empty headlines list is created in the main function
- The CSV file is accessible from your script's location

### **Check Your Work**
- Is `import csv` at the top of your file?
- Have you removed or commented out the old headlines list?
- Is there an empty `headlines = []` list in your main function?
- Can you see the `headlines.csv` file in the same directory?

---

## **Step 2: Open and Read the File**

### **Tasks**
1. Open the CSV file using the `with` statement
2. Create a CSV reader object
3. Skip the header row
4. Set up a loop to process each data row

### **Hints**
- Use the `with open(...)` syntax for safe file handling
- Set the mode to `'r'` for reading
- Include `newline=''` parameter for proper CSV handling
- Consider adding `encoding='utf-8'` for text compatibility
- Create a CSV reader object using `csv.reader()`
- Use `next()` to skip the header row
- Think about the structure of your CSV file

### **Expected Outcomes**
- The CSV file opens successfully without errors
- A CSV reader object is created
- The header row is skipped
- A loop is set up to process each data row
- File is automatically closed when the `with` block ends

### **Check Your Work**
- Does your file open without errors?
- Is the CSV reader object created correctly?
- Is the header row being skipped?
- Is there a loop set up to process the data?
- Does the file close automatically?

---

## **Step 3: Create Objects from File Data**

### **Tasks**
1. Extract text and source from each row
2. Create Headline objects from the file data
3. Add each object to the headlines list
4. Verify the data is loaded correctly

### **Hints**
- Each row is a list of strings
- The first element `row[0]` contains the headline text
- The second element `row[1]` contains the source
- Create Headline objects using the extracted data
- Use the `append()` method to add objects to your list
- Think about the order of operations in your loop

### **Expected Outcomes**
- Headline objects are created from each row of data
- Each object has the correct text and source
- All objects are added to the headlines list
- The list contains the same number of objects as data rows
- The rest of your analysis code works with the loaded data

### **Check Your Work**
- Are Headline objects being created correctly?
- Does each object have the right text and source?
- Are all objects being added to the headlines list?
- Does your analysis code still work with the loaded data?
- Is the data being read from the file instead of hard-coded?

---

## **Common Issues to Watch Out For**

### **File Operations**
- **Wrong file path**: Make sure the CSV file is in the right location
- **File permissions**: Ensure you have read access to the file
- **File encoding**: Use appropriate encoding for text files
- **File not found**: Check the file name and location carefully

### **CSV Processing**
- **Header handling**: Remember to skip the header row
- **Row structure**: Understand how CSV data is organized
- **Data types**: CSV data comes as strings, convert if needed
- **Empty rows**: Handle cases where rows might be empty

### **Object Creation**
- **Wrong indices**: Make sure you're using the right row positions
- **Missing data**: Check that all required data is present
- **Object instantiation**: Verify Headline objects are created correctly
- **List management**: Ensure objects are properly added to the list

### **Integration Issues**
- **Import problems**: Make sure the Headline class is imported
- **Variable scope**: Ensure headlines list is accessible where needed
- **Data flow**: Verify data moves correctly through your program
- **Error handling**: Consider what happens if the file can't be read

---

## **Testing Your Solutions**

### **Test Scenarios**
1. **Basic file reading**: Verify the CSV file opens and reads
2. **Data extraction**: Check that text and source are extracted correctly
3. **Object creation**: Ensure Headline objects are created properly
4. **List population**: Verify all objects are added to the headlines list
5. **Integration**: Test that existing analysis code still works

### **Expected Results**
- CSV file opens without errors
- All rows are processed (except header)
- Headline objects are created with correct data
- Headlines list contains all objects from the file
- Analysis functions work with the loaded data
- No hard-coded data remains in the program

### **Verification Steps**
1. **Run your program** and check for errors
2. **Verify file reading** - check console output for file operations
3. **Inspect the headlines list** - print its length and contents
4. **Test analysis functions** - ensure they work with loaded data
5. **Check data accuracy** - compare with the original CSV file

---

## **Extension Ideas (Optional)**

### **Enhanced File Handling**
- **Error handling**: Add try-except blocks for file operations
- **File validation**: Check if the file exists before opening
- **Data validation**: Verify CSV structure and content
- **Multiple file support**: Handle different CSV files

### **Data Processing**
- **Data cleaning**: Remove extra whitespace or invalid characters
- **Data filtering**: Skip rows that don't meet certain criteria
- **Data transformation**: Modify data as it's loaded
- **Data statistics**: Show information about the loaded data

### **User Experience**
- **Progress indicators**: Show loading progress for large files
- **File selection**: Allow users to choose which file to load
- **Configuration**: Make file paths configurable
- **Logging**: Record file operations for debugging

---

## **Running Your Program**

### **Basic Execution**
- Make sure `headlines.csv` is in the same directory
- Run your modified `main_analysis.py` script
- Check that data is loaded from the file
- Verify that analysis results are correct

### **Troubleshooting**
- **File not found**: Check file name and location
- **Import errors**: Verify Headline class import
- **Data issues**: Check CSV file format and content
- **Logic errors**: Ensure data flows correctly through your program

---

## **Why File I/O?**

File I/O is powerful because it:
- **Separates data from code** - Data can be updated without changing code
- **Enables data persistence** - Information survives between program runs
- **Supports external data sources** - Work with data from other systems
- **Improves flexibility** - Programs can work with different datasets
- **Enables automation** - Process files without manual data entry
- **Supports collaboration** - Multiple people can work with the same data

---

## **Real-World Applications**

File I/O is used everywhere in Python:
- **Data analysis**: Loading datasets from CSV, Excel, or database files
- **Web applications**: Reading configuration files and user data
- **Automation scripts**: Processing log files and reports
- **Scientific computing**: Loading experimental data and results
- **Business applications**: Processing customer data and transactions
- **System administration**: Reading configuration and log files

---

## **File Handling Best Practices**

### **Safe File Operations**
- **Use with statements**: Automatic file closing and error handling
- **Specify encoding**: Handle text files properly
- **Check file existence**: Verify files exist before opening
- **Handle errors gracefully**: Provide meaningful error messages

### **Data Processing**
- **Validate input**: Check data structure and content
- **Handle edge cases**: Empty files, missing data, malformed content
- **Process efficiently**: Read only what you need
- **Clean up resources**: Ensure files are properly closed

### **Code Organization**
- **Separate concerns**: Keep file I/O separate from business logic
- **Reusable functions**: Create functions for common file operations
- **Clear naming**: Use descriptive variable and function names
- **Documentation**: Explain file format and processing logic

---

## **Solutions**

**Complete code examples for all exercises are available in the `solutions/lab-11` folder.**

- `solutions/file_reader.py` - Complete solution with file reading
- `solutions/step_by_step/` - Individual step solutions

---

**Remember**: 
- Start with basic file operations and build complexity gradually
- Always test your file reading with small, known datasets
- Use appropriate error handling for file operations
- Keep file I/O separate from your main program logic
- File handling is essential for building real-world applications

This lab introduces you to one of the most important concepts in Python programming - reading data from external files! 