#!python3

from DecryptAES128 import decrypt_aes_128

def chunkify(lst: dict, n: int) -> list:
    split = [[] for i in range(n)]
    counter = 0
    for char in lst:
        split[counter].append(char)
        counter += 1
        counter %= n
    return split

with open('challenge8', 'r') as file:
    for line in file:
        line_bin = bin(int(line, 16))[2:]
        # If it's not divisible by 128, it's not an AES-128 ECB string, as they need a 128 bit key.
        # Reminder: ECB pads the last block with null bytes if necessary. This ensures block size is also 128 bit.
        if len(line_bin) % 128 == 0:
            # Only 111 lines are possible candidates
            ciphertext_bytes = bytearray.fromhex(line)
            # And now remember: 16 bytes of plaintext == 16 bytes of ciphertext
            ciphertext_split = chunkify(ciphertext_bytes, 16)
            