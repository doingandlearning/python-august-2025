# Extension 1: Sort headlines by length
# This demonstrates advanced list operations and sorting

# Sample headlines
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

print("=" * 60)
print("EXTENSION 1: SORTING HEADLINES BY LENGTH")
print("=" * 60)

# Method 1: Manual sorting by word count
print("Method 1: Manual sorting by word count")
print("-" * 40)

# Create list of tuples (headline, word_count) for sorting
headline_lengths = []
for headline in headlines:
    word_count = len(headline.split())
    headline_lengths.append((headline, word_count))

# Sort by word count (ascending) using simple bubble sort
for i in range(len(headline_lengths)):
    for j in range(len(headline_lengths) - 1):
        if headline_lengths[j][1] > headline_lengths[j + 1][1]:
            # Swap the elements
            headline_lengths[j], headline_lengths[j + 1] = headline_lengths[j + 1], headline_lengths[j]

print("Top 3 shortest headlines:")
for i in range(3):
    headline, count = headline_lengths[i]
    print(f"{i+1}. ({count} words) {headline}")

print("\nTop 3 longest headlines:")
for i in range(3):
    headline, count = headline_lengths[-(i+1)]
    print(f"{i+1}. ({count} words) {headline}")

# Method 2: Display headlines with word counts
print("\n" + "=" * 60)
print("Method 2: Display all headlines with word counts")
print("-" * 40)

print("All headlines with their word counts:")
for i in range(len(headlines)):
    headline = headlines[i]
    word_count = len(headline.split())
    print(f"{i+1:2}. ({word_count:2} words) {headline}")

# Method 3: Manual sorting (bubble sort for educational purposes)
print("\n" + "=" * 60)
print("Method 3: Manual sorting demonstration")
print("-" * 40)

# Create a list of (headline, word_count) pairs
headline_data = []
for headline in headlines:
    word_count = len(headline.split())
    headline_data.append((headline, word_count))

# Simple bubble sort (not efficient but educational)
for i in range(len(headline_data)):
    for j in range(len(headline_data) - 1):
        if headline_data[j][1] > headline_data[j + 1][1]:
            headline_data[j], headline_data[j + 1] = headline_data[j + 1], headline_data[j]

print("Manually sorted (shortest to longest):")
for i in range(len(headline_data)):
    headline, count = headline_data[i]
    print(f"{i+1:2}. ({count:2} words) {headline}")

print("\n" + "=" * 60)
print("Extension 1 Complete!")
print("=" * 60)
