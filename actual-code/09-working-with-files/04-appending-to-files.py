import datetime

try:
  with open("time.log", "a") as file:
    file.write(f"{datetime.datetime.now()}: This is a log message.\n")
except:
  print("Problem opening or writing to file.")