# Step 2: Mapping with List Comprehensions
# This demonstrates using list comprehensions to transform data

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

# Step 2: Mapping with List Comprehensions
print("Step 2: Mapping with List Comprehensions")
print("=" * 50)

# Create a list of word counts for each headline using list comprehension
headline_lengths = [len(headline.split()) for headline in headlines]

print("Headline lengths (word counts):")
for i, (headline, length) in enumerate(zip(headlines, headline_lengths)):
    print(f"{i+1:2}. ({length:2} words) {headline}")

print(f"\nAll headline lengths: {headline_lengths}")

# Verify the results
print("\nVerification:")
print(f"First headline: '{headlines[0]}' -> {headline_lengths[0]} words")
print(f"Second headline: '{headlines[1]}' -> {headline_lengths[1]} words")
print(f"Third headline: '{headline_lengths[2]}' words")

# Manual verification of first few headlines
print("\nManual verification:")
print(f"Headline 1: '{headlines[0]}'")
words1 = headlines[0].split()
print(f"  Split result: {words1}")
print(f"  Word count: {len(words1)} (should match {headline_lengths[0]})")

print(f"\nHeadline 2: '{headlines[1]}'")
words2 = headlines[1].split()
print(f"  Split result: {words2}")
print(f"  Word count: {len(words2)} (should match {headline_lengths[1]})")

# Show the list comprehension breakdown
print("\nList comprehension breakdown:")
print("headline_lengths = [len(headline.split()) for headline in headlines]")
print("  - 'len(headline.split())' is the expression")
print("  - 'for headline in headlines' is the iteration")
print("  - Each headline gets processed and transformed")

print("\n" + "=" * 50)
print("Mapping with list comprehensions complete!")
print("=" * 50)
