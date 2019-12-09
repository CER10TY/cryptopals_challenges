#!python3

import binascii
 
 
def xorstring(hex1, hex2):
    hex1 = binascii.unhexlify(hex1)
    hex2 = binascii.unhexlify(hex2)
    result = ''
    for x, y in zip(hex1, hex2):
        result += chr(x ^ y)
    return result
 
 
a = "1c0111001f010100061a024b53535009181c"
b = "686974207468652062756c6c277320657965"
r = "746865206b696420646f6e277420706c6179"
print(xorstring(a, b))