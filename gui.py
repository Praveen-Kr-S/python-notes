# import pymysql
# db = pymysql.connect(user="root",host="localhost",port=3306,password="")

import tkinter as t
def sp(pg):
    pg.tkraise()



main = t.Tk()
main.geometry("1920x1080")
main.config(background="blue")
#Frames
container = t.Frame(main,bg="red")
container.place(x=0,y=0,width=1920,height=1080)

rg=t.Frame(container,bg="#caf0f8")
lg=t.Frame(container,bg="#caf0f8")
dg=t.Frame(container,bg="light green")

for page in (rg,lg,dg):
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
t.Button(rg,text="Register",font=('Arial',25),bg="#03045e",fg="#caf0f8").place(x=800,y=480)

#login Page
title = t.Label(lg,text="Login Form")
title.place(x=600,y=100)
title.config(font=('Arial bold',30),bg="#caf0f8",fg="#03045e")

t.Label(lg,text="User Email : ",font=('Arial',20),bg="#caf0f8",fg="#0077b6").place(x=530,y=270)
lg_email = t.Entry(lg,font=('Arial',20),bg="#caf0f8",fg="#0077b6")
lg_email.place(x=700,y=270)


t.Label(lg,text="Password : ",font=('Arial',20),bg="#caf0f8",fg="#0077b6").place(x=530,y=340)
rg_pass = t.Entry(lg,font=('Arial',20),bg="#caf0f8",fg="#0077b6",show="*")
rg_pass.place(x=700,y=340)

t.Button(lg,text="Register Form",font=('Arial',25),bg="#03045e",fg="#caf0f8",command=lambda:sp(rg)).place(x=550,y=410)
t.Button(lg,text="Login",font=('Arial',25),bg="#03045e",fg="#caf0f8").place(x=800,y=410)

"shiny"
lg.tkraise()
main.mainloop()


