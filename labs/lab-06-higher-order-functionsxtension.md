**Lab 6 Extension: Advanced Higher-Order Functions**

*Objective:* Enhance your understanding of higher-order functions by implementing complex operations on temperature data.

*Prerequisite:* Completion of Lab 6: Higher-Order Functions.

**Step 1: Implement a Custom Reduce Function**

Python's `reduce` function, available in the `functools` module, applies a binary function cumulatively to the items of an iterable. For this exercise, you'll implement your own version of `reduce`.

**Tasks:**

1. Define a function `custom_reduce(function, iterable, initializer=None)` that:
   - Takes a binary `function` and an `iterable`.
   - Optionally accepts an `initializer` value.
   - Applies the `function` cumulatively to the items of the `iterable`, from left to right, to reduce it to a single value.

2. Use `custom_reduce` to calculate:
   - The **sum** of all temperature readings.
   - The **product** of all temperature readings.

*Hints:*
- If `initializer` is not provided, use the first item of the iterable as the initial value.
- Ensure your function handles empty iterables appropriately.

**Step 2: Compose Functions**

Function composition involves combining two or more functions to produce a new function. This allows for modular and readable code.

**Tasks:**

1. Create a function `compose(f, g)` that:
   - Returns a new function `h(x)` which computes `f(g(x))`.

2. Use `compose` to:
   - First, **double** each temperature reading.
   - Then, **convert** the doubled value from Celsius to Fahrenheit.

*Hints:*
- Define a function `double(x)` that returns `2 * x`.
- Use the previously defined `celsius_to_fahrenheit` function.

**Step 3: Implement a Pipeline of Functions**

A pipeline allows you to pass data through a sequence of functions, where the output of one function becomes the input to the next.

**Tasks:**

1. Define a function `pipeline(functions)` that:
   - Takes a list of functions `functions`.
   - Returns a new function that applies each function in `functions` in sequence to its input.

2. Use `pipeline` to process the temperature readings by:
   - **Filtering** out temperatures below 10°C.
   - **Converting** the remaining temperatures to Fahrenheit.
   - **Rounding** each Fahrenheit temperature to the nearest integer.

*Hints:*
- Each function in the pipeline should take a single argument and return a single value.
- Consider using `filter`, `map`, and `round` in your pipeline.

**Step 4: Implement Function Currying**

Currying is the process of transforming a function that takes multiple arguments into a sequence of functions, each taking a single argument.

**Tasks:**

1. Define a function `curried_add(a)` that:
   - Returns a new function that takes an argument `b` and returns the sum of `a` and `b`.

2. Use `curried_add` to create a function `add_five` that adds 5 to its input.

3. Apply `add_five` to each temperature reading using `map`.

*Hints:*
- The returned function should capture the value of `a` from its enclosing scope.
- This exercise demonstrates the concept of closures in Python.

**Solutions**

*Note: Attempt the exercises before reviewing the solutions.*

<details>
<summary>Click to reveal solutions</summary>

```python
# Lab 6 Extension: Advanced Higher-Order Functions Solution

# Step 1: Implement a Custom Reduce Function
def custom_reduce(function, iterable, initializer=None):
    """
    Custom implementation of the reduce function.
    
    Args:
        function: A binary function to apply cumulatively
        iterable: An iterable to reduce
        initializer: Optional initial value
        
    Returns:
        The reduced value
    """
    it = iter(iterable)
    
    if initializer is None:
        try:
            # Use first item of iterable as initializer if none provided
            initializer = next(it)
        except StopIteration:
            raise TypeError("custom_reduce() of empty sequence with no initial value")
    
    result = initializer
    for item in it:
        result = function(result, item)
    
    return result

# Sample temperature data (in Celsius)
temperatures = [15.2, 19.8, 22.3, 8.7, 12.5, 24.1, 7.9, 18.6]

# Using custom_reduce to calculate sum
sum_temperatures = custom_reduce(lambda x, y: x + y, temperatures)
print(f"Sum of temperatures: {sum_temperatures}")

# Using custom_reduce to calculate product
product_temperatures = custom_reduce(lambda x, y: x * y, temperatures)
print(f"Product of temperatures: {product_temperatures}")

# Step 2: Compose Functions
def compose(f, g):
    """
    Function composition: f(g(x))
    
    Args:
        f: Outer function
        g: Inner function
        
    Returns:
        A new function that computes f(g(x))
    """
    return lambda x: f(g(x))

# Helper functions
def double(x):
    """Doubles the input value"""
    return 2 * x

def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit"""
    return (celsius * 9/5) + 32

# Compose the functions
double_then_convert = compose(celsius_to_fahrenheit, double)

# Apply the composed function to each temperature
converted_temperatures = list(map(double_then_convert, temperatures))
print(f"Doubled and converted temperatures: {converted_temperatures}")

# Step 3: Implement a Pipeline of Functions
def pipeline(functions):
    """
    Creates a pipeline of functions.
    
    Args:
        functions: A list of functions to apply in sequence
        
    Returns:
        A new function that applies each function in sequence
    """
    def apply_pipeline(x):
        result = x
        for func in functions:
            result = func(result)
        return result
    
    return apply_pipeline

# Functions for the pipeline
def filter_low_temperatures(temps):
    """Filter out temperatures below 10°C"""
    return list(filter(lambda temp: temp >= 10, temps))

def convert_to_fahrenheit(temps):
    """Convert a list of Celsius temperatures to Fahrenheit"""
    return list(map(celsius_to_fahrenheit, temps))

def round_temperatures(temps):
    """Round each temperature to the nearest integer"""
    return list(map(round, temps))

# Create and apply the pipeline
temperature_pipeline = pipeline([
    filter_low_temperatures,
    convert_to_fahrenheit,
    round_temperatures
])

processed_temperatures = temperature_pipeline(temperatures)
print(f"Processed temperatures: {processed_temperatures}")

# Step 4: Implement Function Currying
def curried_add(a):
    """
    Returns a function that adds a to its argument.
    
    Args:
        a: The first value to add
        
    Returns:
        A function that takes an argument b and returns a + b
    """
    def add_to_a(b):
        return a + b
    return add_to_a

# Create a function that adds 5 to its input
add_five = curried_add(5)

# Apply add_five to each temperature
adjusted_temperatures = list(map(add_five, temperatures))
print(f"Temperatures with 5 added: {adjusted_temperatures}")

# Demonstration of all concepts
print("\nDemonstration of all concepts together:")

# 1. Filter temperatures above 10°C
# 2. Double each temperature
# 3. Convert to Fahrenheit
# 4. Add 5 to each temperature
# 5. Round to nearest integer
# 6. Calculate the sum and average

# Create specialized functions for the demonstration
def advanced_pipeline(temps):
    filtered_temps = filter_low_temperatures(temps)
    doubled_temps = list(map(double, filtered_temps))
    fahrenheit_temps = convert_to_fahrenheit(doubled_temps)
    adjusted_temps = list(map(add_five, fahrenheit_temps))
    rounded_temps = round_temperatures(adjusted_temps)
    
    sum_temps = custom_reduce(lambda x, y: x + y, rounded_temps)
    avg_temp = sum_temps / len(rounded_temps) if rounded_temps else 0
    
    return {
        'filtered': filtered_temps,
        'doubled': doubled_temps,
        'fahrenheit': fahrenheit_temps,
        'adjusted': adjusted_temps,
        'rounded': rounded_temps,
        'sum': sum_temps,
        'average': avg_temp
    }

result = advanced_pipeline(temperatures)
print("Processing steps:")
print(f"1. Filtered temperatures (≥10°C): {result['filtered']}")
print(f"2. Doubled temperatures: {result['doubled']}")
print(f"3. Converted to Fahrenheit: {result['fahrenheit']}")
print(f"4. Added 5 to each temperature: {result['adjusted']}")
print(f"5. Rounded temperatures: {result['rounded']}")
print(f"6. Sum of processed temperatures: {result['sum']}")
print(f"7. Average of processed temperatures: {result['average']:.2f}")
```
</details>