# import datetime
from datetime import datetime  # datetime -> we want datetime
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

try:
  with open("time.log", "a") as file:
    file.write(f"{datetime.now()}: This is a log message.\n")
except:
  print("Problem opening or writing to file.")