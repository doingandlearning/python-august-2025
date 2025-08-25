# Lab 7: Structuring Data with Classes - Complete Solution
# This program demonstrates creating and using a Headline class

class Headline:
    """
    A class to represent a news headline with its source.
    
    Attributes:
        text (str): The headline text
        source (str): The news source (e.g., "BBC News")
    """
    
    def __init__(self, text, source):
        """
        Initialize a new Headline object.
        
        Args:
            text (str): The headline text
            source (str): The news source
        """
        self.text = text
        self.source = source
    
    def __str__(self):
        """
        Return a string representation of the Headline object.
        
        Returns:
            str: A readable representation of the headline
        """
        return f"Headline(text='{self.text}', source='{self.source}')"
    
    def get_word_count(self):
        """
        Get the number of words in the headline text.
        
        Returns:
            int: The word count
        """
        return len(self.text.split())
    
    def get_character_count(self):
        """
        Get the total character count of the headline text.
        
        Returns:
            int: The character count
        """
        return len(self.text)
    
    def is_long_headline(self):
        """
        Check if the headline is considered long (more than 8 words).
        
        Returns:
            bool: True if headline has more than 8 words
        """
        return self.get_word_count() > 8
    
    def contains_keyword(self, keyword):
        """
        Check if the headline contains a specific keyword.
        
        Args:
            keyword (str): The keyword to search for
            
        Returns:
            bool: True if keyword is found in headline
        """
        return keyword.lower() in self.text.lower()

def main():
    """
    Main function to demonstrate the Headline class.
    """
    print("Lab 7: Structuring Data with Classes")
    print("=" * 50)
    
    # Step 1: Creating Headline objects
    print("\nStep 1: Creating Headline Objects")
    print("-" * 40)
    
    # Create individual headline objects
    headline1 = Headline("General election: Labour and Tories clash over tax", "BBC News")
    headline2 = Headline("England crowned T20 world champions", "Sky Sports")
    headline3 = Headline("Summer travel chaos feared as airline strikes loom", "The Guardian")
    
    print("Created headline objects:")
    print(f"1. {headline1}")
    print(f"2. {headline2}")
    print(f"3. {headline3}")
    
    # Step 2: Testing string representation
    print("\n\nStep 2: String Representation")
    print("-" * 40)
    
    print("Printing headline objects:")
    print(headline1)
    print(headline2)
    print(headline3)
    
    # Step 3: Testing methods
    print("\n\nStep 3: Testing Methods")
    print("-" * 40)
    
    print("Word counts:")
    print(f"Headline 1: {headline1.get_word_count()} words")
    print(f"Headline 2: {headline2.get_word_count()} words")
    print(f"Headline 3: {headline3.get_word_count()} words")
    
    print("\nCharacter counts:")
    print(f"Headline 1: {headline1.get_character_count()} characters")
    print(f"Headline 2: {headline2.get_character_count()} characters")
    print(f"Headline 3: {headline3.get_character_count()} characters")
    
    print("\nLong headline check:")
    print(f"Headline 1 is long: {headline1.is_long_headline()}")
    print(f"Headline 2 is long: {headline2.is_long_headline()}")
    print(f"Headline 3 is long: {headline3.is_long_headline()}")
    
    print("\nKeyword search:")
    print(f"Headline 1 contains 'election': {headline1.contains_keyword('election')}")
    print(f"Headline 2 contains 'cricket': {headline2.contains_keyword('cricket')}")
    print(f"Headline 3 contains 'travel': {headline3.contains_keyword('travel')}")
    
    # Step 4: Working with a list of Headline objects
    print("\n\nStep 4: Working with a List of Headline Objects")
    print("-" * 40)
    
    # Create a list of Headline objects
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
    
    print(f"Created list of {len(headlines)} headline objects")
    
    # Process all headlines
    print("\nProcessing all headlines:")
    for i, headline in enumerate(headlines, 1):
        word_count = headline.get_word_count()
        source = headline.source
        print(f"{i:2}. ({word_count:2} words) [{source}] {headline.text}")
    
    # Analyze headlines by source
    print("\n\nAnalysis by Source:")
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
        
        # Show headlines from this source
        for headline in source_headlines:
            print(f"    • {headline.text}")
    
    # Find headlines containing specific keywords
    print("\n\nKeyword Analysis:")
    print("-" * 40)
    
    keywords = ["new", "UK", "future", "AI", "technology"]
    for keyword in keywords:
        matching_headlines = [h for h in headlines if h.contains_keyword(keyword)]
        print(f"\nHeadlines containing '{keyword}': {len(matching_headlines)}")
        for headline in matching_headlines:
            print(f"  • [{headline.source}] {headline.text}")
    
    # Find the longest and shortest headlines
    print("\n\nHeadline Length Analysis:")
    print("-" * 40)
    
    longest_headline = max(headlines, key=lambda h: h.get_word_count())
    shortest_headline = min(headlines, key=lambda h: h.get_word_count())
    
    print(f"Longest headline: '{longest_headline.text}'")
    print(f"  Source: {longest_headline.source}")
    print(f"  Words: {longest_headline.get_word_count()}")
    
    print(f"\nShortest headline: '{shortest_headline.text}'")
    print(f"  Source: {shortest_headline.source}")
    print(f"  Words: {shortest_headline.get_word_count()}")
    
    print("\n" + "=" * 50)
    print("Class demonstration complete!")
    print("=" * 50)

if __name__ == "__main__":
    main()
