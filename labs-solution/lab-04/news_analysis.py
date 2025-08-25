# Lab 4: Analyzing News Headlines - Complete Solution
# This program demonstrates working with lists, loops, and string operations

# Step 1: Create a list of headlines
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
print("BBC NEWS HEADLINES ANALYSIS")
print("=" * 60)

# Step 2: Count the headlines
total_headlines = len(headlines)
print(f"There are {total_headlines} headlines in the list.")
print()

# Step 3: Calculate the average headline length
total_words = 0
for headline in headlines:
    # Split each headline into words and count them
    words = headline.split()
    total_words += len(words)

# Calculate and display the average
average_words = total_words / total_headlines
print(f"The average headline length is {average_words:.1f} words.")
print()

# Step 4: Find headlines about a specific topic
print("-" * 40)
search_term = input("What topic would you like to search for? ")

# Search through headlines (case-insensitive)
matching_headlines = 0
print(f"\nHeadlines containing '{search_term}':")
print("-" * 40)

for headline in headlines:
    # Convert both to lowercase for case-insensitive search
    if search_term.lower() in headline.lower():
        print(f"• {headline}")
        matching_headlines += 1

# Display the final count
if matching_headlines == 0:
    print(f"No headlines found containing '{search_term}'.")
else:
    print(f"\nFound {matching_headlines} headline(s) containing '{search_term}'.")

print("\n" + "=" * 60)
print("Analysis complete!")
print("=" * 60)
