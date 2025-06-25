import csv

with open("data.csv") as file:
  reader = csv.reader(file)
  header_row = next(reader)
  # for row in reader:
  #   print(f"{header_row[0]}: {row[0]}, {header_row[1]}: {row[1]}, {header_row[2]}: {row[2]}")
  # for title, release_date, genre in reader:
  #   print(f"{header_row[0]}: {title}, {header_row[1]}: {release_date}, {header_row[2]}: {genre}")
  for row in reader:
    title, release_date, genre = row
    print(f"{header_row[0]}: {title}, {header_row[1]}: {release_date}, {header_row[2]}: {genre}")

with open("data.csv", "a") as file:
  writer = csv.writer(file)
  title = input("What is the film title? ")
  release = input("What is the release year? ")
  genre = input("What genre (separate with commas)? ")
  writer.writerow([title, release, genre])