# Step 4: Refactoring Code to Use the Class
# This demonstrates using the Headline class in practice with lists and loops

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

# Step 4: Using the Class in Practice
print("Step 4: Using Classes in Practice")
print("=" * 50)

# Create a list of Headline objects instead of strings
print("Creating a list of Headline objects:")
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

print(f"Created list of {len(headlines)} Headline objects")
print(f"Type of headlines list: {type(headlines)}")
print(f"Type of first item: {type(headlines[0])}")

# Loop through the list and use object methods
print("\nProcessing all headlines:")
print("-" * 40)

for i, headline in enumerate(headlines, 1):
    # Use the object's method to get word count
    word_count = headline.get_word_count()
    source = headline.source
    text = headline.text
    
    print(f"{i:2}. ({word_count:2} words) [{source}] {text}")

# Compare with the old functional approach
print("\n\nComparison with Functional Approach:")
print("-" * 40)

print("OLD WAY (functional):")
print("  get_word_count(headline_text)")
print("  get_word_count('General election: Labour and Tories clash over tax')")

print("\nNEW WAY (object-oriented):")
print("  headline.get_word_count()")
print("  headline1.get_word_count()")

print("\nBenefits of the object-oriented approach:")
print("  • Cleaner syntax: headline.get_word_count() vs get_word_count(headline)")
print("  • More readable: 'tell the headline to get its word count'")
print("  • Data and behavior are bundled together")
print("  • Easier to extend with new methods")

# Demonstrate additional functionality
print("\n\nAdditional Functionality:")
print("-" * 40)

# Group headlines by source
print("Grouping headlines by source:")
source_groups = {}
for headline in headlines:
    source = headline.source
    if source not in source_groups:
        source_groups[source] = []
    source_groups[source].append(headline)

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
long_headlines = [h for h in headlines if h.get_word_count() > 8]
print(f"Headlines with more than 8 words: {len(long_headlines)}")
for headline in long_headlines:
    print(f"  • [{headline.source}] {headline.text} ({headline.get_word_count()} words)")

# Headlines from BBC News
bbc_headlines = [h for h in headlines if h.source == "BBC News"]
print(f"\nBBC News headlines: {len(bbc_headlines)}")
for headline in bbc_headlines:
    print(f"  • {headline.text} ({headline.get_word_count()} words)")

# Statistics
print("\n\nOverall Statistics:")
print("-" * 40)

total_words = sum(h.get_word_count() for h in headlines)
avg_words = total_words / len(headlines)
longest_headline = max(headlines, key=lambda h: h.get_word_count())
shortest_headline = min(headlines, key=lambda h: h.get_word_count())

print(f"Total headlines: {len(headlines)}")
print(f"Total words across all headlines: {total_words}")
print(f"Average words per headline: {avg_words:.1f}")
print(f"Longest headline: '{longest_headline.text}' ({longest_headline.get_word_count()} words)")
print(f"Shortest headline: '{shortest_headline.text}' ({shortest_headline.get_word_count()} words)")

print("\n" + "=" * 50)
print("Step 4 complete! Classes are working in practice.")
print("=" * 50)

print([h.get_word_count() for h in headlines])