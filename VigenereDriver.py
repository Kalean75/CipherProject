ciphertext = "ELFMASBQDXISZMNMHIBFEFQIMEUVNGLMLRETHAZAQPPDOTEGDEDONLYVZJNWHCKBLPPQWDQZZGFFUKDWCIXWPZKKSIDYBGBATBUMOWFMYGFBPKYVELFHRHBMDMESJLQMZVHSXMCPDIOWKJKLOVFGOWCBSIOOPAYVDEZWJYKORVFGOAYVHMMZJGDAEEORWYKQYWUYQOKQEXISZMNMCIUINFCBZLJGWHKZEQFBPORMCIVDKFOVEISWJYKVOGMCOAXOELFRKGBPPMTDNGWXEPZUNSLJPHCMPOYUPRXVKXYZNIIWIAXBZXISXSDPCSPAWFNASSWSDACPPEEWJLRMESJZALDPPCESISXLXSOSUGGMOXPXWUUQPXSSAZYZYWBMEFQBSEUHDWNCOITKEXOJFROMYDKQXIEVAOKARSPRBGBQEFFTKJOWYIPTPZOBSYHGQJSVLXFGKFDPPHVRAKBCRWBMEFQMGISHDMCBZHFOZTOIEWMSXGGAVMCSSAVLPVFRPZOLFHFQKFFQYGFGPZOUELBHPZOGSEWSPZOECSOULWBAZRBGDWSAYXNONJSMOEORYSXBASTGETVGASTGAKCBSIBAKMXBZJNCJWIBSIZOOCPWCPPCGAXOLVPIJVDPPJJFOLDPFKSSWDSHPWUVAQRIGINOZWKUTWUOGWKVOQVGPZKDPXISSJYVRPFPKOCSTVFUWJNTPWTHDWIJCIBYKFOWQLJGXSDPCSPAPAVMDFFTKJOTPEWWJYDPPHVRAUKTWWBTPWBBSINGWQSVREUZASCBTENVKMCMMVPYAFDPPHVRAEOMEWVDSADPSMTPKOVQYKUSWEKBELFZKUKTLPMSUSXLEEMYOLYBSINOXGEBSMTJEGVMYXFBYGEVEISKWDDMCWPPYZKSCIBQPKGQELBBCWBIYHWSJYOIYGFCJZSAXMORKXDMYWQSWCSVRSGVEKDQXITSNNOLTRWWALXIXXPFADKBPXPHDWSADYFGHGGETXUSZLRMZHPFAVYVLPERKFXGVISOXSDAZWPTPWXMYXFFEFQKZRWSNKKBTSOGDSVNHEZHDJYCRLQWLWCQYFVHEKZZZQQHHQDWWHZCQSBMZYUCBQYCCIMSIWXBMCXOHLOZ"
printSubstrings = False
printOccurence = False
customCipher = False
frequencyAnalysis = False

    # Help
def Help():
        print("Commands:")
        print("-h for help")
        print("-pss to print all the substrings")
        print("-po to print all substrings with count greater than 1")
        print("-fss to search the text for the highest occuring substring")
        print("-vdc to decrypt message, with a known key")
        print("-cc to input a custom cipher: otherwise uses a built in one")
        print("-f to show current flags")
        print("-ec to encrypt a cipher with the given key")
        return
    # current active flags


def Flags():
        print("FLAGS")
        print("Print All substrings of size: " + str(printSubstrings))
        print("Print occurrences of substrings of size greater than 1: " +
              str(printOccurence))
        print("Using a custom cipher: " + str(customCipher))
        return

#substring size
def inputss(self):
    while(True):
        try:
            n = int(input("Enter size of substrings to search for "))
            if n < 3:
                print("Minimum size must be greater than or equal to 3")
                continue
            break
        except ValueError:
            print("Please enter a valid Integer\n")
    self.findSubStrings(ciphertext,n)

def main():
    import VigenereDecrypt as VD
    import VigenereEncrypt as VE

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
                decryptedmessage= VD.VigenereDecrypt.decryptVigenere(newCipher,keyString)
            else:
                keyString = input("Enter the key ")
                decryptedmessage= VD.VigenereDecrypt.decryptVigenere(ciphertext,keyString)
                print(decryptedmessage)
                break
        elif string == "-ec":
            MessageToEncrypt = input("enter your message ")
            keyString = input("Enter the key ")
            encryptedmessage = VE.encryptVigenere(MessageToEncrypt,keyString)
            print("Original Message ", MessageToEncrypt)
            print("Encrypted Message ", encryptedmessage)
        else:
            print("Please enter a valid Command")
if __name__ == "__main__":
    main()
