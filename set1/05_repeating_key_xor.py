from itertools import cycle


PLAINTEXT = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
KEY = "ICE"
CIPHERTEXT = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"


class RepeatingXOR:
    def __init__(self, text, key):
        self.text = text
        self.text_b = [ord(c) for c in text]
        self.key = key
        self.key_b = [ord(c) for c in key]

    def encrypt(self):
        ciphertext_b = [x ^ y for (x, y) in zip(self.text_b, cycle(self.key_b))]

        return bytes(ciphertext_b).hex()

    def decrypt(self):
        ciphertext_b = bytes.fromhex(self.text)

        return str(bytes([x ^ y for (x, y) in
                          zip(list(ciphertext_b), cycle(self.key_b))]))


if __name__ == '__main__':
    cipher = RepeatingXOR(PLAINTEXT, KEY)

    assert cipher.encrypt() == CIPHERTEXT
    print("OK")

