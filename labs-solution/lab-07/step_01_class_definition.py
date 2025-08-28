# Step 1: Defining the Headline Class
# This demonstrates basic class definition and constructor

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

# Test the class definition
print("Step 1: Class Definition Complete!")
print("=" * 50)


# Create test objects
headline1 = Headline("General election: Labour and Tories clash over tax", "BBC News")
headline2 = Headline("England crowned T20 world champions", "Sky Sports")

print("Created headline objects:")
print(f"Object 1: {headline1}")
print(f"Object 2: {headline2}")

# Test attribute access
print("\nTesting attribute access:")
print(f"Headline 1 text: '{headline1.text}'")
print(f"Headline 1 source: '{headline1.source}'")
print(f"Headline 2 text: '{headline2.text}'")
print(f"Headline 2 source: '{headline2.source}'")

# Verify object creation
print("\nVerification:")
print(f"headline1 is a Headline object: {isinstance(headline1, Headline)}")
print(f"headline2 is a Headline object: {isinstance(headline2, Headline)}")
print(f"headline1 has text attribute: {hasattr(headline1, 'text')}")
print(f"headline1 has source attribute: {hasattr(headline1, 'source')}")

# Test with different data
print("\nTesting with different data:")
test_headline = Headline("Test headline", "Test Source")
print(f"Test object: {test_headline}")
print(f"Test text: '{test_headline.text}'")
print(f"Test source: '{test_headline.source}'")

print("\n" + "=" * 50)
print("Step 1 complete! Class is working correctly.")
print("=" * 50)
