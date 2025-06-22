### **Lab 8 Extension: Advanced Operator Overloading**  
This extension builds on **Lab 8: Operators**, adding:  
✅ **In-place operators (`+=`, `-=`)**  
✅ **Unit consistency checks** (Celsius vs Fahrenheit)  
✅ **Implementing a temperature range class**  
✅ **Allowing arithmetic with other data types (e.g., lists, tuples)**  

---

## **Step 6: Implement In-Place Operators (`+=`, `-=`)**  
Modify `TemperatureReading` to support **in-place arithmetic operations** (`+=` and `-=`).  

### **Tasks**  
1. Define `__iadd__()` to allow modifying a temperature in-place.  
2. Define `__isub__()` to subtract values in-place.  
3. Ensure that in-place operations only update the **temperature value**, not the date/location.  

💡 **Hints:**  
- Modify `self.temp` directly inside `__iadd__()` and `__isub__()`.  
- Return `self` instead of creating a new object.  

### **Example Usage**  
```python
temp = TemperatureReading(10, "10/03/25", "London", "Celsius")
temp += 5
print(temp)  # TemperatureReading[Celsius](15 on 10/03/25 at London)

temp -= 3
print(temp)  # TemperatureReading[Celsius](12 on 10/03/25 at London)
```

---

## **Step 7: Enforce Unit Consistency (Celsius vs Fahrenheit)**  
Modify **arithmetic operators (`+`, `-`)** to ensure:  
✅ Temperatures **must be in the same scale** before addition/subtraction.  
✅ If different scales exist, **convert one before performing the operation**.  

### **Tasks**  
1. If two temperatures have different scales, **convert** one before applying the operation.  
2. Raise a `ValueError` if an unsupported operation is attempted.  

💡 **Hints:**  
- Use a helper method `convert_to(scale)` that returns a **converted copy** of the object.  
- Ensure `self.scale == other.scale` before performing arithmetic.  

### **Example Usage**  
```python
temp1 = TemperatureReading(10, "10/03/25", "London", "Celsius")
temp2 = TemperatureReading(50, "10/03/25", "London", "Fahrenheit")

temp3 = temp1 + temp2  # temp2 should be converted to Celsius before addition
print(temp3)  # Should print a result in Celsius
```

---

## **Step 8: Implement a Temperature Range Class**  
Introduce a **new class `TemperatureRange`** that:  
✅ Stores **a minimum and maximum** temperature.  
✅ Uses `__contains__()` so `temp in range_obj` works.  
✅ Allows **addition/subtraction** of ranges.  

### **Tasks**  
1. Create a class `TemperatureRange(min_temp, max_temp, scale="Celsius")`.  
2. Implement `__contains__()` so that `x in range_obj` checks if a value is within range.  
3. Implement `__add__()` and `__sub__()` so ranges can be expanded/reduced.  

💡 **Hints:**  
- `min_temp <= value <= max_temp` for checking containment.  
- Addition/subtraction should **increase/decrease the range values**.  

### **Example Usage**  
```python
temp_range = TemperatureRange(10, 20, "Celsius")
print(15 in temp_range)  # True
print(25 in temp_range)  # False

expanded_range = temp_range + 5  # Expands range by 5 degrees
print(expanded_range)  # TemperatureRange(5, 25, "Celsius")
```

---

## **Step 9: Allow Arithmetic with Lists and Tuples**  
Modify `__add__` and `__sub__` so that:  
✅ Adding/subtracting a **list/tuple** of numbers **adjusts multiple temperature readings**.  
✅ Returns a **list of new TemperatureReading instances** instead of a single object.  

### **Tasks**  
1. If `other` is a `list` or `tuple`, apply the arithmetic **element-wise**.  
2. Return a **new list of TemperatureReading objects**.  

💡 **Hints:**  
- Check `isinstance(other, (list, tuple))`.  
- Use **list comprehensions** to apply the operation across all values.  

### **Example Usage**  
```python
temp = TemperatureReading(10, "10/03/25", "London", "Celsius")
adjusted_temps = temp + [1, 2, -1, 5]  # Should return a list of new TemperatureReading instances
print(adjusted_temps)  # [TemperatureReading(11), TemperatureReading(12), ...]
```

