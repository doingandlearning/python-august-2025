count = 1

def print_count():
  global count  # I want to change the variable outside the function! (try to avoid!)
  count += 1
  print(count)
  time = "12:15"


print_count()  
print(count)
# print(time)

"""
- Functions can read any variable out of themselves
- They can have their own versions (shadowing)
- Any created variables are not accessible outside the function
- Functions can't write to variables outside of themselves 
  - You can override this with global
"""