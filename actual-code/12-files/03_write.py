with open("myfile.txt", "w") as file:  # write -> destroys the file and writes from the start.
    file.write("Hello\n")
    file.write("How are you?\n")
    file.writelines(["I'm fine\n", "Thanks for asking\n", "How are you?\n"])


# opening files in write mode is destructive!

with open("logfile.txt", "a") as file:  # append mode -> appends to the end of the file.
    file.write("This is a new line.\n")

with open("test.txt") as file:
    for line in file:
        print(line.strip())
