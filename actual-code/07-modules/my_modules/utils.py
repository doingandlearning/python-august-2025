"""
This is a doc string for the utils module
It has useful stuff
It tells things about this file
"""

def printer(thing_to_print):
  print("I am the printer!")
  print(thing_to_print)
  print("Did I do okay?")
  print("-" * 20)

class Shape:
  def __init__(self, type):
    self.type = type

  def __str__(self):
    return f"Shape of type {self.type}"



default_shape = Shape("triangle")

def main():
  print("I am in the utils.py file")
  print(f"utils.py name is {__name__}")
  print(__file__)
  print(__doc__)

if __name__ == "__main__":
  main()