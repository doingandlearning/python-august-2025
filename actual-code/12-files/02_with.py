# Context Handler
# file = open("test.txt")
# file.close()

with open("test.txt") as file:
    print(file.readlines())

# a more idiomatic (pythonic) way to open files.