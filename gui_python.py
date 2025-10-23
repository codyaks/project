from tkinter import*
from datetime import date

window=Tk()
window.title("getting started with GUI in python")
window.geometry("300x400")

lbl=Label(text="hello everyone",fg='white',bg='red',height=1,width=300)
name_lbl=Label(text='full name',bg='green')
entry_lbl=Entry()

def display():
    name=entry_lbl.get()
    global message
    message="hello welcome to the application \ntoday's date is:"
    greet="hello "+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
text_box=Text(height=3)

btn=Button(text='begain',command=display,fg='blue',bg='pink',height=1)

lbl.pack()
name_lbl.pack()
entry_lbl.pack()
btn.pack()
text_box.pack()

window.mainloop()