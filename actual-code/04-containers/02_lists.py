import random
empty_list = []

print(empty_list)
print(type(empty_list))

beatles = ["George", "Paul", "John", "Ringo", "John", "John"]  # creates the list -> and assigns the point in memory to the vairable

beatles.append("Radu")  # add a single element to our list
print(beatles)

beatles.extend(("Lily", "Armeen", "Lantana"))  # add multiple elements
print(beatles)

beatles.insert(2, "Tommy")  # is more "expensive" in terms of memory!
print(beatles)

print(beatles.pop())  # LIFO - stack
print(beatles)

print(beatles.count("Kevin"))

beatles_cover_band = beatles.copy()  # assignment by reference not by value
beatles_cover_band.append("Annika")

print(beatles_cover_band)
print(beatles)

beatles.remove("John")  # the first instance!
print(beatles)

while "John" in beatles:
    beatles.remove("John")

print(beatles)

for member in beatles:
    print(f"{member} is a band member of the beatles and plays {random.choice(['drums', 'guitar', 'bass', 'vocals', 'triangle', 'tamborine'])}")

