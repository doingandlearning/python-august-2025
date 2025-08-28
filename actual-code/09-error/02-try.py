import traceback

def divide(a,b):
  try:
    return a / b
  except ZeroDivisionError:
    print("Whoops! You tried to divide by zero.")
    return "No result"

def get_valid_number_from_user():
  try:
    return float(input("Give me a number: "))
  except ValueError:
    print("Invalid number.")
    return get_valid_number_from_user()

try:
  first_number = get_valid_number_from_user()
  second_number = get_valid_number_from_user()
  print(divide(first_number, second_number))
except Exception as exp:  # A bare except block is too broad!
  # User friendly error message
  print("Something went wrong, please try again!")
  # Still get the error to log for ops - log for debugging
  print(exp)
  traceback.print_exc()
else:
  print("Only if there wasn't an error!")
finally:
  print("This will run always - this is for cleanup!")

print("Do some more work!!")