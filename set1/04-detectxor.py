import xorcipher


strings = []
with open('./4.txt') as f:
    for line in f:
        strings.append(line.rstrip('\n'))

results = []
hit = xorcipher.XorCiphertext.get_most_probable

for s in strings:
    x = xorcipher.XorCiphertext(s)
    results.append(hit(plaintexts=x.get_plaintexts()))

rs = hit(plaintexts=results)
print(rs.plaintext, rs.ciphertext, rs.key)
