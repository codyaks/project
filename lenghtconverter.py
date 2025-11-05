from tkinter import *
window=Tk()
window.title("lenght converter")
window.geometry("600x500")
window.configure(bg="pink")

lbl1=Label(window,text="welcome to the length converter",bg="brown",fg="white")
lbl1.place(x=200,y=80)
lbl2=Label(window,text="enter the value you want to convert")
lbl2.place(x=200,y=110)
enter=Entry(window)
def m_to_cm():
    num=int(enter.get())
    value=num*100
    enter1.delete(0,END)
    enter1.insert(END,str(value))
def cm_to_m():
    num=int(enter.get())
    value=num//100
    enter1.delete(0,END)
    enter1.insert(END,str(value))
lbl3=Label(window,text="convert meter to centimeter")
lbl3.place(x=200,y=150)
btn1=Button(window,command=m_to_cm,relief="sunken",text="convert")
btn1.place(x=200,y=180)
lbl4=Label(window,text="convert centimeter to meter")
lbl4.place(x=200,y=210)
btn2=Button(window,command=cm_to_m,relief="sunken",text="convert to meter")
btn2.place(x=200,y=240)
enter1=Entry(window)
enter1.place(x=250,y=270)
enter.place(x=200,y=130)
window.mainloop()