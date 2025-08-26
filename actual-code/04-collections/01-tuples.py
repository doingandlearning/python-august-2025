# empty_tuple = ()  

# print(type(empty_tuple))
# print(empty_tuple)

# # immutable, fixed size
# names = ("Anya", "Hemini", "Jack", "Neil", "David", "Rob", True, 1, 1.2, "Harriet")
# print(type(names))
# print(len(names))
# print(names[1]) # referenced by index
# print(names[6])
# # print(names[20]) will crash the program - be careful!
# print(names[1:])
# print(names[1:5])
# print(names[:6])

# # filtered_names = tuple([name for name in names if isinstance(name, str)]) # TODO - check we get this tomorrow!
# # print(filtered_names)

# names = names[:6]
# print(names)

# print("Neil" in names)
# print("Kevin" in names)

# # user_name = input("What's your name? ")

# # if user_name in names:
# #   print("Welcome!")
# # else:
# #   print("Unauthorized")

# for name in names:   
#   print(f"{name} works at the BBC")

# target_name = "Rob"

# if target_name in names:
#   print(f"{target_name} is in position { names.index(target_name)}")
# else:
#   print(f"{target_name} not in the tuple.")

# print(names.count("Emma"))
# # double underscores ... dunders ... special methods

# # destructuring -> unpacking
# first_name, second_name, *other_names = names
# print(first_name)
# print(second_name)
# print(other_names)

import os
os.system('cls' if os.name == 'nt' else 'clear')

nested_numbers = (1, 2, (3, 4, (5, 6)))

print(nested_numbers[0])
print(nested_numbers[1])
print(nested_numbers[2][0])
print(nested_numbers[2][1])
print(nested_numbers[2][2][0])