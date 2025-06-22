def square(num):
    # multiple lines!
    return num ** 2

data = [1,2,3,4,5,6]
print([square(num)
       for num in data
       if num > 2
    ])

print(square(3))


square = lambda num: num ** 2  # a single operation! implicit return!
print(square(3))

