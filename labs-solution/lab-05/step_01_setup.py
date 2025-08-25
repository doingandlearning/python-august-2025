# Step 1: Getting Started
# This demonstrates the basic setup for the headline analyzer lab

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
for i in range(min(3, len(headlines))):
    headline = headlines[i]
    print(f"{i+1}. {headline}")

print("\nReady to add functions!")
print("=" * 50)
