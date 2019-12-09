#!python3

def repeatKeyXOR(plaintext: bytes, key: str) -> str:
  plaintext_bytes = bytearray(plaintext)
  key_bytes = bytearray(key.encode('utf-8'))
  ciphertext = bytearray()

  for i in range(len(plaintext_bytes)):
    k = key_bytes[i % len(key)]
    c = plaintext_bytes[i] ^ k
    ciphertext.append(c)

  return ciphertext