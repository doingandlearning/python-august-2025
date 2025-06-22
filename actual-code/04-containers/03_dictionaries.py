cities = {
    "Scotland": "Glasgow",
    "England": ["London", "Salford", "Oxford"],
    "Wales": "Cardiff",
    "Northern Ireland": "Belfast",
    # 2: "valid",
    # (1,2,3): "valid",
    # True: "valid"
}
# key -> anything that is immutable
# value -> anything!
print(cities)
print(cities["England"])
print(list(cities.values()))  # a
print(list(cities.keys()))
print(list(cities.items()))

# unpacking - destructuring
country, city, *others = ("Ireland", "Dublin", "Other", "Cities")
print(others)

print(f"{city} is the captial of {country}")

for country, city in cities.items():
    print(f"{city} {"is" if isinstance(city, str) else "are"} in {country}")


print("England" in cities)  # checking against the keys!
print("Glasgow" in cities.values())

print(cities.get("Italy", "Unknown"))
print(cities.get("Wales", "Unknown"))
print(cities)
print(cities.setdefault("Wales", "Brilliant City"))
print(cities)
print(cities.setdefault("Italy", "Brilliant City"))
print(cities)


cache = {}

print(cache.setdefault("John", {}))

cache["John"]["colour"] = "blue"
print(cache)
# cache.update("John", {"location": "Amsterdam"})
# print(cache)  - TODO - come back when we look at lambda functions!
