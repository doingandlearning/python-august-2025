empty_dict = {}

print(empty_dict)
print(type(empty_dict))

user_dict = {
  "name": "Tariq",
  "location": "London",
  "department": ["Short form", "Finance"],
  "base_office": "London",
  "name": "Tariq Atia"
}

print(user_dict)

# Indexing is by key
print(user_dict["name"])

# Checking membership (of keys not values)
print("name" in user_dict)
print("London" in user_dict)

print(user_dict.keys())  # list of the keys
print(user_dict.values()) # list of the values
print(user_dict.items())  # a list of (key, value) tuples

if "favourite_tv_show" in user_dict:
  print(user_dict["favourite_tv_show"])
else:
  print("Don't know what his favourite tv is.")

print(user_dict.get("favourite_tv_show", "Don't know what his favourite tv show is."))

user_dict["favourite_tv_show"] = "The Office"

print(user_dict.get("favourite_tv_show", "Don't know what his favourite tv show is."))

print(user_dict)

user_dict.update({"location": "Glasgow", "name": "Tariq", "weather": "Rainy"}) 
print(user_dict)