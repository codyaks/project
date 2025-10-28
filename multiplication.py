from tkinter import *

window=Tk()
window.title('multipication')
window.geometry('400x300')

lbl1=Label(text='multiplicator application',height=2,width=400,bg='blue')
lbl2=Label(master=window,text='please enter the first number',bg='blue',height=2,)
lbl3=Label(master=window,text='please enter the second number',bg='blue',height=2)

enter1=Entry(bg='pink')
enter2=Entry(bg='pink')

def mul():
    num1=enter1.get()
    num2=enter2.get()
    int_1=int(num1)
    int_2=int(num2)
    global ans
    ans=int_1*int_2
    str1=str(ans)
    greet="welcome to the application\n"
    sol='the multiplication of these numbers is-'
    text_box.insert(END,greet)
    text_box.insert(END,sol+str1)
text_box=Text(height=5,fg='pink')
btn=Button(text='enter',command=mul,bg='red',height=1)

lbl1.pack(pady=2)
lbl2.pack(pady=2)
enter1.pack(pady=2)
lbl3.pack(pady=2)
enter2.pack(pady=2)
btn.pack(pady=5)
text_box.pack(pady=1)

window.mainloop()