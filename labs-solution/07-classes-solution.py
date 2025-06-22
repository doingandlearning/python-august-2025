"""
Solution for the Classes Lab: Structuring Data with a Headline Class.
"""

# Step 1, 2, 3: Defining the Headline Class
class Headline:
    """A class to represent a single news headline and its source."""

    def __init__(self, text, source):
        """Initializes a Headline object."""
        self.text = text
        self.source = source

    def __repr__(self):
        """Returns an unambiguous string representation of the object."""
        return f"Headline(text='{self.text}', source='{self.source}')"

    def get_word_count(self):
        """Returns the number of words in the headline's text."""
        return len(self.text.split())


# Step 4: Refactoring Your Code to Use the Class

# Create a list of Headline objects instead of a list of strings
headlines = [
    Headline("General election: Labour and Tories clash over tax", "BBC News"),
    Headline("England crowned T20 world champions", "Sky Sports"),
    Headline("Summer travel chaos feared as airline strikes loom", "The Guardian"),
    Headline("UK inflation rate falls to lowest level in three years", "Reuters"),
    Headline("New David Hockney exhibition opens in London", "BBC News"),
    Headline("Science discovers new way to tackle plastic waste", "Nature"),
    Headline("Government announces new funding for NHS", "BBC News"),
    Headline("Stock market hits record high on tech boom", "Financial Times"),
    Headline("Debate rages over future of Artificial Intelligence", "The Economist"),
    Headline("Classic Doctor Who episodes to be released in colour", "BBC News")
]

print("--- Full list of headline objects ---")
print(headlines)
print("-" * 20)


print("\n--- Headline Analysis using Objects ---")
# Loop through the list of objects and use the method
for h in headlines:
    word_count = h.get_word_count()
    print(f"'{h.text}' (from {h.source}) has {word_count} words.")

print("-" * 20)


# You can still use list comprehensions with objects!
print("\n--- Finding headlines from BBC News ---")
bbc_headlines = [h for h in headlines if h.source == "BBC News"]
for h in bbc_headlines:
    print(h.text) 