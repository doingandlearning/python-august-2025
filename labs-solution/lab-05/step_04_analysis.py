# Step 4: A Main Analysis Function
# This demonstrates calling functions from within other functions

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

def get_word_count(headline_text):
    """Count the number of words in a headline."""
    words = headline_text.split()
    return len(words)

def find_headlines_with_keyword(list_of_headlines, keyword):
    """Find headlines that contain a specific keyword."""
    matching_headlines = []
    
    for headline in list_of_headlines:
        if keyword.lower() in headline.lower():
            matching_headlines.append(headline)
    
    return matching_headlines

def analyse_all_headlines(list_of_headlines):
    """
    Analyze all headlines and display statistics.
    
    Args:
        list_of_headlines (list): List of headline strings
    """
    total_words = 0
    
    # Count words in each headline using our function
    for headline in list_of_headlines:
        word_count = get_word_count(headline)
        total_words += word_count
    
    # Calculate and display average
    average_words = total_words / len(list_of_headlines)
    
    print("=" * 50)
    print("HEADLINE ANALYSIS RESULTS")
    print("=" * 50)
    print(f"Total headlines analyzed: {len(list_of_headlines)}")
    print(f"Total words across all headlines: {total_words}")
    print(f"Average words per headline: {average_words:.1f}")
    print("=" * 50)

# Test the analysis function
print("Step 4: Analysis Function Complete!")
print("=" * 50)

# Run the analysis
analyse_all_headlines(headlines)

# Show how the function integrates with other functions
print("\nDemonstrating function integration:")
print("-" * 40)

# Use our functions together
print("Headlines with 'new':")
new_headlines = find_headlines_with_keyword(headlines, "new")
for headline in new_headlines:
    word_count = get_word_count(headline)
    print(f"  • '{headline}' ({word_count} words)")

print("\nHeadlines with 'tax':")
tax_headlines = find_headlines_with_keyword(headlines, "tax")
for headline in tax_headlines:
    word_count = get_word_count(headline)
    print(f"  • '{headline}' ({word_count} words)")

print("\nAll functions are working together!")
print("=" * 50)
