#!/usr/bin/env python3

import codecs
import pyaes
import secrets

password = b'0123456789abcdef' # any 16-byte string, 128-bit key (16 bytes)
print("\n\nKey\n\n")
print("AES encryption key: %s" % codecs.encode(password, 'hex'))
print("\n\nPlaintext\n\n")
data = 'hello world 1818'
print("Plaintext %s" % data)
print("Data length %d" % len(data))
print("\n\nEncryption\n\n")
iv = secrets.randbits(128)
aes_e = pyaes.AESModeOfOperationCTR(password, pyaes.Counter(iv))
ciphertext = aes_e.encrypt(data)
print("Ciphertext %s" % ciphertext)
print("HEX: %s" % codecs.encode(ciphertext, 'hex'))
print("\n\nDecryption\n\n")
aes_d = pyaes.AESModeOfOperationCTR(password, pyaes.Counter(iv))
plaintext = aes_d.decrypt(ciphertext)
print("Decrypted: %s" % plaintext)
