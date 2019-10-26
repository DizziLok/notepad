import tkinter
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror
from tkinter import messagebox




FILE_NAME = tkinter.NONE

def new_file():
    global FILE_NAME
    FILE_NAME = "Untetled"
    text.delete('1.0',tkinter.END)

def save_file():
    data = text.get('1.0', tkinter.END)
    out = open(FILE_NAME, "w")
    out.write(data)
    out.close()

def save_as():
    out = asksaveasfile(mode="w", defaultextension='.txt')
    date = text.get('1.0', tkinter.END)

    try:
        out.write(data.strip())
    except Exception:
        showerror(title="Ошибка", massage="Невозможно сохранить файл")


def open_file():
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
        return
    FILE_NAME = inp.name
    data = inp.read()
    text.delate('1.0', tkinter.END)
    text.insert('1.0', data)

def into():
    messagebox.showinfo("Информация", "GO-IT Notepad\nVersion: 1.0 beta")

def update(event):
    var.set(str(len(text.get('1.0', 'end-1c'))))

root = tkinter.Tk()
root.title("GO_IT Notepad")
root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)

text = tkinter.Text(root, width=400, height=400, wrap="word")
var = StringVar()
text.bind("<Key>", update)
scrollb = Scrollbar(root, orient=VERTICAL, command=text.yview)
scrollb.pack(side="right", fill="y")
text.configure(yscrollcommand=scrollb.set)
label = Label(root, text="", textvariable=var)
label.pack(expand=1, anchor=SE)
text.pack()

menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar)

menuBar.add_cascade(label="Файл", menu=fileMenu)
menuBar.add_cascade(label="Информация", command=into)
menuBar.add_cascade(label="Выход", command=root.quit)

fileMenu.add_command(label="Новый", command=new_file)
fileMenu.add_command(label="Открить", command=open_file)
fileMenu.add_command(label="Сохранить", command=save_file)
fileMenu.add_command(label="Сохранить как", command=save_as)





root.config(menu=menuBar)
root.mainloop()