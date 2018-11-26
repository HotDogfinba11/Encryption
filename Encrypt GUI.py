from tkinter import *

class Sezar(Frame):
    LETTERS = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, pencere):
        Frame.__init__(self, pencere)
        self.pencere = pencere

        Label(pencere, text="Enter your message: ", width=20).place(x=20, y=30) #location of element along with included text
        self.Ent1 = Entry(pencere, width=30) #located in pencere and states width
        self.Ent1.place(x=170, y=30) #where entry box is located

        self.Ent2 = Scale(pencere, from_=1, to=25, orient=HORIZONTAL,length=300) #creats a scale ranging from 1 to 25 and creating it horizontal
        self.Ent2.pack() #gets value from scale
        self.Ent2.place(x=20, y=70) #location of scale
        

        Button(pencere, text="encrypt", command=self.encrypt).place(x=50, y=150) #creates a button with a name and runs a function when pressed
        Button(pencere, text="decrypt", command=self.decrypt).place(x=110, y=150) #creates a button with a name and runs a function when pressed

        self.result = Entry(pencere, width=30) 
        self.result.place(x=170, y=200)

    def encrypt(self):
        key = int(self.Ent2.get()) #set key from the integer in box

        cipher = ''

        for char in self.Ent1.get(): #leave it as a space
            if char == ' ':
              cipher = cipher + char #leave it as a space
            elif  char.isupper(): #if character is upper case
              cipher = cipher + chr((ord(char) + key - 65) % 26 + 65) #getting the order of the characters in ASCII shifting them by the shift value
            else:
              cipher = cipher + chr((ord(char) + key - 97) % 26 + 97) #divides characters by 26 and adds 97 ASCII value


        self.result.delete(0, END)
        self.result.insert(0, cipher)

    def decrypt(self): #defines `decrypy function
        key = int(self.Ent2.get()) #set key from the integer in box

        cipher = ''

        for char in self.Ent1.get(): #leave it as a space
            if char == ' ':
              cipher = cipher + char #leave it as a space
            elif  char.isupper(): #if character is upper case
              cipher = cipher + chr((ord(char) - key - 65) % 26 + 65) #getting the order of the characters in ASCII shifting them by the shift value
            else:
              cipher = cipher + chr((ord(char) - key - 97) % 26 + 97) #divides characters by 26 and adds 97 ASCII value


        self.result.delete(0, END)
        self.result.insert(0, cipher)

if __name__ == "__main__": 
    root = Tk() #creates gui and calles it root
    root.title("Caesar Cipher") #name of UI
    root.geometry("400x300+50+50") #size of window
    Sezar(root).pack(side="top", fill="both") #describes where UI elements will be
    root.mainloop() #endless loop of root
