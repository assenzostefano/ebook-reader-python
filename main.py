import tkinter
from tkinter import *

#Create window
top = tkinter.Tk()
top.geometry("1280x800")

#Title window
top.title('Ebook reader')

#Text center
text = Label(top, text= "Ebook Reader", font= ('Helvetica 20 bold')).grid(row=300, column=500, padx= 550, pady= 300)

top.mainloop()