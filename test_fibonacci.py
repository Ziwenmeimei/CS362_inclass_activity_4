import unittest
import fibonacci

class TestCaseFibonacci(unittest.TestCase):
    def test_fibonacci_1(self):
        result = fibonacci.fib(10)
        self.assertEqual(result,55)

    def test_fibonacci_2(self):
        result = fibonacci.fib(5)
        self.assertEqual(result,5)

    def test_fibonacci_3(self):
        result = fibonacci.fib(7)
        self.assertEqual(result,13)

class TestCasefactorial(unittest.TestCase):
    def test_factorial_1(self):
        result = fibonacci.factorial(4)
        self.assertEqual(result,24)

    def test_factorial_2(self):
        result = fibonacci.factorial(6)
        self.assertEqual(result,720)

    def test_factorial_3(self):
        result = fibonacci.factorial(3)
        self.assertEqual(result,6)
    
if __name__ == "__main__":
    unittest.main(verbosity = 2)