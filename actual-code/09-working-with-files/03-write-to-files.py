with open("log.txt", "w") as file:  # this is destructive!!
  file.write("Hello \n")
  file.write("Python rocks! \n")
  for number in range(100):
    file.write(f"{number + 1} - I love Python!\n")
  file.writelines(["This\n", "and this\n", "and also this\n"])