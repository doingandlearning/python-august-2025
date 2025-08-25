# Lab 5: Building a Headline Analysis Toolkit with Functions - Complete Solution
# This program demonstrates function definition, parameters, and return values

# Headlines data
headlines = [
    "General election: Labour and Tories clash over tax",
    "England crowned T20 world champions",
    "Summer travel chaos feared as airline strikes loom",
    "UK inflation rate falls to lowest level in three years",
    "New David Hockney exhibition opens in London",
    "Science discovers new way to tackle plastic waste",
    "Government announces new funding for NHS",
    "Stock market hits record high on tech boom",
    "Debate rages over future of Artificial Intelligence",
    "Classic Doctor Who episodes to be released in colour"
]

def get_word_count(headline_text):
    """
    Count the number of words in a headline.
    
    Args:
        headline_text (str): The headline to count words in
        
    Returns:
        int: The number of words in the headline
    """
    words = headline_text.split()
    return len(words)

def find_headlines_with_keyword(list_of_headlines, keyword):
    """
    Find headlines that contain a specific keyword.
    
    Args:
        list_of_headlines (list): List of headline strings
        keyword (str): The keyword to search for
        
    Returns:
        list: Headlines containing the keyword
    """
    matching_headlines = []
    
    for headline in list_of_headlines:
        # Case-insensitive search
        if keyword.lower() in headline.lower():
            matching_headlines.append(headline)
    
    return matching_headlines

def analyse_all_headlines(list_of_headlines):
    """
    Analyze all headlines and display statistics.
    
    Args:
        list_of_headlines (list): List of headline strings
    """
    total_words = 0
    
    # Count words in each headline using our function
    for headline in list_of_headlines:
        word_count = get_word_count(headline)
        total_words += word_count
    
    # Calculate and display average
    average_words = total_words / len(list_of_headlines)
    
    print("=" * 50)
    print("HEADLINE ANALYSIS RESULTS")
    print("=" * 50)
    print(f"Total headlines analyzed: {len(list_of_headlines)}")
    print(f"Total words across all headlines: {total_words}")
    print(f"Average words per headline: {average_words:.1f}")
    print("=" * 50)

def display_headline_details(list_of_headlines):
    """
    Display detailed information about each headline.
    
    Args:
        list_of_headlines (list): List of headline strings
    """
    print("\n" + "=" * 50)
    print("DETAILED HEADLINE BREAKDOWN")
    print("=" * 50)
    
    for i in range(len(list_of_headlines)):
        headline = list_of_headlines[i]
        word_count = get_word_count(headline)
        char_count = len(headline)
        
        print(f"{i+1:2}. Words: {word_count:2}, Chars: {char_count:3}")
        print(f"    '{headline}'")
        print()

def main():
    """
    Main function to run the headline analysis.
    """
    print("Welcome to the Headline Analysis Toolkit!")
    print("This program demonstrates functions for analyzing news headlines.")
    
    # Analyze all headlines
    analyse_all_headlines(headlines)
    
    # Show detailed breakdown
    display_headline_details(headlines)
    
    # Demonstrate search functionality
    print("=" * 50)
    print("SEARCH FUNCTIONALITY DEMONSTRATION")
    print("=" * 50)
    
    # Search for different keywords
    search_keywords = ["new", "tax", "NHS", "London", "AI"]
    
    for keyword in search_keywords:
        print(f"\nSearching for '{keyword}':")
        print("-" * 30)
        
        matching = find_headlines_with_keyword(headlines, keyword)
        
        if matching:
            print(f"Found {len(matching)} headline(s):")
            for headline in matching:
                print(f"  • {headline}")
        else:
            print(f"No headlines found containing '{keyword}'")
    
    print("\n" + "=" * 50)
    print("Analysis complete!")
    print("=" * 50)

# Run the main function if this script is run directly
if __name__ == "__main__":
    main()
