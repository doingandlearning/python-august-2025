string_1 = "This is a string"
string_2 = '"This is a string", they said\nAnd this?'
string_3 = """This is a string
This is part of the same string"""

print(string_1)
print(string_2)
print(string_3)

print(string_1.title())
print(string_1.replace("is", "was"))
print(string_1.center(100))
print(string_1.find("is"))
"This is a string"
#012
print(string_1.find("Kevin"))