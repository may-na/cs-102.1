import unittest
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), ".."))
sys.path.append(parent_dir)

from src.lab2.rsa import is_prime, gcd, multiplicative_inverse, generate_keypair, encrypt, decrypt

class TestRSAFunctions(unittest.TestCase):

    def test_is_prime(self):
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(17))
        self.assertFalse(is_prime(10))

    def test_gcd(self):
        self.assertEqual(gcd(7, 21), 7)
        self.assertEqual(gcd(5, 11), 1)

    def test_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(7, 40), 23)

    def test_generate_keypair(self):
        p, q = 11, 19
        public_key, private_key = generate_keypair(p, q)

    # Проверка на то, что оба ключа имеют два элемента
        self.assertEqual(len(public_key), 2)
        self.assertEqual(len(private_key), 2)

    # Проверка, что оба ключа содержат только целые числа
        self.assertIsInstance(public_key[0], int)
        self.assertIsInstance(public_key[1], int)
        self.assertIsInstance(private_key[0], int)
        self.assertIsInstance(private_key[1], int)


if __name__ == '__main__':
    unittest.main()
