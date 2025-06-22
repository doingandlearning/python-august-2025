# if <test -> True or False>:
if True:
    # run this code!
    print("I will always print!")

if False:
    print("I will never print!")

num = 13

if num < 18:  # True
    print("Still not able to vote.")
else:
    print("You are able to vote - make sure you are registered!")

print("Keep going!")

# favourite_colour = input("What is your favourite colour? ").lower()
#
# if favourite_colour == "blue":
#     print("The sky is blue.")
# elif favourite_colour == "green":  # else if
#     print("Happy St. Patrick's day!")
# elif favourite_colour == "yellow":
#     print("The sun can be yellow.")
# elif favourite_colour.startswith("y"):
#     print(f"I like colours that start with y, especially {favourite_colour}!")
# else:
#     print(f"{favourite_colour} is a nice color - good choice!")

# jump to here!

age = 15

if age > 12 and age < 20:  # or
    print("You are a teenager.")
elif age >= 20:
    print("You used to be a teenager.")
else:
    print("You will soon be a teenager.")

is_game_over = True

if not is_game_over:
    print("Keep playing!")
else:
    print("Who won?")


colour = "green"

match colour:  # 3.10
    case "blue":
        print("That's a nice colour!")
    case "red":
        print("So is that")
    case _:
        print("I didn't think of that colour!")
