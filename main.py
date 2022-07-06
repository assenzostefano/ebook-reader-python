import tkinter as tk
from tkinter import *
from tkinter import Button


#Create window
tk = tk.Tk()
tk.geometry("1280x800")

#Title window
tk.title('Ebook reader')

#Text center
text = Label(tk, text= "Ebook Reader", font= ('Helvetica 20 bold')).grid(row=300, column=500, padx= 550, pady= 300)

def page1():
    label = Label(text='this is the page1')
    label.place(relx=0.3,rely=0.4)

def page2():
    label = Label(text='this is the page2')
    label.place(relx=0.3,rely=0.4)

bt = Button(tk,text='page1',command=page1)
bt.grid(column=100,row=100)

bt1 = Button(tk,text='page2',command=page2)
bt1.grid(row=0,column=1)

tk.mainloop()