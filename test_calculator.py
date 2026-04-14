import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

######### Partner 2

def test_add(self): # 3 assertions
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract(self): # 3 assertions
    assert subtract(5, 3) == 2
    assert subtract(0, 4) == -4
    assert subtract(-2, -3) == 1

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

######## Partner 2

def test_divide_by_zero(self):
    with self.assertRaises(ZeroDivisionError):
        div(0, 5)

def test_logarithm(self):
    self.assertEqual(logarithm(2, 8), 3)
    self.assertEqual(logarithm(10, 100), 2)
    self.assertAlmostEqual(logarithm(2, 4), 2)

def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)
###########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()