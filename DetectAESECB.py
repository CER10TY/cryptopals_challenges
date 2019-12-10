#!python3

# Cryptopals Challenge 8 Set 1 says DETECT, NOT DECRYPT
# I swear to god

import itertools

def chunkify(lst: dict, n: int) -> list:
    split = [[] for i in range(n)]
    counter = 0
    for char in lst:
        split[counter].append(char)
        counter += 1
        counter %= n
    return split

with open('challenge8', 'r') as file:
    for index, line in enumerate(file):
        ciphertext_bytes = bytearray.fromhex(line.rstrip())
        # And now remember: 16 bytes of plaintext == 16 bytes of ciphertext
        ciphertext_split = chunkify(ciphertext_bytes, 16)