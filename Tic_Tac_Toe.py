import random
from tkinter import *

window = Tk()

window.title("Tic Tac Toe")
window.geometry("310x700")
window.resizable(width=False, height=False)

width_sq = 300
height_sq = 260

Menu_frame = Frame(window, bd=0, cursor="arrow")
Play_frame = Frame(window, bd=2, cursor="circle", bg="green")
Result_frame = Frame(window, bd=3, height=10, cursor="arrow", bg="red")
New_frame = Frame(window, bd=1, cursor="arrow", bg="blue")

Menu_frame.pack()
Play_frame.pack()
Result_frame.pack()
New_frame.pack()

cnv = Canvas(Play_frame)
cnv.pack(fill=BOTH, expand=1)
cnv.create_rectangle(0, 0, width_sq, height_sq, fill="#FFE4B5")

result = Canvas(Result_frame)
result.pack(fill=BOTH)
result.create_rectangle(0, 0, 300, 80, fill="#F0E68C")
result.create_text(150, 48, text="Aaaa", justify=CENTER)

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
    cx1, cy1, cx2, cy2 = Number_Coords(comp_choice)

    if type_man == "Cross":
        Draw_cross(cornerx+5, cornery+5, cornerx2-5, cornery2-5)
        Draw_zero(cx1 + 5, cy1 + 5, cx2 - 5, cy2 - 5)
    else:
        Draw_zero(cornerx+5, cornery+5, cornerx2-5, cornery2-5)
        Draw_cross(cx1 + 5, cy1 + 5, cx2 - 5, cy2 - 5)


def Draw_cross(x1, y1, x2, y2):
    cnv.create_line(x1, y1, x2, y2, width=3, fill="#DC143C")
    cnv.create_line(x2, y1, x1, y2, width=3, fill="#DC143C")


def Draw_zero(x1, y1, x2, y2):
    cnv.create_oval(x1, y1, x2, y2, width=3, outline="#DC143C")


def Number_Coords(n):
    global free, x1, x2, y1, y2
    c1, c2, c3, c4 = 0, 0, 0, 0
    if n == 1:
        c1 = 0
        c2 = 0
        c3 = x1
        c4 = y1
    elif n == 2:
        c1 = x1
        c2 = 0
        c3 = x2
        c4 = y1
    elif n == 3:
        c1 = x2
        c2 = 0
        c3 = width_sq
        c4 = y1
    elif n == 4:
        c1 = 0
        c2 = y1
        c3 = x1
        c4 = y2
    elif n == 5:
        c1 = x1
        c2 = y1
        c3 = x2
        c4 = y2
    elif n == 6:
        c1 = x2
        c2 = y1
        c3 = width_sq
        c4 = y2
    elif n == 7:
        c1 = 0
        c2 = y2
        c3 = x1
        c4 = height_sq
    elif n == 8:
        c1 = x1
        c2 = y2
        c3 = x2
        c4 = height_sq
    elif n == 9:
        c1 = x2
        c2 = y2
        c3 = width_sq
        c4 = height_sq
    return c1, c2, c3, c4


def Coords_Number():
    return 1


def new_game():
    print(1)


type_sym = StringVar()

select_lbl = Label(Menu_frame, text="   Who goes the first?   ")
select = Button(Menu_frame, text="Let's go!", command=WhoFirst, bg="#FFFFE0")
text = Label(Menu_frame, text="")
lblcross = Label(Menu_frame, text="Cross")
lblzero = Label(Menu_frame, text="Zero")

cross = Radiobutton(Menu_frame, variable=type_sym, value="Cross")
zero = Radiobutton(Menu_frame, variable=type_sym, value="Zero")
type_sym.set("Cross")


New_game = Button(New_frame, text=" NEW GAME ", command=new_game)
New_game.pack(side=TOP)

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
