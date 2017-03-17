import sys

xor = __import__('05_repeating_key_xor')


key = sys.argv[3]

with open(sys.argv[2], 'r') as f:
    text = f.read()

cipher = xor.RepeatingXOR(text, key)

if sys.argv[1] == 'e':
    print(cipher.encrypt())

elif sys.argv[1] == 'd':
    print(cipher.decrypt())

else:
    print('Wrong operation.  Give "e" or "d".')


