import os
os.system('cls' if os.name == 'nt' else 'clear')

# empty_list = []
# print(type(empty_list))

# beatles = ["John", "Paul", "George", "Ringo"]

# print(len(beatles))
# print(beatles[1:3])

# print("George" in beatles)
# print("Antonio" in beatles)

# for beatle in beatles:
#   print(f"{beatle} was a member of the beatles.")

# beatles.append("Antonio")
# print(beatles)

# beatles.insert(1, "Kostiantyn") # try to avoid ... costly!
# print(beatles)

# beatles.extend(("Jack", "Adam", "Harriet", "John"))
# print(beatles)

# # beatles.remove("John")
# # beatles.remove("John")
# # beatles.remove("John")

# while "John" in beatles:
#   beatles.remove("John")

# print(beatles)

# print(beatles.count("Harriet"))
# print(beatles.index("Harriet"))

# while len(beatles) > 0:
#   beatle = beatles.pop()
#   print(beatle)
#   print(beatles)  # LIFO


# expenses = []
# user_input = input("Give me the value of your expense (q to quit): ")

# while user_input != "q":
#   expenses.append(float(user_input))
#   user_input = input("Give me the value of your expense (q to quit): ")

# print(expenses)

bands = [
    ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"],  # The Beatles
    ["Freddie Mercury", "Brian May", "Roger Taylor", "John Deacon"],      # Queen
    ["Kurt Cobain", "Krist Novoselic", "Dave Grohl"],                     # Nirvana
    ["Mick Jagger", "Keith Richards", "Charlie Watts", "Ronnie Wood"],   # The Rolling Stones
    ["Beyoncé", "Kelly Rowland", "Michelle Williams"],                   # Destiny's Child
    ["Thom Yorke", "Jonny Greenwood", "Colin Greenwood", "Ed O'Brien", "Phil Selway"],  # Radiohead
    ["Bono", "The Edge", "Adam Clayton", "Larry Mullen Jr."],            # U2
    ["Chris Martin", "Guy Berryman", "Jonny Buckland", "Will Champion"], # Coldplay
    ["Debbie Harry", "Chris Stein", "Clem Burke", "Jimmy Destri"],       # Blondie
    ["Jack White", "Meg White"]                                          # The White Stripes
]

print(bands[2][2])
print(bands[6][2])


nested_lists = ([1,2,3], [4,5,6])
print(nested_lists)

nested_lists[0].append(4)
print(nested_lists)

list_1 = [1,2,3,4]
list_2 = list_1.copy()

list_2.extend([3,4,5])
print(list_2)
print(list_1)