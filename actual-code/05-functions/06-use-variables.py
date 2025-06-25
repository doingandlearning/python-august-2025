count = 1


# functions can read variables outside of themselves
def print_count():
  print(count)

def double(number):
  return number * 2

print_count()

count = double(count)  # you can change them outside of the function
print_count()