import random
from tkinter import *

window = Tk()
window.geometry("400x300")
window.title("Tic Tac Toe")

Menu_frame = Frame(window)
Play_frame = Frame(window, relief=RAISED, bd=3, cursor="cross")

Menu_frame.pack(side=TOP)
Play_frame.pack()


select_lbl = Label()