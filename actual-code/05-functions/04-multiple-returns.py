def get_stats(list_of_numbers):
  total = 0
  min = float("inf")
  max = float("-inf")
  for number in list_of_numbers:
    total += number
    if number < min:
      min = number
    if number > max:
      max = number

  return total, max, min, total / len(list_of_numbers)

# unpacking
total, *other_stats = get_stats([4,6,2,6,4,8,10,3,-2])

# total = stats[0]
# max = stats[1]
# min = stats[2]
# avg = stats[3]

print(f"The total is {total}")
print(f"The other stats: {other_stats}")