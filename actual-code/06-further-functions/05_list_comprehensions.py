data = [
    {"name": "Lily", "age": 21, "region": "SE"},
    {"name": "Tommy", "age": 41, "region": "NW"},
    {"name": "Radhika", "age": 26, "region": "NW"},
    {"name": "Ben", "age": 12, "region": "SE"},
    {"name": "Radu", "age": 24, "region": "Scotland"},
    {"name": "Lantana", "age": 43, "region": "NW"}
]

user_names = [user["name"]
              for user in data
              if user["region"] == "SE"
            ]  # list comprehension

print(user_names)

user_names = []
for user in data:
    user_names.append(user["name"])

print(user_names)