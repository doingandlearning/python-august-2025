# Extension 9: Build a simple frequency counter
# This demonstrates advanced data analysis with dictionaries

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
print("EXTENSION 9: WORD FREQUENCY COUNTER")
print("=" * 60)

# Count word frequencies
word_freq = {}
for headline in headlines:
    # Split headline into words
    words = headline.lower().split()
    
    for word in words:
        # Remove basic punctuation
        clean_word = word.strip('.,:;!?')
        
        if clean_word:  # Only count non-empty words
            # Add to frequency count
            if clean_word in word_freq:
                word_freq[clean_word] += 1
            else:
                word_freq[clean_word] = 1

# Display all word frequencies
print("All word frequencies:")
print("-" * 40)
for word, count in sorted(word_freq.items()):
    print(f"'{word}': {count}")

# Find the most frequent words
print("\n" + "=" * 60)
print("MOST FREQUENT WORDS")
print("=" * 60)

# Sort words by frequency (descending)
sorted_words = []
for word, count in word_freq.items():
    sorted_words.append((word, count))

# Simple sorting (bubble sort) to find top words
for i in range(len(sorted_words)):
    for j in range(len(sorted_words) - 1):
        if sorted_words[j][1] < sorted_words[j + 1][1]:
            # Swap the elements
            sorted_words[j], sorted_words[j + 1] = sorted_words[j + 1], sorted_words[j]

# Display top 10 most frequent words
print("Top 10 most frequent words:")
print("-" * 40)
for i in range(min(10, len(sorted_words))):
    word, count = sorted_words[i]
    print(f"{i+1:2}. '{word}': {count} times")

# Show word length analysis
print("\n" + "=" * 60)
print("WORD LENGTH ANALYSIS")
print("=" * 60)

# Count words by length
length_freq = {}
for word, count in word_freq.items():
    word_length = len(word)
    if word_length not in length_freq:
        length_freq[word_length] = []
    length_freq[word_length].append((word, count))

# Display words grouped by length
for length in sorted(length_freq.keys()):
    words_of_length = length_freq[length]
    print(f"\n{length} letter words ({len(words_of_length)} words):")
    for word, count in words_of_length:
        print(f"  '{word}': {count}")

# Show statistics
print("\n" + "=" * 60)
print("FREQUENCY STATISTICS")
print("=" * 60)

total_words = len(word_freq)
total_occurrences = 0
for count in word_freq.values():
    total_occurrences += count

print(f"Total unique words: {total_words}")
print(f"Total word occurrences: {total_occurrences}")
print(f"Average frequency: {total_occurrences / total_words:.1f}")

# Find words that appear only once
single_occurrence_words = []
for word, count in word_freq.items():
    if count == 1:
        single_occurrence_words.append(word)

print(f"Words appearing only once: {len(single_occurrence_words)}")

# Show some examples of single-occurrence words
if single_occurrence_words:
    print("Examples of single-occurrence words:")
    for i in range(min(10, len(single_occurrence_words))):
        word = single_occurrence_words[i]
        print(f"  • '{word}'")

print("\n" + "=" * 60)
print("Extension 9 Complete!")
print("=" * 60)
