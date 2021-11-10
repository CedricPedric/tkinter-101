from math import radians
import random
import tkinter


def updateWindow():
    randomItems = ['Bulbasaur','Charmander','Squirtle']
    randomItem = random.choice(randomItems)
    button.destroy()
    reward = tkinter.Label(root, text = 'You got ' + randomItem,)
    if randomItem == 'Bulbasaur':
        reward['background'] = 'green'
    elif randomItem == 'Charmander':
        reward['background'] = 'red'
    elif randomItem == 'Squirtle':
        reward['background'] = 'blue'
    reward.pack(ipadx=100,ipady=100,expand=True)

root = tkinter.Tk()

root.configure(bg='gray')

button = tkinter.Button(root)
button.configure(text='Choose a pokemon!',command=updateWindow)
button.pack(padx=20,pady=20)

root.mainloop()