import unittest
from ex_25 import factorial, power_of, runMain

class Testex_25(unittest.TestCase):
    def test_factorial5(self):
        print("\nTest factorial of 5")
        self.assertEqual(factorial(5), 120)

    def test_factiorial0(self):
        print("\nTest factorial of 0")
        self.assertEqual(factorial(0), 1)

    def test_power_of_5_3(self):
        print("\nTest Power of base 5 with exponent 3")
        self.assertEqual(power_of(5, 3), 125)
    
    def test_main(self):
        print("\nTest the main function")
        self.assertEqual(runMain(2, 3), '6.33')

if __name__ == '__main__':
    unittest.main()