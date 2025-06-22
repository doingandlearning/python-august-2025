data = [1, 3, 5, 2, 7, 4, 1.5, 6, 10]

# I want all the even numbers
def is_even(number):
    return number % 2 == 0

print(is_even(10))
print(is_even(11))
print(is_even(1.1))

results = []

for number in data:
    if is_even(number):
        results.append(number)

print(results)
print(list(filter(is_even, data)))

# for number in filter(is_even,data):
#     print(number)

print(list(filter(lambda number: number > 5, data)))

data = [
    {"name": "Lily", "age": 21, "region": "SE"},
    {"name": "Tommy", "age": 41, "region": "NW"},
    {"name": "Radhika", "age": 26, "region": "NW"},
    {"name": "Ben", "age": 12, "region": "SE"},
    {"name": "Radu", "age": 24, "region": "Scotland"},
    {"name": "Lantana", "age": 43, "region": "NW"}

]

users_in_scotland = list(filter(lambda user: user['region'] == "Scotland", data))

print(users_in_scotland)
"""
True and False

"" => False
[] => False
None => False
() => False
False => False



"""

users_in_se = list(filter(lambda user: user['region'] == 'SE', data))
print(users_in_se)

users_under_40 = list(filter(lambda user: user['age'] < 40, data))
print(users_under_40)