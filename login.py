from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
import os


class login_System:
    def __init__(self,root):
        self.root=root
        self.root.title("Login system")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#fafafa")

        #==== images ============

        self.phone_image=PhotoImage(file="images/phone.png")
        self.lbl_phone_image=Label(self.root,image=self.phone_image,bd=0).place(x=200,y=50)

        #=== login frame==
        self.employee_id=StringVar()
        self.password=StringVar()

        login_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        login_frame.place(x=650,y=90,width=350,height=460)

        title=Label(login_frame,text="  Login ",font=("Elephant",30,"bold"),bg="white").place(x=0,y=30,relwidth=1)

        lbl_user=Label(login_frame,text="Employee Id",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=100)
       

        txt_employee_id=Entry(login_frame,textvariable=self.employee_id,font=("times new roman",15),bg="#ECECEC").place(x=50,y=140,width=250)
        
        lbl_pass=Label(login_frame,text="Password",font=("Andalus",15),bg="white",fg="#767171").place(x=50,y=190)
        txt_pass=Entry(login_frame,textvariable=self.password,show="*",font=("times new roman",15),bg="#ECECEC").place(x=50,y=240,width=250)

        btn_login=Button(login_frame,command=self.login,text="Log In",font=("Arial Rounded MT Bold",15),bg="#00B0f0",activebackground="#00B0f0",fg="white",activeforeground="white",cursor="hand2").place(x=50,y=300,width=250,height=35)

        hr=Label(login_frame,bg="lightgray").place(x=50,y=370,width=250,height=2)
        or_=Label(login_frame,text="OR",bg="white",fg="lightgray",font=("times new roman",15,"bold")).place(x=150,y=355)

        btn_forget=Button(login_frame,text="forget Password?",command=self.forget_window,font=("times new roman",13),bg="white",fg="#00759E",bd=0, activebackground="white",activeforeground="#00759E").place(x=100,y=390)

        #=== frame2====
        register_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        register_frame.place(x=650,y=570,width=350,height=60)

        lbl_reg=Label(register_frame,text="subscribe | Like",font=("times new roman",13),bg="white").place(x=0,y=20,relwidth=1)
       
        # btn_signup=Button(register_frame,text="Sign up ?",font=("times new roman",13,"bold"),bg="white",fg="#00759E",bd=0).place(x=200,y=17)

       #==== Animation images===
        self.im1=ImageTk.PhotoImage(file="images/im1.png")
        self.im2=ImageTk.PhotoImage(file="images/im2.png")
        self.im3=ImageTk.PhotoImage(file="images/im3.png")

        self.lbl_change_image=Label(self.root,bg="white")
        self.lbl_change_image.place(x=367,y=153,width=240,height=428)

        self.animate()





    def animate(self):
        self.im=self.im1
        self.im1=self.im2
        self.im2=self.im3
        self.im3=self.im
        self.lbl_change_image.config(image=self.im)
        self.lbl_change_image.after(2000,self.animate)


     
     
    def login(self):
        con= sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get=="":
                messagebox.showerror('Error',"All firlds are required",parent=self.root)
            else:
                cur.execute("select utype from employee where eid=? AND pass = ?",(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror('Error',"Invalid Username / Password",parent=self.root)
                else:
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashbord.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    


    def forget_window(self):
        con= sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.employee_id.get()=="":
                messagebox.showerror('Error',"Employee ID must be required",parent=self.root)
            else:
                cur.execute("select email from employee where eid=? ",(self.employee_id.get(),))
                email=cur.fetchone()
                if email==None:
                    messagebox.showerror('Error',"Invalid Employee ID ,try again",parent=self.root)
                else:
                    #============= forget window====
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_conf_pass=StringVar()
                    # call send_email_function()

                    self.forget_win=Toplevel(self.root)
                    self.forget_win.title('RESET PASSWORD')
                    self.forget_win.geometry('400x350+500+100')
                    self.forget_win.focus()

                    title=Label(self.forget_win,text='Reset Password',font=('goudy old style',15,'bold'),bg="#3f51b5",fg="white" ).pack(side=TOP,fill=X)
                    lbl_reset=Label(self.forget_win,text="Enter OTP Sent on Registered Email",font=("times new roman",15)).place(x=20,y=60)
                    txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg="lightyellow").place(x=20,y=100,width=250,height=30)
                    self.btn_reset=Button(self.forget_win,text="SUBMIT",font=("times new roman",15),bg="lightblue")
                    self.btn_reset.place(x=280,y=100,width=100,height=30)

                    lbl_new_pass=Label(self.forget_win,text="New password",font=("times new roman",15)).place(x=20,y=160)
                    txt_new_pass=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg="lightyellow").place(x=20,y=190,width=250,height=30)



                    lbl_c_pass=Label(self.forget_win,text="confirm Passwrd",font=("times new roman",15)).place(x=20,y=255)
                    txt_c_pass=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg="lightyellow").place(x=20,y=255,width=250,height=30)

                    self.btn_update=Button(self.forget_win,text="UPDATE",state="disabled",font=("times new roman",15),bg="lightblue")
                    self.btn_update.place(x=150,y=300,width=100,height=30)



        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
       



root=Tk()
obj=login_System(root)
root.mainloop()
