ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generate_key(text, key):
    key = key.upper()
    return (key * (len(text) // len(key) + 1))[:len(text)]

def encrypt(text, key):
    text = text.upper().replace(" ", "")
    key = generate_key(text, key)
    return ''.join(ALPHABET[(ALPHABET.index(t) + ALPHABET.index(k)) % 26]
                   for t, k in zip(text, key))

def decrypt(cipher, key):
    key = generate_key(cipher, key)
    return ''.join(ALPHABET[(ALPHABET.index(c) - ALPHABET.index(k)) % 26]
                   for c, k in zip(cipher, key))
