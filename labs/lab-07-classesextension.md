# **Lab 7 Extension: Enhancing the `TemperatureReading` Class**

## **Objective**
This extension builds on **Lab 7: Classes**, introducing:
1. **Data validation** to enforce correct input.
2. **Encapsulation** using private attributes.
3. **Class-level tracking** to monitor temperature readings.
4. **A factory method** to create instances from a formatted string.

---

## **Step 5: Enforce Data Validation**
Ensure that temperature values, dates, and scales are **valid** when a `TemperatureReading` is created.

### **Tasks**
1. Modify `__init__` to:
   - **Restrict temperature** to numeric values.
   - **Validate the scale** (must be `"Celsius"` or `"Fahrenheit"`).
   - **Check the date format** (use `dd/mm/yy` format).
   
2. If invalid data is provided, **raise a `ValueError`**.

💡 **Hints**
- Use `isinstance(value, (int, float))` to check if a value is a number.
- Use `in` to check if `scale` is either `"Celsius"` or `"Fahrenheit"`.
- Use `.split("/")` to check if a date has three parts.

---

## **Step 6: Encapsulate Temperature Data**
Modify the class to **protect the attributes** and provide **getter methods**.

### **Tasks**
1. Change `temp`, `date`, `location`, and `scale` to **private attributes** (`self._temp`, `self._date`, etc.).
2. Provide **getter methods** (e.g., `get_temperature()`) to retrieve values.
3. Provide a **setter method for temperature** that:
   - Ensures only **valid numeric values** are assigned.
   - Prevents modification if the object is **already converted**.

💡 **Hints**
- Prefix attributes with `_` to indicate **they should not be modified directly**.
- Use `def get_temperature(self):` to allow controlled access.

---

## **Step 7: Class-Level Tracking**
Keep track of **how many temperature readings have been created**.

### **Tasks**
1. Add a **class attribute** `total_readings = 0` to track the count.
2. **Increment** this attribute every time a new `TemperatureReading` is created.
3. Add a **class method** `get_total_readings()` to return the count.

💡 **Hints**
- Use `TemperatureReading.total_readings += 1` inside `__init__`.
- Define `@classmethod def get_total_readings(cls):` to retrieve the count.

---

## **Step 8: Create a Factory Method**
A factory method allows creating an instance from a **formatted string** instead of passing multiple arguments.

### **Tasks**
1. Implement a **class method** `from_string(cls, data_string)`.
2. The method should:
   - Accept a string in the format: `"13.5,01/05/20,London,Celsius"`.
   - Parse the string and create a new `TemperatureReading` instance.

3. Test it by creating multiple instances from **formatted strings**.

💡 **Hints**
- Use `.split(",")` to break the string into parts.
- Convert the **temperature to a float** before passing it to `__init__`.

---

# **Solutions (Spoilers)**

<details>
<summary>Click to reveal solutions</summary>

```python
class TemperatureReading:
    """Represents a temperature reading with validation and tracking."""

    CELSIUS = "Celsius"
    FAHRENHEIT = "Fahrenheit"

    total_readings = 0  # Class attribute to track number of readings

    def __init__(self, temp, date, location, scale=CELSIUS):
        # Step 5: Validate Data
        if not isinstance(temp, (int, float)):
            raise ValueError("Temperature must be a number.")

        if scale not in (self.CELSIUS, self.FAHRENHEIT):
            raise ValueError(f"Scale must be '{self.CELSIUS}' or '{self.FAHRENHEIT}'.")

        date_parts = date.split("/")
        if len(date_parts) != 3 or not all(part.isdigit() for part in date_parts):
            raise ValueError("Date must be in dd/mm/yy format.")

        # Step 6: Encapsulation (Private attributes)
        self._temp = temp
        self._date = date
        self._location = location
        self._scale = scale

        # Step 7: Increment total readings count
        TemperatureReading.total_readings += 1

    # Getters
    def get_temperature(self):
        return self._temp

    def get_date(self):
        return self._date

    def get_location(self):
        return self._location

    def get_scale(self):
        return self._scale

    # Setter with validation
    def set_temperature(self, new_temp):
        if not isinstance(new_temp, (int, float)):
            raise ValueError("Temperature must be a number.")
        self._temp = new_temp

    # Step 7: Class method to get total readings count
    @classmethod
    def get_total_readings(cls):
        return cls.total_readings

    # Step 8: Factory Method
    @classmethod
    def from_string(cls, data_string):
        """Creates a TemperatureReading from a comma-separated string."""
        parts = data_string.split(",")
        if len(parts) != 4:
            raise ValueError("Data string must be in the format 'temp,date,location,scale'.")

        temp, date, location, scale = parts
        return cls(float(temp), date, location, scale)

    # String representation for debugging
    def __repr__(self):
        return f"TemperatureReading({self._temp}, {self._date}, {self._location}, {self._scale})"

# Testing Step 5: Validation
try:
    invalid_reading = TemperatureReading("not-a-number", "01/05/20", "London")
except ValueError as e:
    print(e)

# Testing Step 6: Encapsulation
reading1 = TemperatureReading(13.5, "01/05/20", "London")
print(f"Original temp: {reading1.get_temperature()}")
reading1.set_temperature(15.0)
print(f"Updated temp: {reading1.get_temperature()}")

# Testing Step 7: Tracking total instances
reading2 = TemperatureReading(12.3, "02/05/20", "Edinburgh")
print(f"Total readings created: {TemperatureReading.get_total_readings()}")

# Testing Step 8: Factory Method
reading3 = TemperatureReading.from_string("14.6,05/05/20,Paris,Celsius")
print(f"Factory-created reading: {reading3}")
```

</details>

