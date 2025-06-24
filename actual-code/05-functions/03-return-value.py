def square(number):
  return number * number

print(square(5) + 1)

def get_user_search_terms():
  readings = []

  while True:
    input_string = input("What term do you want to search for (q to quit): ")

    if input_string == "q":
      break

    readings.append(input_string)

  return readings

def find_average_word_length(word_list):
  number_of_words = len(word_list)
  total_characters = 0
  for word in word_list:
    total_characters += len(word)
  return total_characters / number_of_words

search_terms = get_user_search_terms()
average_word_length = find_average_word_length(search_terms)
print(f"The average word length of this list: {search_terms} is {average_word_length}.")

print(average_word_length(search_terms()))