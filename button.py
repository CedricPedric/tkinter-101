from math import radians
import random
import tkinter

def makeButton():
    button = tkinter.Button(root)
    button.configure(text='You will get a pokemon!',command=updateWindow)
    button.pack(padx=50,pady=50,expand=True)

randomItems = ['Bulbasaur','Charmander','Squirtle','Pikachu','Scorbunny','Axel','Raichu','Glalie','Dragonair','Leafon']
def updateWindow():
    if len(randomItems) == 0:
        root.destroy()
        return
    randomItem = random.choice(randomItems)
    randomItems.remove(randomItem)
    reward = tkinter.Label(root, text = 'You got ' + randomItem,)
    if randomItem == 'Bulbasaur':
        reward['background'] = 'green'
    elif randomItem == 'Charmander':
        reward['background'] = 'red'
    elif randomItem == 'Squirtle':
        reward['background'] = 'blue'
    else:
        reward['background'] = 'yellow'
    reward.pack(ipadx=20,ipady=20)



root = tkinter.Tk()
root.configure(bg='gray')

button = tkinter.Button(root)
button.configure(text='You will get a pokemon!',command=updateWindow)
button.pack(padx=50,pady=50,expand=True)


root.mainloop()
