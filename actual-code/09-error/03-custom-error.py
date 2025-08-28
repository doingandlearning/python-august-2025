class BBCError(Exception):
  pass

try:
  headline = input("What's your headline? ")
  if len(headline) < 10:
    raise BBCError("Headlines should be at least 15 characters")
except BBCError as exp:
  print(f"Fails because of {exp}")