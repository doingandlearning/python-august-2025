# Step 2: Count the Headlines and Calculate Average Length
# This demonstrates basic list operations and loops

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

# Count the total number of headlines
total_headlines = len(headlines)
print(f"There are {total_headlines} headlines in the list.")

# Calculate the average headline length
total_words = 0
for headline in headlines:
    # Split each headline into words and count them
    words = headline.split()
    total_words += len(words)
    # total_words = total_words + len(words)

# Calculate and display the average
average_words = total_words / total_headlines
print(f"The average headline length is {average_words:.1f} words.")

# Display some additional statistics
print(f"Total words across all headlines: {total_words}")
print(f"Longest headline: {max(headlines, key=len)}")
print(f"Shortest headline: {min(headlines, key=len)}")
