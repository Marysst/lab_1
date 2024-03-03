import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
sys.path.append(root_dir)

sys.path.append("..")  
from is_prime import is_prime

class TestIsPrime(unittest.TestCase):
        def test_is_prime_composite_numbers(self):
                self.assertFalse(is_prime(4))
                self.assertFalse(is_prime(12))
                self.assertFalse(is_prime(25))
                self.assertFalse(is_prime(49))
                self.assertFalse(is_prime(93))

if __name__ == '__main__':
    unittest.main()
