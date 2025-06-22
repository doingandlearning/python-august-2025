import csv

with open("data.csv") as file:
    reader = csv.reader(file)
    next(reader)  # to skip the header row if it exists!
    for row in reader:
        print(f"{row[0]} lives in {row[1]} and is {row[2]} years old.")

with open("data.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # print(row)
        print(f"{row["name"]} lives in {row["location"]} and is {row["age"]} years old.")

with open("movies.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["title", "release_year", "rating"])
    writer.writerow(["Wicked", 2024, 4])
    writer.writerow(["Matrix", 1998, 4])
    writer.writerow(["Forest Gump", 1990, 3])


with open("movies_dict.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "release_year", "rating"])
    writer.writeheader()
    writer.writerow({"rating":4, "name": "Wicked", "release_year":2024})
    writer.writerow({"name": "Forest Gump", "release_year":1990, "rating":3})
    writer.writerow({"name": "Matrix", "release_year": 1998, "rating": 4})
