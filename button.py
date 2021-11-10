from math import radians
import random
import tkinter

def makeButton():
    button = tkinter.Button(root)
    button.configure(text='You will get a pokemon!',command=updateWindow)
    button.pack(padx=50,pady=50,expand=True)

randomItems = ['Bulbasaur','Charmander','Squirtle','Pikachu','Scorbunny','Axel','Raichu','Glalie','Dragonair','Leafon']
def updateWindow():
    global randomItems
    if len(randomItems) == 0:
        root.destroy()
        return
    randomItem = random.choice(randomItems)
    randomItems.remove(randomItem)
    reward['text'] = f'The pokemon is {randomItem}'
    if randomItem == 'Bulbasaur' or randomItem == 'Leafon' or randomItem == 'Axel':
        reward['background'] = 'green'
    elif randomItem == 'Charmander' or randomItem == 'Scorbunny':
        reward['background'] = 'red'
    elif randomItem == 'Squirtle' or randomItem == 'Glalie' or randomItem == 'Dragonair':
        reward['background'] = 'blue'
    else:
        reward['background'] = 'yellow'
    



root = tkinter.Tk()
root.configure(bg='gray')


button = tkinter.Button(root)

button.configure(text='You will get a pokemon!',command=updateWindow)
button.pack(padx=50,pady=50,expand=True)
reward = tkinter.Label(root, text = 'You will get a pokemon!')
reward.pack(ipadx=20,ipady=20)

root.mainloop()
