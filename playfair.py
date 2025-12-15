import string

def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            result += 'X'
        i += 1
    if len(result) % 2 != 0:
        result += 'X'
    return result

def generate_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used = set()
    for c in key + string.ascii_uppercase:
        if c not in used and c != 'J':
            matrix.append(c)
            used.add(c)
    return [matrix[i:i+5] for i in range(0, 25, 5)]
