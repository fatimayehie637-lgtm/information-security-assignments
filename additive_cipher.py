ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    return ''.join(ALPHABET[(ALPHABET.index(c) + key) % 26] for c in plaintext)

def decrypt(ciphertext, key):
    return ''.join(ALPHABET[(ALPHABET.index(c) - key) % 26] for c in ciphertext)

def brute_force(ciphertext):
    results = {}
    for key in range(26):
        results[key] = decrypt(ciphertext, key)
    return results

# Example
c = encrypt("HELLO", 3)
print(c)
print(decrypt(c, 3))
print(brute_force(c))
