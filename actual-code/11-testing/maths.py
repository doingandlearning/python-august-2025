def add(a, b):
    if not isinstance(a, int | float):
        raise TypeError("Should only pass numbers.")
    if not isinstance(b, int | float):
        raise TypeError("Should only pass numbers")
    if not all((isinstance(a, int|float), isinstance(b, int | float))):
        raise TypeError("Should only pass numbers")
    if not all([isinstance(x, int | float) for x in (a,b)]):
        raise TypeError("Should only pass numbers")
    return a + b

