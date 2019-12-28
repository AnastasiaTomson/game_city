from tkinter import *


def clicked():
    if txt.get():
        print(txt.get())


window = Tk()
window.geometry('500x500')
window.title("Добро пожаловать в Города!")
lbl = Label(window, text="Введите Ваш город", font=("Arial Bold", 18))
lbl.grid(column=0, row=0)
txt = Entry(window, width=50)
txt.grid(column=0, row=1)
bt = Button(window, text='Ответить', bg='#b2b2b2', fg="white", font=('Arial Bold', 15),
            width=10, command=clicked)
bt.grid(column=0, row=2)
window.mainloop()