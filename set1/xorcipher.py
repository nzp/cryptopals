from array import array


FREQUENCIES = {
    #  Made up frequency for space.  It's slightly higher than 'e', but I can't
    #  find the actual number.
    ord(' '): 13.0,
    ord('e'): 12.02, ord('E'): 12.02,
    ord('t'): 9.10, ord('T'): 9.10,
    ord('a'): 8.12, ord('A'): 8.12,
    ord('o'): 7.68, ord('O'): 7.68,
    ord('i'): 7.31, ord('I'): 7.31,
    ord('n'): 6.95, ord('N'): 6.95,
    ord('s'): 6.28, ord('S'): 6.28,
    ord('r'): 6.02, ord('R'): 6.02,
    ord('h'): 5.92, ord('H'): 5.92,
    ord('d'): 4.32, ord('D'): 4.32,
    ord('l'): 3.98, ord('L'): 3.98,
    ord('u'): 2.88, ord('U'): 2.88,
    ord('c'): 2.71, ord('C'): 2.71,
    ord('m'): 2.61, ord('M'): 2.61,
    ord('f'): 2.30, ord('F'): 2.30,
    ord('y'): 2.11, ord('Y'): 2.11,
    ord('w'): 2.09, ord('W'): 2.09,
    ord('g'): 2.03, ord('G'): 2.03,
    ord('p'): 1.82, ord('P'): 1.82,
    ord('b'): 1.49, ord('B'): 1.49,
    ord('v'): 1.11, ord('V'): 1.11,
    ord('k'): 0.69, ord('K'): 0.69,
    ord('x'): 0.17, ord('X'): 0.17,
    ord('q'): 0.11, ord('Q'): 0.11,
    ord('j'): 0.10, ord('J'): 0.10,
    ord('z'): 0.07, ord('Z'): 0.07
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

            for c in list(plaintext.plaintext):
                try:
                    freqs.append(FREQUENCIES[c])
                except KeyError:
                    continue

            plaintext.freq_sum = sum(freqs)
            results.append(plaintext)

        return sorted(results, key=lambda result: result.freq_sum, reverse=True)
