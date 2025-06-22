counter = 0

while counter < 10:
    print(f"Okay ... I'll keep going! The counter is {counter}")
    # counter = counter + 1
    counter += 1

print("All done!")

# while True:
#     name = input("What is your name? ")
#
#     if name == "Kevin":
#         print("We don't like your type around here!")
#         # break  # exits the loop once and for all!
#         continue  # goes to back to the test without finishing the loop
#
#     print(name)

print("Thank goodness we're done with that!")

counter = 0
target = 100

while counter < 10:
    if counter == target:
        print("Found it!")
        break
    counter += 1
    print("Still looking!")

while True:
    print("Python rocks 🐍")
    continue
    print("I will never print!")