# Step 3: A Function to Find Headlines with a Keyword
# This demonstrates function with multiple parameters and returning lists

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
    """
    Find headlines that contain a specific keyword.
    
    Args:
        list_of_headlines (list): List of headline strings
        keyword (str): The keyword to search for
        
    Returns:
        list: Headlines containing the keyword
    """
    matching_headlines = []
    
    for headline in list_of_headlines:
        # Case-insensitive search
        if keyword.lower() in headline.lower():
            matching_headlines.append(headline)
    
    return matching_headlines

# Test the search function
print("Step 3: Search Function Complete!")
print("=" * 50)

# Test with different keywords
test_keywords = ["new", "tax", "NHS", "London", "to"]

for keyword in test_keywords:
    print(f"\nSearching for '{keyword}':")
    print("-" * 30)
    
    matching = find_headlines_with_keyword(headlines, keyword)
    
    if matching:
        print(f"Found {len(matching)} headline(s):")
        for i in range(len(matching)):
            headline = matching[i]
            word_count = get_word_count(headline)
            print(f"  {i+1}. '{headline}' ({word_count} words)")
    else:
        print(f"No headlines found containing '{keyword}'")

# Test with a keyword that shouldn't exist
print(f"\nSearching for 'xyz123':")
print("-" * 30)
xyz_results = find_headlines_with_keyword(headlines, "xyz123")
if not xyz_results:
    print("Correctly found no matches for 'xyz123'")

print("\nSearch function is working correctly!")
print("=" * 50)
