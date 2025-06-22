# Encapsulation - group together data and things done with that data
class Person:
    """
    This is a class of a Person
    """
    def __init__(self, name, age):   # double underscore -> dunder methods
        self.name = name
        self.age = age

    def __str__(self):  # more human-readable
        return f"Person called {self.name}, aged {self.age}."

    def __repr__(self):  # more machine-readable
        return f"Person({self.name}, {self.age})"

    def birthday(self):
        print(f"Happy birthday {self.name}! You were {self.age}")
        self.age += 1
        print(f"You are now {self.age}")

    def calculate_pay(self, hours_worked):
        rate_of_pay = 10
        if self.age >= 21:
            rate_of_pay += 2.5
        return hours_worked * rate_of_pay

    def is_teenager(self):
        return self.age > 12 and self.age < 20



person1 = Person(name="Ethan", age=12)
person2 = Person("Kevin", 41)
print(person1.name)
print(person1.age)
print(person1)
print(person2)
print([person1, person2])

son = Person(person1.name, person1.age)
print(id(son))
print(id(person1))

print(person1.is_teenager())
person1.birthday()  # You were 12. Happy birthday! Now you are 13.
print(person1.is_teenager())
person2.birthday()


print(person2.calculate_pay(10))

# Here's what you could have had:
person1 = {"name": "Ethan", "age": 12}  # has no opinion about right/wrong keys
print(person1["name"])
print(person1["age"])

def birthday(user):
    print(f"Happy birthday {user["name"]}, you were {user["age"]}")
    user["age"] += 1
    print(f"Now you are {user["age"]}")



birthday(person1)
