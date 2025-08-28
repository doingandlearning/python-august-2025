file = open("test.txt")

print(file.read()) # opens the whole file as a string

file.seek(0)  # move the 'cursor' to the start of the file
lines = [line.strip() for line in file.readlines()]  # opens the whole file and splits the new lines into strings in a list

print(lines[2])

file.seek(0)

line = file.readline()

while line:
  print(line.strip())
  line = file.readline()

file.close()