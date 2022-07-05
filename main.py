import tkinter
from tkinter import *

#Create window
top = tkinter.Tk()

#Title window
top.title('Ebook reader')

#Text center
text = Label(top, text="Ebook reader", fg='red', font=("Helvetica", 16))
text.place(anchor="center")
text.pack()

top.mainloop()