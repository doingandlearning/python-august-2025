# if number > 50:
#   print("hello")

# count = 0

# while count < 5:  # infinite loop!
#   print("Hello!")
#   count += 1
#   # count = count + 1
# # is it 5 or forever?

user_input = input("Give me a positive integer: ")

while not user_input.isdigit():
  print("Whoops! You gave me some non-numbers, try again.")
  user_input = input("Give me a positive number: ")

user_input = int(user_input)

print(f"One more than that is {user_input + 1}")