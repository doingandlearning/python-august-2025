"""
Solution for the News Analysis Lab.
"""

# Step 2: Start with a list of headlines
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

# Step 3: Count the Headlines and Average Length

# Count the headlines
number_of_headlines = len(headlines)
print(f"There are {number_of_headlines} headlines in the list.")

# Calculate the average headline length
total_words = 0
for headline in headlines:
    words_in_headline = headline.split()
    total_words += len(words_in_headline)

# It's good practice to check for division by zero
if number_of_headlines > 0:
    average_words = total_words / number_of_headlines
    print(f"The average headline has {average_words:.1f} words.")
else:
    print("The list of headlines is empty.")


# Step 4: Find the most common topics
print("-" * 20)
search_term = input("What topic are you interested in? ")

matching_headlines_list = []
for headline in headlines:
    if search_term.lower() in headline.lower():
        matching_headlines_list.append(headline)

print("-" * 20)
if matching_headlines_list:
    print(f"Found {len(matching_headlines_list)} headlines about '{search_term}':")
    for headline in matching_headlines_list:
        print(f"- {headline}")
else:
    print(f"Sorry, no headlines were found about '{search_term}'.") 