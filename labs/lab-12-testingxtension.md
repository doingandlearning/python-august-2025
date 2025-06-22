### **Lab Extension: Advanced Fixtures & More Complex Testing**

## **Objective**
This extension builds on **Lab: Testing**, introducing:
1. **More advanced fixture usage** for setup and cleanup.
2. **Parameterized fixtures** to test multiple cases efficiently.
3. **Integration testing** by combining multiple fixtures.
4. **Testing for edge cases and exceptions** to improve robustness.

---

## **Step 5: Using Fixtures for Reusable Test Data**
Instead of manually defining test data in every function, **use fixtures** to provide **consistent and reusable test cases**.

### **Tasks**
1. Create a fixture called `temperature_readings` that returns a **list of `TemperatureReading` objects**.
2. Modify test functions to use this fixture instead of manually defining data.

💡 **Hints**
- Define fixtures in **`conftest.py`** (or in the test file if you don’t have `conftest.py`).
- Use `@pytest.fixture` and return **a list of pre-defined temperature readings**.

---

## **Step 6: Adding a Parameterized Fixture**
Modify the fixture so it **generates multiple sets of test data**, testing different scenarios.

### **Tasks**
1. Modify `temperature_readings` to accept **a parameter** (`dataset_type`).
2. Return different data depending on the parameter:
   - `"normal"`: A standard dataset with mixed values.
   - `"high_temps"`: A dataset with **only high temperatures**.
   - `"low_temps"`: A dataset with **only low temperatures**.
3. Use `pytest.mark.parametrize` to run tests for **all three datasets**.

💡 **Hints**
- Use `@pytest.fixture(params=["normal", "high_temps", "low_temps"])` to create **multiple versions of a fixture**.
- Inside the fixture, check `request.param` to decide **which dataset to return**.

---

## **Step 7: Integration Testing – Combining Fixtures**
Instead of testing **single functions**, test **how multiple components work together**.

### **Tasks**
1. Define another fixture `temperature_log` that:
   - Uses `temperature_readings` to **simulate a temperature log file**.
   - Returns a **string** containing temperature data in CSV format.
2. Write a test that:
   - Reads data from `temperature_log`.
   - Parses it into a list of `TemperatureReading` objects.
   - Ensures **all readings are correctly processed**.

💡 **Hints**
- Use `"\n".join(f"{t.date},{t.location},{t.temp}" for t in readings)` to create a **fake log file**.
- Simulate **reading from a file** by using `.split("\n")`.

---

## **Step 8: Testing Edge Cases & Exceptions**
Ensure the functions handle **invalid input properly**.

### **Tasks**
1. Test `TemperatureReading.__init__` for:
   - **Non-numeric temperatures** (should raise `ValueError`).
   - **Invalid date formats**.
   - **Incorrect temperature scales** (only `"Celsius"` or `"Fahrenheit"` should be allowed).
2. Test conversion functions for:
   - **Extreme temperatures** (e.g., `-273.15` Celsius).
   - **Invalid input types** (e.g., passing a string instead of a number).

💡 **Hints**
- Use `pytest.raises(ValueError)` to **assert that exceptions are raised**.
- Use **parameterized tests** to check **multiple invalid cases at once**.

---

## **Solutions (Spoilers)**

<details>
<summary>Click to reveal solutions</summary>

```python
import pytest
from readings import TemperatureReading, CELSIUS, FAHRENHEIT
from utils import celsius_to_fahrenheit, fahrenheit_to_celsius

# Step 5: Basic Fixture
@pytest.fixture
def temperature_readings():
    """Fixture to create standard temperature readings"""
    return [
        TemperatureReading(10.5, "01/01/2025", "London", CELSIUS),
        TemperatureReading(15.3, "02/01/2025", "London", CELSIUS),
        TemperatureReading(12.8, "03/01/2025", "London", CELSIUS),
        TemperatureReading(8.2, "04/01/2025", "London", CELSIUS),
        TemperatureReading(18.7, "05/01/2025", "London", CELSIUS),
    ]

# Step 6: Parameterized Fixture
@pytest.fixture(params=["normal", "high_temps", "low_temps"])
def parameterized_readings(request):
    """Fixture that returns different temperature datasets"""
    if request.param == "normal":
        return [TemperatureReading(12, "01/02/2025", "London", CELSIUS)]
    elif request.param == "high_temps":
        return [TemperatureReading(40, "02/02/2025", "Dubai", CELSIUS)]
    elif request.param == "low_temps":
        return [TemperatureReading(-10, "03/02/2025", "Oslo", CELSIUS)]

# Step 7: Integration Testing Fixture
@pytest.fixture
def temperature_log(temperature_readings):
    """Simulates a log file containing temperature readings"""
    return "\n".join(f"{t.date},{t.location},{t.temp}" for t in temperature_readings)

# Step 7: Integration Test
def test_temperature_log_parsing(temperature_log):
    """Ensure temperature log is correctly parsed"""
    lines = temperature_log.split("\n")
    assert len(lines) == 5
    assert "01/01/2025,London,10.5" in lines

# Step 8: Testing for Edge Cases & Exceptions
def test_invalid_temperature():
    """Ensure non-numeric temperatures raise ValueError"""
    with pytest.raises(ValueError):
        TemperatureReading("not-a-number", "01/01/2025", "London")

@pytest.mark.parametrize("invalid_date", ["2025-01-01", "01-01-2025", "1/1/25", "not-a-date"])
def test_invalid_date_format(invalid_date):
    """Ensure invalid date formats raise ValueError"""
    with pytest.raises(ValueError):
        TemperatureReading(10, invalid_date, "London")

@pytest.mark.parametrize("invalid_scale", ["Kelvin", "Rankine", "F"])
def test_invalid_temperature_scale(invalid_scale):
    """Ensure invalid scales raise ValueError"""
    with pytest.raises(ValueError):
        TemperatureReading(10, "01/01/2025", "London", invalid_scale)

@pytest.mark.parametrize("celsius, expected_fahrenheit", [
    (0, 32), (100, 212), (-40, -40), (-273.15, -459.67)
])
def test_celsius_to_fahrenheit(celsius, expected_fahrenheit):
    """Test Celsius to Fahrenheit conversion"""
    assert celsius_to_fahrenheit(celsius) == pytest.approx(expected_fahrenheit, rel=0.01)

@pytest.mark.parametrize("fahrenheit, expected_celsius", [
    (32, 0), (212, 100), (-40, -40), (-459.67, -273.15)
])
def test_fahrenheit_to_celsius(fahrenheit, expected_celsius):
    """Test Fahrenheit to Celsius conversion"""
    assert fahrenheit_to_celsius(fahrenheit) == pytest.approx(expected_celsius, rel=0.01)
```

</details>

---

## **Summary: What This Extension Adds**
| Feature | What It Teaches |
|---------|----------------|
| **Fixtures** | Reusable test setup across multiple tests. |
| **Parameterized Fixtures** | Run tests with different datasets dynamically. |
| **Integration Testing** | Combine multiple fixtures to test real-world workflows. |
| **Edge Case & Exception Handling** | Ensures functions handle errors correctly. |
