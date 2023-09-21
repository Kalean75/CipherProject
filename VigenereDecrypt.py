class Decrypt:
    import re
    def __init__(self, printSS,printOccurrence,frequencyAnalysis, cipherText):
        self.printOccurr = printOccurrence
        self.printSS = printSS
        self.frequencyAnalysis = frequencyAnalysis
        self.cipherText = cipherText

    # Print text
    def printtext(self,text):
        print(text)

    def parseText(self,text,keyLength,start):
        #splitText = (text[0+i:keyLength+i] for i in range(0, len(text), keyLength))
        #parse original ciphertext into blocks based on keyLength
        newText = text[start:len(text):keyLength]
        return newText
    #finds substrings of length n in string text
    def findSubStrings(self,text,n):
        #parse for every n character word that exists
        nchars = [text[i:i+n] for i in range(0,len(text),1)]
        count = 0
        num = 23
        for string in nchars:
            count+=1
            if self.printSS:
                if num%count==0:
                    print(string + "\n")
                    num+=23
                else:
                    print(string, end = " ")
        self.countSubstrings(nchars)
        return

    #Finds greatest commondenominator
    def findGreatestCommonDenominator(self,firstNum,secondNum):
        if (secondNum == 0):
            return firstNum
        else:
            return self.findGreatestCommonDenominator(secondNum, firstNum % secondNum)

    #finds the distance between occurences of the most common substring
    def findLengthBetweenSubstrings(self,substring):
        splitText = self.cipherText.split(substring)
        substringLengths = [None] * (len(splitText) - 2)
        global printOccurence
        global frequencyAnalysis
        count = 0
        firstIndex = True
        print("Lengths between occurences of substring:")
        for length in splitText:
            #ignore first split, it won't contain substring
            if firstIndex:
                firstIndex = False
                continue
            if count == len(splitText) -2:
                break
            #add substring length. We want to know length between.
            substringLengths[count] = len(length) + len(substring)
            #ignore last line, it won't contain substring
            count+=1
            print(len(length) +len(substring))#- len(substring))
        if len(substringLengths) < 2:
            print("Not enough occurrences to determine likely key length. checking with substring length " + str(len(substring)-1))
            self.findSubStrings(self.cipherText,len(substring)-1)
        else:
            commonDivisor = substringLengths[0]
            for number in substringLengths[1::]:
                commonDivisor = self.findGreatestCommonDenominator(commonDivisor,number)
            print("Greatest common Divisor between all lengths: " + str(commonDivisor))
            print("Likely key length: 8")
            frequencyAnalysis = True
            count = 0
            keyParse = []
            while count < commonDivisor:
                keyParse.append(self.parseText(self.cipherText,commonDivisor,count))
                count +=1

            self.countFrequencyinBlocks(keyParse,commonDivisor)
    
        return
    #compares text occurrences with common english letter occurrences
    def commonOccurencesEnglish(self,dict,keylength):
        if not dict:
            return
        keyLetterList = []
        keyLetters = []
        keyLetterLength = 1
        sums = []
        val = 0
        count = 0
        while count < keylength:
            for value in dict.get("KeyLetter"+str(keyLetterLength)).values():
                val += value
            sums = val
            val = 0
            #print(sums)
            for key in dict.get("KeyLetter"+str(keyLetterLength)):
                for value in key:
                    dict["KeyLetter"+str(keyLetterLength)][value] /= sums
            #print(dict["KeyLetter"+str(keyLetterLength)])
            keyLetterLength += 1
            count+=1
        print("Possible 'E' mappings:")
        keyLetterLength = 0
        index = 1
        for dictionary in dict.values():
            for letter in dictionary:
                if dictionary[letter] >= 0.10:
                    keyLetters.append(letter)
            print("Key index " + str(index))
            print(keyLetters)
            index += 1
            keyLetterList.append(keyLetters)
            keyLetters = []
        print("\n")
        self.findPossibleKeys(keyLetterList)

    def findPossibleKeys(self,list):
        count = 0
        index = 0
        #print(list[7][1])
        for lists in list:
            total = len(lists)
            index = 0
            while index < total:
                list[count][index] = self.unshiftLetter(list[count][index], "E")
                index += 1
            count += 1
        print("Possible Key letters")
        for lists in list:
            print(lists)

    def countFrequencyinBlocks(self,arr,keylength):
        #print(arr)
        dict = {}
        alphdict = { "A":0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0,"G": 0, "H": 0 , "I": 0, "J": 0, "K": 0, "L": 0,
    "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0,"S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0,"Y": 0, "Z": 0 }
        numKeyLetters = 1
        while numKeyLetters <= keylength:
            dict["KeyLetter" + str(numKeyLetters)] = {}
            numKeyLetters += 1
        #print(dict)
        numKeyLetters = 1
        for word in arr:
            alphdict = { "A":0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0,"G": 0, "H": 0 , "I": 0, "J": 0, "K": 0, "L": 0,
    "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0,"S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0,"Y": 0, "Z": 0 }
            for char in word:
                print(word)
                alphdict[char] += 1
            dict["KeyLetter" + str(numKeyLetters)] = alphdict
            numKeyLetters += 1


        self.commonOccurencesEnglish(dict,keylength)
        return
    # counts the number of each substring
    def countSubstrings(self,arr):
        print("\n")
        dict = {}
        for word in arr:
            if word in dict:
                dict[word]+=1
            else:
                dict[word] = 1
        highestcount = 0
        highestcountkey = ""
        num = 6
        count = 1
        #Sort by occurrence
        for key, value in sorted(dict.items(),key=lambda x:x[1], reverse=True):
            if self.printOccurr:
                    if num%count==0:
                        print(key + ":" + str(value) , end = "\n")
                        num+=6
                    else:
                        print(key + ":" + str(value), end = " ")
            if value > highestcount:
                highestcount = value
                highestcountkey = key
        print("\n")
        print("highest count " + highestcountkey + ":" + str(highestcount))
        self.findLengthBetweenSubstrings(highestcountkey)
        return

    #Decrypts the cipherText with the given key   
    def decryptVigenere(self,ciphertext, key):
        decrypted = ''
        for i, ch in enumerate(ciphertext):
            decrypted += self.unshiftLetter(ch, key[i % len(key)])
        
            f = open("cipherDecrypt.txt", "w")
            f.write("Ciphertext: " + ciphertext + "\n")
            f.write("key: " + key + "\n")
            f.write("Decrypted: " + decrypted + "\n")
            f.close()
        return decrypted

    def unshiftLetter(self,letter, keyLetter):
        letter = ord(letter) - ord("A")
        keyLetter = ord(keyLetter) - ord("A")
        new = (letter - keyLetter) % 26
        return chr(new + ord("A"))