for character in "BBC is great":  # iterator -> list, dictionary, tuple, range(), string
  print(character)
  if character == "i":
    print("me")

for _ in range(10):
  print("Hello")


target = 10
for test_value in range(100):
  if test_value == target:
    print("Found it!")
    break  # exits the loop early!
  else:
    print("Still looking!")


for number in range(100):
  if number % 3 == 0:
    continue  # don't do any more work with this value, go get the next one!
  print(number)