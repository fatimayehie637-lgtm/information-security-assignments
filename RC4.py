def KSA(key):
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S, n):
    i = j = 0
    stream = []
    for _ in range(n):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        stream.append(S[(S[i] + S[j]) % 256])
    return stream

def binary_derivative(stream):
    return [stream[i] ^ stream[i+1] for i in range(len(stream)-1)]

def change_point_test(stream):
    mean = sum(stream) / len(stream)
    return [abs(x - mean) for x in stream]
