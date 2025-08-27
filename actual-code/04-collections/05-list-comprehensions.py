numbers = [1,2,3,4,5,6,7,8,9,10]

doubles = []

for number in numbers:
  if number > 5:
    doubles.append(number * 2)

print(doubles)

doubles = [value * 2 for value in numbers if value > 5]
print(doubles)

emails = ["alice@gmail.com", "bob@", "carol@hotmail.com", "dan#mail.com"]
valid_emails = [e for e in emails if "@" in e and "." in e]
# ['alice@gmail.com', 'carol@hotmail.com']

files = [f"report_{year}.csv" for year in range(2020, 2025)]
# ['report_2020.csv', 'report_2021.csv', ...]

names = ["Alice", "Bob", "Charlie"]
masked = [n[0] + "*"*(len(n)-1) for n in names]
# ['A****', 'B**', 'C******']

