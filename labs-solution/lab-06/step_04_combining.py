# Step 4: Combining Mapping and Filtering
# This demonstrates using list comprehensions to both filter and transform data

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

# Step 4: Combining Mapping and Filtering
print("Step 4: Combining Mapping and Filtering")
print("=" * 50)

# Create a list of word counts for headlines containing "new"
specific_headline_lengths = [len(headline.split()) for headline in headlines if "new" in headline.lower()]

print("Word counts of headlines containing 'new':")
for i, headline in enumerate(headlines):
    if "new" in headline.lower():
        word_count = len(headline.split())
        print(f"• '{headline}' -> {word_count} words")

print(f"\nAll word counts for 'new' headlines: {specific_headline_lengths}")

# Verify the results manually
print("\nManual verification:")
print("Headlines containing 'new':")
new_headlines = []
for headline in headlines:
    if "new" in headline.lower():
        new_headlines.append(headline)
        word_count = len(headline.split())
        print(f"  • '{headline}' -> {word_count} words")

print(f"\nTotal headlines with 'new': {len(new_headlines)}")
print(f"Word counts extracted: {specific_headline_lengths}")

# Show the list comprehension breakdown
print("\nList comprehension breakdown:")
print("specific_headline_lengths = [len(headline.split()) for headline in headlines if 'new' in headline.lower()]")
print("  - 'len(headline.split())' is the expression (mapping)")
print("  - 'for headline in headlines' is the iteration")
print("  - 'if \"new\" in headline.lower()' is the condition (filtering)")

# Demonstrate other combinations
print("\nOther combination examples:")

# Word counts of headlines with 6 words or fewer
short_headline_lengths = [len(headline.split()) for headline in headlines if len(headline.split()) <= 6]
print(f"\nWord counts of headlines with ≤6 words: {short_headline_lengths}")
print("Corresponding headlines:")
for headline in headlines:
    if len(headline.split()) <= 6:
        print(f"  • '{headline}' -> {len(headline.split())} words")

# First word of headlines containing "UK"
uk_headline_first_words = [headline.split()[0] for headline in headlines if "UK" in headline]
print(f"\nFirst words of headlines containing 'UK': {uk_headline_first_words}")
print("Corresponding headlines:")
for headline in headlines:
    if "UK" in headline:
        first_word = headline.split()[0]
        print(f"  • '{headline}' -> first word: '{first_word}'")

# Headlines converted to title case that contain "future"
future_title_headlines = [headline.title() for headline in headlines if "future" in headline.lower()]
print(f"\nTitle case of headlines containing 'future': {future_title_headlines}")
print("Original headlines:")
for headline in headlines:
    if "future" in headline.lower():
        print(f"  • '{headline}' -> '{headline.title()}'")

# Statistics using combined comprehensions
print("\nStatistics using combined comprehensions:")

# Average word count of headlines containing "new"
if specific_headline_lengths:
    avg_new_headlines = sum(specific_headline_lengths) / len(specific_headline_lengths)
    print(f"Average word count of headlines with 'new': {avg_new_headlines:.1f}")
else:
    print("No headlines contain 'new'")

# Longest headline containing "new"
if new_headlines:
    longest_new_headline = max(new_headlines, key=lambda x: len(x.split()))
    print(f"Longest headline with 'new': '{longest_new_headline}' ({len(longest_new_headline.split())} words)")
else:
    print("No headlines contain 'new'")

print("\n" + "=" * 50)
print("Combining mapping and filtering complete!")
print("=" * 50)

# Summary of what we've learned
print("\nSummary of List Comprehension Techniques:")
print("1. Mapping: [expression for item in list]")
print("2. Filtering: [item for item in list if condition]")
print("3. Combining: [expression for item in list if condition]")
print("\nKey benefits:")
print("- Concise and readable code")
print("- Efficient processing")
print("- Easy to combine operations")
print("- Pythonic and elegant")
print("=" * 50)
