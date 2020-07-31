import random
from tkinter import *

window = Tk()

window.title("Tic Tac Toe")
window.geometry("310x450")
window.resizable(width=False, height=False)

width_sq = 300
height_sq = 260

Menu_frame = Frame(window, bd=0, cursor="arrow")
Play_frame = Frame(window, width=width_sq, height=height_sq, bd=1, cursor="circle")
Result_frame = Frame(window, bd=3, cursor="arrow")

Menu_frame.pack()
Play_frame.pack()
Result_frame.pack()

cnv = Canvas(Play_frame)
cnv.pack(fill=BOTH, expand=1)
cnv.create_rectangle(0, 0, width_sq, height_sq, fill="#FFE4B5")

result = Canvas(Result_frame)
result.pack(fill=BOTH)
result.create_rectangle(0, 0, 300, 100, fill="#F0E68C")
result.create_text(150, 50, text="", justify=CENTER)


def WhoFirst():
    move = random.choice([1, 0])
    if move == 0:
        text.config(text="   Computer!   ")
    else:
        text.config(text="   You!   ")


def MakeDecision(event):
    global x1, x2, y1, y2, free
    global cornerx, cornery, cornerx2, cornery2
    x = event.x
    y = event.y
    if x < x1:
        cornerx = 0
        cornerx2 = x1
    elif x < x2:
        cornerx = x1
        cornerx2 = x2
    elif x < width_sq:
        cornerx = x2
        cornerx2 = width_sq

    if y < y1:
        cornery = 0
        cornery2 = y1
    elif y < y2:
        cornery = y1
        cornery2 = y2
    elif y < height_sq:
        cornery = y2
        cornery2 = height_sq
    type_man = type_sym.get()
    comp_choice = random.choice(free)
    Number_Coords(comp_choice)

    if type_man == "Cross":
        Draw_cross(cornerx, cornery, cornerx2, cornery2)
    else:
        Draw_zero(cornerx, cornery, cornerx2, cornery2)


def Draw_cross(x1, y1, x2, y2):
    cnv.create_line(x1, y1, x2, y2)
    cnv.create_line(x2, y1, x1, y2)


def Draw_zero(x1, y1, x2, y2):
    cnv.create_oval(x1, y1, x2, y2)

def Number_Coords(n):
    return 1


def Coords_Number():
    return 1


type_sym = StringVar()

select_lbl = Label(Menu_frame, text="   Who goes the first?   ")
select = Button(Menu_frame, text="Let's go!", command=WhoFirst, bg="#FFFFE0")
text = Label(Menu_frame, text="")
lblcross = Label(Menu_frame, text="Cross")
lblzero = Label(Menu_frame, text="Zero")

cross = Radiobutton(Menu_frame, variable=type_sym, value="Cross")
zero = Radiobutton(Menu_frame, variable=type_sym, value="Zero")
type_sym.set("Cross")

free = [i for i in (1, 10)]
x1 = width_sq / 3
x2 = width_sq / 3 * 2
y1 = height_sq / 3
y2 = height_sq / 3 * 2
cornerx = 0
cornery = 0
cornerx2 = 0
cornery2 = 0

cnv.create_line(x1, 0, x1, height_sq)
cnv.create_line(x2, 0, x2, height_sq)
cnv.create_line(0, y1, width_sq, y1)
cnv.create_line(0, y2, width_sq, y2)

select_lbl.grid(row=0, column=0)
select.grid(row=0, column=1)
text.grid(row=0, column=2)
cross.grid(row=1, column=0)
lblcross.grid(row=1, column=1)
zero.grid(row=2, column=0)
lblzero.grid(row=2, column=1)

cnv.bind("<Button-1>", MakeDecision)

window.mainloop()
