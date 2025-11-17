import unittest
from calculator import add, sub, div, log

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

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

    def test_add():
        assert add(2, 3) == 5
        assert add(-1, 4) == 3
        assert add(0, 0) == 0
    
    def test_subtract():
        assert sub(10, 3) == 7
        assert sub(4, 8) == -4
        assert sub(0, 0) == 0
    
    def test_divide_by_zero():
        with unittest.TestCase().assertRaises(ZeroDivisionError):
            div(5, 0)
        
    def test_logarithm():
        assert log(10, 100) == 2
        assert log(2, 8) == 3

    def test_log_invalid_base():
        with unittest.TestCase().assertRaises(ValueError):
            log(-2, 8)
        with unittest.TestCase().assertRaises(ValueError):
            log(0, 5) 
        with unittest.TestCase().assertRaises(ValueError):
            log(10, -3)


if __name__ == "__main__":
    unittest.main()