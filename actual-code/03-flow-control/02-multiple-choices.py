user_colour = input("What is your favourite colour? ").lower().strip()
# input validation

if user_colour == "green":
  print("You must like grass.")

elif user_colour.startswith("g"):
  print("Oh! I didn't know any other colours but green started with g!")

else:
  print(f"{user_colour} is a nice colour!")
