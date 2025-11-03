from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
window=Tk()
window.geometry("600x500")
window.title("text editor")
window.rowconfigure(0,minsize=500,weight=1)
window.columnconfigure(1,minsize=500,weight=1)
def open_file():
    fileopen=askopenfilename(filetypes=[("text files","*.txt"),("all files","*.*")])
    if not fileopen:
        return
    txt_edit.delete(1.0,END)
    with open(fileopen,"r") as input_file:
        text=input_file.read()
        txt_edit.insert(END,text)
        input_file.close()
        window.title(f"my text editor-{fileopen}")
def savefile():
    fileopen=asksaveasfilename(defaultextension=("*.txt"),filetypes=[("text files","*.txt"),("al files","*.*")])
    if not fileopen:
        return
    with open(fileopen,"w") as outputfile:
       text=txt_edit.get(1.0,END)
       outputfile.write(text)
       window.title(f"my text editor-{fileopen}")
txt_edit=Text(window)

fr_buttons = Frame(window, relief=RAISED, bd=2)

btn_open = Button(fr_buttons, text="Open", command=open_file)

btn_save = Button(fr_buttons, text="Save As...", command=savefile)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")

txt_edit.grid(row=0, column=1, sticky="nsew")


window.mainloop()