import tkinter


def color6():
    print('6')
    window.geometry('100x100')
    window['background'] = 'purple'

def color5():
    print('5')
    window.geometry('150x150')
    window['background'] = 'pink'

def color4():
    print('4')
    window.geometry('200x200')
    window['background'] = 'yellow'

def color3():
    print('3')
    window.geometry('250x250')
    window['background'] = 'orange'

def color2():
    print('2')
    window.geometry('300x300')
    window['background'] = 'red'

def color1():
    print('1')
    window.geometry('350x350')
    window['background'] = 'black'

def destroy():
    window.destroy()


window = tkinter.Tk()
window.geometry('50x50')
window.configure(bg='white')
window.title("My First Window")

window.after(1000,color6)
window.after(2000,color5)
window.after(3000,color4)
window.after(4000,color3)
window.after(5000,color2)
window.after(6000,color1)
window.after(7000,destroy)
window.mainloop()
print("BOOM")