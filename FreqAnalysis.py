plaintext = "ethicslawanduniversitypolicieswarningtodefendasystemyouneedtobeabletothinklikeanattackerandthatincludesunderstandingtechniquesthatcanbeusedtocompromisesecurityhoweverusingthosetechniquesintherealworldmayviolatethelawortheuniversitysrulesanditmaybeunethicalundersomecircumstancesevenprobingforweaknessesmayresultinseverepenaltiesuptoandincludingexpulsioncivilfinesandjailtimeourpolicyincsfortyfourfortyisthatyoumustrespecttheprivacyandpropertyrightsofothersatalltimesorelseyouwillfailthecourseactinglawfullyandethicallyisyourresponsibilitycarefullyreadthecomputerfraudandabuseactcfaaoneofseveralfederallawsthatbroadlycriminalizescomputerintrusioniehackingunderstandwhatthelawprohibitsifindoubtwecanreferyoutoanattorneypleasereviewtheuniversitysacceptableusepolicyconcerningproperuseofinformationtechnologyaswellasthestudentcodeasmembersofthe"
#plaintext = "ETHICSLAWANDUNIVERSITYPOLICIESWARNINGTODEFENDASYSTEMYOUNEEDTOBEABLETOTHINKLIKEANATTACKERANDTHATINCLUDESUNDERSTANDINGTECHNIQUESTHATCANBEUSEDTOCOMPROMISESECURITYHOWEVERUSINGTHOSETECHNIQUESINTHEREALWORLDMAYVIOLATETHELAWORTHEUNIVERSITYSRULESANDITMAYBEUNETHICALUNDERSOMECIRCUMSTANCESEVENPROBINGFORWEAKNESSESMAYRESULTINSEVEREPENALTIESUPTOANDINCLUDINGEXPULSIONCIVILFINESANDJAILTIMEOURPOLICYINCSFORTYFOURFORTYISTHATYOUMUSTRESPECTTHEPRIVACYANDPROPERTYRIGHTSOFOTHERSATALLTIMESORELSEYOUWILLFAILTHECOURSEACTINGLAWFULLYANDETHICALLYISYOURRESPONSIBILITYCAREFULLYREADTHECOMPUTERFRAUDANDABUSEACTCFAAONEOFSEVERALFEDERALLAWSTHATBROADLYCRIMINALIZESCOMPUTERINTRUSIONIEHACKINGUNDERSTANDWHATTHELAWPROHIBITSIFINDOUBTWECANREFERYOUTOANATTORNEYPLEASEREVIEWTHEUNIVERSITYSACCEPTABLEUSEPOLICYCONCERNINGPROPERUSEOFINFORMATIONTECHNOLOGYASWELLASTHESTUDENTCODEASMEMBERSOFTHE"
relativeFreq = { "A": .08167, "B": .01492, "C": .02782, "D": .04253, "E": .12702, "F": .02228,
"G": .02015, "H": .06094, "I": .06966, "J": .00153, "K": .00772, "L": .04025,
"M": .02406, "N": .06749, "O": .07507, "P": .01929, "Q": .00095, "R": .05987,
"S": .06327, "T": .09056, "U": .02758, "V": .00978, "W": .02360, "X": .00150,
"Y": .01974, "Z": .00074 }


def findSubStrings(text,n):

    #parse for every n character word that exists
    nchars = [text[i:n+i] for i in range(0,len(text),n)]

    #print(nchars,end = " ")
    return countSubstrings(nchars) 

def parseText(text,Length,start):
    #parse original ciphertext into blocks based on keyLength
    newTxt = text[start:len(text):Length]

    #print(newText)
    return newTxt

def countSubstrings(arr):
    dict = { "A":0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0,
"G": 0, "H": 0 , "I": 0, "J": 0, "K": 0, "L": 0,
"M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0,
"S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0,
"Y": 0, "Z": 0 }

    newText = ''
    for word in arr:
        newText+=word
        if word in dict:
            dict[word]+=1
        else:
            dict[word] = 1
    return getFrequencies(dict,newText)

def getFrequencies(dict,text):
    for key in dict:
        dict[key] = dict[key]/len(text)
    #print(text)
    #print(sorted(dict.items(),key=lambda x:x[1], reverse=True), end = "\n")
    #print("\n")
    return getpopulationVariance(dict)

#N = 26, 
# small x = a given frequency for a letter
# mean = 1/26
def getpopulationVariance(dict):
    variance = 0.0
    mean = getMean(dict)
    sum = 0.0
    for letter in dict:
        sum+= (dict[letter]  - mean)**2.0
    variance = (1.0/26.0) * sum
    return variance
#encryptVigeneres text with vigenere

def getMean(data):
    sum = 0.0
    for key in data:
        sum += data[key]
    sum = sum/26
    return sum

def freqAnalysisBlocks(arr,keyLength):
    mean = 0
    count = 0
    while count < keyLength:
        mean += findSubStrings(parseText(arr,keyLength,count),1)
        count += 1
    mean  = mean/keyLength
    count = 0
    print("{:.4E}".format(mean))
#relative letter freqs in English
variance = getpopulationVariance(relativeFreq)
print("Relative Freq population variance")
print("{:.4E}".format(variance))
print("\n")

print("Given plaintext population variance")
print("{:.4E}".format(findSubStrings(plaintext,1)))
print("\n")

#yz
key = "YZ"
YZ = encryptVigenere(plaintext, key)
#print(YZ)
print("YZ")
#print(YZ)
print("{:.4E}".format(findSubStrings(YZ,1)))
#xyz
key = "XYZ"
XYZ = encryptVigenere(plaintext, key)
print("XYZ")
#print(XYZ)
print("{:.4E}".format(findSubStrings(XYZ,1)))
# wxyz 
key = "WXYZ"
WXYZ = encryptVigenere(plaintext, key)
print("WXYZ")
#print(WXYZ)
print("{:.4E}".format(findSubStrings(WXYZ,1)))
# vwxyz 
key = "VWXYZ"
VWXYZ = encryptVigenere(plaintext, key)
print("VWXYZ")
#print(VWXYZ)
print("{:.4E}".format(findSubStrings(VWXYZ,1)))
# uvwxyz,
key = "UVWXYZ"
UVWXYZ = encryptVigenere(plaintext, key)
print("UVWXYZ")
#print(UVWXYZ)
print("{:.4E}".format(findSubStrings(UVWXYZ,1)))
print("\n")

#yz
key = "YZ"
YZ = encryptVigenere(plaintext, key)
#print(YZ)
freqAnalysisBlocks(YZ,2)
#xyz
key = "XYZ"
XYZ = encryptVigenere(plaintext, key)
freqAnalysisBlocks(XYZ,3)
# wxyz 
key = "WXYZ"
WXYZ = encryptVigenere(plaintext, key)
freqAnalysisBlocks(WXYZ,4)
# vwxyz 
key = "VWXYZ"
VWXYZ = encryptVigenere(plaintext, key)
freqAnalysisBlocks(VWXYZ,5)
# uvwxyz,
key = "UVWXYZ"
UVWXYZ = encryptVigenere(plaintext, key)
freqAnalysisBlocks(UVWXYZ,6)
print("\n")

key = "UVWXYZ"
UVWXYZ = encryptVigenere(plaintext, key)
print("using UVWXYZ encryption with all the other keys")
print("key size 2")
freqAnalysisBlocks(UVWXYZ,2)
print("key size 3")
freqAnalysisBlocks(UVWXYZ,3)
print("key size 4")
freqAnalysisBlocks(UVWXYZ,4)
print("key size 5")
freqAnalysisBlocks(UVWXYZ,5)
print("\n")




