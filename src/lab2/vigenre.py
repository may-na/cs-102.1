def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("HELLO", "A")
    'HELLO'
    >>> encrypt_vigenere("hello", "a")
    'hello'
    >>> encrypt_vigenere("HELLO", "HI")
    'OMSTV'
    """
    ciphertext = ""
    keyword = keyword.upper()
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            shift = ord(keyword[i % len(keyword)]) - ord('A')
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphertext += char
    return ciphertext



def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("HELLO", "A")
    'HELLO'
    >>> decrypt_vigenere("hello", "a")
    'hello'
    >>> decrypt_vigenere("OMSTV", "HI")
    'HELLO'
    """
    plaintext = ""
    keyword = keyword.upper()
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            shift = ord(keyword[i % len(keyword)]) - ord('A')
            if char.isupper():
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            plaintext += char
    return plaintext