import random
from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Tic Tac Toe")
window.geometry("310x460")
window.resizable(width=False, height=False)

width_sq = 300
height_sq = 260

Menu_frame = Frame(window, bd=0, cursor="arrow")
Play_frame = Frame(window, bd=2, cursor="circle")
Result_frame = Frame(window, bd=3, cursor="arrow")
New_frame = Frame(window, bd=1, cursor="arrow")

Menu_frame.pack(side=TOP)
Play_frame.pack(side=TOP)
Result_frame.pack(side=TOP)
New_frame.pack(side=TOP)

cnv = Canvas(Play_frame)
cnv.pack(fill=BOTH, expand=1)


def WhoFirst():
    move = random.choice([1, 0])
    if move == 0:
        text.config(text="   Computer!   ")
    else:
        text.config(text="   You!   ")


def Check(cells):
    global x1, x2, y1, y2
    des = 0
    xc1, xc2, yc1, yc2 = 0, 0, 0, 0
    if (1 in cells) & (2 in cells) & (3 in cells):
        des = 1
        xc1 = 5
        yc1 = y1 / 2
        xc2 = width_sq - 5
        yc2 = y1 / 2
    elif (4 in cells) & (5 in cells) & (6 in cells):
        des = 1
        xc1 = 5
        yc1 = y1 + y1 / 2
        xc2 = width_sq - 5
        yc2 = y1 + y1 / 2
    elif (7 in cells) & (8 in cells) & (9 in cells):
        des = 1
        xc1 = 5
        yc1 = y2 + y1 / 2
        xc2 = width_sq - 5
        yc2 = y2 + y1 / 2
    elif (1 in cells) & (4 in cells) & (7 in cells):
        des = 1
        xc1 = x1 / 2
        yc1 = 5
        xc2 = x1 / 2
        yc2 = height_sq - 5
    elif (2 in cells) & (5 in cells) & (8 in cells):
        des = 1
        xc1 = x1 + x1 / 2
        yc1 = 5
        xc2 = x1 + x1 / 2
        yc2 = height_sq - 5
    elif (3 in cells) & (6 in cells) & (9 in cells):
        des = 1
        xc1 = x2 + x1 / 2
        yc1 = 5
        xc2 = x2 + x1 / 2
        yc2 = height_sq - 5
    elif (1 in cells) & (5 in cells) & (9 in cells):
        des = 1
        xc1 = 5
        yc1 = 5
        xc2 = width_sq - 5
        yc2 = height_sq - 5
    elif (3 in cells) & (5 in cells) & (7 in cells):
        des = 1
        xc1 = width_sq - 5
        yc1 = 5
        xc2 = 5
        yc2 = height_sq - 5
    return des, xc1, yc1, xc2, yc2


def CheckThePlay():
    # 1 - man, 2 - comp, 0 - nobody
    global man, comp
    if Check(man)[0] == 1:
        return 1, Check(man)[1], Check(man)[2], Check(man)[3], Check(man)[4]
    elif Check(comp)[0] == 1:
        return 2, Check(comp)[1], Check(comp)[2], Check(comp)[3], Check(comp)[4]
    else:
        return 0, Check(comp)[1], Check(comp)[2], Check(comp)[3], Check(comp)[4]


def MakeDecision(event):
    global x1, x2, y1, y2, free
    global cornerx, cornery, cornerx2, cornery2
    x = event.x
    y = event.y

    man_choice = Coords_Number(x, y)
    free.remove(man_choice)
    man.append(man_choice)
    type_man = type_sym.get()

    comp_choice = random.choice(free)
    free.remove(comp_choice)
    comp.append(comp_choice)
    cx1, cy1, cx2, cy2 = Number_Coords(comp_choice)

    check, lx1, ly1, lx2, ly2 = CheckThePlay()

    if type_man == "Cross":
        Draw_cross(cornerx+5, cornery+5, cornerx2-5, cornery2-5)
        if check == 0:  # Никто еще не выиграл
            lblResult.config(text="Comp's choice")
            window.update()
            if len(free) > 0:
                window.after(600, Draw_zero(cx1 + 5, cy1 + 5, cx2 - 5, cy2 - 5))
                lblResult.config(text="Your choice")
            else:
                messagebox.showinfo("Ничья")
        elif check == 1:
            # Выиграл человек
            Draw_finish_line(lx1, ly1, lx2, ly2)
            lblResult.config(text="ВЫ ПОБЕДИЛИ!")
            window.update()
        elif check == 2:  # Выиграл компьютер
            Draw_finish_line(lx1, ly1, lx2, ly2)
            lblResult.config(text="ПОБЕДИЛ КОМПЬЮТЕР!")
            window.update()
    else:
        Draw_zero(cornerx+5, cornery+5, cornerx2-5, cornery2-5)
        if check == 0:  # Никто еще не выиграл
            lblResult.config(text="Comp's choice")
            window.update()
            if len(free) > 0:
                window.after(600, Draw_cross(cx1 + 5, cy1 + 5, cx2 - 5, cy2 - 5))
                lblResult.config(text="Your choice")
            else:
                messagebox.showinfo("Ничья")
        elif check == 1:
            # Выиграл человек
            Draw_finish_line(lx1, ly1, lx2, ly2)
            lblResult.config(text="ВЫ ПОБЕДИЛИ!")
            window.update()
        elif check == 2:  # Выиграл компьютер
            Draw_finish_line(lx1, ly1, lx2, ly2)
            lblResult.config(text="ПОБЕДИЛ КОМПЬЮТЕР!")
            window.update()


def Draw_cross(x1, y1, x2, y2):
    cnv.create_line(x1, y1, x2, y2, width=3, fill="#DC143C")
    cnv.create_line(x2, y1, x1, y2, width=3, fill="#DC143C")


def Draw_zero(x1, y1, x2, y2):
    cnv.create_oval(x1, y1, x2, y2, width=3, outline="#DC143C")


def Draw_finish_line(x1, y1, x2, y2):
    cnv.create_line(x1, y1, x2, y2, width=4, fill="#8B0000")


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


def Coords_Number(x, y):
    global cornerx, cornery, cornerx2, cornery2
    if x < x1:
        cornerx = 0
        cornerx2 = x1
        nx = 1
    elif x < x2:
        cornerx = x1
        cornerx2 = x2
        nx = 2
    elif x < width_sq:
        cornerx = x2
        cornerx2 = width_sq
        nx = 3

    if y < y1:
        cornery = 0
        cornery2 = y1
        ny = 4
    elif y < y2:
        cornery = y1
        cornery2 = y2
        ny = 5
    elif y < height_sq:
        cornery = y2
        cornery2 = height_sq
        ny = 6
    xy = nx * ny
    if xy == 4:
        num = 1
    elif xy == 8:
        num = 2
    elif xy == 12:
        if nx == 3:
            num = 3
        else:
            num = 8
    elif xy == 5:
        num = 4
    elif xy == 10:
        num = 5
    elif xy == 15:
        num = 6
    elif xy == 6:
        num = 7
    elif xy == 18:
        num = 9
    return num


def new_game():
    global free, man, comp
    cnv.create_rectangle(0, 0, width_sq, height_sq, fill="#FFE4B5")
    cnv.create_line(x1, 0, x1, height_sq)
    cnv.create_line(x2, 0, x2, height_sq)
    cnv.create_line(0, y1, width_sq, y1)
    cnv.create_line(0, y2, width_sq, y2)
    free = [i for i in range(1, 10)]
    man = []
    comp = []


type_sym = StringVar()

select_lbl = Label(Menu_frame, text="   Who goes the first?   ")
select = Button(Menu_frame, text="Let's go!", command=WhoFirst, bg="#00FF7F")
text = Label(Menu_frame, text="")
lblcross = Label(Menu_frame, text="Cross")
lblzero = Label(Menu_frame, text="Zero")
lblResult = Label(Result_frame, text="", bg="#FFFFE0", width=100, height=4, justify=CENTER)
lblResult.pack()

cross = Radiobutton(Menu_frame, variable=type_sym, value="Cross")
zero = Radiobutton(Menu_frame, variable=type_sym, value="Zero")
type_sym.set("Cross")


New_game = Button(Result_frame, text=" NEW GAME ", command=new_game, pady=10, bg="#32CD32", fg="#FFFFE0")
New_game.pack()

x1 = width_sq / 3
x2 = width_sq / 3 * 2
y1 = height_sq / 3
y2 = height_sq / 3 * 2
cornerx = 0
cornery = 0
cornerx2 = 0
cornery2 = 0

new_game()

select_lbl.grid(row=0, column=0)
select.grid(row=0, column=1)
text.grid(row=0, column=2)
cross.grid(row=1, column=0)
lblcross.grid(row=1, column=1)
zero.grid(row=2, column=0)
lblzero.grid(row=2, column=1)

cnv.bind("<Button-1>", MakeDecision)

window.mainloop()
