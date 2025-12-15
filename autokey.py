ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    key_stream = key.upper() + plaintext
    cipher = ""
    for p, k in zip(plaintext, key_stream):
        cipher += ALPHABET[(ALPHABET.index(p) + ALPHABET.index(k)) % 26]
    return cipher

def decrypt(ciphertext, key):
    key = key.upper()
    plaintext = ""
    for i, c in enumerate(ciphertext):
        k = key[i] if i < len(key) else plaintext[i - len(key)]
        plaintext += ALPHABET[(ALPHABET.index(c) - ALPHABET.index(k)) % 26]
    return plaintext
