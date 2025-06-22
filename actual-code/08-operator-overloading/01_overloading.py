class Quantity:
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return f"Quantity of amount {self.amount}"

    def add(self, other):
        new_amount = self.amount + other.amount
        return Quantity(new_amount)

    def __add__(self, other):
        if not isinstance(other, Quantity):
            raise TypeError("Can't non-Quantity to Quantity")
        new_amount = self.amount + other.amount
        return Quantity(new_amount)

    def __repr__(self):
        return f"Quantity({self.amount})"

    def __lt__(self, other):
        return self.amount < other.amount

    def __mul__(self, other):  # polymorphism
        if not isinstance(other, float | int):
            raise TypeError("Need to multiply by a number")
        new_value = other * self.amount
        return Quantity(new_value)

    def __eq__(self, other):
        return self.amount == other.amount


q1 = Quantity(30)
q2 = Quantity(5)


print(q1)
print(q2)

q3 = q1.add(q2)
q3 = q1 + q2
# q4 = q1 + 7

print(q3)

print("-" * 20)

quantity_list = [q1, q2, q3]

print(quantity_list)
quantity_list.sort()
print(quantity_list)

print(q1 * 3)

print(q1 < q2)
print(q1 > q2)
print(Quantity(30) == Quantity(30))

