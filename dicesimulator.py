import random
from tkinter import *
root = Tk()
root.geometry("700x250")
l1= Label(font=("times",250))
def roll():
    num=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    l1.config(text=f'({random.choice(num)}{random.choice(num)})')
    l1.pack()
b1= Button(root,text="Roll",command=roll)
b1.place(x=335,y=100)
l1.pack()
Entry_window= Entry(root, width=20, borderwidth=4)
Entry_window.pack()
root.mainloop()