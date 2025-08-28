"""
This is a utility file that has some useful functions.

- how to use
- what should be in here
- try to keep them small, lean, and focused 
"""

def printer(message):
  print("I am the printer function")
  print(message)
  print("Did I do okay?")
  print("=" * 20)

class Shape:
  def __init__(self, type):
    self.type = type

  def __repr__(self):
    return f"Shape(type={self.type})"

default_shape = Shape("triangle")

def main():
  print(f"I am the utils.py module: __name__ == {__name__}")
  printer("Welcome!")

if __name__ == "__main__":
  main()