#!python3

# Requires pycrypto

from Crypto.Cipher import AES

def decrypt_aes_128(ciphertext: str, key: str) -> str:
  cipher = AES.new(key, AES.MODE_ECB)
  return cipher.decrypt(ciphertext)