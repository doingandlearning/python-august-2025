
age = int(input("What is your age? "))

is_teenager = None
if age < 20 and age > 12:
  is_teenager = True
else:
  is_teenager = False

print(is_teenager)

is_teenager = (True # this is the truth value
          if age < 20 and age > 12   # this is the test
          else False)   # this is the false value
print(is_teenager)