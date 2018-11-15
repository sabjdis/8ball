from tkinter import *

root = Tk()

label = Label(root, text="Hello World")
field = Entry(root)
label1 = Label(root, text="in column1")
label2 = Label(root, text="another text")

label.grid(row=0, column=0)
field.grid(row=0, column=1)
label1.grid(row=1, columnspan=3)
label2.grid(row=0, column=2)

mainloop()