# lists, dictionaries, sets, tuples

for number in range(0,10):
    if number % 2 == 0:
        print("This number is even! Skipping this ... ")
        continue
    if number == 5:
        print("Finishing because we were too excited by 5")
        break
    print(number * number)
