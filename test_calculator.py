import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        assert multiply(1, 1000) == 1000
        assert multiply(-0.5, 20) == -10
        assert multiply(-10, -10) == 100

    def test_divide(self): # 3 assertions
        assert div(100, 1) == 1
        assert div(10, -0.5) == -20
        assert div(-10, -20) == 0.5
     ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
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