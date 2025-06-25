favourite_channel = int(input("What's your favourite channel from the 90s? "))


try:
  if favourite_channel > 5:
    raise ValueError("We didn't have that many channels then")

  print("That's my favourite too!")
except ValueError:
  print("I think your forgetting we only had five channels then.")

class MyError(Exception):
  pass

raise MyError("Something went wrong")