def add(a, b):
    return a + b


def add(a,b,c=0, d=0):
    return a + b + c + d

def add(*numbers, name="User"):  # *args
    # if isinstance(name, int | float):
    #     numbers = (name,) + numbers
    #     name = "User"
    total = 0
    for number in numbers:
        total += number
    return f"{name} did some adding and the answer is {total}"

print(add(1))
print(add(1,2, name="Michele"))
print(add(1,2, 3))
print(add(1,2,3,4))


print(1,3,4,5,6,7,8, end="\n", sep="-")