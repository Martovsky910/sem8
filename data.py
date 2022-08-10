import input 
import logger 
from tkinter import *

def join():
    name, surname, location, number = input.get_phonebook_data()
    logger.append(name, surname, location, number)
    return name, surname, location, number

window = Tk()
window.title("Телефонный справочник")
window.geometry('400x250')
txt = Entry(window,width=10)  
txt.grid(column=1, row=0) 
txt = Entry(window,width=10, state='disabled')
btn = Button(window, text="Загрузить", bg = "grey", fg = "white")
btn.grid(column = 2, row =0)
btn = Button(window, text="Поиск", bg = "grey", fg = "white")
btn.grid(column = 3, row =0)
btn = Button(window, text="Удалить", bg = "grey", fg = "white")
btn.grid(column = 4, row =0)
lbl = Label()
window.mainloop()

def clicked():  
    res = "{}".format(txt.get())  
    lbl.configure(text=res) 

