import sys


def fixedxor(x, y):
    if len(x) != len(y):
        return 1

    s1, s2 = (bytes.fromhex(z) for z in (x, y))
    l = len(s1)

    r = int.from_bytes(s1, sys.byteorder) ^ int.from_bytes(s2, sys.byteorder)
    print((r.to_bytes(l, sys.byteorder)).hex())

x = '1c0111001f010100061a024b53535009181c'
y = '686974207468652062756c6c277320657965'

fixedxor(x, y)

# output: 746865206b696420646f6e277420706c6179
