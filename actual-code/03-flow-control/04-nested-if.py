# minimise nesting ... 
# Cyclomatic Complexity
# 

is_sunny = False
temperature_in_celcius = 19
has_airconditioning = True

if is_sunny:
  if temperature_in_celcius > 20:
    if has_airconditioning:
      print("What the airconditioning up (sorry planet)")
    else:  
      print("Try not to melt - stay hydrated")
  else:
    print("It's nice outside")
else:
  print("I like it when it's not sunny!")