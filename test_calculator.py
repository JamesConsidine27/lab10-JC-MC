import calculator
import unittest

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(calculator.mult(2,3),6)
        self.assertEqual(calculator.mult(3,4),12)
        self.assertEqual(calculator.mult(6,7),42)


    def test_divide(self): # 3 assertions
        self.assertEqual(calculator.div(3,2),1.5)
        self.assertEqual(calculator.div(100,10),10)
        self.assertEqual(calculator.div(50,10),5)


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
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.log(0,5)


    def test_hypotenuse(self):
        self.assertEqual(calculator.hypotenuse(3,4),5.0)
        self.assertEqual(calculator.hypotenuse(6,8),10.0)
        self.assertEqual(calculator.hypotenuse(30,40),50.0)

    def test_sqrt(self):
        with self.asserRaises(ValueError):
            calculator.square_root(-4)
        self.assertEqual(calculator.square_root(1),1.0)
        self.assertEqual(calculator.square_root(4),2.0)
        self.assertEqual(calculator.square_root(100),10.0)


# Do not touch this
if __name__ == "__main__":
    unittest.main()