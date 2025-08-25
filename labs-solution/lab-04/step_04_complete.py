# Step 4: Complete News Analysis Program
# This demonstrates all concepts working together

# Create a list of news headlines
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

def display_header():
    """Display the program header"""
    print("=" * 60)
    print("BBC NEWS HEADLINES ANALYSIS")
    print("=" * 60)

def analyze_headlines():
    """Analyze basic statistics about the headlines"""
    total_headlines = len(headlines)
    print(f"There are {total_headlines} headlines in the list.")
    
    # Calculate average word count
    total_words = 0
    for headline in headlines:
        words = headline.split()
        total_words += len(words)
    
    average_words = total_words / total_headlines
    print(f"The average headline length is {average_words:.1f} words.")
    print(f"Total words across all headlines: {total_words}")
    print()

def search_headlines():
    """Search for headlines containing a specific topic"""
    print("-" * 40)
    search_term = input("What topic would you like to search for? ")
    
    # Search through headlines (case-insensitive)
    matching_headlines = 0
    print(f"\nHeadlines containing '{search_term}':")
    print("-" * 40)
    
    for headline in headlines:
        if search_term.lower() in headline.lower():
            print(f"• {headline}")
            matching_headlines += 1
    
    # Display results
    if matching_headlines == 0:
        print(f"No headlines found containing '{search_term}'.")
    else:
        print(f"\nFound {matching_headlines} headline(s) containing '{search_term}'.")

def main():
    """Main program function"""
    display_header()
    analyze_headlines()
    search_headlines()
    
    print("\n" + "=" * 60)
    print("Analysis complete!")
    print("=" * 60)

# Run the program
if __name__ == "__main__":
    main()
