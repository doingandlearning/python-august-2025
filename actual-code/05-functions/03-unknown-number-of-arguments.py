def add(a, b, c = 0, d = 0):
  return a + b + c + d 

print(add(1,2))
print(add(4,5))
print(add(1,2,3))
print(add(1,2,3,4))


def add(asker, *numbers):
  total = 0
  for number in numbers:
    total += number
  return f"Hey {asker} the total is {total}"

print(add("Antonio", 1,2))
print(add("Antonio", 4,5))
print(add("Antonio", 1,2,3))
print(add("Antonio", 1,2,3,4))
print(add("Antonio", ))
print(add("Antonio", 1,2,3,4,5,6,7,8,9,10))