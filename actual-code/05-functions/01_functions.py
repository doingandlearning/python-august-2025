# define!

# parameters
def print_message():
    """

    :return:
    """
    print("This is a message!")


# arguments
print_message()


def print_message(message: str, number_of_dashes=25, is_shouting=False):
    """
    Print a message from the user
    :param message: This is the custom message from the user.
    :param number_of_dashes: How many dashes should follow the message
    :param is_shouting: A boolean to decide if the message is shouted
    :return:
    """
    if is_shouting:
        print("HEAR YE, HEAR YE!")
        print(message.upper())
    else:
        print(message)
    print("-" * number_of_dashes)


print_message("This is an important message!!", 30, True)
print_message("This is an important message!!", 30)
print_message("This is an important message!!")

print_message(number_of_dashes=100, message="Weird - this is backwards!")
