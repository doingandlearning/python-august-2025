count = 10


def increment_count():
    global count
    count += 1
    print(count)

def use_count():  # functions can read values that are in "scope" - even global values!
    # print(count)
    # count = 8  # we can 'shadow' variables!
    global count   # i want write access to the outer variable!
    count = 8
    print(count)

increment_count()
print(count)

use_count()
print(count)


def increment_value(value):  # pure function
    return value + 1


count = increment_value(count)
print(count)


count = increment_value(count)
print(count)


count = increment_value(count)
print(count)