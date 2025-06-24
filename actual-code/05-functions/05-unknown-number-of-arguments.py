def add(a, b, c=0, d=0):
  return a + b + c + d


print(add(4,5))

print(add(4,5,6))

print(add(4,5,6,7))

def add(*numbers):
  total = 0
  for number in numbers:
    total += number
  return total

print(add(1,2,3))
print(add(1))
print(add(1,2,3,4,5,6,3,5,6,23,5,3,5,6,3,2))
print(add(2))


def input():
  print("i don't want to do input")

input()  # 