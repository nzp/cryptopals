FREQUENCIES = {
    #  Made up frequency for space.  It's slightly higher than 'e', but I can't
    #  find the actual number.
    ' ': 13.0,
    'e': 12.02, 'E': 12.02,
    't': 9.10, 'T': 9.10,
    'a': 8.12, 'A': 8.12,
    'o': 7.68, 'O': 7.68,
    'i': 7.31, 'I': 7.31,
    'n': 6.95, 'N': 6.95,
    's': 6.28, 'S': 6.28,
    'r': 6.02, 'R': 6.02,
    'h': 5.92, 'H': 5.92,
    'd': 4.32, 'D': 4.32,
    'l': 3.98, 'L': 3.98,
    'u': 2.88, 'U': 2.88,
    'c': 2.71, 'C': 2.71,
    'm': 2.61, 'M': 2.61,
    'f': 2.30, 'F': 2.30,
    'y': 2.11, 'Y': 2.11,
    'w': 2.09, 'W': 2.09,
    'g': 2.03, 'G': 2.03,
    'p': 1.82, 'P': 1.82,
    'b': 1.49, 'B': 1.49,
    'v': 1.11, 'V': 1.11,
    'k': 0.69, 'K': 0.69,
    'x': 0.17, 'X': 0.17,
    'q': 0.11, 'Q': 0.11,
    'j': 0.10, 'J': 0.10,
    'z': 0.07, 'Z': 0.07
}

KEYS = [
    " ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-",
    ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";",
    "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H", "I",
    "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
    "X", "Y", "Z", "[", "\\", "]", "^", "_", "`", "a", "b", "c", "d", "e",
    "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
    "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~", "\n", "\t", "\r"
]

ciphertext = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'


def get_plaintexts(ciphertext):
    ciphertext_b = bytes.fromhex(ciphertext)
    plaintexts = []

    for k in KEYS:
        k_b = bytes(k, 'ascii')
        xored = []

        for i in list(ciphertext_b):
            xored.append(
                i ^ int.from_bytes(k_b, 'little')
            )
        plaintexts.append(bytes(xored))

    return plaintexts


def get_most_probable(plaintexts):
    freq_sums = {}

    for plaintext in plaintexts:
        plaintext_a = plaintext.decode('ascii')
        freqs = []

        for c in plaintext_a:
            try:
                freqs.append(FREQUENCIES[c])
            except KeyError:
                # Penalty for chars not in freq table.
                freqs.append(-1)

        freq_sums[plaintext_a] = sum(freqs)

    return sorted(freq_sums, key=lambda text: freq_sums[text], reverse=True)


pts = get_plaintexts(ciphertext)
print(get_most_probable(pts)[0])

