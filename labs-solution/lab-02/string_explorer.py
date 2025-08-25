# Step 3: Input Two Strings
# This program demonstrates string input and concatenation

# Get two strings from the user
first_string = input('Please enter a string: ')
second_string = input('Please enter another string: ')

# Concatenate the strings
combined_value = first_string + second_string

# Display the result and its type
print('The new value is', combined_value)
print(f'The type of the value is {type(combined_value)}')

# Step 4: Concatenate a Number and a String
# This demonstrates the need for type conversion

# Try to concatenate a string with a number (this would cause an error)
# Uncomment the next line to see the error:
# title = 'Data Processing App Version ' + 1.0

# Correct way: convert the number to a string first
title = 'Data Processing App Version ' + str(1.0)
print(f'The title of this app is {title}')
