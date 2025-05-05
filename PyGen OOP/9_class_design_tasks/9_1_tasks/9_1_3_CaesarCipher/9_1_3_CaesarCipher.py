'''
TODO:
    Implement the CaesarCipher class to encrypt and decrypt text using
    the Caesar cipher.

    When creating an instance of the CaesarCipher class, you must specify
    the shift that will be used for encryption and decryption.

    The encode() method should be responsible for the encryption operation,
    and the decode() method should be responsible for the decryption operation:
        cipher = CaesarCipher(5)
        print(cipher.encode('Beegeek')) # Gjjljjp
        print(cipher.decode('Gjjljjp')) # Beegeek

    Note that when encrypting, the shift must be to the right, and also note
    that the case of letters must be preserved during encryption and
    decryption.

    Only Latin letters should be encrypted and decrypted, all other characters,
    if present, should remain unchanged:
        print(cipher.encode('Биgeek123')) # Биljjp123
        print(cipher.decode('Биljjp123')) # Биgeek123

NOTE:
    The shift is guaranteed to be a number from the range [1; 26].
'''


class CaesarCipher:
    """
    A class for encrypting/decrypting text using Caesar cipher.
    """
    def __init__(self, shift: int) -> None:
        """
        Initialize cipher with shift value.

        Args:
            shift: Shift value for encryption/decryption (1 to 26).
        """
        self.shift = shift

    def _code(self, text: str, shift: int) -> str:
        """
        Apply Caesar cipher to text with given shift.

        Args:
            text: Text to encode or decode.
            shift: Shift value (positive for encode, negative for decode).

        Returns:
            Transformed text with preserved case and non-letters.
        """
        result = []
        for c in text:
            if c.isalpha() and c.isascii():
                # Determine base and modulus for case (A=65, a=97)
                base = 65 if c.isupper() else 97
                res = (ord(c) - base + shift) % 26 + base
                result.append(chr(res))
            else:
                result.append(c)
        return ''.join(result)

    def encode(self, text: str) -> str:
        """
        Encrypt text using Caesar cipher.

        Args:
            text: Text to encrypt.

        Returns:
            Encrypted text.
        """
        return self._code(text, self.shift)

    def decode(self, text: str) -> str:
        """
        Decrypt text using Caesar cipher.

        Args:
            text: Text to decrypt.

        Returns:
            Decrypted text.
        """
        return self._code(text, -self.shift)
