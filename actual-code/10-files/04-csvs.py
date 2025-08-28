import csv

# with open("movies.csv", mode="r") as file:
#   reader = csv.reader(file)
#   header = next(reader)
#   years = set()
#   for title, release, director, genre in reader:
#     print(f"{title}({release}) is a {genre.lower()} movie directed by {", ".join(director.split("; "))}.") 
#     years.add(release)
#   print(f"These movies are from {min(years)} to the {max(years)}.")

with open("movies.csv", mode="a") as file:
  writer = csv.writer(file)
  writer.writerow(["Forest Gump", 1994, "Robert Zemeckis", "Drama"])

"""
rb
wb
ab
"""