# Extension 7: Support multiple search terms
# This demonstrates string splitting and multiple searches

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
print("EXTENSION 7: MULTIPLE SEARCH TERMS")
print("=" * 60)

# Show available headlines
print("Available headlines:")
print("-" * 40)
for i in range(len(headlines)):
    headline = headlines[i]
    print(f"{i+1:2}. {headline}")

print("\n" + "=" * 60)
print("MULTIPLE SEARCH DEMONSTRATION")
print("=" * 60)

# Get search terms from user
search_input = input("Enter search terms separated by commas: ")

# Split the input into individual search terms
search_terms = []
for term in search_input.split(','):
    # Remove extra spaces and convert to lowercase for searching
    clean_term = term.strip()
    if clean_term:  # Only add non-empty terms
        search_terms.append(clean_term)

print(f"\nSearching for: {search_terms}")

# Search for each term
for term in search_terms:
    print(f"\n" + "-" * 40)
    print(f"Searching for: '{term}'")
    print("-" * 40)
    
    # Find matches for this term
    matches = []
    for headline in headlines:
        if term.lower() in headline.lower():
            matches.append(headline)
    
    # Display results
    if matches:
        print(f"Found {len(matches)} match(es):")
        for i in range(len(matches)):
            headline = matches[i]
            print(f"  {i+1}. {headline}")
    else:
        print(f"No matches found for '{term}'")

# Show summary of all searches
print("\n" + "=" * 60)
print("SEARCH SUMMARY")
print("=" * 60)

total_matches = 0
for term in search_terms:
    match_count = 0
    for headline in headlines:
        if term.lower() in headline.lower():
            match_count += 1
    total_matches += match_count
    print(f"'{term}': {match_count} match(es)")

print(f"\nTotal matches across all terms: {total_matches}")

# Show headlines that match multiple terms
print("\n" + "=" * 60)
print("HEADLINES MATCHING MULTIPLE TERMS")
print("=" * 60)

multi_match_headlines = []
for headline in headlines:
    match_count = 0
    for term in search_terms:
        if term.lower() in headline.lower():
            match_count += 1
    
    if match_count > 1:
        multi_match_headlines.append((headline, match_count))

if multi_match_headlines:
    print("Headlines that match multiple search terms:")
    for headline, match_count in multi_match_headlines:
        print(f"  • {headline} (matches {match_count} terms)")
else:
    print("No headlines match multiple search terms.")

print("\n" + "=" * 60)
print("Extension 7 Complete!")
print("=" * 60)
