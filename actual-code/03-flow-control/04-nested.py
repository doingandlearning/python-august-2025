is_sunny = True 
temperature = 25
has_airconditioning = True

if is_sunny:
  if temperature > 20:
    if not has_airconditioning:
      print("It's hot - make sure you stay hydrated!")
    else:
      print("Whack the airconditioning up to full!")
  else:
    print("It's quite hot")
else:
  print("I like it when it's not sunny!")

# minimise nesting ... 