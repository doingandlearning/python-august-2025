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

# DRY - Don't Repeat Yourself
total_number_of_headlines = len(headlines)
print(f"There are {total_number_of_headlines} headlines.")
total_words = 0

for headline in headlines:
  headline_length = len(headline.split(" "))
  total_words += headline_length

print(f"The average headline length is {total_words / total_number_of_headlines} words.")

user_search = input("What term do you want to search for? ").lower()

matching_headlings = 0

for headline in headlines:
  if headline.lower().find(user_search) > -1:
    matching_headlings+=1

print(f"There are {matching_headlings} headlines with your search term.")