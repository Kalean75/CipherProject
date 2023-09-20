class VigenereEncrypt:

    def __init__(self, ciphertext,key):
        self.ciphertext = ciphertext
        self.key = key
        print(key)
    
    def encryptVigenere(self,ciphertext, key):
        ciphertext = ciphertext.upper()
        encrypted = ''
        for i, ch in enumerate(ciphertext):
            encrypted += self.shiftLetter(self,ch, key[i % len(key)])
            f = open("cipher.txt", "w")
            f.write("Ciphertext: " + ciphertext + "\n")
            f.write("key: " + key + "\n")
            f.write("Encrypted: " + ciphertext + "\n")
            f.close()
        return encrypted

    def _shiftLetter(self,letter, keyLetter):
        letter = ord(letter) - ord("A")
        keyLetter = ord(keyLetter) - ord("A")
        new = (letter + keyLetter) % 26
        return chr(new + ord("A"))