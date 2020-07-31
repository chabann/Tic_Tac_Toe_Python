import random
from tkinter import *

window = Tk()
window.geometry("400x310")
window.title("Tic Tac Toe")
#window["bg"] = "#FFFFE0"

Menu_frame = Frame(window, width=400, height=100, bd=0)
Play_frame = Frame(window, relief=RAISED, bd=1, cursor="cross", width=400, height=300)

Menu_frame.pack(side=TOP, expand=True)
Play_frame.pack()

cnv = Canvas(Play_frame)
cnv.pack(fill=BOTH, expand=1)
cnv.create_rectangle(0, 0, 400, 300, fill="#FFE4B5")

#%%%%%%%%%%%%


def WhoFirst():
    move = random.choice([1, 0])
    if move == 0:
        text.config(text="   Computer!   ")
    else:
        text.config(text="   You!   ")


select_lbl = Label(Menu_frame, text="   Who goes the first?   ")
select = Button(Menu_frame, text="Let's go!", command=WhoFirst, bg="#FFFFE0")
text = Label(Menu_frame, text="")


select_lbl.grid(row=0, column=0)
select.grid(row=0, column=1)
text.grid(row=0, column=2)

window.mainloop()