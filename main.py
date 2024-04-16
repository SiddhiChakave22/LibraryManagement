from tkinter import*
from PIL import Image,ImageTk,ImageDraw,ImageFont
import time
import mysql.connector
import mysql.connector

class Library:
    def __init__(self, master,img,img1,img2,img3,img4,img5,img6,img7):
        self.master = master
        self.img=img;
        self.img1=img1
        self.img2=img2
        self.img3=img3
        self.img4=img4
        self.img5=img5
        self.img6=img6
        self.img7=img7
        self.master.geometry("1600x1000")
        self.myconn=mysql.connector.connect(host="localhost",user="root",passwd="1234",database="library")
        self.mycursor=self.myconn.cursor()
        self.frame1=Frame(master)
        self.frame1.pack()
        self.canvas=Canvas(self.frame1, width=1600, height=1000)
        self.canvas.pack()
        self.welcome()

    def welcome(self):
        self.canvas.create_image(0, 0, image=self.img, anchor=NW)
        self.canvas.create_text(750, 150, text="WELCOME TO SAS LIBRARY", fill="white",font=('ALGERIAN',50))
        self.canvas.create_text(550,620,text='"One best book is equal to hundred good friends',fill="white",font=('lucida calligraphy',20))
        self.canvas.create_text(700,660,text='One good friend is equal to a Library"',fill="white",font=('lucida calligraphy',20))
        self.canvas.create_text(1000,730,text="~Dr.APJ Abdul Kalam",fill="white",font=('lucida calligraphy',20))
        Button(self.frame1,text="LOGIN",bg="black",fg="white",font=("bookman old style",20),command=self.login).place(x=1175,y=30)
        Button(self.frame1,text="REGISTER",bg="black",fg="white",font=("bookman old style",20),command=self.register).place(x=1325,y=30)
    
    def login(self):
        def login():
            self.v1=int(e1.get())
            v2=e2.get()
            val=(self.v1,v2)
            s1="SELECT * FROM student_data WHERE member_id=%s AND password=%s"
            self.mycursor.execute(s1,val)
            if (self.mycursor.fetchone()==None):
                self.canvas1.create_text(295,310,text="Invalid id or password!!",fill="red",font=("Times",15))
            else:
                self.homepage()
        self.canvas.delete("all")
        self.lb=Label(self.frame1)
        self.lb.place(x=0,y=0)
        self.lb.config(image=self.img1)
        self.canvas1=Canvas(self.frame1, width=500, height=500,bg="white")
        self.canvas1.place(x=500,y=100)
        self.canvas1.create_text(250,100,text="Login",fill="black",font=("Pristina",45))
        self.canvas1.create_text(95,202,text="Member Id",fill="black",font=("lucida fax",15))
        e1=Entry(self.frame1,width=18,font=('arial',18),bd=2)
        e1.place(x=700,y=290)

        self.canvas1.create_text(90,269,text="Password",fill="black",font=("lucida fax",15))
        e2=Entry(self.frame1,width=18,font=("arial",18),bd=2)
        e2.place(x=700,y=355)
        Button(self.frame1,width=300,height=60,bg="white",image=self.img2,bd=0,command=login).place(x=600,y=450)
    
    def register(self):
        def func():
            mem_id=int(e1.get())
            password=e2.get()
            name=e3.get()
            email=e4.get()
            if (len(e5.get())!=10):
                canvas.create_text(350,300,text="Invalid Mobile Number!!",fill="red",font=("Times",10))
            else:
                mob=int(e5.get())
            cl=self.menu.get()
            if(self.r.get()==1):
                gender="Male"
            else:
                gender="Female"
            val=(mem_id,password,name,email,mob,cl,gender)
            
            s1="INSERT INTO student_data VALUES (%s,%s,%s,%s,%s,%s,%s)"
            self.mycursor.execute(s1,val)
            self.myconn.commit()
        
        self.canvas.delete("all")
        self.lb=Label(self.frame1)
        self.lb.place(x=0,y=0)
        self.lb.config(image=self.img1)
        self.canvas1=Canvas(self.frame1, width=500, height=620,bg="white")
        self.canvas1.place(x=500,y=50)
        self.canvas1.create_text(250, 60, text="Register", fill="black",font=('pristina',40))

        self.canvas1.create_text(88, 150, text="Member id", fill="black",font=('lucinda',15))
        e1=Entry(self.frame1,width=20,font=('aerial',18),bd=2)
        e1.place(x=700,y=190)

        self.canvas1.create_text(85, 200, text="Password", fill="black",font=('lucinda',15))
        e2=Entry(self.frame1,width=20,font=('aerial',18),bd=2)
        e2.place(x=700,y=240)

        self.canvas1.create_text(102, 250, text="Student Name", fill="black",font=('lucinda',15))
        e3=Entry(self.frame1,width=20,font=('aerial',18),bd=2)
        e3.place(x=700,y=290)

        self.canvas1.create_text(75, 300, text="Email id", fill="black",font=('lucinda',15))
        e4=Entry(self.frame1,width=20,font=('aerial',18),bd=2)
        e4.place(x=700,y=340)

        self.canvas1.create_text(88, 350, text="Mobile No.", fill="black",font=('lucinda',15))
        e5=Entry(self.frame1,width=20,font=('aerial',18),bd=2)
        e5.place(x=700,y=390)

        self.canvas1.create_text(65, 400, text="Class", fill="black",font=('lucinda',15))

        self.canvas1.create_text(75, 450, text="Gender", fill="black",font=('lucinda',15))
        self.r=IntVar()
        self.r1=Radiobutton(self.frame1,text="Male",variable=self.r,value=1)
        self.r1.place(x=700,y=490)
        self.r2=Radiobutton(self.frame1,text="Female",variable=self.r,value=2)
        self.r2.place(x=780,y=490)
        self.menu=StringVar()
        self.menu.set("select your class")
        self.drop=OptionMenu(self.frame1,self.menu,"F.Y","S.E","T.E","B.E")
        self.drop.place(x=700,y=440)
        Button(self.frame1,width=400,height=50,bg="white",image=self.img3,bd=0,command=func).place(x=565,y=550)
    def homepage(self):
        self.canvas.delete("all")
        self.lb=Label(self.frame1)
        self.lb.place(x=0,y=0)
        self.lb.config(image=img1)
        def profile():
            self.canvas=Canvas(self.frame1,width=1500,height=1000)
            self.canvas.place(x=0,y=0)
            self.lb=Label(self.frame1)
            self.lb.config(image=self.img1)

            self.canvas.create_text(530,80,text="Profile",fill="black",font=("Pristina",40))

            self.canvas.create_text(200,153,text="Name",fill="black",font=("arial rounded mt bold",20))
            self.canvas.create_text(786,146,text="Member Id",fill="black",font=("arial rounded mt bold",20))
            self.canvas.create_text(210,300,text="Gender",fill="black",font=("arial rounded mt bold",20))
            self.canvas.create_text(815,300,text="Mobile Number",fill="black",font=("arial rounded mt bold",20))
            self.canvas.create_text(215,450,text="Email Id",fill="black",font=("arial rounded mt bold",20))
            self.canvas.create_text(750,446,text="Class",fill="black",font=("arial rounded mt bold",20))



            #PROFILE PAGE
            s1="SELECT * FROM student_data WHERE member_id=%s"
            self.mycursor.execute(s1,(self.v1,))
            x=self.mycursor.fetchone()
            self.canvas.create_text(750,196,text=str(x[0]),fill="black",font=("times",20))
            self.canvas.create_text(200,203,text=x[2],fill="black",font=("times",20))
            self.canvas.create_text(266,500,text=x[3],fill="black",font=("times",20))
            self.canvas.create_text(788,350,text=x[4],fill="black",font=("times",20))
            self.canvas.create_text(740,496,text=x[5],fill="black",font=("times",20))
            self.canvas.create_text(205,350,text=x[6],fill="black",font=("times",20))
            
            
        def home():
            self.b2=Button(self.frame1,text="Profile",bg="orange",fg="white",font=("times",15),width=5,command=profile).place(x=1200,y=60)
            self.b3=Button(self.frame1,text="History",bg="orange",fg="white",font=("times",15),width=5).place(x=1200,y=100)
            self.b4=Button(self.frame1,text="books",bg="orange",fg="white",font=("times",15),width=5).place(x=1200,y=140)
            self.b5=Button(self.frame1,text="Logout",bg="orange",fg="white",font=("times",15),width=5).place(x=1200,y=180)
        self.canvas1=Canvas(self.frame1,bg="black",width=1500,height=70)
        self.canvas1.place(x=0,y=0)
        #canvas=Canvas(root,width=1500,height=60,bg="black")
        #canvas.place(x=0,y=0)

        Label(self.frame1,text="SAS library",bg="black",fg="white",font=("Pristina",20)).place(x=10,y=20)
        self.b1=Button(self.frame1,text="Home",bg="orange",fg="white",font=("times",15),command=home)
        self.b1.place(x=1200,y=20)
        self.b2=Button(self.frame1,text="About",bg="orange",fg="white",font=("times",15)).place(x=1300,y=20)
        self.b2=Button(self.frame1,text="Contact Us",bg="orange",fg="white",font=("times",15)).place(x=1390,y=20)
        #for search
        self.e1=Entry(self.frame1,font=("arial",30),fg="black",bg="white",width=40)
        self.e1.place(x=300,y=100)
        Button(self.frame1,width=40,height=45,bg="white",image=self.img4).place(x=1150,y=100)

        #creating canvas for books
        self.canvas2=Canvas(self.frame1,width=1300,height=700)
        self.canvas2.place(x=100,y=250)

        self.c1=Label(self.frame1)
        self.c1.place(x=200,y=300)
        self.c1.config(image=self.img5)

        self.c2=Label(self.frame1)
        self.c2.place(x=600,y=300)
        self.c2.config(image=self.img6)

        self.c3=Label(self.frame1)
        self.c3.place(x=1000,y=300)
        self.c3.config(image=self.img7)



root=Tk()
root.title("library management")
root.configure(bg='grey')
img=Image.open("l1.jpg")
img=img.resize((1600,1000))
img=ImageTk.PhotoImage(img)

img1=Image.open("background.jpg")
img1=img1.resize((1600,1000))
img1=ImageTk.PhotoImage(img1)

img2=Image.open("login_btn.png")
img2=img2.resize((300,60))
img2=ImageTk.PhotoImage(img2)

img3=Image.open("register_btn.png")
img3=img3.resize((400,50))
img3=ImageTk.PhotoImage(img3)

img4=Image.open("search.jpg")
img4=img4.resize((40,50))
img4=ImageTk.PhotoImage(img4)

img5=Image.open("b1.jpg")
img5=img5.resize((300,300))
img5=ImageTk.PhotoImage(img5)

img6=Image.open("b2.jpg")
img6=img6.resize((300,300))
img6=ImageTk.PhotoImage(img6)

img7=Image.open("b3.jpg")
img7=img7.resize((300,300))
img7=ImageTk.PhotoImage(img7)


Library(root,img,img1,img2,img3,img4,img5,img6,img7)

mainloop()
