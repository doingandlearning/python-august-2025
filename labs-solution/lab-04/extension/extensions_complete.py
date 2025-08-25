# Lab 4: Extended Exploration of Containers - Complete Solution
# This program demonstrates all extensions from the extension lab

# Sample headlines for demonstration
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

print("=" * 70)
print("LAB 4 EXTENSIONS: ADVANCED NEWS HEADLINES ANALYSIS")
print("=" * 70)

# Basic analysis from the original lab
print("\n--- BASIC ANALYSIS ---")
total_headlines = len(headlines)
print(f"Total headlines: {total_headlines}")

# Count words
total_words = 0
for headline in headlines:
    words = headline.split()
    total_words += len(words)

average_words = total_words / total_headlines
print(f"Average words per headline: {average_words:.1f}")
print(f"Total words: {total_words}")

# Extension 1: Sort headlines by length
print("\n--- EXTENSION 1: SORTING BY LENGTH ---")

# Create list of tuples (headline, word_count) for sorting
headline_lengths = []
for headline in headlines:
    word_count = len(headline.split())
    headline_lengths.append((headline, word_count))

# Sort by word count (ascending) - using simple bubble sort
# Note: This is a manual implementation since we haven't covered advanced sorting yet
for i in range(len(headline_lengths)):
    for j in range(len(headline_lengths) - 1):
        if headline_lengths[j][1] > headline_lengths[j + 1][1]:
            # Swap the elements
            headline_lengths[j], headline_lengths[j + 1] = headline_lengths[j + 1], headline_lengths[j]

sorted_by_length = headline_lengths

print("Top 3 shortest headlines:")
for i in range(3):
    headline, count = sorted_by_length[i]
    print(f"{i+1}. ({count} words) {headline}")

print("\nTop 3 longest headlines:")
for i in range(3):
    headline, count = sorted_by_length[-(i+1)]
    print(f"{i+1}. ({count} words) {headline}")

# Extension 2: Count total characters
print("\n--- EXTENSION 2: CHARACTER COUNTING ---")

total_chars = 0
for headline in headlines:
    total_chars += len(headline)

average_chars = total_chars / len(headlines)
print(f"Total characters (including spaces): {total_chars}")
print(f"Average characters per headline: {average_chars:.1f}")

# Show character vs word comparison
print(f"Characters per word average: {total_chars / total_words:.1f}")

# Extension 3: Find question headlines
print("\n--- EXTENSION 3: QUESTION HEADLINES ---")

question_headlines = []
for headline in headlines:
    if headline.endswith('?'):
        question_headlines.append(headline)

if question_headlines:
    print(f"Found {len(question_headlines)} question headline(s):")
    for headline in question_headlines:
        print(f"• {headline}")
else:
    print("No question headlines found.")
    print("Note: You can add headlines ending with '?' to test this feature.")

# Extension 4: Uniform capitalization
print("\n--- EXTENSION 4: UNIFORM FORMATTING ---")

print("Original headlines:")
for i in range(3):
    print(f"{i+1}. {headlines[i]}")

print("\nTitle case formatting:")
for i in range(3):
    print(f"{i+1}. {headlines[i].title()}")

# Extension 5: Dictionary of headline lengths
print("\n--- EXTENSION 5: DICTIONARY OF LENGTHS ---")

length_dict = {}
for headline in headlines:
    word_count = len(headline.split())
    length_dict[headline] = word_count

print("Headline lengths dictionary:")
for headline, word_count in length_dict.items():
    if len(headline) > 40:
        short_headline = headline[:40] + "..."
    else:
        short_headline = headline
    print(f"'{short_headline}' -> {word_count} words")

# Extension 6: Group by first word
print("\n--- EXTENSION 6: GROUPING BY FIRST WORD ---")

# Group headlines by first word
groups = {}
for headline in headlines:
    first_word = headline.split()[0]
    if first_word not in groups:
        groups[first_word] = []
    groups[first_word].append(headline)

print("Headlines grouped by first word:")
for first_word, headline_list in groups.items():
    print(f"\n'{first_word}' ({len(headline_list)} headline(s)):")
    for headline in headline_list:
        print(f"  • {headline}")

# Interactive extensions
print("\n" + "=" * 70)
print("INTERACTIVE EXTENSIONS")
print("=" * 70)

# Extension 7: Multiple search terms
print("\n--- EXTENSION 7: MULTIPLE SEARCH TERMS ---")

search_input = input("Enter search terms separated by commas: ")
search_terms = []
for term in search_input.split(','):
    search_terms.append(term.strip())

print(f"\nSearching for: {search_terms}")

for term in search_terms:
    matches = []
    for headline in headlines:
        if term.lower() in headline.lower():
            matches.append(headline)
    
    print(f"\n'{term}': {len(matches)} match(es)")
    for headline in matches:
        print(f"  • {headline}")

# Extension 8: Highlight search terms
print("\n--- EXTENSION 8: SEARCH TERM HIGHLIGHTING ---")

search_term = input("Enter a search term to highlight: ")

print(f"\nHeadlines with '{search_term}' highlighted:")
for headline in headlines:
    if search_term.lower() in headline.lower():
        # Highlight the search term with asterisks
        highlighted = headline.replace(search_term, f"*{search_term}*")
        print(f"• {highlighted}")

# Extension 9: Word frequency counter
print("\n--- EXTENSION 9: WORD FREQUENCY COUNTER ---")

# Count word frequencies
word_freq = {}
for headline in headlines:
    words = headline.lower().split()
    for word in words:
        # Remove basic punctuation
        clean_word = word.strip('.,:;!?')
        if clean_word:
            if clean_word in word_freq:
                word_freq[clean_word] += 1
            else:
                word_freq[clean_word] = 1

# Sort by frequency (descending)
sorted_words = []
for word, count in word_freq.items():
    sorted_words.append((word, count))

# Simple sorting (bubble sort)
for i in range(len(sorted_words)):
    for j in range(len(sorted_words) - 1):
        if sorted_words[j][1] < sorted_words[j + 1][1]:
            sorted_words[j], sorted_words[j + 1] = sorted_words[j + 1], sorted_words[j]

print("Top 10 most frequent words:")
for i in range(min(10, len(sorted_words))):
    word, count = sorted_words[i]
    print(f"{i+1:2}. '{word}': {count} times")

print("\n" + "=" * 70)
print("ALL EXTENSIONS COMPLETE!")
print("=" * 70)
