# Extension 5: Dictionary of headline lengths
# This demonstrates creating and working with dictionaries

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
print("EXTENSION 5: DICTIONARY OF HEADLINE LENGTHS")
print("=" * 60)

# Create a dictionary where each headline is a key and the value is the word count
length_dict = {}
for headline in headlines:
    word_count = len(headline.split())
    length_dict[headline] = word_count

# Display the dictionary
print("Headline lengths dictionary:")
print("-" * 40)
for headline, word_count in length_dict.items():
    print(f"'{headline}' -> {word_count} words")

# Show dictionary statistics
print("\n" + "=" * 60)
print("DICTIONARY STATISTICS")
print("=" * 60)

total_headlines = len(length_dict)
print(f"Total headlines in dictionary: {total_headlines}")

# Find shortest and longest headlines
shortest_headline = ""
shortest_length = 1000  # Start with a large number
longest_headline = ""
longest_length = 0

for headline, word_count in length_dict.items():
    if word_count < shortest_length:
        shortest_length = word_count
        shortest_headline = headline
    if word_count > longest_length:
        longest_length = word_count
        longest_headline = headline

print(f"Shortest headline: '{shortest_headline}' ({shortest_length} words)")
print(f"Longest headline: '{longest_headline}' ({longest_length} words)")

# Calculate average word count
total_words = 0
for word_count in length_dict.values():
    total_words += word_count

average_words = total_words / total_headlines
print(f"Average words per headline: {average_words:.1f}")

# Show headlines grouped by word count
print("\n" + "=" * 60)
print("HEADLINES GROUPED BY WORD COUNT")
print("=" * 60)

# Create a reverse dictionary (word_count -> list of headlines)
word_count_groups = {}
for headline, word_count in length_dict.items():
    if word_count not in word_count_groups:
        word_count_groups[word_count] = []
    word_count_groups[word_count].append(headline)

# Display groups
for word_count in sorted(word_count_groups.keys()):
    headlines_in_group = word_count_groups[word_count]
    print(f"\n{word_count} word(s):")
    for headline in headlines_in_group:
        print(f"  • {headline}")

print("\n" + "=" * 60)
print("Extension 5 Complete!")
print("=" * 60)
