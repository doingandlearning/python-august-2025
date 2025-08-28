file = open("test.txt")
print(file.read())
file.close()


# context handler!
with open("test.txt") as file:
  print(file.read())


  # idiomatic python - Pythonic