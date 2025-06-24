# def to define a function
# name our function
def print_hello():  # no parameters/arguments
  print("Hello")
  print("Hello")
  print("-" * 20)  

# modular (lego bricks)
# encapsulated

print(print_hello())

empty_list = []
print(empty_list.extend([1,2,3,4]))
print(empty_list)

# def input
# def print

# input()
# print()

def say_hello_to_user(name):
  print(f"Hello {name}, nice to meet you!")
  print("-" * 20)

say_hello_to_user("Niranjan")

def print_message_to_user(name, message):
  print(f"Hello {name}, {message}")
  print("-" * 20)

print_message_to_user("Niranjan", "I'm going to airfry some chicken")

