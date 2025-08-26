value = 12.34

print(type(str(value)))

value = "12.34"
print(float(value) + 12)

user_number = int(input("Give me a number: "))  # it is always a str!

user_number = input("Give me a number: ")  # it is always a str!
user_number = int(user_number)

print("Your number is " + str(user_number) + ", 10 more than this is:")
print(int(user_number) + 10)
print(type(user_number))