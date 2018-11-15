from random import randint
from tkinter import *

root = Tk()
root.title("8 Ball App")

canv = Canvas(root, width=480, height=480, bg='red')
canv.grid(row=1,columnspan=2)

#Label sample option
#labelsample = Label(root, text="Or your question can be here")
#labelsample.grid(row=1, column=0)



img = PhotoImage(file="8ball3.gif")
canv.create_image(0,0, anchor=NW, image=img)

label = Label(root, text='Enter a yes or no question below: ', font=("Courier",16))
label.grid(row=2, column=0)
question = Entry(root,width=50, bg='orange')
question.grid(row=3, column=0)

def displayfortune():
    my_list = ['Definitely!', 'No', 'Maybe', 'Not in this lifetime', 'Try again later',
               "Don't count on it", 'Outlook not so good', 'You Betcha!', 'Affrimative',
               'It is possible', 'Count your lucky stars', 'Absolutely', 'Concentrate and ask again',
               'Looking Slim', 'My sources say yes', 'With out a doubt']
    answer = (my_list[randint(0, len(my_list) - 1)])
    canv.itemconfig(canvid,fill='blue')
    canv.itemconfig(textid,text = answer)


# 2nd Canvas Sample
canv1 = Canvas(canv, width=150, height=100, bg='blue')
canvid = canv.create_oval(140, 140, 350, 350, fill='')
textid = canv.create_text(245,205,text='',fill='white',font=("Courier",15,'bold'))
label.grid()


button = Button(root, text="Click for your fortune", command=displayfortune)
button.grid()


mainloop()


