def get_guess():
    guess_str = input("Please guess a channel number: ")
    try:
      return int(guess_str)
    except ValueError:
      print("That isn't a valid number.")
      return get_guess()

class ChannelError(Exception):
  pass