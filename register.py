from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Form")
        self.root.geometry("1350x1000+0+0")
        self.bg=ImageTk.PhotoImage(file="C:/Users/planet/Downloads/bg2.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        frame1=Frame(self.root,bg="white")
        frame1.place(x=300,y=100,width=700,height=550)

        l1=Label(frame1,text="- By Naman Sharma ",font=("times",10,"bold"),bg="white",fg="black")
        l1.place(x=570,y=525)

        title=Label(frame1,text="REGISTER HERE",font=("times",30,"bold"),bg="white",fg="green").place(x=40,y=30)

        #---------row1

        first=Label(frame1,text="First Name", font=("times",15,"bold"), bg="white", fg="grey").place(x=50,y=100)
        self.f_enter=Entry(frame1,font=("times",15),width=25,bg="lightgray")
        self.f_enter.place(x=50,y=135)

        last= Label(frame1, text="Last Name", font=("times", 15, "bold"), bg="white", fg="grey").place(x=370, y=100)
        self.l_enter = Entry(frame1, font=("times", 15), width=25, bg="lightgray")
        self.l_enter.place(x=370, y=135)

        #---------row2

        contact= Label(frame1, text="Contact No.", font=("times", 15, "bold"), bg="white", fg="grey").place(x=50, y=180)
        self.c_enter = Entry(frame1, font=("times", 15), width=25, bg="lightgray")
        self.c_enter.place(x=50, y=220)

        email= Label(frame1, text="Email", font=("times", 15, "bold"), bg="white", fg="grey").place(x=370, y=180)
        self.e_enter = Entry(frame1, font=("times", 15), width=25, bg="lightgray")
        self.e_enter.place(x=370, y=220)

        #---------row3

        question = Label(frame1, text="Security Question",cursor="hand2", font=("times", 15, "bold"), bg="white", fg="grey").place(x=50, y=260)
        self.cmb_enter = ttk.Combobox(frame1, font=("times", 13),cursor="hand2",state='readonly', width=25)
        self.cmb_enter['values']=("Select","Your First Pet Name","Your Birth Place","Your Best friend Name","Your Lucky Number","Your Favourite Colour")
        self.cmb_enter.place(x=50, y=303)
        self.cmb_enter .current(0)

        answer = Label(frame1, text="Answer", font=("times", 15, "bold"), bg="white", fg="grey").place(x=370, y=260)
        self.a_enter = Entry(frame1, font=("times", 15), width=25, bg="lightgray")
        self.a_enter.place(x=370, y=303)

        #---------row4

        password = Label(frame1, text="Password", font=("times", 15, "bold"), bg="white", fg="grey").place(x=50,y=350)
        self.p_enter = Entry(frame1, font=("times", 15), width=25, bg="lightgray")
        self.p_enter.place(x=50, y=390)

        confirm_password = Label(frame1, text="Confirm Password", font=("times", 15, "bold"), bg="white", fg="grey").place(x=370, y=350)
        self.cp_enter = Entry(frame1, font=("times", 15), width=25, bg="lightgray")
        self.cp_enter.place(x=370, y=390)

        #----------row5

        self.var_chk=IntVar()
        self.chk=Checkbutton(frame1,text="I Agree The terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times",12)).place(x=50,y=420)

        self.btn_img=ImageTk.PhotoImage(file="C:/Users/planet/Downloads/ff.png")
        but=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data,font=("times",1)).place(x=450,y=440)

    def clear(self):
        self.f_enter.delete(0,END)
        self.l_enter.delete(0, END)
        self.c_enter.delete(0, END)
        self.e_enter.delete(0, END)
        self.cmb_enter.current(0)
        self.a_enter.delete(0, END)
        self.p_enter.delete(0, END)
        self.cp_enter.delete(0, END)
        self.chk_enter = 0

    def register_data(self):
        if self.f_enter.get()=="" or self.l_enter.get()=="" or self.e_enter.get()=="" or self.c_enter.get()==""  or self.cmb_enter.get()=="Select" or self.a_enter.get()=="" or self.p_enter.get()=="" or self.cp_enter.get()=="" or self.chk=="":
            messagebox.showerror("Error","ALL Fields Are Required",parent=self.root)
        elif self.c_enter.get().isalpha():
            messagebox.showerror("Error","Please Enter A Valid Contact Number",parent=self.root)
        elif self.p_enter.get()!=self.cp_enter.get() :
            messagebox.showerror("Error", "Confirm Password Must Be same As Password", parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "Please Agree Our Terms & Conditions", parent=self.root)
        elif len(self.p_enter.get()) < 8:
            messagebox.showerror("Error","Password Must Contains Atleast 8 Characters",parent=self.root)
        else:
            messagebox.showinfo("Success", "Registered Successfully", parent=self.root)
            self.clear()

root=Tk()
obj = Register(root)
root.mainloop()