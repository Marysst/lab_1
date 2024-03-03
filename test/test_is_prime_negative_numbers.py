import unittest
  
from is_prime import is_prime

class TestIsPrime(unittest.TestCase):
    def test_is_prime_negative_numbers(self):
        self.assertIsNone(is_prime(-2))
        self.assertIsNone(is_prime(-3))
        self.assertIsNone(is_prime(-5))
        self.assertIsNone(is_prime(-7))
        self.assertIsNone(is_prime(-9))

if __name__ == '__main__':
    unittest.main()
