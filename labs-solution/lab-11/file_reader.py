# Lab 11: Reading Data From a File - Complete Solution
# This script reads headlines from a CSV file instead of using hard-coded data

import csv
from headline_module import Headline

def load_headlines_from_csv(filename):
    """
    Load headlines from a CSV file and return a list of Headline objects.
    
    Args:
        filename (str): The name of the CSV file to read
        
    Returns:
        list: List of Headline objects created from the CSV data
    """
    headlines = []
    
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as csv_file:
            # Create a CSV reader object
            csv_reader = csv.reader(csv_file)
            
            # Skip the header row (text, source)
            next(csv_reader)
            
            # Process each data row
            for text, source in csv_reader:
                # Extract text and source from the row
                # text = row[0]
                # source = row[1]
                
                # Create a Headline object and add it to the list
                headline = Headline(text, source)
                headlines.append(headline)
                
        print(f"✅ Successfully loaded {len(headlines)} headlines from {filename}")
        
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found. Make sure it's in the same directory.")
        return []
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return []
    
    return headlines

def analyze_headlines(headlines):
    """
    Analyze the loaded headlines and display statistics.
    
    Args:
        headlines (list): List of Headline objects to analyze
    """
    if not headlines:
        print("No headlines to analyze.")
        return
    
    print("\n" + "=" * 60)
    print("HEADLINES ANALYSIS")
    print("=" * 60)
    
    # Display all headlines with word counts
    print("All Headlines:")
    print("-" * 40)
    for i, headline in enumerate(headlines, 1):
        word_count = headline.get_word_count()
        print(f"{i:2}. ({word_count:2} words) [{headline.source}] {headline.text}")
    
    # Calculate statistics
    total_headlines = len(headlines)
    total_words = sum(headline.get_word_count() for headline in headlines)
    average_words = total_words / total_headlines if total_headlines > 0 else 0
    
    print(f"\nStatistics:")
    print(f"- Total headlines: {total_headlines}")
    print(f"- Total words: {total_words}")
    print(f"- Average words per headline: {average_words:.1f}")
    
    # Find shortest and longest headlines
    if headlines:
        shortest = min(headlines, key=lambda h: h.get_word_count())
        longest = max(headlines, key=lambda h: h.get_word_count())
        
        print(f"\nShortest headline ({shortest.get_word_count()} words):")
        print(f"  {shortest.text}")
        print(f"\nLongest headline ({longest.get_word_count()} words):")
        print(f"  {longest.text}")

def search_headlines(headlines, search_term):
    """
    Search headlines for a specific term and display matching results.
    
    Args:
        headlines (list): List of Headline objects to search
        search_term (str): Term to search for
    """
    if not headlines:
        print("No headlines to search.")
        return
    
    print(f"\n" + "=" * 60)
    print(f"SEARCH RESULTS FOR: '{search_term}'")
    print("=" * 60)
    
    matching_headlines = []
    for headline in headlines:
        if search_term.lower() in headline.text.lower():
            matching_headlines.append(headline)
    
    if matching_headlines:
        print(f"Found {len(matching_headlines)} matching headlines:")
        print("-" * 40)
        for i, headline in enumerate(matching_headlines, 1):
            word_count = headline.get_word_count()
            print(f"{i}. ({word_count:2} words) [{headline.source}] {headline.text}")
    else:
        print(f"No headlines found containing '{search_term}'")

def main():
    """
    Main function to run the file reading and analysis program.
    """
    print("Lab 11: Reading Data From a File")
    print("=" * 60)
    print("This program reads headlines from a CSV file and analyzes them.")
    print("=" * 60)
    
    # Step 1: Load headlines from CSV file
    filename = "headlines_sources.csv"
    headlines = load_headlines_from_csv(filename)
    
    if not headlines:
        print("❌ Failed to load headlines. Program cannot continue.")
        return
    
    # Step 2: Analyze the loaded headlines
    analyze_headlines(headlines)
    
    # Step 3: Interactive search
    print("\n" + "=" * 60)
    print("INTERACTIVE SEARCH")
    print("=" * 60)
    
    while True:
        search_term = input("\nEnter a search term (or 'quit' to exit): ").strip()
        
        if search_term.lower() == 'quit':
            break
        
        if search_term:
            search_headlines(headlines, search_term)
        else:
            print("Please enter a search term.")
    
    print("\n" + "=" * 60)
    print("Program completed successfully!")
    print("=" * 60)
    print("Key achievements:")
    print("✅ Successfully read data from CSV file")
    print("✅ Created Headline objects from file data")
    print("✅ Analyzed headlines with statistics")
    print("✅ Implemented interactive search functionality")
    print("✅ Separated data loading from data processing")
    print("=" * 60)

if __name__ == "__main__":
    main()
