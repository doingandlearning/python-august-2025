import os
os.system('cls' if os.name == 'nt' else 'clear')

empty_dict = {}
print(empty_dict)
print(type(empty_dict))

user_dict = {
  "name": "Emma",  # key : value
  "team": "CCOG",
  "role_details": ["social media", "matlab", "data analyst"],
  "address": {
    "first_line": "2 High Streeet",
    "second_line": "",
    "postcode": ""
  },
  (0,1): "",
}

print(user_dict["name"])
print(user_dict["address"]["first_line"])

print("name" in user_dict)
print("Emma" in user_dict)  # in checks the keys and not the values!

print(list(user_dict.keys())) # a list of the keys
print(user_dict.values())     # a list of hte values
print(user_dict.items())      # a list of tuples 

for key, value in user_dict.items():
  print(f"The key {key} has a value {value}")

# print(user_dict["birthday"])
print(user_dict.get("birthday", "We don't know that birthday."))

bands = {
  "Queen":  ["Freddie Mercury", "Brian May", "Roger Taylor", "John Deacon"],      # Queen
  "Nirvana":  ["Kurt Cobain", "Krist Novoselic", "Dave Grohl"],                     # Nirvana
   "The Rolling Stones": ["Mick Jagger", "Keith Richards", "Charlie Watts", "Ronnie Wood"],   # The Rolling Stones
    # ["Beyoncé", "Kelly Rowland", "Michelle Williams"],                   # Destiny's Child
    # ["John Lennon", "Paul McCartney", "George Harrison", "Ringo Starr"],  # The Beatles
    # ["Thom Yorke", "Jonny Greenwood", "Colin Greenwood", "Ed O'Brien", "Phil Selway"],  # Radiohead
    # ["Bono", "The Edge", "Adam Clayton", "Larry Mullen Jr."],            # U2
    # ["Chris Martin", "Guy Berryman", "Jonny Buckland", "Will Champion"], # Coldplay
    # ["Debbie Harry", "Chris Stein", "Clem Burke", "Jimmy Destri"],       # Blondie
    # ["Jack White", "Meg White"]                                          # The White Stripes
}

bands["Queen"][0]
print(bands.pop("Queen"))
print(bands)

bands.setdefault("The Rolling Stones", [])
bands.setdefault("Snow Patrol", [])
print(bands)
