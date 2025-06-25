import sys

print(sys.version)
print(sys.maxsize)
print(sys.platform)  

if sys.maxsize < 9_223_372_036_854_775_807 + 1:  
  print("Sorry, this computer does not have enough memory to run this program")
  sys.exit(1) 
  # exit code of 0 means no error
  # non-zero exit codes

