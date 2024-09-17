class Encrypt:
    def __init__(self):
        # self.ciphertext = ciphertext
        # self.key = key
        return

    def encryptVigenere(self, ciphertext, key):
        ciphertext = ciphertext.upper()
        encrypted = ""
        for i, ch in enumerate(ciphertext):
            encrypted += self._shiftLetter(ch, key[i % len(key)])
            f = open("cipher.txt", "w")
            f.write(ciphertext + "\n")
            f.write(key + "\n")
            f.write(encrypted + "\n")
            f.close()
        return encrypted

    def _shiftLetter(self, letter, keyLetter):
        letter = ord(letter) - ord("A")
        keyLetter = ord(keyLetter) - ord("A")
        new = (letter + keyLetter) % 26
        return chr(new + ord("A"))
