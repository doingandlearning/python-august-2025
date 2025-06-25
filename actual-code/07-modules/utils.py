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

print("I am in the utils.py file")

default_shape = Shape("triangle")