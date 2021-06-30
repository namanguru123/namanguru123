import random
from tkinter import *
root=Tk()
root.title("Guess The Number")
root.geometry("700x500")
root.config(bg="Black")
frame=Frame(root,bg="white")
frame.place(x=50,y=50,width=600,height=400)

title=Label(frame,text="Guess The Number",font=("times",40,"bold"),bg="white",fg="green")
title.place(x=80,y=30)

l2=Label(frame,text="Between 1-10",font=("times",1old"),bg="white",fg="green")
l2.place(x=190,y=110)

entry= Entry(frame,width=40,bg="Lightgray")
entry.place(x=180,y=150)


mainloop()