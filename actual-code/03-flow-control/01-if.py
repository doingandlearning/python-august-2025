print("I come before the if statement")

number_input = int(input("Give me a number: "))  # non-blocking

if number_input == 42:
  print("That's my favourite number")

if number_input > 50:
  print("That's a big number!")

if number_input < 50:
  print("I would like that many crisps.")


print("I come after the if statement")

user_color = input("What's your favourite colour? ")

if user_color == "green":
  print("You must like grass")

if user_color.startswith("b"):
  print("Colours that start with b are blue and burgundy")