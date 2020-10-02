#!/usr/bin/env python3

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import codecs
private_key = RSA.generate(2048)    # generate 2048-bit RSA key pair (public/private)
public_key = private_key.publickey()
# RSA
# Choose two primes, p,q
# N = (p-1) * (q-1)
# choose e, usually 0x10001 (65537)
# find d, where    ed = 1 mod N
# Then, for a message m,
# ciphertext c = m ^ e mod N
# plaintext p = c ^ d mod N = m
# (n, e) is a public key and (n, d) is a private key
# to get d from (n, e), you need to decompose n into (p-1)(q-1),
# and if the RSA key is 2048 bit, then both p and q are
# 2^1023 < p, q < 2^1024, so these are the large numbers (over 300 digits)
# so it's based on the difficulty of prime factorization.
print("\n\nKey\n\n")
print(f"Public key:  (n={hex(public_key.n)}, e={hex(public_key.e)})")
print(f"Private key: (n={hex(public_key.n)}, d={hex(private_key.d)})")
print("\n\nPlaintext\n\n")
data = b'hello world 18, ' * 13 # (224 bytes)
print("Plaintext %s" % data)
print("Data length %d" % len(data))
print("\n\nEncryption\n\n")
encryptor = PKCS1_OAEP.new(public_key)
ciphertext = encryptor.encrypt(data)
print("Ciphertext %s" % ciphertext)
print("Data length %d" % len(ciphertext))
print("HEX: %s" % codecs.encode(ciphertext, 'hex'))
print("\n\nDecryption\n\n")
decryptor = PKCS1_OAEP.new(private_key)
plaintext = decryptor.decrypt(ciphertext)
print("Decrypted %s" % plaintext)
print("Data length %d" % len(plaintext))
