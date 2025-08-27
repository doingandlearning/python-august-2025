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

headline_lengths = []
for h in headlines:
    headline_lengths.append(len(h.split()))

print(headline_lengths)
print(sum(headline_lengths))

alt_headline_length = [len(h.split()) for h in headlines]

# Map  (a => b)
shouted_headlines = [(h.upper(), "BBC") for h in headlines]
print(shouted_headlines)

# Filter (is allowed)
short_headlines = [h for h in headlines if len(h.split()) <= 5]
print(short_headlines)

shouted_short_headlines =[h.upper() for h in headlines if len(h.split()) > 5] 
print(shouted_short_headlines)

