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
    def test_multiply(self): # 3 assertions
        assert multiply(1, 1000) == 1000
        assert multiply(-0.5, 20) == -10
        assert multiply(-10, -10) == 100

    def test_divide(self): # 3 assertions
        assert div(100, 1) == 100
        assert div(10, -0.5) == -20
        assert div(-10, -20) == 0.5
     ##########################

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
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
              log(-10, 1)
              

    def test_hypotenuse(self): # 3 assertions
        assert hypotenuse(3, 4) == 5
        assert hypotenuse(6, 8) == 10
        assert hypotenuse(15, 8) == 17

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
              square_root(-10)

        assert square_root(100) == 10
        assert square_root(225) == 15
        assert square_root(25) == 5
        
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()