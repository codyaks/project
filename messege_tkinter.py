from tkinter import *
from tkinter import messagebox
window=Tk()
window.title('event message box')
window.geometry('200x200')

def msg():
    messagebox.showwarning("alert","virus found !!!")
btn=Button(text='scan for virus',bg='pink',command=msg)
btn.place(x=80,y=60)

window.mainloop()