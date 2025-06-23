user_input = input("Give me a positive integer: ")

while not user_input.isdigit():  # defensive programming!
  print("Whoops! You gave me some non-numbers, try again.")
  user_input = input("Give me a positive number: ")

user_input = int(user_input)

for temperature in range(1000):
  print(f"Checking {temperature}")
  if temperature == user_input:
    print("Found your number!")
    break
  else:
    print(f"Still looking ...")

for temperature in range(1000):
  print(f"Checking {temperature}")
  if temperature % user_input == 0:
    continue
  print(f"{temperature} is not a multiple of {user_input}")
   

