from tkinter import *
window=Tk()
window.title('event managing')
window.geometry('200x200')

def key_press(event):
    print("the pressed key is -")
    print(event.char)
window.bind("<Key>",key_press)

def click(event):
    print("a button is pressed")

btn=Button(text='click me')
btn.pack()

window.bind("<Button-1>",click)



window.mainloop()