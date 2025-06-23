user_color = input("What's your favourite colour? ")

if user_color == "green":
  print("You must like grass")
elif user_color.startswith("b"):  # elif -> contraction of else if
  print("Colours that start with b are blue and burgundy")
elif user_color.startswith("g"):
  print("Colours that with g are green and gold.")
else:
  print(f"{user_color} is a nice colour")