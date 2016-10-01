import xorcipher


ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'



#pts = get_plaintexts(ciphertext)
#print(get_most_probable(pts)[0])

txt = xorcipher.XorCiphertext(ciphertext)

#ptxts = txt.get_plaintexts()

#for t in ptxts:
#    print(t)

t = txt.get_most_probable()

for i in t:
    print(i.plaintext, i.key, i.freq_sum)
