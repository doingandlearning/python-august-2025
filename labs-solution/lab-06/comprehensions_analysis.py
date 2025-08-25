# Lab 6: Supercharging Analysis with List Comprehensions - Complete Solution
# This program demonstrates list comprehensions for mapping, filtering, and combining operations

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

def main():
    """
    Main function to demonstrate all list comprehension techniques.
    """
    print("Lab 6: List Comprehensions Analysis")
    print("=" * 50)
    
    # Step 2: Mapping with List Comprehensions
    print("\nStep 2: Mapping with List Comprehensions")
    print("-" * 40)
    
    # Create a list of word counts for each headline
    headline_lengths = [len(headline.split()) for headline in headlines]
    
    print("Headline lengths (word counts):")
    for i, (headline, length) in enumerate(zip(headlines, headline_lengths)):
        print(f"{i+1:2}. ({length:2} words) {headline}")
    
    print(f"\nAll headline lengths: {headline_lengths}")
    
    # Step 3: Filtering with List Comprehensions
    print("\n\nStep 3: Filtering with List Comprehensions")
    print("-" * 40)
    
    # Create a list of headlines with 7 words or fewer
    short_headlines = [headline for headline in headlines if len(headline.split()) <= 7]
    
    print("Headlines with 7 words or fewer:")
    for i, headline in enumerate(short_headlines):
        word_count = len(headline.split())
        print(f"{i+1}. ({word_count} words) {headline}")
    
    print(f"\nTotal short headlines: {len(short_headlines)}")
    
    # Step 4: Combining Mapping and Filtering
    print("\n\nStep 4: Combining Mapping and Filtering")
    print("-" * 40)
    
    # Create a list of word counts for headlines containing "new"
    specific_headline_lengths = [len(headline.split()) for headline in headlines if "new" in headline.lower()]
    
    print("Word counts of headlines containing 'new':")
    for i, headline in enumerate(headlines):
        if "new" in headline.lower():
            word_count = len(headline.split())
            print(f"• '{headline}' -> {word_count} words")
    
    print(f"\nAll word counts for 'new' headlines: {specific_headline_lengths}")
    
    # Additional analysis using list comprehensions
    print("\n\nAdditional Analysis with List Comprehensions")
    print("-" * 40)
    
    # Find headlines that start with specific letters
    headlines_starting_with_s = [headline for headline in headlines if headline.lower().startswith('s')]
    print(f"Headlines starting with 'S': {len(headlines_starting_with_s)}")
    for headline in headlines_starting_with_s:
        print(f"  • {headline}")
    
    # Find headlines containing numbers
    headlines_with_numbers = [headline for headline in headlines if any(char.isdigit() for char in headline)]
    print(f"\nHeadlines containing numbers: {len(headlines_with_numbers)}")
    for headline in headlines_with_numbers:
        print(f"  • {headline}")
    
    # Find headlines ending with specific punctuation
    headlines_ending_with_colon = [headline for headline in headlines if headline.endswith(':')]
    print(f"\nHeadlines ending with colon: {len(headlines_ending_with_colon)}")
    for headline in headlines_ending_with_colon:
        print(f"  • {headline}")
    
    # Calculate statistics using list comprehensions
    print("\n\nStatistics Using List Comprehensions")
    print("-" * 40)
    
    # Average word count
    average_words = sum(len(headline.split()) for headline in headlines) / len(headlines)
    print(f"Average words per headline: {average_words:.1f}")
    
    # Longest and shortest headlines
    longest_headline = max(headlines, key=lambda x: len(x.split()))
    shortest_headline = min(headlines, key=lambda x: len(x.split()))
    
    print(f"Longest headline: '{longest_headline}' ({len(longest_headline.split())} words)")
    print(f"Shortest headline: '{shortest_headline}' ({len(shortest_headline.split())} words)")
    
    # Word count distribution
    word_counts = [len(headline.split()) for headline in headlines]
    unique_counts = sorted(set(word_counts))
    
    print(f"\nWord count distribution:")
    for count in unique_counts:
        count_frequency = word_counts.count(count)
        print(f"  {count} words: {count_frequency} headline(s)")
    
    print("\n" + "=" * 50)
    print("List comprehensions analysis complete!")
    print("=" * 50)

if __name__ == "__main__":
    main()
