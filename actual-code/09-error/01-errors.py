"""
1. Developer errors - not closing brackets, using a method that doesn't exist
- Do want your program to crash!! Quick feedback to be able improve

2. Real-world errors - user input, database being down, webserver authentication changing ...
- It's worth crashing!! 
- To allow programs to recover!

Error <-> Exception
SyntaxError
FileNotFoundException


try:
  do some code
  interact with users
  raise Exception   (throw)

  -> catch  (except)

"""
raise TypeError("That's incorrect!")
print("Hello!")
