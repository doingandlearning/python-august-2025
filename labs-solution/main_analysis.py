"""
Solution for the Modules Lab: The Main Analysis Script.

This file imports the Headline class from headline_module and uses it
to perform an analysis.
"""

from headline_module import Headline

def main():
    """The main function for our script."""
    # Create a list of Headline objects
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

    print("--- Headline Analysis using a Module ---")
    for h in headlines:
        word_count = h.get_word_count()
        print(f"'{h.text}' (from {h.source}) has {word_count} words.")

# This block ensures that main() is only called when the script is executed directly
if __name__ == "__main__":
    main() 