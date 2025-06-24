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
  Returns the number of words in a string of text.
  """
  word_count = len(headline_text.split(" "))
  return word_count

def find_headlines_with_keyword(list_of_headlines, keyword):
  result = []
  lower_keyword = keyword.lower()
  for headline in list_of_headlines:
    if lower_keyword in headline.lower():
      result.append(headline)
  return result

def analyse_all_headlines(list_of_headlines):
  total = 0
  for headline in list_of_headlines:
    total += get_word_count(headline)
  average = total / len(list_of_headlines)
  print(f"The average headline length is {average}")
  return average




print("--- Headline Analysis ---")
analyse_all_headlines(headlines)  # print the average length ... 

print("\n--- Searching for 'New' ---")
new_headlines = find_headlines_with_keyword(headlines, "new")
for h in new_headlines:
    print(h)

print("\n--- Searching for 'Tax' ---")
tax_headlines = find_headlines_with_keyword(headlines, "tax")
for h in tax_headlines:
    print(h)