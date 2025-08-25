# Extension 6: Group headlines by first word
# This demonstrates advanced data organization using dictionaries

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
print("EXTENSION 6: GROUPING BY FIRST WORD")
print("=" * 60)

# Group headlines by first word
groups = {}
for headline in headlines:
    # Get the first word of the headline
    first_word = headline.split()[0]
    
    # If this first word isn't in our groups yet, create a new list
    if first_word not in groups:
        groups[first_word] = []
    
    # Add this headline to the appropriate group
    groups[first_word].append(headline)

# Display the groups
print("Headlines grouped by first word:")
print("=" * 60)

for first_word in sorted(groups.keys()):
    headline_list = groups[first_word]
    print(f"\n'{first_word}' ({len(headline_list)} headline(s)):")
    print("-" * 40)
    
    for i in range(len(headline_list)):
        headline = headline_list[i]
        print(f"  {i+1}. {headline}")

# Show summary statistics
print("\n" + "=" * 60)
print("GROUPING SUMMARY")
print("=" * 60)

total_groups = len(groups)
print(f"Total unique first words: {total_groups}")

# Find the group with the most headlines
largest_group = ""
largest_count = 0
for first_word, headline_list in groups.items():
    if len(headline_list) > largest_count:
        largest_count = len(headline_list)
        largest_group = first_word

print(f"Most common first word: '{largest_group}' ({largest_count} headlines)")

# Show all first words and their counts
print(f"\nFirst word distribution:")
for first_word in sorted(groups.keys()):
    count = len(groups[first_word])
    print(f"  '{first_word}': {count} headline(s)")

# Show headlines that start with specific words
print("\n" + "=" * 60)
print("EXAMPLES OF SPECIFIC GROUPS")
print("=" * 60)

# Show a few specific groups in detail
example_words = list(groups.keys())[:3]  # Take first 3 groups
for word in example_words:
    print(f"\nGroup: '{word}'")
    print("-" * 30)
    for headline in groups[word]:
        print(f"  • {headline}")

print("\n" + "=" * 60)
print("Extension 6 Complete!")
print("=" * 60)
