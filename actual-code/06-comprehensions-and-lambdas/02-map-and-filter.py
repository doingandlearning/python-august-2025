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
    """
    Count the number of words in a headline.
    
    Args:
        headline_text (str): The headline to count words in
        
    Returns:
        int: The number of words in the headline
    """
    words = headline_text.split()
    return len(words)


print(list(map(get_word_count, headlines)))

# lambda

def add(a, b):
  return a + b

print(add(1,2))

add = lambda a, b: a + b

print(add(1,2))

# Higher Order Functions 

print(list(map(lambda h: len(h.split()), headlines)))
print(list(map(lambda h: h.upper(), headlines)))
print([h.upper() for h in headlines])


print(list(filter(lambda h: len(h) < 50, headlines))) 
# one off, throw away functions ... 
print([h for h in headlines if len(h) < 50])