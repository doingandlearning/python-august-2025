
age = int(input("What is your age? "))

is_teenager = None
if age < 20 and age > 12:
  is_teenager = True
else:
  is_teenager = False

print(is_teenager)

is_teenager = True if age < 20 and age > 12 else False   # if statement -> ternary
print(is_teenager)