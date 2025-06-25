file = open("file.txt") # handle to the file

# UTF-8 -> 8 bits per character (256)
# a-z A-Z 0-9 !@£$%^ ;'[]
# UTF-16 -> 16 bits per character

print(file.read())  # extracts the whole file as one big string

print("-" * 25)
file.seek(0)
lines = file.readlines()  # returns a list, split by line

for line in lines:
  print(line.strip())

print("-" * 25)

file.seek(0)
line = file.readline()

while line:
  print(line.strip())
  line = file.readline()  # returns None when no more lines

file.close()