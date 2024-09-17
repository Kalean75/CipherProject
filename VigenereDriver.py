import tkinter as tk
import tkinter.font as tkFont

# ciphertext = "ELFMASBQDXISZMNMHIBFEFQIMEUVNGLMLRETHAZAQPPDOTEGDEDONLYVZJNWHCKBLPPQWDQZZGFFUKDWCIXWPZKKSIDYBGBATBUMOWFMYGFBPKYVELFHRHBMDMESJLQMZVHSXMCPDIOWKJKLOVFGOWCBSIOOPAYVDEZWJYKORVFGOAYVHMMZJGDAEEORWYKQYWUYQOKQEXISZMNMCIUINFCBZLJGWHKZEQFBPORMCIVDKFOVEISWJYKVOGMCOAXOELFRKGBPPMTDNGWXEPZUNSLJPHCMPOYUPRXVKXYZNIIWIAXBZXISXSDPCSPAWFNASSWSDACPPEEWJLRMESJZALDPPCESISXLXSOSUGGMOXPXWUUQPXSSAZYZYWBMEFQBSEUHDWNCOITKEXOJFROMYDKQXIEVAOKARSPRBGBQEFFTKJOWYIPTPZOBSYHGQJSVLXFGKFDPPHVRAKBCRWBMEFQMGISHDMCBZHFOZTOIEWMSXGGAVMCSSAVLPVFRPZOLFHFQKFFQYGFGPZOUELBHPZOGSEWSPZOECSOULWBAZRBGDWSAYXNONJSMOEORYSXBASTGETVGASTGAKCBSIBAKMXBZJNCJWIBSIZOOCPWCPPCGAXOLVPIJVDPPJJFOLDPFKSSWDSHPWUVAQRIGINOZWKUTWUOGWKVOQVGPZKDPXISSJYVRPFPKOCSTVFUWJNTPWTHDWIJCIBYKFOWQLJGXSDPCSPAPAVMDFFTKJOTPEWWJYDPPHVRAUKTWWBTPWBBSINGWQSVREUZASCBTENVKMCMMVPYAFDPPHVRAEOMEWVDSADPSMTPKOVQYKUSWEKBELFZKUKTLPMSUSXLEEMYOLYBSINOXGEBSMTJEGVMYXFBYGEVEISKWDDMCWPPYZKSCIBQPKGQELBBCWBIYHWSJYOIYGFCJZSAXMORKXDMYWQSWCSVRSGVEKDQXITSNNOLTRWWALXIXXPFADKBPXPHDWSADYFGHGGETXUSZLRMZHPFAVYVLPERKFXGVISOXSDAZWPTPWXMYXFFEFQKZRWSNKKBTSOGDSVNHEZHDJYCRLQWLWCQYFVHEKZZZQQHHQDWWHZCQSBMZYUCBQYCCIMSIWXBMCXOHLOZ"
# defKey = "LEBOWSKI"
printSubstrings = False
printOccurence = False
customCipher = False
frequencyAnalysis = False
decrypt = False
encrypt = False
cipherText = " "
key = " "


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
    print(
        "Print occurrences of substrings of size greater than 1: " + str(printOccurence)
    )
    print("Using a custom cipher: " + str(customCipher))
    return


# substring size
def inputss(VD, cipherText):
    while True:
        try:
            n = int(input("Enter size of substrings to search for "))
            if n < 3:
                print("Minimum size must be greater than or equal to 3")
                continue
            break
        except ValueError:
            print("Please enter a valid Integer\n")
    VD.findSubStrings(cipherText, n)


def main():
    Help()
    Flags()
    CommandMenu(
        printSubstrings,
        printOccurence,
        True,
        frequencyAnalysis,
        False,
        decrypt,
        encrypt,
    )


def CommandMenu(pss, pO, cc, fa, ct, vdc, vec):
    from VigenereDecrypt import Decrypt as VD
    from VigenereEncrypt import Encrypt as VE

    f = open("CipherProject\cipher.txt")
    # ciphertextList = f.readlines()
    # ciphertext = ciphertextList[2].strip()
    # defKey = ciphertextList[1].strip()
    global cipherText
    global key
    if cipherText == " ":
        cipherText = "ELFMASBQDXISZMNMHIBFEFQIMEUVNGLMLRETHAZAQPPDOTEGDEDONLYVZJNWHCKBLPPQWDQZZGFFUKDWCIXWPZKKSIDYBGBATBUMOWFMYGFBPKYVELFHRHBMDMESJLQMZVHSXMCPDIOWKJKLOVFGOWCBSIOOPAYVDEZWJYKORVFGOAYVHMMZJGDAEEORWYKQYWUYQOKQEXISZMNMCIUINFCBZLJGWHKZEQFBPORMCIVDKFOVEISWJYKVOGMCOAXOELFRKGBPPMTDNGWXEPZUNSLJPHCMPOYUPRXVKXYZNIIWIAXBZXISXSDPCSPAWFNASSWSDACPPEEWJLRMESJZALDPPCESISXLXSOSUGGMOXPXWUUQPXSSAZYZYWBMEFQBSEUHDWNCOITKEXOJFROMYDKQXIEVAOKARSPRBGBQEFFTKJOWYIPTPZOBSYHGQJSVLXFGKFDPPHVRAKBCRWBMEFQMGISHDMCBZHFOZTOIEWMSXGGAVMCSSAVLPVFRPZOLFHFQKFFQYGFGPZOUELBHPZOGSEWSPZOECSOULWBAZRBGDWSAYXNONJSMOEORYSXBASTGETVGASTGAKCBSIBAKMXBZJNCJWIBSIZOOCPWCPPCGAXOLVPIJVDPPJJFOLDPFKSSWDSHPWUVAQRIGINOZWKUTWUOGWKVOQVGPZKDPXISSJYVRPFPKOCSTVFUWJNTPWTHDWIJCIBYKFOWQLJGXSDPCSPAPAVMDFFTKJOTPEWWJYDPPHVRAUKTWWBTPWBBSINGWQSVREUZASCBTENVKMCMMVPYAFDPPHVRAEOMEWVDSADPSMTPKOVQYKUSWEKBELFZKUKTLPMSUSXLEEMYOLYBSINOXGEBSMTJEGVMYXFBYGEVEISKWDDMCWPPYZKSCIBQPKGQELBBCWBIYHWSJYOIYGFCJZSAXMORKXDMYWQSWCSVRSGVEKDQXITSNNOLTRWWALXIXXPFADKBPXPHDWSADYFGHGGETXUSZLRMZHPFAVYVLPERKFXGVISOXSDAZWPTPWXMYXFFEFQKZRWSNKKBTSOGDSVNHEZHDJYCRLQWLWCQYFVHEKZZZQQHHQDWWHZCQSBMZYUCBQYCCIMSIWXBMCXOHLOZ"
        key = "LEBOWSKI"
    printSubstrings = pss
    printOccurence = pO
    customCipher = cc
    frequencyAnalysis = fa
    decrypt = vdc
    encrypt = vec
    while True:
        # string = sys.stdin.read().strip
        if pO:  # string=="-po":
            if not printOccurence:
                printOccurence = True
            else:
                printOccurence = False
                print(
                    "Print occurrences of substrings of size greater than 1: "
                    + str(printOccurence)
                )
        if pss:  # string=="-pss":
            if not printSubstrings:
                printSubstrings = True
            else:
                printSubstrings = False
                print("Print All substrings of size: " + str(printSubstrings))
        # elif h: string=="-h":
        #             Help()
        # elif string=="-fss":
        #             Vd = VD(printSS = printSubstrings,printOccurrence = printOccurence, frequencyAnalysis = frequencyAnalysis, cipherText=ciphertext)
        #             inputss(Vd,ciphertext)
        #             break
        if f:  # string=="-f":
            Flags()
        if cc:  # string=="-cc":
            if not customCipher:
                customCipher = True
                print("Using a custom cipher: " + str(customCipher))
                newCipher = cleanCipher(input("enter your custom cipher: "))
            else:
                customCipher = False
                print("Using a default cipher: " + str(customCipher))
        if decrypt is True:  # string=="-vdc":
            print("Decrypting")
            Vd = VD(
                printSS=printSubstrings,
                printOccurrence=printOccurence,
                frequencyAnalysis=frequencyAnalysis,
                cipherText=cipherText,
            )
            if customCipher:
                print("Cipher is , ", newCipher)
                keyString = input("Enter the key ")
                decryptedmessage = Vd.decryptVigenere(
                    ciphertext=newCipher, key=keyString
                )
                print(decryptedmessage)
                break
            else:
                cipherText = cleanCipher(cipherText)
                keyString = key
                # keyString = input("Enter the key ")
                decryptedmessage = Vd.decryptVigenere(
                    ciphertext=cipherText, key=keyString
                )
                print(decryptedmessage)
                break
        elif encrypt is True:  # string == "-ec":
            print("Encrypting")
            Ve = VE()
            # MessageToEncrypt = cleanCipher(input("enter your message "))
            MessageToEncrypt = cleanCipher(cipherText)
            # keyString = input("Enter the key ")
            keyString = key
            encryptedmessage = Ve.encryptVigenere(
                ciphertext=MessageToEncrypt, key=keyString
            )
            print("Original Message ", MessageToEncrypt)
            print("Encrypted Message ", encryptedmessage)
        else:
            print("Please enter a valid Command")
        break


def cleanCipher(cipherText):
    newText = ""
    for i in cipherText:
        if i != " ":
            newText += i
    if len(newText) > 1:
        return newText
    return cipherText


class App:
    def __init__(self, root):
        self.selectedOption = tk.IntVar()
        # setting title
        root.title("Cipher App")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # GMessage_192=tk.Message(root)
        # ft = tkFont.Font(family='Times',size=10)
        # GMessage_192["font"] = ft
        # GMessage_192["fg"] = "#333333"
        # GMessage_192["justify"] = "center"
        # GMessage_192["text"] = ""
        # GMessage_192.place(x=50,y=20,width=489,height=174)

        # Message
        self.GLineEdit_593 = tk.Entry(root)
        self.GLineEdit_593["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        self.GLineEdit_593["font"] = ft
        self.GLineEdit_593["fg"] = "#333333"
        self.GLineEdit_593["justify"] = "center"
        self.GLineEdit_593["text"] = "Message"
        self.GLineEdit_593.place(x=180, y=220, width=249, height=30)

        # Key
        self.GLineEdit_713 = tk.Entry(root)
        self.GLineEdit_713["borderwidth"] = "1px"
        ft = tkFont.Font(family="Times", size=10)
        self.GLineEdit_713["font"] = ft
        self.GLineEdit_713["fg"] = "#333333"
        self.GLineEdit_713["justify"] = "center"
        self.GLineEdit_713["text"] = "Key"
        self.GLineEdit_713.place(x=180, y=250, width=250, height=30)

        keyLabel = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        keyLabel["font"] = ft
        keyLabel["fg"] = "#333333"
        keyLabel["justify"] = "center"
        keyLabel["text"] = "Key"
        keyLabel.place(x=110, y=250, width=70, height=25)

        textLabel = tk.Label(root)
        ft = tkFont.Font(family="Times", size=10)
        textLabel["font"] = ft
        textLabel["fg"] = "#333333"
        textLabel["justify"] = "center"
        textLabel["text"] = "Text"
        textLabel.place(x=110, y=220, width=70, height=25)

        encryptRadio = tk.Radiobutton(root, variable=self.selectedOption, value=1)
        ft = tkFont.Font(family="Times", size=10)
        encryptRadio["font"] = ft
        encryptRadio["fg"] = "#333333"
        encryptRadio["justify"] = "center"
        encryptRadio["text"] = "Encrypt"
        encryptRadio.place(x=170, y=290, width=85, height=25)
        encryptRadio["command"] = self.encryptRadio_Command

        decryptRadio = tk.Radiobutton(root, variable=self.selectedOption, value=2)
        ft = tkFont.Font(family="Times", size=10)
        decryptRadio["font"] = ft
        decryptRadio["fg"] = "#333333"
        decryptRadio["justify"] = "center"
        decryptRadio["text"] = "Decrypt"
        decryptRadio.place(x=360, y=290, width=85, height=25)
        decryptRadio["command"] = self.decryptRadio_Command

        GoButton = tk.Button(root)
        GoButton["bg"] = "#f0f0f0"
        ft = tkFont.Font(family="Times", size=10)
        GoButton["font"] = ft
        GoButton["fg"] = "#000000"
        GoButton["justify"] = "center"
        GoButton["text"] = "Go!"
        GoButton.place(x=270, y=430, width=70, height=25)
        GoButton["command"] = self.GoButton_command

        CCiphCheckBox = tk.Checkbutton(root)
        ft = tkFont.Font(family="Times", size=10)
        CCiphCheckBox["font"] = ft
        CCiphCheckBox["fg"] = "#333333"
        CCiphCheckBox["justify"] = "center"
        CCiphCheckBox["text"] = "Custom Cipher"
        CCiphCheckBox.place(x=60, y=340, width=109, height=30)
        CCiphCheckBox["offvalue"] = "0"
        CCiphCheckBox["onvalue"] = "1"
        CCiphCheckBox["command"] = self.CCiphCheckBox_command

        PSSCheckBox = tk.Checkbutton(root)
        ft = tkFont.Font(family="Times", size=10)
        PSSCheckBox["font"] = ft
        PSSCheckBox["fg"] = "#333333"
        PSSCheckBox["justify"] = "center"
        PSSCheckBox["text"] = "Print SubStrings"
        PSSCheckBox.place(x=190, y=340, width=128, height=30)
        PSSCheckBox["offvalue"] = "0"
        PSSCheckBox["onvalue"] = "1"
        PSSCheckBox["command"] = self.PSSCheckBox_command

        FSSCheckBox = tk.Checkbutton(root)
        ft = tkFont.Font(family="Times", size=10)
        FSSCheckBox["font"] = ft
        FSSCheckBox["fg"] = "#333333"
        FSSCheckBox["justify"] = "center"
        FSSCheckBox["text"] = "Find SubStrings"
        FSSCheckBox.place(x=340, y=340, width=133, height=30)
        FSSCheckBox["offvalue"] = "0"
        FSSCheckBox["onvalue"] = "1"
        FSSCheckBox["command"] = self.FSSCheckBox_command

        FKeyCheckBox = tk.Checkbutton(root)
        ft = tkFont.Font(family="Times", size=10)
        FKeyCheckBox["font"] = ft
        FKeyCheckBox["fg"] = "#333333"
        FKeyCheckBox["justify"] = "center"
        FKeyCheckBox["text"] = "Find Key"
        FKeyCheckBox.place(x=510, y=340, width=70, height=25)
        FKeyCheckBox["offvalue"] = "0"
        FKeyCheckBox["onvalue"] = "1"
        FKeyCheckBox["command"] = self.FKeyCheckbox_command

    def encryptRadio_Command(self):
        global encrypt
        if encrypt is False:
            encrypt = True
        else:
            encrypt = False

    def decryptRadio_Command(self):
        global decrypt
        if decrypt is False:
            decrypt = True
        else:
            decrypt = False

    def GoButton_command(self):
        global cipherText
        cipherText = self.GLineEdit_593.get()
        global key
        key = self.GLineEdit_713.get()
        CommandMenu(
            printSubstrings,
            printOccurence,
            customCipher,
            frequencyAnalysis,
            False,
            decrypt,
            encrypt,
        )

    def CCiphCheckBox_command(self):
        global customCipher
        if customCipher is True:
            customCipher = False
        else:
            customCipher = True

    def PSSCheckBox_command(self):
        global printSubstrings
        if printSubstrings is True:
            printSubstrings = False
        else:
            printSubstrings = True

    def FSSCheckBox_command(self):
        print("command")

    def FKeyCheckbox_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
