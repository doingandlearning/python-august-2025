# **Lab 4: Containers (Extended)**
## **Objective**
This extension lab builds on the original **Lab 4: Containers**, adding work with **tuples and dictionaries**. You will:
1. **Explore lists further** with additional operations.
2. **Work with tuples**, understanding immutability.
3. **Use dictionaries** to structure temperature data.

This lab contains **four steps**:
1. **Advanced List Operations**
2. **Tuples: Immutable Data Containers**
3. **Dictionaries: Storing Data with Meaningful Keys**
4. **Challenge Task: Organising Readings by Location**

### **Hints**
- This lab provides **hints instead of code completions**.
- Try using `dir(list)`, `dir(tuple)`, and `dir(dict)` to discover useful methods.
- Solutions are provided at the bottom.

---

## **Step 1: Advanced List Operations**
In the original lab, you used sorting, reversing, copying, and counting elements. Let’s go further.

### **Tasks**
1. Insert a new value **at a specific position** in the list.
2. Remove a value **by its index** (rather than by content).
3. Find the **minimum and maximum** values in the list without sorting it.
4. Sum all the values in the list in **two different ways**.

💡 **Hints**
- Look at the `.insert()` and `.pop()` methods.
- Python has built-in `min()` and `max()` functions.
- Try using `sum()` vs iterating over the list with a loop.

---

## **Step 2: Tuples - Immutable Data Containers**
Tuples are like lists but **immutable**—once created, they cannot be modified.

### **Tasks**
1. Convert the `readings` list into a tuple.
2. Attempt to modify an element in the tuple—what happens?
3. Try **indexing and slicing** the tuple to access specific values.
4. Use tuple **unpacking** to extract the **first and last** values.

💡 **Hints**
- Convert a list to a tuple with `tuple()`.
- Try `my_tuple[0] = 99` and observe the error.
- Use slicing `my_tuple[:3]` to extract part of the tuple.
- Tuple unpacking looks like: `first, last = my_tuple[0], my_tuple[-1]`.

---

## **Step 3: Dictionaries - Storing Data with Meaningful Keys**
Instead of storing raw temperature readings in a list, let’s structure them using **dictionaries**.

### **Tasks**
1. Create a dictionary where **keys are timestamps** and **values are temperature readings**.
2. Add a **new reading** with a timestamp.
3. Retrieve a reading **for a specific timestamp**.
4. Print all **keys** and **values** separately.
5. Remove an entry from the dictionary.

💡 **Hints**
- Dictionaries are created using `{}` or `dict()`.
- You can access values with `dict[key]` and use `.get(key, default)`.
- Try `.keys()` and `.values()` for listing keys and values.
- Use `.pop(key)` to remove an item.

---

## **Step 4: Challenge Task - Organising Readings by Location**
Real-world temperature readings often come from multiple locations. Instead of a flat list, let’s organise them by city.

### **Tasks**
1. Create a **nested dictionary** where:
   - The **keys** are city names.
   - The **values** are **lists of temperature readings**.
2. Add a new reading for a city.
3. Compute the **average temperature** for a given city.
4. Sort the readings **inside each city’s list**.

💡 **Hints**
- A nested dictionary looks like `{ "London": [12.3, 15.1, 14.8], "New York": [8.4, 10.2] }`.
- Use `dict.setdefault(city, [])` to ensure a list exists before appending.
- Use `sum()` and `len()` to compute averages.
- Use `.sort()` to order the list.

---

# **Solutions (Spoilers)**
<details>
<summary>Click to reveal solutions</summary>

```python
# Step 1: Advanced List Operations
readings.insert(2, 7.8)  # Insert at index 2
readings.pop(3)  # Remove element at index 3
print(f"Min: {min(readings)}, Max: {max(readings)}")
print(f"Sum using sum(): {sum(readings)}")
total = 0
for r in readings:
    total += r
print(f"Sum using loop: {total}")

# Step 2: Tuples
readings_tuple = tuple(readings)
# readings_tuple[0] = 99  # This will raise an error
print(f"First three readings: {readings_tuple[:3]}")
first, last = readings_tuple[0], readings_tuple[-1]
print(f"First: {first}, Last: {last}")

# Step 3: Dictionaries
temperature_log = {
    "2025-03-17T10:00:00": 12.3,
    "2025-03-17T12:00:00": 15.4,
    "2025-03-17T14:00:00": 14.8
}
temperature_log["2025-03-17T16:00:00"] = 16.2  # Add a new reading
print(f"Reading at 12:00: {temperature_log.get('2025-03-17T12:00:00')}")
print(f"All timestamps: {list(temperature_log.keys())}")
print(f"All readings: {list(temperature_log.values())}")
temperature_log.pop("2025-03-17T10:00:00")  # Remove a reading

# Step 4: Organising Readings by Location
city_readings = {
    "London": [12.3, 15.1, 14.8],
    "New York": [8.4, 10.2]
}
city_readings.setdefault("London", []).append(16.5)  # Ensure key exists before appending
avg_temp = sum(city_readings["London"]) / len(city_readings["London"])
print(f"Average temp in London: {avg_temp:.2f}")
city_readings["London"].sort()
print(f"Sorted readings for London: {city_readings['London']}")
```
</details>

---
