# Step 1: Getting Started
# This demonstrates the basic setup for the list comprehensions lab

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

# Basic verification that data is loaded
print("Step 1: Basic Setup Complete!")
print("=" * 50)
print(f"Loaded {len(headlines)} headlines")
print("First few headlines:")
for i in range(min(5, len(headlines))):
    headline = headlines[i]
    print(f"{i+1}. {headline}")

print("\nReady to work with list comprehensions!")
print("=" * 50)

# Verify we can access individual headlines
print("\nTesting headline access:")
print(f"First headline: '{headlines[0]}'")
print(f"Last headline: '{headlines[-1]}'")
print(f"Headline at index 5: '{headlines[5]}'")

print("\nTesting basic operations:")
print(f"Number of headlines: {len(headlines)}")
print(f"First headline word count: {len(headlines[0].split())}")
print(f"Second headline word count: {len(headlines[1].split())}")

print("=" * 50)
