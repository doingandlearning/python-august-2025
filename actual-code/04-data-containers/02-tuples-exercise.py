# https://gist.github.com/doingandlearning/dd134549e8418db346dba35238e5e5b0
names = ("Joel", "Catherine", "Halit", "Rob", True, 1, 2.3, "Rob", "Rob")


# Count how many of the values are not strings.
count = 0 
for name in names:
  if isinstance(name, str):
    print(name.upper())
  else:
    count += 1

# 2
print(f"There were {count} values that were not strings.")

# 3
print(f"The first index of Rob is {names.index("Rob")}.")
print(len(names) - 1 - names[::-1].index("Rob"))

# 4
for name in names:
  print(f"{name} {type(name)}")

# 5
first_three_names = names[0:3]
print(first_three_names)