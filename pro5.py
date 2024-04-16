from tkinter import*
from PIL import ImageTk,Image
root=Tk()
root.geometry("1500x1000")
def home():
    b2=Button(root,text="Profile",bg="orange",fg="white",font=("times",15),width=5).place(x=1200,y=60)
    b3=Button(root,text="History",bg="orange",fg="white",font=("times",15),width=5).place(x=1200,y=100)
    b4=Button(root,text="books",bg="orange",fg="white",font=("times",15),width=5).place(x=1200,y=140)
    b5=Button(root,text="Logout",bg="orange",fg="white",font=("times",15),width=5).place(x=1200,y=180)
    


img1=Image.open("background.jpg")
lb=Label(root)
lb.place(x=0,y=0)
img1=img1.resize((1600,2000))
img1=ImageTk.PhotoImage(img1)
lb.config(image=img1)

#create frame for heading
f1=Frame(root,bg="black",width=500,height=70)
f1.pack(side=TOP,fill='x')
#canvas=Canvas(root,width=1500,height=60,bg="black")
#canvas.place(x=0,y=0)

Label(root,text="SAS library",bg="black",fg="white",font=("Pristina",20)).place(x=10,y=20)
b1=Button(root,text="Home",bg="orange",fg="white",font=("times",15),command=home)
b1.place(x=1200,y=20)
b2=Button(root,text="About",bg="orange",fg="white",font=("times",15)).place(x=1300,y=20)
b2=Button(root,text="Contact Us",bg="orange",fg="white",font=("times",15)).place(x=1390,y=20)
#for search
e1=Entry(root,font=("arial",30),fg="black",bg="white",width=40)
e1.place(x=300,y=100)
#puting search image as button
img=Image.open("search.jpg")
img=img.resize((40,50))
img=ImageTk.PhotoImage(img)
Button(root,width=40,height=45,bg="white",image=img).place(x=1150,y=100)

#creating canvas for books
canvas=Canvas(root,width=1300,height=700,relief=RIDGE,scrollregion=(0,0,2000,2000))
canvas.place(x=100,y=250)

##img2=Image.open("")


b1=Image.open("b1.jpg")
c1=Label(root)
c1.place(x=200,y=300)

b1=b1.resize((320,400))
b1=ImageTk.PhotoImage(b1)
c1.config(image=b1)

b2=Image.open("b2.jpg")
c2=Label(root)
c2.place(x=600,y=300)

b2=b2.resize((320,400))
b2=ImageTk.PhotoImage(b2)
c2.config(image=b2)


b3=Image.open("b3.jpg")
c3=Label(root)
c3.place(x=1000,y=300)

b3=b3.resize((320,400))
b3=ImageTk.PhotoImage(b3)
c3.config(image=b3)

v=Scrollbar(root)
v.place(x=1400,y=250)
v.config(command=canvas.yview)


##images=[b1,b2,b3]
##for i in images:
   



root.mainloop()
