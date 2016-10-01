from array import array


FREQUENCIES = {
    #  Made up frequency for space.  It's slightly higher than 'e', but I can't
    #  find the actual number.
    b' ': 13.0,
    b'e': 12.02, b'E': 12.02,
    b't': 9.10, b'T': 9.10,
    b'a': 8.12, b'A': 8.12,
    b'o': 7.68, b'O': 7.68,
    b'i': 7.31, b'I': 7.31,
    b'n': 6.95, b'N': 6.95,
    b's': 6.28, b'S': 6.28,
    b'r': 6.02, b'R': 6.02,
    b'h': 5.92, b'H': 5.92,
    b'd': 4.32, b'D': 4.32,
    b'l': 3.98, b'L': 3.98,
    b'u': 2.88, b'U': 2.88,
    b'c': 2.71, b'C': 2.71,
    b'm': 2.61, b'M': 2.61,
    b'f': 2.30, b'F': 2.30,
    b'y': 2.11, b'Y': 2.11,
    b'w': 2.09, b'W': 2.09,
    b'g': 2.03, b'G': 2.03,
    b'p': 1.82, b'P': 1.82,
    b'b': 1.49, b'B': 1.49,
    b'v': 1.11, b'V': 1.11,
    b'k': 0.69, b'K': 0.69,
    b'x': 0.17, b'X': 0.17,
    b'q': 0.11, b'Q': 0.11,
    b'j': 0.10, b'J': 0.10,
    b'z': 0.07, b'Z': 0.07
}

KEYS = array(
    'B',
    [ord(" "), ord("!"), ord("\""), ord("#"), ord("$"), ord("%"), ord("&"),
     ord("'"), ord("("), ord(")"), ord("*"), ord("+"), ord(","), ord("-"),
     ord("."), ord("/"), ord("0"), ord("1"), ord("2"), ord("3"), ord("4"),
     ord("5"), ord("6"), ord("7"), ord("8"), ord("9"), ord(":"), ord(";"),
     ord("<"), ord("="), ord(">"), ord("?"), ord("@"), ord("A"), ord("B"),
     ord("C"), ord("D"), ord("E"), ord("F"), ord("G"), ord("H"), ord("I"),
     ord("J"), ord("K"), ord("L"), ord("M"), ord("N"), ord("O"), ord("P"),
     ord("Q"), ord("R"), ord("S"), ord("T"), ord("U"), ord("V"), ord("W"),
     ord("X"), ord("Y"), ord("Z"), ord("["), ord("\\"), ord("]"), ord("^"),
     ord("_"), ord("`"), ord("a"), ord("b"), ord("c"), ord("d"), ord("e"),
     ord("f"), ord("g"), ord("h"), ord("i"), ord("j"), ord("k"), ord("l"),
     ord("m"), ord("n"), ord("o"), ord("p"), ord("q"), ord("r"), ord("s"),
     ord("t"), ord("u"), ord("v"), ord("w"), ord("x"), ord("y"), ord("z"),
     ord("{"), ord("|"), ord("}"), ord("~"), ord("\n"), ord("\t"), ord("\r")]
)


class XorCiphertext:
    def __init__(self, ciphertext):
        self.ciphertext = ciphertext
        self._ciphertext_b = bytes.fromhex(self.ciphertext)

    class Plaintext:
        def __init__(self, plaintext, key):
            self.plaintext = plaintext
            self.key = key
            self.freq_sum = 0

    def get_plaintexts(self):
        for k in KEYS:
            xored = []

            for i in list(self._ciphertext_b):
                xored.append(i^k)

            yield self.Plaintext(plaintext=bytes(xored), key=chr(k))

    def get_most_probable(self):
        results = []

        for plaintext in self.get_plaintexts():
            freqs = []

            for c in plaintext.plaintext:
                c_b = bytes([c])
                try:
                    freqs.append(FREQUENCIES[c_b])
                except KeyError:
                    continue

            plaintext.freq_sum = sum(freqs)
            results.append(plaintext)

        return sorted(results, key=lambda result: result.freq_sum, reverse=True)
