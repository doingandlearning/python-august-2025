from calculator import add

def test_add_two_whole_numbers():
  number1 = 5
  number2 = 12
  expected_result = 17
  assert add(number1, number2) == expected_result