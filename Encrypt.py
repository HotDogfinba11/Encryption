from time import sleep
import sys

def encrypt(string, shift): #creates `encrpyt` function calling for string and shift value
 
  cipher = '' #creating `cipher` variable
  for char in string: #reads each character
    if char == ' ':
      cipher = cipher + char #leave it as a space
    elif  char.isupper(): #If character is upper case
      cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65) #getting the order of the characters in ASCII shifting them by the shift value
    else:
      cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97) #divides characters by 26 and adds 97 ASCII value
  
  return cipher #new value for cipher


def decrypt(string, shift): #creates `encrpyt` function calling for string and shift value
 
  cipher = '' #creating `cipher` variable
  for char in string: #reads each character
    if char == ' ':
      cipher = cipher + char #leave it as a space
    elif  char.isupper(): #If character is upper case
      cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65) #getting the order of the characters in ASCII shifting them by the shift value
    else:
      cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97) #divides characters by 26 and adds 97 ASCII value
  
  return cipher #new value for cipher


def emessage():
    text = input("Enter string: ") #asks for string
    s = int(input("Enter shift number: ")) #how much down ASCII the characters will move
    print("\nOriginal string: ", text) #prints text variable]
    sleep(0.6)
    print("After encryption: ", encrypt(text, s)) #prints encrypted string using the shift value
    sleep(1)
    

def dmessage():
    text = input("Enter string: ") #asks for string
    s = int(input("Enter shift number: ")) #how much down ASCII the characters will move
    print("\nOriginal string: ", text) #prints text variable
    sleep(0.6)
    print("After decryption: ", decrypt(text, s)) #prints encrypted string using the shift value
    sleep(1)


def mode():
    while True:
        print("\nPlease choose from the following options:\n") #Asks to choose an option
        sleep(0.8)
        print("1 = Encrypt the string.\n") #option 1
        sleep(0.8)
        print("2 = Decrypt the string.\n") #option 2
        sleep(0.8)
        print("3 = Exit the program.\n") #option 3
        mode = input().lower() #assigning input to mode and lower casing it
        
        if(mode == "1"): #
            dmessage() #runs `dmessage` function
        elif(mode == "2"):
            emessage() #runs `emssage` function
        elif(mode == "3"):
            sys.exit() #quits program
        else:
            print("Enter either `1` for encrypt or `2` for decrypt or `3` to exit.") #if criteria is matches


mode() #runs `mode` function first 
