# Step 3: Filtering with List Comprehensions
# This demonstrates using list comprehensions to filter data

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

# Step 3: Filtering with List Comprehensions
print("Step 3: Filtering with List Comprehensions")
print("=" * 50)

# Create a list of headlines with 7 words or fewer using list comprehension
short_headlines = [headline for headline in headlines if len(headline.split()) <= 7]

print("Headlines with 7 words or fewer:")
for i, headline in enumerate(short_headlines):
    word_count = len(headline.split())
    print(f"{i+1}. ({word_count} words) {headline}")

print(f"\nTotal short headlines: {len(short_headlines)}")
print(f"Original headlines: {len(headlines)}")
print(f"Filtered out: {len(headlines) - len(short_headlines)} headlines")

# Verify the filtering worked correctly
print("\nVerification:")
print("Checking each headline manually:")

for i, headline in enumerate(headlines):
    word_count = len(headline.split())
    is_short = word_count <= 7
    status = "✓ INCLUDED" if is_short else "✗ EXCLUDED"
    print(f"{i+1:2}. ({word_count:2} words) {status} - {headline}")

# Show the list comprehension breakdown
print("\nList comprehension breakdown:")
print("short_headlines = [headline for headline in headlines if len(headline.split()) <= 7]")
print("  - 'headline' is the expression (we want the full headline)")
print("  - 'for headline in headlines' is the iteration")
print("  - 'if len(headline.split()) <= 7' is the condition")

# Demonstrate different filtering conditions
print("\nOther filtering examples:")

# Headlines containing the word "new"
headlines_with_new = [headline for headline in headlines if "new" in headline.lower()]
print(f"\nHeadlines containing 'new': {len(headlines_with_new)}")
for headline in headlines_with_new:
    print(f"  • {headline}")

# Headlines starting with specific letters
headlines_starting_with_s = [headline for headline in headlines if headline.lower().startswith('s')]
print(f"\nHeadlines starting with 'S': {len(headlines_starting_with_s)}")
for headline in headlines_starting_with_s:
    print(f"  • {headline}")

# Headlines ending with specific punctuation
headlines_ending_with_colon = [headline for headline in headlines if headline.endswith(':')]
print(f"\nHeadlines ending with colon: {len(headlines_ending_with_colon)}")
for headline in headlines_ending_with_colon:
    print(f"  • {headline}")

print("\n" + "=" * 50)
print("Filtering with list comprehensions complete!")
print("=" * 50)
