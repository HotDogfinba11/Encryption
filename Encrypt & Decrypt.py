import sys

MAX_KEY_SIZE = 26



def mode():

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

def again():
    print("Do you want to go again?")
    print("1 = yes")
    play = input("2 = no")


    if(play == "1"):
        mode()
    if(play == "2"):
        print("Have fun")
    else:
        print("Enter either `1` to have another go or `2` to close the program.")

def message():
    print("Please enter a string:\n")
    return input()






def translatedMessage(mode, message, key):

    if mode[0] == "d":
        key = 3
        translated = ''
    else:
        key =-3
    translated = ''


    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num -= key


            if symbol.isupper():
                if num > ord("Z"):
                    num -= 26
                elif num < ord("A"):
                    num += 26
            elif symbol.islower():
                if num > ord("z"):
                    num -= 26
                elif num < ord("a"):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated



mode = mode()
message = message()
key = 3



print('Your translated string is:')
print(translatedMessage(mode, message, key))
again()


