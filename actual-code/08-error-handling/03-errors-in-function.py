def get_a_number_from_user():
  user_number = input("Give me a number: ")

  try:
    user_number = int(user_number)
  except ValueError:
    raise Exception("Silly user")
    print("That wasn't a number")
    return get_a_number_from_user()


  return user_number

print(get_a_number_from_user())