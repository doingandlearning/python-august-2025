"""
This is a module of utility functions
"""

def printer(message):
    print("I'm about to print a message")
    print(message)
    print("How did I do?")


class Shape:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f"Shape of type {self.type}"


default_shape = Shape("rhombus")

def main():
    print("Hello - I am in the utils module!")
    print("This is from utils.py")
    print(__name__)
    print(__doc__)
    print(__file__)
    print("-" * 25)

if __name__ == "__main__":
    main()