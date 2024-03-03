import unittest

class TestIsPrime(unittest.TestCase):
    def test_is_prime_zero(self):
        self.assertIsNone(is_prime(0))

if __name__ == '__main__':
    unittest.main()
