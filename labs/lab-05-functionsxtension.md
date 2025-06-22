# **Lab 5 Extension: Advanced Function Techniques**
### **Objective**
This extension lab builds on **Lab 5: Functions** by exploring:
1. **Recursive functions** to work with the temperature dataset.
2. **Using decorators** to enhance function behavior.
3. **Memoization** to optimise repeated computations.

---

## **Step 1: Implementing Recursion**
Modify your `minimum()` and `maximum()` functions to use **recursion** instead of loops.

### **Tasks**
1. Write a **recursive `minimum_recursive(data, index=0)`** function that:
   - Returns the smallest value in `data`.
   - Uses recursion instead of `min()` or loops.
   - Uses `index` to process one item at a time.

2. Do the same for a **`maximum_recursive(data, index=0)`** function.

💡 **Hints**
- Base case: If there's **one element left**, return it.
- Recursive case: Compare the current element to the **minimum of the rest**.

---

## **Step 2: Using Decorators**
A **decorator** is a function that **wraps another function** to modify its behavior.

### **Tasks**
1. Write a **`timing_decorator`** that:
   - Measures the execution time of any function.
   - Prints how long the function took to run.

2. Apply it to:
   - `average()`
   - `median()`
   - Your new `minimum_recursive()` function

💡 **Hints**
- Use the `time` module (`time.perf_counter()`).
- A decorator takes a function **as an argument** and returns a new function.

---

## **Step 3: Function Memoization**
Memoization **caches function results** to improve performance.

### **Tasks**
1. Modify `celsius_to_fahrenheit()` to use **memoization** so:
   - If it’s called with the **same input multiple times**, it **doesn’t recompute**.
   - Instead, it **retrieves the result from a cache**.

2. Do the same for `fahrenheit_to_celsius()`.

💡 **Hints**
- Use a **dictionary** to store results `{input_value: result}`.
- Check if a value is **already cached** before computing.

---

## **Step 4: Challenge Task - Function Factory**
A **function factory** creates functions dynamically.

### **Tasks**
1. Write **`make_temperature_converter(scale)`**:
   - If `scale="F"`, return a function that converts **Celsius to Fahrenheit**.
   - If `scale="C"`, return a function that converts **Fahrenheit to Celsius**.

2. Test it like this:
```python
to_fahrenheit = make_temperature_converter("F")
to_celsius = make_temperature_converter("C")

print(to_fahrenheit(0))   # ➝ 32.0
print(to_celsius(100))    # ➝ 37.77
```

💡 **Hints**
- A function can **return another function**.
- Use **closures** to store `scale` inside the returned function.

---

# **Solutions (Spoilers)**
<details>
<summary>Click to reveal solutions</summary>

```python
import time

# Step 1: Recursion
def minimum_recursive(data, index=0):
    """Finds the minimum value using recursion."""
    if index == len(data) - 1:
        return data[index]
    return min(data[index], minimum_recursive(data, index + 1))

def maximum_recursive(data, index=0):
    """Finds the maximum value using recursion."""
    if index == len(data) - 1:
        return data[index]
    return max(data[index], maximum_recursive(data, index + 1))

# Step 2: Decorators
def timing_decorator(func):
    """Measures execution time of a function."""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

@timing_decorator
def average(data):
    return sum(data) / len(data)

@timing_decorator
def median(data):
    sorted_data = sorted(data)
    mid = len(data) // 2
    return sorted_data[mid] if len(data) % 2 else (sorted_data[mid - 1] + sorted_data[mid]) / 2

# Step 3: Memoization
def memoized_celsius_to_fahrenheit():
    cache = {}
    def convert(celsius):
        if celsius in cache:
            return cache[celsius]
        result = (celsius * 9 / 5) + 32
        cache[celsius] = result
        return result
    return convert

celsius_to_fahrenheit = memoized_celsius_to_fahrenheit()

# Step 4: Function Factory
def make_temperature_converter(scale):
    if scale == "F":
        return lambda c: (c * 9 / 5) + 32
    elif scale == "C":
        return lambda f: (f - 32) * 5 / 9
    else:
        raise ValueError("Invalid scale")

to_fahrenheit = make_temperature_converter("F")
to_celsius = make_temperature_converter("C")

print(to_fahrenheit(0))  # 32.0
print(to_celsius(100))   # 37.77
```
</details>
