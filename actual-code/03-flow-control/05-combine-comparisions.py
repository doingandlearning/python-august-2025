is_sunny = True 
temperature = 18
has_airconditioning = True

# >, <, >=, <=, ==, != (not equal to)


if is_sunny and temperature > 20:  # True and True
    if not has_airconditioning:
      print("It's hot - make sure you stay hydrated!")
    else:
      print("Whack the airconditioning up to full!")
else:
  print("When it's warm and sunny, you need to be careful")  
             # it could be sunny and cold, 
             # or it sound be not sunny and hot,
             # it could be not sunny and cold

# minimise nesting ... 

user_password = input("What's your new password: ")

if len(user_password) < 8:
  print("Passwords should have at least 8 characters")

if not user_password.isalnum():
  print("Sorry, we don't allow special characters in our passwords")