# Extension 2: Count total characters
# This demonstrates character counting vs word counting

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
print("EXTENSION 2: CHARACTER COUNTING")
print("=" * 60)

# Count total characters (including spaces and punctuation)
total_chars = 0
for headline in headlines:
    total_chars += len(headline)

# Calculate average characters per headline
average_chars = total_chars / len(headlines)

print(f"Total characters (including spaces): {total_chars}")
print(f"Average characters per headline: {average_chars:.1f}")

# Compare with word count
total_words = 0
for headline in headlines:
    words = headline.split()
    total_words += len(words)

average_words = total_words / len(headlines)
print(f"\nTotal words: {total_words}")
print(f"Average words per headline: {average_words:.1f}")

# Show character vs word comparison
chars_per_word = total_chars / total_words
print(f"Characters per word average: {chars_per_word:.1f}")

# Show detailed breakdown
print("\n" + "-" * 40)
print("DETAILED BREAKDOWN BY HEADLINE")
print("-" * 40)

for i in range(len(headlines)):
    headline = headlines[i]
    char_count = len(headline)
    word_count = len(headline.split())
    chars_per_word_this = char_count / word_count
    
    print(f"{i+1:2}. {char_count:3} chars, {word_count:2} words, {chars_per_word_this:4.1f} chars/word")
    print(f"    '{headline}'")

print("\n" + "=" * 60)
print("Extension 2 Complete!")
print("=" * 60)
