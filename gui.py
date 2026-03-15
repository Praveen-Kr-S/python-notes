import pymysql
import tkinter as t
from tkinter import messagebox,ttk
from PIL import Image,ImageTk

def register_remove():
    rg_name.delete(0,"end")
    rg_email.delete(0,"end")
    rg_phone.delete(0,"end")
    rg_pass.delete(0,"end")

def login_remove():
    lg_email.delete(0,"end")
    lg_pass.delete(0,"end")


def sp(pg):
    pg.tkraise()

def register():
    name=rg_name.get()
    email=rg_email.get()
    phone=rg_phone.get()
    password=rg_pass.get()
    if not all([name,email,phone,password]):
        messagebox.showwarning("Filed Warning","Fill All the Fields")
        return None
    db = pymysql.connect(host="localhost",user="root",passwd="1234",db="live_tech",port=3306)
    cur = db.cursor()
    cur.execute(""" insert into users(name,email,phone,password) values(%s,%s,%s,%s)""",(name,email,phone,password))
    db.commit()
    db.close()
    messagebox.showinfo("Register","Registered Successfully😊😊")
    register_remove()

def login():
    email=lg_email.get()
    password=lg_pass.get()
    if not all([email,password]):
        messagebox.showwarning("Filed Warning","Fill All the Fields")
        return None
    db = pymysql.connect(host="localhost", user="root", passwd="1234", db="live_tech", port=3306)
    cur = db.cursor()
    cur.execute(""" select * from live_tech.users where email = %s and password = %s """, (email, password))
    if cur.fetchone():
        db.close()
        messagebox.showinfo("Login","Successfully login")
        dg.tkraise()
        login_remove()
    else:
        messagebox.showerror("Login","Invalid Credentials")


main = t.Tk()
main.geometry("1920x1080")
main.config(background="blue")
#Frames
container = t.Frame(main,bg="red")
container.place(x=0,y=0,width=1920,height=1080)

rg=t.Frame(container,bg="#caf0f8")
lg=t.Frame(container,bg="#caf0f8")
dg=t.Frame(container,bg="light green")
laptops=t.Frame(container,bg="#0077b6")

for page in (rg,lg,dg,laptops):
    page.place(x=0,y=0,width=1920,height=1080)


#Register Page
title = t.Label(rg,text="Register Form")
title.place(x=600,y=100)
title.config(font=('Arial bold',30),bg="#caf0f8",fg="#03045e")

t.Label(rg,text="User Name : ",font=('Arial',20),bg="#caf0f8",fg="#0077b6").place(x=530,y=200)
rg_name = t.Entry(rg,font=('Arial',20),bg="#caf0f8",fg="#0077b6")
rg_name.place(x=700,y=200)

t.Label(rg,text="User Email : ",font=('Arial',20),bg="#caf0f8",fg="#0077b6").place(x=530,y=270)
rg_email = t.Entry(rg,font=('Arial',20),bg="#caf0f8",fg="#0077b6")
rg_email.place(x=700,y=270)

t.Label(rg,text="User Phone : ",font=('Arial',20),bg="#caf0f8",fg="#0077b6").place(x=530,y=340)
rg_phone = t.Entry(rg,font=('Arial',20),bg="#caf0f8",fg="#0077b6")
rg_phone.place(x=700,y=340)

t.Label(rg,text="Password : ",font=('Arial',20),bg="#caf0f8",fg="#0077b6").place(x=530,y=410)
rg_pass = t.Entry(rg,font=('Arial',20),bg="#caf0f8",fg="#0077b6",show="*")
rg_pass.place(x=700,y=410)

t.Button(rg,text="Login Form",font=('Arial',25),bg="#03045e",fg="#caf0f8",command=lambda:sp(lg)).place(x=550,y=480)
t.Button(rg,text="Register",font=('Arial',25),bg="#03045e",fg="#caf0f8",command=register).place(x=800,y=480)

#login Page
title = t.Label(lg,text="Login Form")
title.place(x=600,y=100)
title.config(font=('Arial bold',30),bg="#caf0f8",fg="#03045e")

t.Label(lg,text="User Email : ",font=('Arial',20),bg="#caf0f8",fg="#0077b6").place(x=530,y=270)
lg_email = t.Entry(lg,font=('Arial',20),bg="#caf0f8",fg="#0077b6")
lg_email.place(x=700,y=270)


t.Label(lg,text="Password : ",font=('Arial',20),bg="#caf0f8",fg="#0077b6").place(x=530,y=340)
lg_pass = t.Entry(lg,font=('Arial',20),bg="#caf0f8",fg="#0077b6",show="*")
lg_pass.place(x=700,y=340)

t.Button(lg,text="Register Form",font=('Arial',25),bg="#03045e",fg="#caf0f8",command=lambda:sp(rg)).place(x=550,y=410)
t.Button(lg,text="Login",font=('Arial',25),bg="#03045e",fg="#caf0f8",command=login).place(x=800,y=410)


#dashboard


t.Label(dg,text="Welcome to Amazon",font=('Arial bold',30),bg="#caf0f8",fg="#03045e").place(x=550,y=100)

img = Image.open(r"C:\Users\Livewire\Pictures\mobiles.webp")
img = img.resize((200,150))
pic = ImageTk.PhotoImage(image=img)
t.Label(dg,image=pic).place(x=150,y=200)

img1 = Image.open(r"C:\Users\Livewire\Pictures\laptops.webp")
img1 = img1.resize((200,150))
pic1 = ImageTk.PhotoImage(image=img1)
t.Button(dg,image=pic1,command=lambda:sp(laptops)).place(x=400,y=200)
#Text box
t.Label(dg,text="message area :",font=('Arial',16),bg="#caf0f8",fg="#0077b6").place(x=250,y=370)
t.Text(dg,width=30,height=10,font=('Arial',16),bg="#caf0f8",fg="#0077b6").place(x=200,y =400)

#combo box
city = ["Salem",'Chennai','Kovai']
cb = ttk.Combobox(dg,values=city,font=("Arial",20)).place(x=700,y=200)


ttk.Checkbutton(dg,text="Yes").place(x=700,y=300)
ttk.Checkbutton(dg,text="No").place(x=750,y=300)

t.Button(dg,text="Logout",font=('Arial',25),bg="#03045e",fg="#caf0f8",command=lambda:sp(lg)).place(x=1100,y=50)

rg.tkraise()
main.mainloop()

