empty_tuple = ()

print(empty_tuple)
print(type(empty_tuple))

names = ("Joel", "Catherine", "Halit", "Rob", True, 1, 2.3, "Rob", "Rob")
print(type(names))
print(len(names))
print(names[0])
print(names[6])
print(names[1:])
print(names[0:4])  # sub-listing/sub-indexing 
print(names[:4])

print("Liz" in names)
print("Joel" in names)
print("Kevin" not in names)

# ("Joel", "Catherine", "Halit", "Rob", True, 1, 2.3)

for username in names[:3]:
  print(username)
  # ...
  # ... 
  # ...

print(username)

print("Count of Robs: " + str(names.count("Rob")))
print(f"Count of Robs: {names.count("Rob")}")
name_to_check = "Rob"

if name_to_check in names:  # defensive programming - guard clause
  print(f"Rob at index {names.index(name_to_check)}")
else:
  print("Name not found")

for index in range(len(names)):
  if names[index] == "Rob":
    print(f"Rob at index {index}")


print(names)
print(type(names))