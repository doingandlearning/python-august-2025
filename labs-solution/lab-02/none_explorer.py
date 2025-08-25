# Step 5: Using None
# This program demonstrates the special None value and its properties

# Create a variable that holds the value None
user = None

# Print the variable to see what it displays
print('user:', user)

# Test whether the value is None using 'is None'
print('user is None:', user is None)

# Test whether the value is not None using 'is not None'
print('user is not None:', user is not None)

# Show the type of the None value
print('The type of the user:', type(user))

# Additional examples to understand None better
print("\n--- Additional None Examples ---")

# None vs empty string
empty_string = ""
print(f'empty_string: "{empty_string}"')
print(f'empty_string is None: {empty_string is None}')
print(f'empty_string == "": {empty_string == ""}')

# None vs zero
zero_number = 0
print(f'zero_number: {zero_number}')
print(f'zero_number is None: {zero_number is None}')
print(f'zero_number == 0: {zero_number == 0}')
