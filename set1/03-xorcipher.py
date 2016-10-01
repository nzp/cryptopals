import xorcipher


ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

txt = xorcipher.XorCiphertext(ciphertext)
result = txt.get_most_probable(plaintexts=txt.get_plaintexts())
print(result.plaintext, result.key)

