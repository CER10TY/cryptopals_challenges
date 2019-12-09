#!python3

import base64
from SingleXOR import singlexor
from RepeatXOR import repeatKeyXOR

def chunkify(lst: dict, n: int) -> list:
    split = [[] for i in range(n)]
    counter = 0
    for char in lst:
        split[counter].append(char)
        counter += 1
        counter %= n
    return split

def hamming(a: bytes, b: bytes) -> int:
    distance: int = 0
    # Get the xor'ed bytes (not bits) -> 1 means difference, 0 means equal
    xor_bytes = [a1 ^ b1 for a1,b1 in zip(a,b)]

    # Then iterate through bits and sum up distance
    for byte in xor_bytes:
        # Aka: Add 1 distance for every bit in byte if bit is 1
        distance += sum([1 for bit in bin(byte) if bit == '1'])

    return distance

def test() -> int:
    a: bytes = "this is a test".encode('utf-8')
    b: bytes = "wokka wokka!!!".encode('utf-8')
    return hamming(a, b)

def breakRepeatXOR(file) -> str:
    # First we read and decode from base64
    ciphertexts: str = base64.b64decode(file)
    key_sizes = []
    # Cryptopals recommends keysize between 2 and 40 for this challenge
    # However with increased key length comes increased security
    for KEYSIZE in range(2, 40):
        running_sum = []
        for i in range(0, int(len(ciphertexts) / KEYSIZE) - 1):
            # Take first part of KEYSIZE length, then second.
            running_sum.append(hamming(ciphertexts[i * KEYSIZE:(i + 1) * KEYSIZE],
                                    ciphertexts[(i + 1) * KEYSIZE:(i + 2) * KEYSIZE]) / KEYSIZE)
        key_sizes.append((sum(running_sum)/ len(running_sum), KEYSIZE))
    # Lowest distance first
    key_sizes.sort(key=lambda a: a[0])
    # Chunks again
    chunks = chunkify(ciphertexts,key_sizes[0][1])
    key = ""
    # Use SingleXOR.singlexor to find likely key using ETAOIN SHRDLU
    for chunk in chunks:
        xor = singlexor(chunk)
        key += xor[0]
    # Decrypt the mfer
    return repeatKeyXOR(ciphertexts, key)