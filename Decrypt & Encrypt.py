MAX_KEY_SIZE = 26



def getMode():

    while True:
        print("Please choose following options:\n")
        print("1 = Encrypt the string.\n")
        print("2 = Decrypt the string.\n")
        mode = input().lower()
        
        if(mode == "1"):
             return("e")
        if(mode == "2"):
             return("d")
        else:
            print("Enter either `1` for encrypt or `2` for decrypt.")



def getMessage():
    print('Enter your message:')
    return input()




def getTranslatedMessage(mode, message, key):

    if mode[0] == 'd':
        key = 3
        translated = ''


    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num -= key


            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated



mode = getMode()
message = getMessage()
key = 3



print('Your translated text is:')
print(getTranslatedMessage(mode, message, key))
