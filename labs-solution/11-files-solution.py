"""
Solution for Lab 11: Reading Data From a File.

This solution modifies the main analysis script to load Headline objects
from a CSV file instead of a hard-coded list.
"""

import csv
from headline_module import Headline

def load_headlines_from_csv(filename="headlines.csv"):
    """
    Loads headlines from a CSV file and returns a list of Headline objects.
    """
    headlines = []
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            # Skip the header row
            next(csv_reader)

            # Create a Headline object for each row
            for row in csv_reader:
                # Assuming row format is [text, source]
                if row: # Make sure the row is not empty
                    h = Headline(row[0], row[1])
                    headlines.append(h)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return headlines

def main():
    """The main function for our script."""
    # Load headlines from the CSV file
    headlines = load_headlines_from_csv()

    if not headlines:
        print("No headlines were loaded. Exiting.")
        return # Exit the main function if no data was loaded

    print(f"--- Loaded {len(headlines)} headlines from CSV ---")
    for h in headlines:
        word_count = h.get_word_count()
        print(f"'{h.text}' (from {h.source}) has {word_count} words.")

# This block ensures that main() is only called when the script is executed directly
if __name__ == "__main__":
    main() 