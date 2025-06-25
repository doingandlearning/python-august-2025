import headline_module
from headline_module import Headline
import csv

headlines = []

def main():
  with open("headlines.csv") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
      headline = Headline(title=row[0], source=row[1])
      headlines.append(headline)

  print("----- Analysis of Headlines -----")
  for headline in headlines:                                      # get_word_count(headline.title)
    print(f"From {headline.source}: {headline.title} (word count: {headline.word_count()})")

if __name__ == "__main__":
  main()