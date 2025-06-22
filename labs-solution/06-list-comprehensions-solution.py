"""
Solution for the List Comprehensions Lab.
"""

# Step 1: Getting Started
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

print("--- Original Headlines ---")
print(headlines)

# Step 2: Mapping with List Comprehensions
print("\n--- Headline Word Counts (Mapping) ---")
headline_lengths = [len(h.split()) for h in headlines]
print(headline_lengths)


# Step 3: Filtering with List Comprehensions
print("\n--- Short Headlines (Filtering) ---")
short_headlines = [h for h in headlines if len(h.split()) <= 7]
for h in short_headlines:
    print(h)


# Step 4: Combining Mapping and Filtering
print("\n--- Word counts of headlines containing 'new' (Map + Filter) ---")
specific_headline_lengths = [len(h.split()) for h in headlines if "new" in h.lower()]
print(specific_headline_lengths) 