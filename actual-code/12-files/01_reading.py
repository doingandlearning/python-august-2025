file = None

try:
    file = open("test.txt")   # file handle
    # 1 - .read()
    print(file.read())  # returns the whole file as a single string!
    # 2 - .readlines()
    file.seek(0)  # moves the cursor to position 0
    print([line.strip() for line in file.readlines()])  # returns the whole file as a list of strings
    # 3 - .readline()
    file.seek(0)
    line = file.readline().strip()
    while line:
        print(line)
        line = file.readline().strip()
except FileNotFoundError:
    print("Can't find file.")
finally:
    print("About to close file!")
    file.close()

