# Lab 11: Reading Data From a File

Our program is great, but having the data hard-coded inside the script is inflexible. Real-world programs almost always load their data from external files.

The aim of this lab is to modify our program to read headlines from the `headlines.csv` file using Python's built-in `csv` module.

This lab is made up of 3 steps:
1.  Import the `csv` module and prepare an empty list.
2.  Open `headlines.csv` and use `csv.reader` to loop over the data.
3.  Create `Headline` objects from the file data and append them to your list.

---
## Step 1: Getting Started

You'll be modifying the `main_analysis.py` script from the modules lab.

**Your goal:** Prepare your script to read the CSV file.

**Hints:**
- At the top of `main_analysis.py`, you'll need to import Python's `csv` module: `import csv`.
- In your `main()` function, find the hard-coded `headlines` list. You can delete it or comment it out.
- In its place, create an empty list that we will fill with data from the file: `headlines = []`.
- Make sure the `headlines.csv` file is in the same directory as your Python script.

---
## Step 2: Open and Read the File

We need to open the file and create a "reader" object to help us process the CSV data. The `with open(...)` syntax is the safest way to handle files in Python.

**Your goal:** Open `headlines.csv` and loop through its rows.

**Hints:**
- Use the `with open(...)` syntax to open `headlines.csv`. Make sure to set the `mode` to `'r'` for reading and specify `newline=''` which is recommended for CSV files.
  ```python
  with open('headlines.csv', mode='r', newline='', encoding='utf-8') as csv_file:
      # ... your code will go here ...
  ```
- Inside the `with` block, create a CSV reader object: `csv_reader = csv.reader(csv_file)`.
- The first row of our CSV is the header (`text`, `source`). We want to skip this so it doesn't get treated as a headline. You can do this with the `next()` function: `next(csv_reader)`.
- Now, you can loop directly over the `csv_reader` object to get each `row`: `for row in csv_reader:`.

---
## Step 3: Create Objects from File Data

Inside the loop, each `row` will be a list of strings. For example, the first data row will be `['General election: Labour and Tories clash over tax', 'BBC News']`. We need to use this data to create our `Headline` objects.

**Your goal:** Inside your loop, create a `Headline` object from each `row` and append it to your `headlines` list.

**Hints:**
- Inside the `for row in csv_reader:` loop:
- The text is the first item in the row, `row[0]`.
- The source is the second item, `row[1]`.
- Create a new `Headline` object using this data: `h = Headline(row[0], row[1])`.
- Append the new object to your `headlines` list: `headlines.append(h)`.

---
## Run Your Program

After the `with open(...)` block finishes, your `headlines` list should be full of objects created from the CSV file.

The rest of your `main()` function, which performs the analysis on this list, should work exactly as it did before! This shows the power of separating your data loading from your data processing logic. 