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
