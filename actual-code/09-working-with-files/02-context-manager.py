file = open("file.txt")
print(file.read())
file.close()

print("-" * 25)

with open("file.txt") as file:  # Pythonic 
  print(file.read())