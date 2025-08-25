# Lab Z: Final Case Study - Live News Analysis

### **Objective**
In this final case study, you will bring together all the skills you have learned in this course to build a complete news analysis application.

You'll be reading live news data from the internet, processing it using a class you design, performing analysis, and writing a report to a file.

---

## **What is a Case Study?**

**Case studies** are comprehensive projects that integrate multiple concepts and skills into a single, real-world application. They demonstrate how individual programming concepts work together to solve complex problems and provide practical experience with industry-standard development practices.

### **Key Concepts**
- **Integration**: Combining multiple programming concepts
- **Real-world Application**: Building practical, useful programs
- **API Integration**: Working with external data sources
- **Data Processing**: Analyzing and transforming information
- **Report Generation**: Creating output files with results
- **Professional Development**: Industry-standard coding practices

---

## **The Goal**

Your task is to fetch recent news headlines from a live API, analyze the sources of these headlines, and generate a `report.txt` file that summarizes how many headlines came from each source.

### **Expected Output**
The final output, `report.txt`, should look something like this:

```
--- NEWS SOURCE REPORT ---
There are 40 total headlines.
The following sources were found:

* BBC News: 10 headlines
* Reuters: 8 headlines
* The Guardian: 7 headlines
* ...and so on for all sources
```

---

## **Core Concepts Review**

This lab will require you to use:

- **File I/O:** To write your final report
- **APIs & Networking:** To fetch the live headline data
- **Lists & Dictionaries:** To store and analyze the data
- **Classes:** To structure your headline data neatly
- **Functions:** To organize your code into logical, reusable blocks
- **Modules:** To keep your code clean and separated

---

## **Setup: API Key and 'requests' library**

### **Tasks**
1. Install the requests library for HTTP operations
2. Obtain a NewsAPI key for accessing news data
3. Set up your development environment

### **Hints**
- Use pip to install the requests library
- The NewsAPI service requires registration for an API key
- Ensure your Python environment is properly configured
- Test that you can import the requests library

### **Expected Outcomes**
- Requests library is successfully installed
- API key is obtained and ready for use
- Development environment is properly configured
- Basic imports work without errors

### **Check Your Work**
- Can you import the requests library?
- Do you have a valid API key?
- Is your Python environment working correctly?
- Can you run basic Python scripts?

---

## **Step 1: The `headline_module.py`**

### **Tasks**
1. Create a file named `headline_module.py`
2. Define the `Headline` class with required methods
3. Ensure the class meets all specifications

### **Hints**
- This step is the same as from the Modules and Testing labs
- You can copy the class you created in the Classes lab
- Focus on clean, well-structured class definition
- Test that your class works correctly

### **Expected Outcomes**
- `headline_module.py` file is created
- `Headline` class has proper `__init__` method
- `__str__` method returns formatted string
- Class can be imported and used in other files

### **Check Your Work**
- Does the file exist with the correct name?
- Can you create Headline objects?
- Does the `__str__` method work correctly?
- Can you import the class from other files?

---

## **Step 2: The `main_analysis.py`**

### **Tasks**
1. Create a second file named `main_analysis.py`
2. Import the Headline class from your module
3. Import the requests library
4. Set up the basic file structure

### **Hints**
- This will contain the main logic of your application
- Start with basic imports and file structure
- Plan the organization of your functions
- Think about how to structure the main function

### **Expected Outcomes**
- `main_analysis.py` file is created
- Required imports are working correctly
- Basic file structure is in place
- Ready for implementing the main logic

### **Check Your Work**
- Does the file exist with the correct name?
- Can you import the Headline class?
- Can you import the requests library?
- Is the basic file structure ready?

---

## **Step 3: Fetching the Data from the API**

### **Tasks**
1. Create a function to load headlines from the API
2. Handle API requests and responses
3. Process JSON data into Headline objects
4. Implement proper error handling

### **Hints**
- Use the NewsAPI endpoint: `https://newsapi.org/v2/top-headlines`

The data comes back in a format called **JSON**. It will look something like this:

```json
{
  "status": "ok",
  "totalResults": 38,
  "articles": [
    {
      "source": { "id": "bBC-news", "name": "BBC News" },
      "author": "BBC News",
      "title": "UK economy grows more slowly than expected in January - BBC News",
      "description": "The economy grew by 0.8% at the start of the year, but is still smaller than before the pandemic.",
      "url": "https://www.bbc.co.uk/news/business-60706216",
      "urlToImage": "https://ichef.bbci.co.uk/news/1024/branded_news/1547F/production/_123633538_mediaitem123633537.jpg",
      "publishedAt": "2022-03-11T07:49:35Z",
      "content": "By Faisal Islam, economics editor"
    },
    {
       "source": { "id": "reuters", "name": "Reuters" },
       "author": null,
       "title": "ECB to stop bond-buying,..."
       /* ... more fields ... */
    }
  ]
}

- Create a `params` dictionary with sources and API key
- Use `requests.get()` with your parameters
- Handle the JSON response structure carefully
- Extract title and source name from nested data
- Use `.get()` method to avoid errors with missing keys

### **Expected Outcomes**
- Function successfully fetches data from the API
- JSON response is properly parsed
- Headline objects are created from API data
- Error handling manages API failures gracefully
- List of Headline objects is returned

### **Check Your Work**
- Does the function accept an API key parameter?
- Does it make a successful API request?
- Are Headline objects created correctly?
- Is error handling working for failed requests?
- Does the function return the expected data structure?

---

## **Step 4: Analyzing the Sources**

### **Tasks**
1. Create a function to analyze headline sources
2. Count headlines from each source
3. Return a dictionary with source counts
4. Handle edge cases and data validation

### **Hints**
- Loop through your list of Headline objects
- Check if each source is already in your results dictionary
- Increment existing counts or add new sources
- Think about how to handle missing or invalid source data
- Consider the structure of your output dictionary

### **Expected Outcomes**
- Function processes list of Headline objects
- Dictionary is created with source names as keys
- Count values represent number of headlines per source
- All sources are properly counted
- Edge cases are handled gracefully

### **Check Your Work**
- Does the function accept a headlines list?
- Is the output dictionary structured correctly?
- Are all sources being counted properly?
- Does it handle empty or invalid data?
- Is the return value in the expected format?

---

## **Step 5: Generating the Report**

### **Tasks**
1. Create a function to generate the report string
2. Format the analysis data into readable text
3. Include header information and source breakdown
4. Structure the output for file writing

### **Hints**
- Start with a header string for your report
- Loop through the analysis dictionary items
- Format each source and count consistently
- Consider the final format of your report.txt file
- Think about readability and presentation

### **Expected Outcomes**
- Function creates a formatted report string
- Header includes total headline count
- Each source is listed with its count
- Output is properly formatted for file writing
- Report structure matches the expected format

### **Check Your Work**
- Does the function accept analysis data and total count?
- Is the output string properly formatted?
- Does it include all required information?
- Is the format suitable for writing to a file?
- Does the structure match the expected output?

---

## **Step 6: Putting It All Together**

### **Tasks**
1. Create a main function to orchestrate the entire process
2. Integrate all the functions you've created
3. Handle the complete workflow from API to report
4. Implement proper error handling and user feedback

### **Hints**
- Store your API key securely in the main function
- Call your functions in the correct order
- Check for successful data retrieval
- Write the report to `report.txt` with proper encoding
- Provide clear feedback about the process

### **Expected Outcomes**
- Main function coordinates all operations
- API data is successfully fetched and processed
- Analysis is performed on the headline data
- Report is generated and written to file
- User receives confirmation of successful completion

### **Check Your Work**
- Does the main function call all required functions?
- Is the API key properly stored and used?
- Does the complete workflow execute successfully?
- Is the report.txt file created with correct content?
- Does the program provide appropriate user feedback?

---

## **Common Issues to Watch Out For**

### **API Integration**
- **Invalid API key**: Ensure your key is correct and active
- **Rate limiting**: Be aware of API usage restrictions
- **Network errors**: Handle connection failures gracefully
- **Response validation**: Check API response structure

### **Data Processing**
- **Missing data**: Handle cases where fields are empty
- **Data types**: Ensure proper conversion of API data
- **Nested structures**: Navigate complex JSON responses carefully
- **Error handling**: Implement robust error management

### **File Operations**
- **File permissions**: Ensure write access to create report.txt
- **Encoding issues**: Use UTF-8 for special characters
- **Path problems**: Verify file creation location
- **Error handling**: Manage file write failures

### **Integration Issues**
- **Function dependencies**: Ensure proper function calling order
- **Data flow**: Verify data moves correctly between functions
- **Error propagation**: Handle errors at appropriate levels
- **Resource cleanup**: Ensure proper cleanup of resources

---

## **Testing Your Solutions**

### **Test Scenarios**
1. **API Connection**: Verify successful API requests
2. **Data Processing**: Check headline object creation
3. **Source Analysis**: Validate source counting logic
4. **Report Generation**: Test report formatting
5. **File Writing**: Confirm report.txt creation
6. **End-to-End**: Test complete workflow

### **Expected Results**
- API requests return valid data
- Headline objects are created correctly
- Source analysis produces accurate counts
- Report is properly formatted
- File is written successfully
- Complete workflow executes without errors

### **Verification Steps**
1. **Run your program** and check for errors
2. **Verify API response** - check data structure and content
3. **Inspect headline objects** - verify attributes and methods
4. **Check source analysis** - confirm counting accuracy
5. **Review report.txt** - verify format and content
6. **Test error conditions** - ensure graceful failure handling

---

## **Extension Ideas (Optional)**

### **Enhanced API Integration**
- **Multiple sources**: Fetch from different news sources
- **Caching**: Implement data caching to reduce API calls
- **Filtering**: Add date or category filtering
- **Pagination**: Handle large result sets

### **Advanced Analysis**
- **Trend analysis**: Identify patterns in news sources
- **Content analysis**: Analyze headline content and topics
- **Time-based analysis**: Group headlines by publication time
- **Source reliability**: Implement source credibility scoring

### **User Experience**
- **Interactive interface**: Add user input for search terms
- **Multiple reports**: Generate different report formats
- **Configuration**: Make API keys and sources configurable
- **Logging**: Add detailed operation logging

---

## **Running Your Application**

### **Basic Execution**
- Ensure all required files are in place
- Verify API key is properly configured
- Run the main analysis script
- Check for successful execution
- Verify report.txt creation

### **Troubleshooting**
- **API errors**: Check key validity and network connection
- **Import errors**: Verify file structure and imports
- **Data errors**: Check API response format
- **File errors**: Verify write permissions and paths

---

## **Why This Case Study?**

This final project is powerful because it:
- **Integrates concepts** - Combines all course learning into one project
- **Builds real skills** - Creates a practical, useful application
- **Demonstrates capability** - Shows mastery of multiple programming concepts
- **Prepares for industry** - Uses professional development practices
- **Provides portfolio piece** - Creates a project you can showcase
- **Builds confidence** - Proves you can build complete applications

---

## **Real-World Applications**

This type of application is used everywhere in professional development:
- **News aggregation**: Building news monitoring systems
- **Data analysis**: Processing external data sources
- **Report generation**: Creating automated reporting systems
- **API integration**: Working with third-party services
- **Content management**: Processing and organizing information
- **Business intelligence**: Analyzing data for insights

---

## **Professional Development**

This case study introduces you to:
- **Full-stack development**: Building complete applications
- **API integration**: Working with external services
- **Data processing**: Analyzing and transforming information
- **Error handling**: Managing real-world failure scenarios
- **Code organization**: Structuring complex applications
- **Testing and validation**: Ensuring application reliability

---

## **Success Criteria**

Your application is successful when:
- ✅ API data is successfully fetched
- ✅ Headline objects are properly created
- ✅ Source analysis produces accurate counts
- ✅ Report is correctly formatted
- ✅ File is successfully written
- ✅ Complete workflow executes without errors
- ✅ Code is well-organized and maintainable
- ✅ Error handling is robust and user-friendly

---

## **Solutions**

**Complete code examples for all exercises are available in the `solutions/final-case-study` folder.**

- `solutions/headline_module.py` - Headline class definition
- `solutions/main_analysis.py` - Complete news analysis application
- `solutions/step_by_step/` - Individual step solutions

---

**Remember**: 
- Start with the basic structure and build complexity gradually
- Test each component individually before integration
- Handle errors gracefully at every level
- Keep your code organized and well-documented
- This is your chance to demonstrate everything you've learned

Good luck! This final case study is your opportunity to see how all the individual pieces you've learned can come together to create a useful, real-world application that showcases your programming skills! 