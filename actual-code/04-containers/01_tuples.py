empty_tuple = ()

print(empty_tuple)
print(type(empty_tuple))

print(empty_tuple.count(0))

if 0 in empty_tuple:
    print(empty_tuple.index(0))  # -1
else:
    print("0 not in tuple.")

odd_tuple = (1, 3, 5, 7, 9)

print(odd_tuple[0])  # single number - give me the value at that position!
print(odd_tuple[2:4])  # start:end - start inclusive, end exclusive
print(odd_tuple[:4])   # :end  - from position 0, end exclusive
print(odd_tuple[2:])  # 2:  - start at position 2 up to the end of the tuple
print(odd_tuple[1:4:2])  # [start:end:step]
print("This is a string"[:10:2])

for number in odd_tuple:
    print(number)

print((True, 1, 2, (1,2), (2, (3,))))