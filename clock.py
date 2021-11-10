import time
import tkinter





def Time():
    Tijd = time.localtime()
    Hour = Tijd[3]
    Min = Tijd[4]
    Sec = Tijd[5]

def updateLabel():
    Tijd = time.localtime()
    Hour = Tijd[3]
    Min = Tijd[4]
    Sec = Tijd[5]
    
    stringVar.set(f"{Hour}:{Min}:{Sec}")
    label.after(1000,updateLabel)


root = tkinter.Tk()

stringVar = tkinter.StringVar(value='Welkom')

label = tkinter.Label(root)
label.config(textvariable=stringVar)
label.pack(pady=20)
updateLabel()


root.mainloop()


