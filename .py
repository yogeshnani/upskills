#__________INTRO PAGE____________#
from tkinter import *
from PIL import ImageTk

root=Tk()
root.geometry("1590x800+0+0")
root.title("demo")
root.config(bg="#ea5455")

def lg_in():
    root.destroy()
    import register


btn_img=ImageTk.PhotoImage(file="button_sign-u.png")
title=Label(text="Welcome to Password Manager",font=("Verdana 15underline",50,"bold"),relief="groove",bg="#ea5455",fg="white")
title.place(x=0,y=150,relwidth=1)
des=Label(text="It gives you a easy access to store, generate , and manage\n your passwords for local applications and online services.",font=("helvetica",25,"italic"),bg="#ea5455",fg='white')
des.place(x=330,y=350)
sign_up_btn=Button(image=btn_img,borderwidth=0,bd=0,command=lg_in,bg="#ea5455")
sign_up_btn.place(x=650,y=550)

root.mainloop()







File:#______________signuppage______________#
from tkinter import *
from tkinter import messagebox
import mysql.connector


root=Tk()
root.geometry("1590x800+0+0")
root.title("demo")
root.config(bg="#ea5455")
img_reg=PhoyoImage(file="images/button_sign_up.png")
frame1=Frame(bg="white",bd=0)
frame1.place(x=550,y=30,width=500,height=740)

lbl_sign_up=Label(text="SIGN UP",font("times new roman",30,"bold"),bg="white",fg="black")
lbl_sign_up.place(x=690,y=70)
username=Label(text="enter your email",font=("helvetica",15),bg="white")
username.place(x=600,y=200)
user_mail=Entry(text="hell",font=("helvetica",15),bg="white",relief="ridge",borderwidth=1)
user_mail.place(x=600,y=260,width=300)
user_mail.focus()
paswd=Label(text="New Password",font=("helvetica",15),bg="white")
paswd.place(x=600,y=330)
new_pswd=Entry(font=("helvetica",15),show="*",relief="ridge",borderwidth=1)
new_pswd.place(x=600,y=380,width=300)
cfrm_paswd=Label(text="confirm password",font=("helvetica",15),bh="white")
cfrm_paswd.place(x=600,y=440,height=35)
cnfrm_pswd=Entry(font=("helvetica",15),show="*",relief="ridge",borderwidth=1)
cnfrm_pswd.place(x=600,y=490,width=300)



def regs():
    if new_pswd.get()=="" or cnfrm_pswd.get()=="" or user_mail.get()=="" :
        messagebox.showerror("Error","All Fields are required")
    elif new_pswd.get()!=cnfrm_pswd.get():
        messagebox.showerror("Error","Password and confirm password doen't match")
    else:
        try:
            db=mysql.connector.connect(host='localhost',user='root',passwd='root',database="password_manager")
            cur=db.cursor()
            cur.execute("Insert into useraccounts(mail_id,password)values(%s, %s)",(user_mail.get(),new_pswd.get()))
            db.commit()
            db.close()
            root.destroy()
            import log_in
        except EXCEPTION as e:
            messagebox.showerror("Error",f "Error Due to {e}")

    frame1=Frame(bg="white",bd=0)
    frame1.place(x=550,y=30,width=500,height=740)

    btn_login=PhotoImage(file="images/button_log-in.png")
    title=Label(text="Login In",bg="white",font=("Californian FB",35,"bold"))
    title.place(x=710,y=80)

    label=Label(text="username",compound=LEFT,font=("helvetica",18),bg="white")
    label.place(x=600,y=200)

    email_txt=Entry(text="hell",font=("helvetica",18),bg="white",relief="sunken",bd=1)
    email_txt.place(x=600,y=260,width=300)
    email_txt.focus()

    pass_lbl=Label(text="Password",font=("helvetica",18),bg="white")
    pass_lbl.place(x=600,y=320)
    paswd_txt=Entry(font=("helvetica",15),show="*",relief="sunken",bd=1)
    paswd_txt.place(x=600,y=380,width=300)
    sign_in=Button(image=btn_login,bd=0,bg="white",command=login)
    sign_in.place(x=610,y=500)

    root.mainloop()

file:    #___________password manager__________________#
from tkinter import *
from PIL import ImageTk
from random import *
import pyperclip
from tkinter import messagebox
import mysql.connector
from tkinter import ttk
import string

def clear():
    website_entry.delete(0,END)
    password_entry.delete(0,END)
    mail_entry.delete(0,END)
    username_entry.delete(0,END)

    
##_____PASSWORD SAVER_____________###
def save():
    website=website_entry.get()
    username=username_entry.get()
    password=password_entry.get()
    mail_id=mail_entry.get()
    if website=="" or username=="" or password=="" or mail_id=="" :
        messagebox.showerror(title="oops",message="please don't leave any fields empty")
    else:
        is_ok=messagebox.askyesno(title="Website",message="do you confirm to add the details entered")
        if is_ok:
            try:
                db=mysql.connector.connect(host='localhost',user='root',passwd='root',database="password_manager")
                cur=db.cursor()
                cur.execute("INSERT INTO UserData(Website,Username,Password,mail_id)VALUES(%s,%s,%s,%s)",(website,username,password,mail_id))
                db.commit()
                db.close()
                fetch_data()
                clear()
            except EXCEPTION as e:
                messagebox.showerror("Error",f"Error Due to {e}")



def update():
    website=website_entry.get()
    username=username_entry.get()
    password=password_entry.get()
    mail_id=mail_entry.get()
    try:
        db=mysql.connector.connect(host='localhost',user='root',passwd='root',database="password_manager")
        cur=db.cursor()
        cur.execute("UPDATE UserData SET Username=%s,Password=%s,mail_id=%s WHERE Website=%s",(username,password,mail_id,website))
        db.commit()
        db.close()
        fetch_data()
        clear()
    except EXCEPTION as e:
        messagebox.showerror("Error",f"Error due to {e}")



def delete():
     website=website_entry.get()
     db=mysql.connector.connect(host='localhost',user='root',passwd='root',database="password_manager")
     cur=db.cursor()
     cur.execute("DELETE FROM UserData WHERE Website=%s",(website))
     db.commit()
     db.close()
     fetch_data()
     clear()


window=Tk()
window.geometry("1590x800+0+0")
window.title("PASSWORD MANAGER")
window.config(bg="#ea5455")


frame1=Frame(width=1482,height=740,bg="white")
frame1.place(x=20,y=30)

frame2=Frame(frame1,width=600,height=570,bg="white",borderwidth=1,relief="solid")
frame2.place(x=30,y=150)

frame3=LabelFrame(frame1,text="password generator",font=("helvetica",18),width=800,height=260,bg="white",borderwidth=1,relief="solid")
frame3.place(x=650,y=140)


def check():
    upper=upper_var.get()
    lower=lower_var.get()
    number=number_var.get()
    symbol=symbol_var.get()
    ps=""
    if upper=='on':
        ps+=string.ascii_uppercase
    if lower=='on':
        ps+=string.ascii_lowercase
    if number=='on':
        ps+=string.digits
    if symbol=='on':
        ps+=string.punctuation
    else:
        generate_entry.delete(0,END)
        generate_entry.insert(0,"please check any one option")
    return ps


def generate(ev):
    pswrd=check()
    password=''
    for i in range(0,slider.get()):
        password=password+choice(pswrd)
        generate_entry.delete(0,END)
        password_entry.delete(0,END)
        generate_entry.insert(0,password)
        password_entry.insert(0,password)
        pyperclip.copy(password)
    upper_var=StringVar()
    lower_var=StringVar()
    number_var=StringVar()
    symbol_var=StringVar()
    label=Label(frame3,text="customize your password",font=("helvetica",18,"unerline"),bg='white')
    label.place(x=100,y=80)

    slider=Scale(frame3,label="Password length",font=("helvetica",12),from_=0,to=50,length=250,resolution=1,orient=HORIZONTAL,troughcolor='white',relief='groove',activebackground="#ea5455",bg="#ffcccb",bd=0,command=generate)
    slider.place(x=100,y=140)

    upper_check=CheckButton(frame3,text="Uppercase",variable=upper_var,font("helvetica",13),bg='white',onvalue='on',offvalue='off')
    upper_check.place(x=380,y=130)
    upper_check.select()
    lower_check = Checkbutton(frame3, text='Lowercase', variable=lower_var,font=("helvetica", 13), bg='white',onvalue='on', offvalue='off')
    lower_check.place(x=380, y=180)
    lower_check.select()
    number_check = Checkbutton(frame3, text='Numbers', variable=number_var,font=("helvetica", 13), bg='white',onvalue='on', offvalue='off')
    number_check.place(x=525, y=130)
    number_check.deselect()
    symbol_check = Checkbutton(frame3, text='Symbols', variable=symbol_var,font=("helvetica", 13), bg='white',onvalue='on', offvalue='off')
    symbol_check.place(x=525, y=180)
    symbol_check.deselect()
    generate_entry = Entry(frame3, width=40, font=("helvetica", 15),relief="ridge", borderwidth=1)
    generate_entry.place(x=150, y=20, height=35)
    add_image = ImageTk.PhotoImage(file="button_add.png")
    update_img = ImageTk.PhotoImage(file="button_update.png")
    delete_img = ImageTk.PhotoImage(file="button_delete.png")
    title = Label(text="Password Manager", font=("Oswald", 30, "bold"), bg="white")
    title.place(x=590, y=60)
    web_label = Label(frame2, text="Website or App Name", font=("helvetica",20), bg="white")
    web_label.place(x=40, y=50)
    username_label = Label(frame2, text="Username", font=("helvetica", 20), bg="white")
    username_label.place(x=40, y=150)
    password_label = Label(frame2, text="Password", font=("helvetica", 20,), bg="white")
    password_label.place(x=40, y=250)
    mail_label = Label(frame2, text="Email Id", font=("helvetica", 20), bg="white")
    mail_label.place(x=40, y=350)
    website_entry = Entry(frame2, width=40, font=("helvetica", 15), relief="ridge", borderwidth=1)
    website_entry.focus()
    website_entry.place(x=40, y=100, height=25)
    username_entry = Entry(frame2, width=40, font=("helvetica", 15),relief="ridge", borderwidth=1)
    username_entry.place(x=40, y=200, height=25)
    password_entry = Entry(frame2, width=40, font=("helvetica", 15),relief="ridge", borderwidth=1)
    password_entry.place(x=40, y=300, height=25)
    mail_entry = Entry(frame2, width=40, font=("helvetica", 15), relief="ridge", borderwidth=1)
    mail_entry.place(x=40, y=400, height=25)
    add_btn = Button(frame2, image=add_image, borderwidth=0, bg="white",command=save)
    add_btn.place(x=15, y=480)
    update_btn = Button(frame2, image=update_img, bg="white", borderwidth=0,command=update)
    update_btn.place(x=210, y=480)
    delete_btn = Button(frame2, image=delete_img, bg="white", borderwidth=0,command=delete)
    delete_btn.place(x=410, y=480)




# ==================== Treeview================
def get_cursor(event):
     cursor_row = password_tree.focus()
     contents = password_tree.item(cursor_row)
     row = contents['values']
     clear()
     website_entry.insert(0, row[0])
     username_entry.insert(0, row[1])
     password_entry.insert(0, row[2])
     mail_entry.insert(0, row[3])


frame4 = Frame(frame1, width=800, height=300, bg="white", borderwidth=1,relief="solid")
frame4.place(x=650, y=420)

style = ttk.Style()
style.configure("Treeview", rowheight=28)
style.map("Treeview", background=[('selected', '#ea5455')])
password_tree = ttk.Treeview(frame4, columns=("website", "username","password", "mail_id"))
password_tree.tag_configure('oddrow', background='white')
password_tree.tag_configure('evenrow', background='#ffcccb')
password_tree.column("website", width=140)
password_tree.heading("username", text="Username", anchor="w")
password_tree.heading("website", text="Website", anchor="w")
password_tree.heading("password", text="Password", anchor="w")
password_tree.heading("mail_id", text="Email", anchor="w")
password_tree['show'] = 'headings'
password_tree.pack(expand=True, fill=BOTH)
password_tree.bind("<ButtonRelease-1>", get_cursor)

def fetch_data():
    count = 0
    db = mysql.connector.connect(host='localhost',user='root', passwd='root',database="password_manager")
    cur = db.cursor()cur.execute("SELECT * FROM UserData ")
    rows = cur.fetchall()
    if len(rows) != 0:
        password_tree.delete(*password_tree.get_children())
        for row in rows:
            if count % 2 == 0:
                password_tree.insert(parent='', index=END, values=row, tags='evenrow')
                db.commit()
            else:
                password_tree.insert(parent='', index=END, values=row, tags='oddrow')
                db.commit()
    count += 1
    db.close()
    fetch_data()
    window.mainloop()
    


    
     
 File:   #________________datacreation&connection________________#
# ---------------Database Creation------------
import mysql.connect
db = mysql.connector.connect(host='localhost',user='root',passwd='root')
cur=db.cursor()
cur.execute("CREATE DATABASE password_manager")


#----------Table Creation----------
import mysql.connect
db = mysql.connector.connect(host='localhost',user='root', passwd='root',database="password_manager")
cur = db.cursor()
cur.execte(“CREATE TABLE useraccounts (userID int PRIMARY KEYAUTO_INCREMENT, Username VARCHAR(30), Password VARCHAR(30)”)
cur.execte(“CREATE TABLE userdata (Website VARCHAR(50), UsernameVARCHAR(30), Password VARCHAR(30), Email_id VARCHAR(30)” )

db.commit()
