data = [
    {"name": "Lily", "age": 21, "region": "SE"},
    {"name": "Tommy", "age": 41, "region": "NW"},
    {"name": "Radhika", "age": 26, "region": "NW"},
    {"name": "Ben", "age": 12, "region": "SE"},
    {"name": "Radu", "age": 24, "region": "Scotland"},
    {"name": "Lantana", "age": 43, "region": "NW"}
]

mapped_data = map(lambda u: f"Hello {u["name"]}, how are things in {u["region"]}? Do you like being {u["age"]}?",
               data
               )

print(mapped_data)
# generator!
for value in mapped_data:
    print(value)

# print(*list(map(lambda u: {"name": u["name"], "age": u["age"], "logged_in": True}, data)), sep="\n")
# print(data)