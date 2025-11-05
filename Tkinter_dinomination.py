from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

window=Tk()
window.title("Dinomination Calculator")
window.configure(bg="light blue")
window.geometry("650x500")

upload=Image.open("app_img.jpg")
upload=upload.resize((300,300))
image=ImageTk.PhotoImage(upload)
lbl=Label(window,bg="light blue",image=image)
lbl.place(x=180,y=20)

lbl1=Label(window,text="welcome to the application",bg="light blue")
lbl1.place(relx=0.5,y=340,anchor=CENTER)

def msg():
    msg_box=messagebox.showinfo("alert!!","do you want to proceed to the application?")
    if msg_box=="ok":
        startwin()
btn=Button(window,bg="brown",command=msg,text="let's get started",fg="white")
btn.place(x=260,y=360)
def startwin():
    top=Toplevel()
    top.configure(bg="light blue")
    top.geometry("600x400")
    top.title("dimonination calculator")
    lbl2=Label(top,text="enter the total number ",bg="light grey")
    text=Entry(top)
    lbl3=Label(top,bg="light grey",text="thee number of notes for each dinomination are-")

    l1=Label(top,bg="light grey",text="2000")
    l2=Label(top,bg="light grey",text="500")
    l3=Label(top,bg="light grey",text="100")

    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)

    def calculate():
        try:
           global amount
           amount=int(text.get())
           notes_2000=amount//2000
           amount%=2000
           notes_500=amount//500
           amount%=500
           notes_100=amount//100

           t1.delete(0, END)

           t2.delete(0, END)

           t3.delete(0, END)

           t1.insert(END, str(notes_2000))

           t2.insert(END, str(notes_500))

           t3.insert(END, str(notes_100))
        except ValueError():
            messagebox.showwarning("error!","Please enter a valid number")
    btn2=Button(top,command=calculate,fg="white",bg="brown",text="calculate")

    btn2.place(x=240,y=120)
    lbl.place(x=230, y=50)

    text.place(x=200, y=80)


    lbl2.place(x=140, y=170)
    
    l1.place(x=180, y=200)

    l2.place(x=180, y=230)

    l3.place(x=180, y=260)

    t1.place(x=270, y=200)

    t2.place(x=270, y=230)

    t3.place(x=270, y=260)
    top.mainloop()
window.mainloop()