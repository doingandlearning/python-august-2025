user_name = "kevincunningham"
user_name = 'kevincunningham'
#              0123456789
user_name = """kevincunningham"""

print(user_name.find("BBC"))  # The position where the string starts or -1 if it can't find it
print(len(user_name))  # how many characters are in the string
print(user_name)

print(user_name[14])    # print the character at the position (index)
print(user_name[5:15])  # [start:end]   (inclusive , exclusive)
print(user_name[5:])    # from the start value, all the way to the end
print(user_name[:15])   # from the start of the string, up to but not including the end value

user_name = input("What is your name? ")
print("Hello, " + user_name + ", how are you today?")

print(f"Hello, {user_name}, how are you today?")  # ``
result = 1 + 1
print("1 + 1 = " + str(result))
print(f"1 + 1 = {1+1}")  # interpolation -> force Python to not be lazy!

print(len("Elon Musk says something sensible".split()))