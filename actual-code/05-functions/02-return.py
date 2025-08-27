print(sum([1,2,3,4,5,6]))

def square(number):
  return number ** 2  # number * number

print(square(9))

def get_readings_from_user():
  readings = []

  while True:
    reading = input("What is the temperature reading? (q to quit)")
    if reading == "q":
      break
    readings.append(float(reading))
  return readings

readings = get_readings_from_user()

print(sum(readings) / len(readings))