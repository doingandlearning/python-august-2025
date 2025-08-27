# Step 3: Find Headlines About Specific Topics
# This demonstrates searching through lists and string operations

# Create a list of news headlines
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

# Display basic info
print(f"Loaded {len(headlines)} headlines for searching.")
print()

# Get search term from user
search_term = input("What topic would you like to search for? ")

# Search through headlines (case-insensitive)
matching_headlines = 0
print(f"\nHeadlines containing '{search_term}':")
print("-" * 50)

for headline in headlines:
    # Convert both to lowercase for case-insensitive search
    if search_term.lower() in headline:
        print(f"• {headline}")
        matching_headlines += 1

# Display the final count
print("-" * 50)
if matching_headlines == 0:
    print(f"No headlines found containing '{search_term}'.")
else:
    print(f"Found {matching_headlines} headline(s) containing '{search_term}'.")

# Show some example searches
print("\n" + "=" * 50)
print("Try searching for: election, NHS, London, AI, or any other topic!")
print("=" * 50)
