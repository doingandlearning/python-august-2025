user_input = input("What is the password? ")
attempts_tried = 0
is_out_of_tries = False
while user_input != "password123":  # we don't know how many times we want to loop.
  print("Incorrect password.")
  attempts_tried += 1
  if attempts_tried > 3:
    print("All out of tries!")
    is_out_of_tries = True
    break
  user_input = input("What is the password? ")

if not is_out_of_tries:
  print("Here are the secret documents.")