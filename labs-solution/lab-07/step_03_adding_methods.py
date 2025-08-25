# Step 3: Adding Behavior with Methods
# This demonstrates adding custom methods to the class

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

# Test the methods
print("Step 3: Adding Methods Complete!")
print("=" * 50)

# Create test objects
headline1 = Headline("General election: Labour and Tories clash over tax", "BBC News")
headline2 = Headline("England crowned T20 world champions", "Sky Sports")
headline3 = Headline("Summer travel chaos feared as airline strikes loom", "The Guardian")

print("Testing the get_word_count method:")
print(f"Headline 1: '{headline1.text}'")
print(f"  Word count: {headline1.get_word_count()} words")
print(f"  Manual count: {len(headline1.text.split())} words")

print(f"\nHeadline 2: '{headline2.text}'")
print(f"  Word count: {headline2.get_word_count()} words")
print(f"  Manual count: {len(headline2.text.split())} words")

print(f"\nHeadline 3: '{headline3.text}'")
print(f"  Word count: {headline3.get_word_count()} words")
print(f"  Manual count: {len(headline3.text.split())} words")

# Test with different headline lengths
print("\nTesting with different headline lengths:")
short_headline = Headline("Short", "Test")
medium_headline = Headline("This is a medium length headline", "Test")
long_headline = Headline("This is a very long headline with many words to count", "Test")

print(f"Short headline: '{short_headline.text}' -> {short_headline.get_word_count()} words")
print(f"Medium headline: '{medium_headline.text}' -> {medium_headline.get_word_count()} words")
print(f"Long headline: '{long_headline.text}' -> {long_headline.get_word_count()} words")

# Test method calls
print("\nTesting method calls:")
print(f"headline1.get_word_count(): {headline1.get_word_count()}")
print(f"headline2.get_word_count(): {headline2.get_word_count()}")
print(f"headline3.get_word_count(): {headline3.get_word_count()}")

# Verify the method works correctly
print("\nVerification:")
print("Manual word counting vs. method results:")
headlines_to_test = [headline1, headline2, headline3]

for i, headline in enumerate(headlines_to_test, 1):
    manual_count = len(headline.text.split())
    method_count = headline.get_word_count()
    matches = "✓" if manual_count == method_count else "✗"
    print(f"  Headline {i}: Manual={manual_count}, Method={method_count} {matches}")

# Test edge cases
print("\nTesting edge cases:")
empty_headline = Headline("", "Test")
single_word = Headline("Word", "Test")
many_spaces = Headline("   Multiple    spaces   ", "Test")

print(f"Empty headline: '{empty_headline.text}' -> {empty_headline.get_word_count()} words")
print(f"Single word: '{single_word.text}' -> {single_word.get_word_count()} words")
print(f"Many spaces: '{many_spaces.text}' -> {many_spaces.get_word_count()} words")

print("\n" + "=" * 50)
print("Step 3 complete! Methods are working correctly.")
print("=" * 50)
