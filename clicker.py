import tkinter

Number = 0
def Add():
    global Number
    Number += 1
    numberLabel['text'] = Number

    if Number > 0:
        root['background'] = 'green'
    elif Number < 0:
        root['background'] = 'red'
    else:
        root['background'] = 'gray'

def Sub():
    global Number
    Number -= 1
    numberLabel['text'] = Number
    if Number > 0:
        root['background'] = 'green'
    elif Number < 0:
        root['background'] = 'red'
    else:
        root['background'] = 'gray'


root = tkinter.Tk()
root.configure(bg='gray')
root.geometry('300x300')

buttonUp = tkinter.Button(root)
buttonUp.configure(text= 'Up', command=Add)
buttonUp.pack(padx=50,pady=50,expand=True)

buttonDown = tkinter.Button(root)
buttonDown.configure(text= 'Down', command=Sub)
buttonDown.pack(padx=50,pady=50,expand=True)

numberLabel = tkinter.Label(root, text = Number)
numberLabel.pack(ipadx=20,ipady=20)

root.mainloop()