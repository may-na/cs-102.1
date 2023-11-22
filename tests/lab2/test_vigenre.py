import unittest
import random
import string
import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), ".."))
sys.path.append(parent_dir)

from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere

class TestVigenereEncryptionDecryption(unittest.TestCase):
    def test_encrypt_vigenere(self):
        self.assertEqual(encrypt_vigenere("HELLO", "A"), 'HELLO')
        self.assertEqual(encrypt_vigenere("hello", "a"), 'hello')
        self.assertEqual(encrypt_vigenere("HELLO", "HI"), 'OMSTV')

    def test_decrypt_vigenere(self):
        self.assertEqual(decrypt_vigenere("HELLO", "A"), 'HELLO')
        self.assertEqual(decrypt_vigenere("hello", "a"), 'hello')
        self.assertEqual(decrypt_vigenere("OMSTV", "HI"), 'HELLO')
    
    def test_randomized(self):
        kwlen = random.randint(4, 24)
        keyword = ''.join(random.choice(string.ascii_letters) for _ in range(kwlen))
        plaintext = ''.join(random.choice(string.ascii_letters + ' -,') for _ in range(64))
        ciphertext = encrypt_vigenere(plaintext, keyword)
        self.assertEqual(plaintext, decrypt_vigenere(ciphertext, keyword))



if __name__ == '__main__':
    unittest.main()
