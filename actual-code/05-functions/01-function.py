
print("Hello!")

def print_hello():  # no inputs, it returns nothing!
  """
  This is a function that prints hello with a seperator after
  """
  print("Hello")
  print("=" * 20)


print_hello()

def print_hello():
  print("Goodbye!")

print_hello()


def say_hello_to_user(name: str, location, message="I like it there.", seperator=True): # function signature
  print(f"Hello {name}, how is {location} today? {message}")
  if seperator:
    print("=" * 20)

# multiple users
# for first_name, where_they_are in [("Adam", "Salford"), ("Harriet", "Birmingham")]:
#   say_hello_to_user(first_name, where_they_are)

say_hello_to_user("Adam", "Salford", seperator=False)
say_hello_to_user("Hemini", "London")
say_hello_to_user("Emma", "Clapham", "I have only been here on the train from Brighton.", False)
say_hello_to_user(location="Glasgow", 
                  seperator=False, 
                  name=12, 
                  message="I work at the uni there a few times a year.")
# say_hello_to_user()