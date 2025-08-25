# Types Demo - Comprehensive Program
# This program demonstrates all concepts learned in Lab 2: Types

print("=" * 50)
print("Welcome to the Python Types Demonstration Program!")
print("=" * 50)

# Step 1: Interactive greeting
print("\n--- Step 1: Interactive Greeting ---")
user_name = input("Please enter your name: ")
print("Welcome,", user_name, "! Nice to meet you.")

# Step 2: Number calculations
print("\n--- Step 2: Number Calculations ---")
first_num = float(input("Please enter a number: "))
second_num = float(input("Please enter another number: "))

# Perform calculations
sum_result = first_num + second_num
product_result = first_num * second_num
difference_result = first_num - second_num

print("Results:")
print("  ", first_num, "+", second_num, "=", sum_result)
print("  ", first_num, "*", second_num, "=", product_result)
print("  ", first_num, "-", second_num, "=", difference_result)
print("  Type of sum:", type(sum_result))

# Step 3: String operations
print("\n--- Step 3: String Operations ---")
first_string = input("Please enter a string: ")
second_string = input("Please enter another string: ")

# String concatenation
combined_string = first_string + " " + second_string
print("Combined string:", combined_string)
print("Type:", type(combined_string))

# String methods
print("Length of combined string:", len(combined_string))
print("Uppercase:", combined_string.upper())
print("Lowercase:", combined_string.lower())

# Step 4: Type conversion examples
print("\n--- Step 4: Type Conversion Examples ---")

# Number to string
version_number = 2.1
app_title = "My Python App v" + str(version_number)
print("App title:", app_title)

# String to number
user_age = input("Please enter your age: ")
age_number = int(user_age)
print("Age as number:", age_number, "Type:", type(age_number))

# Calculate age in months
age_months = age_number * 12
print("Your age in months:", age_months)

# Step 5: None value exploration
print("\n--- Step 5: None Value Exploration ---")

# Initialize variables
user_preference = None
user_score = 0

print("User preference:", user_preference)
print("User preference is None:", user_preference is None)
print("User score:", user_score)
print("User score is None:", user_score is None)

# Simulate setting a preference
print("\nSetting user preference...")
user_preference = "Python Programming"
print("User preference:", user_preference)
print("User preference is None:", user_preference is None)

# Final summary
print("\n" + "=" * 50)
print("Program Summary:")
print("  User:", user_name)
print("  Numbers processed:", first_num, ",", second_num)
print("  Strings combined:", first_string, ",", second_string)
print("  App version:", version_number)
print("=" * 50)

print("\nThank you for using the Types Demo Program!")
