from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Interest Calculator")
root.geometry("400x300")
root.configure(bg="light green")
def calculate_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())
        interest = (principal * rate * time) / 100
        messagebox.showinfo("Result", f"The calculated interest is: {interest}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")
lbl_principal = Label(root, text="Principal Amount:", bg="light green")
lbl_rate = Label(root, text="Rate of Interest (%):", bg="light green")
lbl_time = Label(root, text="Time (years):", bg="light green")
entry_principal = Entry(root)
entry_rate = Entry(root)
entry_time = Entry(root)
btn_calculate = Button(root, text="Calculate Interest", command=calculate_interest, bg="brown", fg="red")
lbl_principal.place(x=50, y=50)
entry_principal.place(x=200, y=50)
lbl_rate.place(x=50, y=100)
entry_rate.place(x=200, y=100)
lbl_time.place(x=50, y=150)
entry_time.place(x=200, y=150)
btn_calculate.place(x=150, y=200)
root.mainloop()