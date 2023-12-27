from simple_programm import is_prime


def test_one():
   assert is_prime(5) == True

def test_two():
   assert is_prime(6) == False

def test_three():
   assert is_prime(7) == True
