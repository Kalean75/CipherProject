import re
ciphertext = "ELFMASBQDXISZMNMHIBFEFQIMEUVNGLMLRETHAZAQPPDOTEGDEDONLYVZJNWHCKBLPPQWDQZZGFFUKDWCIXWPZKKSIDYBGBATBUMOWFMYGFBPKYVELFHRHBMDMESJLQMZVHSXMCPDIOWKJKLOVFGOWCBSIOOPAYVDEZWJYKORVFGOAYVHMMZJGDAEEORWYKQYWUYQOKQEXISZMNMCIUINFCBZLJGWHKZEQFBPORMCIVDKFOVEISWJYKVOGMCOAXOELFRKGBPPMTDNGWXEPZUNSLJPHCMPOYUPRXVKXYZNIIWIAXBZXISXSDPCSPAWFNASSWSDACPPEEWJLRMESJZALDPPCESISXLXSOSUGGMOXPXWUUQPXSSAZYZYWBMEFQBSEUHDWNCOITKEXOJFROMYDKQXIEVAOKARSPRBGBQEFFTKJOWYIPTPZOBSYHGQJSVLXFGKFDPPHVRAKBCRWBMEFQMGISHDMCBZHFOZTOIEWMSXGGAVMCSSAVLPVFRPZOLFHFQKFFQYGFGPZOUELBHPZOGSEWSPZOECSOULWBAZRBGDWSAYXNONJSMOEORYSXBASTGETVGASTGAKCBSIBAKMXBZJNCJWIBSIZOOCPWCPPCGAXOLVPIJVDPPJJFOLDPFKSSWDSHPWUVAQRIGINOZWKUTWUOGWKVOQVGPZKDPXISSJYVRPFPKOCSTVFUWJNTPWTHDWIJCIBYKFOWQLJGXSDPCSPAPAVMDFFTKJOTPEWWJYDPPHVRAUKTWWBTPWBBSINGWQSVREUZASCBTENVKMCMMVPYAFDPPHVRAEOMEWVDSADPSMTPKOVQYKUSWEKBELFZKUKTLPMSUSXLEEMYOLYBSINOXGEBSMTJEGVMYXFBYGEVEISKWDDMCWPPYZKSCIBQPKGQELBBCWBIYHWSJYOIYGFCJZSAXMORKXDMYWQSWCSVRSGVEKDQXITSNNOLTRWWALXIXXPFADKBPXPHDWSADYFGHGGETXUSZLRMZHPFAVYVLPERKFXGVISOXSDAZWPTPWXMYXFFEFQKZRWSNKKBTSOGDSVNHEZHDJYCRLQWLWCQYFVHEKZZZQQHHQDWWHZCQSBMZYUCBQYCCIMSIWXBMCXOHLOZ"
printSubstrings = False
printOccurence = False
customCipher = False
frequencyAnalysis = False
# Print text
def printtext(text):
    print(text)

def parseText(text,keyLength,start):
    #splitText = (text[0+i:keyLength+i] for i in range(0, len(text), keyLength))
    #parse original ciphertext into blocks based on keyLength
    newText = text[start:len(text):keyLength]
    return newText
#finds substrings of length n in string text
def findSubStrings(text,n):
    #parse for every n character word that exists
    nchars = [text[i:i+n] for i in range(0,len(text),1)]
    count = 0
    num = 23
    for string in nchars:
        count+=1
        if printSubstrings:
            if num%count==0:
                print(string + "\n")
                num+=23
            else:
                print(string, end = " ")
    countSubstrings(nchars)
    return

#Finds greatest commondenominator
def findGreatestCommonDenominator(firstNum,secondNum):
    if (secondNum == 0):
        return firstNum
    else:
         return findGreatestCommonDenominator(secondNum, firstNum % secondNum)

#finds the distance between occurences of the most common substring
def findLengthBetweenSubstrings(substring):
    splitText = ciphertext.split(substring)
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
        findSubStrings(ciphertext,len(substring)-1)
    else:
        commonDivisor = substringLengths[0]
        for number in substringLengths[1::]:
            commonDivisor = findGreatestCommonDenominator(commonDivisor,number)
        print("Greatest common Divisor between all lengths: " + str(commonDivisor))
        print("Likely key length: 8")
        frequencyAnalysis = True
        count = 0
        keyParse = []
        while count < commonDivisor:
            keyParse.append( parseText(ciphertext,commonDivisor,count))
            count +=1

        countFrequencyinBlocks(keyParse,commonDivisor)
 
    return
#compares text occurrences with common english letter occurrences
def commonOccurencesEnglish(dict,keylength):
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
    findPossibleKeys(keyLetterList)

def findPossibleKeys(list):
    count = 0
    index = 0
    #print(list[7][1])
    for lists in list:
        total = len(lists)
        index = 0
        while index < total:
            list[count][index] = unshiftLetter(list[count][index], "E")
            index += 1
        count += 1
    print("Possible Key letters")
    for lists in list:
        print(lists)

def countFrequencyinBlocks(arr,keylength):
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
            alphdict[char] += 1
        dict["KeyLetter" + str(numKeyLetters)] = alphdict
        numKeyLetters += 1
    #print(dict)
    #print(dict)
    commonOccurencesEnglish(dict,keylength)
    return
# counts the number of each substring
def countSubstrings(arr):
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
        if printOccurence:
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
    findLengthBetweenSubstrings(highestcountkey)
    return

#Decrypts the cipherText with the given key   
def decryptVigenere(ciphertext, key):
    decrypted = ''
    for i, ch in enumerate(ciphertext):
        decrypted += unshiftLetter(ch, key[i % len(key)])
    return decrypted

def unshiftLetter(letter, keyLetter):
    letter = ord(letter) - ord("A")
    keyLetter = ord(keyLetter) - ord("A")
    new = (letter - keyLetter) % 26
    return chr(new + ord("A"))
#Help
def Help():
    print("Commands:")
    print("-h for help")
    print("-pss to print all the substrings")
    print("-po to print all substrings with count greater than 1")
    print("-fss to search the text for the highest occuring substring")
    print("-vdc to decrypt message, with a known key")
    print("-cc to input a custom cipher: otherwise uses a built in one")
    print("-f to show current flags")
    print()
    return
#current active flags
def Flags():
    print("FLAGS")
    print("Print All substrings of size: " + str(printSubstrings))
    print("Print occurrences of substrings of size greater than 1: " + str(printOccurence))
    print("Using a custom cipher: " + str(customCipher))
    return
#substring size
def inputss():
    while(True):
        try:
            n = int(input("Enter size of substrings to search for "))
            if n < 3:
                print("Minimum size must be greater than or equal to 3")
                continue
            break
        except ValueError:
            print("Please enter a valid Integer\n")
    findSubStrings(ciphertext,n)

 #Encrypts a vigenere.
def encryptVigenere(ciphertext, key):
    ciphertext = ciphertext.upper()
    encrypted = ''
    for i, ch in enumerate(ciphertext):
        encrypted += shiftLetter(ch, key[i % len(key)])
    return encrypted

def shiftLetter(letter, keyLetter):
    letter = ord(letter) - ord("A")
    keyLetter = ord(keyLetter) - ord("A")
    new = (letter + keyLetter) % 26
    return chr(new + ord("A"))


Help()
Flags()
while(True):
        newCipher = ""
        string = input()
        if string=="-po":
            if not printOccurence:
                printOccurence = True
            else:
                printOccurence = False
            print("Print occurrences of substrings of size greater than 1: " + str(printOccurence))
        if string=="-pss":
            if not printSubstrings:
                printSubstrings = True
            else:
                printSubstrings = False
            print("Print All substrings of size: " + str(printSubstrings))
        elif string=="-h":
            Help()
        elif string=="-fss":
            inputss()
            break
        elif string=="-f":
            Flags()
        elif string=="-cc":
            if not customCipher:
                customCipher = True
                print("Using a custom cipher: " + str(customCipher))
                newCipher = input("enter your custom cipher: ")
            else:
                customCipher = False
                print("Using a custom cipher: " + str(customCipher))
        elif string=="-vdc":
            if(customCipher):
                print("Cipher is , ", customCipher)
                keyString = input("Enter the key ")
                decryptedmessage= decryptVigenere(newCipher,keyString)
            else:
                keyString = input("Enter the key ")
                decryptedmessage= decryptVigenere(ciphertext,keyString)
            print(decryptedmessage)
            break
        else:
            print("Please enter a valid Command")
