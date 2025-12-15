import string

SYMBOLS = "ADFGVX"

def create_matrix(key):
    chars = key + string.ascii_uppercase + string.digits
    seen = []
    for c in chars:
        if c not in seen:
            seen.append(c)
    return [seen[i:i+6] for i in range(0, 36, 6)]

def encrypt(text, key, trans_key):
    matrix = create_matrix(key)
    text = text.upper().replace(" ", "")
    cipher = ""
    for c in text:
        for i in range(6):
            for j in range(6):
                if matrix[i][j] == c:
                    cipher += SYMBOLS[i] + SYMBOLS[j]
    # Columnar Transposition
    order = sorted(list(enumerate(trans_key)), key=lambda x: x[1])
    cols = [''] * len(trans_key)
    for i, c in enumerate(cipher):
        cols[i % len(trans_key)] += c
    return ''.join(cols[i] for i, _ in order)
