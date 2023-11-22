import unittest 
import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), ".."))
sys.path.append(parent_dir)

from src.lab2.caesar import encrypt_caesar, decrypt_caesar

class TestCaesarCipher(unittest.TestCase):
    def test_encrypt_caesar(self):
        self.assertEqual(encrypt_caesar("COOL"), 'FRRO')
        self.assertEqual(encrypt_caesar("cool"), 'frro')
        self.assertEqual(encrypt_caesar("Cool3"), 'Frro3')
        self.assertEqual(encrypt_caesar(""), '')

    def test_decrypt_caesar(self):
        self.assertEqual(decrypt_caesar("FRRO"), 'COOL')
        self.assertEqual(decrypt_caesar("frro"), 'cool')
        self.assertEqual(decrypt_caesar("Frro3"), 'Cool3')
        self.assertEqual(decrypt_caesar(""), '')

if __name__ == '__main__':
    unittest.main()
