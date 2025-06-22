"""
Solution for the Functions Lab: Headline Analysis Toolkit.
"""

# Step 1: Getting Started
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

# --- Function Definitions ---

# Step 2: A Function to Get Word Count
def get_word_count(headline_text):
    """Takes a string and returns the number of words in it."""
    return len(headline_text.split())

# Step 3: A Function to Find Headlines with a Keyword
def find_headlines_with_keyword(list_of_headlines, keyword):
    """
    Takes a list of headlines and a keyword, and returns a new list
    containing only the headlines that include the keyword.
    """
    matching_headlines = []
    for headline in list_of_headlines:
        if keyword.lower() in headline.lower():
            matching_headlines.append(headline)
    return matching_headlines

# Step 4: A Main Analysis Function
def analyse_all_headlines(list_of_headlines):
    """
    Calculates and prints the average word count for a list of headlines.
    """
    total_words = 0
    for headline in list_of_headlines:
        total_words += get_word_count(headline)

    if list_of_headlines:
        average_words = total_words / len(list_of_headlines)
        print(f"The average headline has {average_words:.1f} words.")
    else:
        print("The list of headlines is empty.")


# --- Main Script ---
print("--- Headline Analysis ---")
analyse_all_headlines(headlines)

print("\n--- Searching for 'New' ---")
new_headlines = find_headlines_with_keyword(headlines, "new")
if new_headlines:
    for h in new_headlines:
        print(h)
else:
    print("No headlines found with the keyword 'new'.")


print("\n--- Searching for 'Tax' ---")
tax_headlines = find_headlines_with_keyword(headlines, "tax")
if tax_headlines:
    for h in tax_headlines:
        print(h)
else:
    print("No headlines found with the keyword 'tax'.")

print("\n--- Searching for 'Health' ---")
health_headlines = find_headlines_with_keyword(headlines, "health")
if health_headlines:
    for h in health_headlines:
        print(h)
else:
    print("No headlines found with the keyword 'health'.") 