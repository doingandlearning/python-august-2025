

headlines = [
    "General election: Labour and Tories clash over tax",
    "England crowned T20 world champions",
    "Summer travel chaos feared as airline strikes loom",
    "UK inflation rate falls to lowest level in three years",
    "New David Hockney exhibition opens in London",
    "Science discovers new way to tackle plastic waste",
    "Government announces new funding for NHS",
    "Stock market hits record high on tech boom",
    "Debate rages over future of Artificial Intelligence",
    "Classic Doctor Who episodes to be released in colour"
]
import datetime
with open("log.txt", mode="a") as file:
  for headline in headlines:
    file.write(f"{datetime.date.today()} - {headline}\n")

"""
Mode:

r => read
w => write
a => append

"""