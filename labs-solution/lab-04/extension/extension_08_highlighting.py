# Extension 8: Highlight search terms in headlines
# This demonstrates string replacement and text highlighting

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
print("EXTENSION 8: SEARCH TERM HIGHLIGHTING")
print("=" * 60)

# Show available headlines
print("Available headlines:")
print("-" * 40)
for i in range(len(headlines)):
    headline = headlines[i]
    print(f"{i+1:2}. {headline}")

print("\n" + "=" * 60)
print("SEARCH TERM HIGHLIGHTING")
print("=" * 60)

# Get search term from user
search_term = input("Enter a search term to highlight: ")

# Find and highlight matching headlines
matching_headlines = []
for headline in headlines:
    if search_term.lower() in headline.lower():
        matching_headlines.append(headline)

# Display results with highlighting
if matching_headlines:
    print(f"\nFound {len(matching_headlines)} headline(s) containing '{search_term}':")
    print("=" * 60)
    
    for i in range(len(matching_headlines)):
        headline = matching_headlines[i]
        
        # Method 1: Highlight with asterisks
        highlighted_asterisk = headline.replace(search_term, f"*{search_term}*")
        
        # Method 2: Highlight with ALL CAPS
        highlighted_caps = headline.replace(search_term, search_term.upper())
        
        # Method 3: Highlight with underscores
        highlighted_underscore = headline.replace(search_term, f"_{search_term}_")
        
        print(f"\n{i+1}. Original:     {headline}")
        print(f"   Asterisks:    {highlighted_asterisk}")
        print(f"   ALL CAPS:     {highlighted_caps}")
        print(f"   Underscores:  {highlighted_underscore}")
else:
    print(f"\nNo headlines found containing '{search_term}'.")

# Show different highlighting styles
print("\n" + "=" * 60)
print("DIFFERENT HIGHLIGHTING STYLES")
print("=" * 60)

if matching_headlines:
    print("Choose your preferred highlighting style:")
    print("1. Asterisks: *term*")
    print("2. ALL CAPS: TERM")
    print("3. Underscores: _term_")
    print("4. Brackets: [term]")
    print("5. Double quotes: \"term\"")
    
    # Demonstrate all styles on the first match
    first_match = matching_headlines[0]
    print(f"\nExample with '{first_match}':")
    
    style1 = first_match.replace(search_term, f"*{search_term}*")
    style2 = first_match.replace(search_term, search_term.upper())
    style3 = first_match.replace(search_term, f"_{search_term}_")
    style4 = first_match.replace(search_term, f"[{search_term}]")
    style5 = first_match.replace(search_term, f"\"{search_term}\"")
    
    print(f"  Style 1: {style1}")
    print(f"  Style 2: {style2}")
    print(f"  Style 3: {style3}")
    print(f"  Style 4: {style4}")
    print(f"  Style 5: {style5}")

# Show case-insensitive highlighting
print("\n" + "=" * 60)
print("CASE-INSENSITIVE HIGHLIGHTING")
print("=" * 60)

# Find all variations of the search term
all_variations = []
for headline in headlines:
    # Find all occurrences (case-insensitive)
    lower_headline = headline.lower()
    lower_term = search_term.lower()
    
    if lower_term in lower_headline:
        # Find the actual text as it appears in the headline
        start_pos = lower_headline.find(lower_term)
        actual_term = headline[start_pos:start_pos + len(search_term)]
        all_variations.append(actual_term)

if all_variations:
    print(f"Found these variations of '{search_term}':")
    for variation in all_variations:
        print(f"  • '{variation}'")
    
    print(f"\nTotal variations found: {len(all_variations)}")

print("\n" + "=" * 60)
print("Extension 8 Complete!")
print("=" * 60)
