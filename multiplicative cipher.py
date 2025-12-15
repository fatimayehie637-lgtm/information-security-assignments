import math

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def mod_inverse(a, m=26):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None

def encrypt(plaintext, key):
    if math.gcd(key, 26) != 1:
        raise ValueError("Key must be coprime with 26")
    plaintext = plaintext.upper().replace(" ", "")
    return ''.join(ALPHABET[(ALPHABET.index(c) * key) % 26] for c in plaintext)

def decrypt(ciphertext, key):
    inv = mod_inverse(key)
    return ''.join(ALPHABET[(ALPHABET.index(c) * inv) % 26] for c in ciphertext)

def brute_force(ciphertext):
    results = {}
    for key in range(1, 26):
        if math.gcd(key, 26) == 1:
            results[key] = decrypt(ciphertext, key)
    return results
