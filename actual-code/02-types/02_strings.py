user_name = "kevincunningham"
print(user_name)

# user_name = 'kevincunningham\nThis will be on a new line'
# print(user_name)
# Ctrl-/
# user_name = """kevincunningham
# New line here"""

# print(user_name)

print(len(user_name)) # length of a string

password = "12345"
print(len(password))

# concatenate - join strings
print(user_name + " is in Belfast")
print(1 + 1)
print(user_name + str(1)) 

print(user_name.isdigit())  # Are all the characters digits?
print(password.isdigit())
print(user_name.isalnum())

print(user_name.replace("kevin", "ethan"))
print(user_name)

user_name = user_name.replace("kevin", "ethan")
print(user_name)

count = 1
count = count + 1
print(count)

print(user_name.find("kevin"))  # can't find it? the result will be -1
print(user_name.find("cunningham"))  # Python is zero-indexed

# ethancunningham
# 0123456789

print(user_name[5])  # print character at position 5
print(user_name[5:9])   # [start:end] -> don't include the end!
print(user_name[5:])
print(user_name[:5])

print(user_name.startswith("ethan"))
print(user_name.center(100))
print(user_name.upper())