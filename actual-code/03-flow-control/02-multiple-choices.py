user_colour = input("What is your favourite colour? ").lower().strip()
# input validation

if user_colour == "green":
  print("You must like grass.")

elif user_colour == "grey":
  print("The sky is in Glasgow is normally that colour!")

elif user_colour.startswith("g"):
  print("Oh! I didn't know any other colours but green started with g!")

elif user_colour == "red":
  print("Manchester United play in red")

else:
  print(f"{user_colour} is a nice colour!")
