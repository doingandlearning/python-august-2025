user_input = input("Give me a number: ")
try:
  my_variable = int(user_input)  # never trust users!
  # 5/0
  open("does-not-exist")
except ValueError as error:
  print("That was not a number!")  # a more user/human friendly
  print(error)  # emailing to support/logging ... 

except ZeroDivisionError:
  print("You can't divide by zero!")

except Exception as e:  # catchall for all errors
  print("Something unexpected happened.")
  print(e)

print(f"Your number was {my_variable}")

