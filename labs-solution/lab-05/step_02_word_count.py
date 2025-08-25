# Step 2: A Function to Get Word Count
# This demonstrates basic function definition, parameters, and return values

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

# Test the function
print("Step 2: Word Count Function Complete!")
print("=" * 50)

# Test with a simple headline
test_headline = "This is a test headline"
word_count = get_word_count(test_headline)
print(f"Test headline: '{test_headline}'")
print(f"Word count: {word_count}")

# Test with some actual headlines
print("\nTesting with actual headlines:")
for i in range(min(5, len(headlines))):
    headline = headlines[i]
    word_count = get_word_count(headline)
    print(f"{i+1}. '{headline}' -> {word_count} words")

print("\nFunction is working correctly!")
print("=" * 50)
