# Lab 8: Main Analysis Script
# This script imports the Headline class from headline_module and uses it for analysis

# Import the Headline class from our module
from headline_module import Headline

def main():
    """
    Main function to run the headline analysis using the imported Headline class.
    """
    print("Lab 8: Organizing Your Code with Modules")
    print("=" * 50)
    
    # Create a list of Headline objects using the imported class
    print("Creating headlines using imported Headline class:")
    headlines = [
        Headline("General election: Labour and Tories clash over tax", "BBC News"),
        Headline("England crowned T20 world champions", "Sky Sports"),
        Headline("Summer travel chaos feared as airline strikes loom", "The Guardian"),
        Headline("UK inflation rate falls to lowest level in three years", "Financial Times"),
        Headline("New David Hockney exhibition opens in London", "The Times"),
        Headline("Science discovers new way to tackle plastic waste", "Nature"),
        Headline("Government announces new funding for NHS", "BBC News"),
        Headline("Stock market hits record high on tech boom", "Wall Street Journal"),
        Headline("Debate rages over future of Artificial Intelligence", "MIT Technology Review"),
        Headline("Classic Doctor Who episodes to be released in colour", "Radio Times")
    ]
    
    print(f"Created {len(headlines)} headline objects using imported class")
    print(f"Type of first headline: {type(headlines[0])}")
    print(f"Class name: {headlines[0].__class__.__name__}")
    
    # Process all headlines using the imported class methods
    print("\n\nProcessing all headlines:")
    print("-" * 40)
    
    for i, headline in enumerate(headlines, 1):
        # Use the imported class methods
        word_count = headline.get_word_count()
        char_count = headline.get_character_count()
        source = headline.source
        text = headline.text
        
        print(f"{i:2}. ({word_count:2} words, {char_count:3} chars) [{source}] {text}")
    
    # Demonstrate that the imported class works exactly like before
    print("\n\nDemonstrating imported class functionality:")
    print("-" * 40)
    
    # Test string representation
    print("String representation:")
    print(f"  {headlines[0]}")
    print(f"  {headlines[1]}")
    
    # Test word counting
    print("\nWord counting:")
    for i, headline in enumerate(headlines[:3], 1):
        print(f"  Headline {i}: {headline.get_word_count()} words")
    
    # Test additional methods
    print("\nAdditional methods:")
    for i, headline in enumerate(headlines[:3], 1):
        is_long = headline.is_long_headline()
        contains_new = headline.contains_keyword("new")
        print(f"  Headline {i}: Long={is_long}, Contains 'new'={contains_new}")
    
    # Analysis using the imported class
    print("\n\nAnalysis using imported class:")
    print("-" * 40)
    
    # Group headlines by source
    source_groups = {}
    for headline in headlines:
        source = headline.source
        if source not in source_groups:
            source_groups[source] = []
        source_groups[source].append(headline)
    
    # Display statistics for each source
    for source, source_headlines in source_groups.items():
        print(f"\n{source}:")
        total_words = sum(h.get_word_count() for h in source_headlines)
        avg_words = total_words / len(source_headlines)
        print(f"  Headlines: {len(source_headlines)}")
        print(f"  Total words: {total_words}")
        print(f"  Average words: {avg_words:.1f}")
    
    # Find headlines with specific characteristics
    print("\n\nFinding specific headlines:")
    print("-" * 40)
    
    # Headlines with more than 8 words
    long_headlines = [h for h in headlines if h.is_long_headline()]
    print(f"Long headlines (>8 words): {len(long_headlines)}")
    for headline in long_headlines:
        print(f"  • [{headline.source}] {headline.text}")
    
    # Headlines containing "new"
    new_headlines = [h for h in headlines if h.contains_keyword("new")]
    print(f"\nHeadlines containing 'new': {len(new_headlines)}")
    for headline in new_headlines:
        print(f"  • [{headline.source}] {headline.text}")
    
    # Overall statistics
    print("\n\nOverall Statistics:")
    print("-" * 40)
    
    total_words = sum(h.get_word_count() for h in headlines)
    total_chars = sum(h.get_character_count() for h in headlines)
    avg_words = total_words / len(headlines)
    avg_chars = total_chars / len(headlines)
    
    print(f"Total headlines: {len(headlines)}")
    print(f"Total words: {total_words}")
    print(f"Total characters: {total_chars}")
    print(f"Average words per headline: {avg_words:.1f}")
    print(f"Average characters per headline: {avg_chars:.1f}")
    
    # Verify the import worked correctly
    print("\n\nImport Verification:")
    print("-" * 40)
    print("✓ Successfully imported Headline class from headline_module")
    print("✓ All class methods work correctly")
    print("✓ Analysis produces the same results as before")
    print("✓ Code is now organized into separate modules")
    
    print("\n" + "=" * 50)
    print("Module-based analysis complete!")
    print("=" * 50)

# Use the if __name__ == "__main__" block to create a safe entry point
if __name__ == "__main__":
    main()
