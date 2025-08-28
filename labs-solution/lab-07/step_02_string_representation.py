# Step 2: Adding String Representation
# This demonstrates adding the __str__ method to the class

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
            str: A human readable representation of the headline
        """
        return f"Headline(text='{self.text}', source='{self.source}')"

# Test the string representation
print("Step 2: String Representation Complete!")
print("=" * 50)

# Create test objects
headline1 = Headline("General election: Labour and Tories clash over tax", "BBC News")
headline2 = Headline("England crowned T20 world champions", "Sky Sports")
headline3 = Headline("Summer travel chaos feared as airline strikes loom", "The Guardian")

print("Testing string representation:")
print(f"Headline 1: {headline1}")
print(f"Headline 2: {headline2}")
print(f"Headline 3: {headline3}")

# Test printing objects directly
print("\nPrinting objects directly:")
print(headline1)
print(headline2)
print(headline3)

# Test with str() function
print("\nUsing str() function:")
print(f"str(headline1): {str(headline1)}")
print(f"str(headline2): {str(headline2)}")
print(f"str(headline3): {str(headline3)}")

# Test in different contexts
print("\nTesting in different contexts:")
headlines_list = [headline1, headline2, headline3]
print("In a list:")
for i, headline in enumerate(headlines_list, 1):
    print(f"  {i}. {headline}")

# Test with f-strings
print("\nTesting with f-strings:")
print(f"First headline: {headline1}")
print(f"Second headline: {headline2}")

# Verify the improvement
print("\nVerification:")
print("Before __str__ method, objects would show:")
print("  <__main__.Headline object at 0x...>")
print("\nAfter __str__ method, objects show:")
print(f"  {headline1}")

print("\n" + "=" * 50)
print("Step 2 complete! String representation is working.")
print("=" * 50)

print([headline1, headline2, headline3])

# print -> __str__ -> __repr__ -> ugly!
# print(list) -> __repr__ -> ugly