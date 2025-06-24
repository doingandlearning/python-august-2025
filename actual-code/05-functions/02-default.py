def print_message_to_user(name, message="How did you enjoy that program?", method="email"):
  """
  Will print a message directed at a user

  :param name: The user's name
  :param message: The message to the user
  :param method: How to send the message
  """
  print(f"Send {method} to {name}: {message}")
  print("-" * 20)


print_message_to_user("Halit", "How was your lunch?")
print_message_to_user(method="SMS", name="Ciaran")
print_message_to_user("Sophia", "How's monitoring going?", "WhatsApp")
print_message_to_user()

for number in range(10):
  print(number, end=" ")

