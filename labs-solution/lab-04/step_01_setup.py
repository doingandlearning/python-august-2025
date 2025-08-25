# Step 1: Create a New File and List of Headlines
# This demonstrates the basic setup for the news analysis lab

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

# Display the headlines to verify they're loaded
print("Headlines loaded successfully!")
print(f"Number of headlines: {len(headlines)}")
print("\nFirst few headlines:")
for i, headline in enumerate(headlines[:3], 1):
    print(f"{i}. {headline}")
