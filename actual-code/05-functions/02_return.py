import time

def square(number):  # Global Interpreter Lock
    print("Thinking about it ...")
    # time.sleep(1)
    return number * number
    return number ** 2


print(square(10))
answer = square(9)
print(answer)
print(f"5 squared is {square(5)}")

if square(-1) > 0:
    print("That's funny!")


def summarize_a_list(list_of_numbers):
    """

    :param list_of_numbers:
    :return: A tuple of (max, min, average)
    """
    max_of_list = max(list_of_numbers)
    min_of_list = min(list_of_numbers)
    average = sum(list_of_numbers) / len(list_of_numbers)
    return max_of_list, min_of_list, average

print(summarize_a_list([1, 1, 2, 3, 5, 8, 13, 21, 34, 55]))

max, min, average = summarize_a_list([1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

print(f"{max} is the max of my list")
print(f"{min} is the min of my list")
print(f"{average} is the average of my list")

# (stats) = summarize_a_list([1, 1, 2, 3, 5, 8, 13, 21, 34, 55])