empty_list = []

print(empty_list)
print(type(empty_list))

beatles = ["John", "Paul", "George", "Ringo"]

# Check for membership
print("John" in beatles)
print("Kevin" not in beatles)

# Length
print(len(beatles))

# Loop over lists
for band_member in beatles:
  print(band_member)

# Index 
print(beatles[0])
print(beatles[1:])
print(beatles[::-1])


beatles.append("Sophia") # adds a single element to the end of the list
print(beatles)

beatles.extend(["Jordi", "Yoko", "Tom", "John"]) # Adds multiple elements
print(beatles)

beatles.insert(1, "Tariq")  # use wisely!
print(beatles)

beatles.remove("John")  # removes the first instance 
print(beatles)

while "John" in beatles:
  beatles.remove("John")

print(beatles)

last_person = beatles.pop()  # Last In First Out
print(last_person)
print(beatles)

beatles.count("")
beatles.index("Ringo")

user_input = input("Give me a new band member(q to quit): ")

while user_input != "q":
  beatles.append(user_input)
  user_input = input("Give me a new band member (q to quit): ")

print(beatles)

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

print(bands[0])