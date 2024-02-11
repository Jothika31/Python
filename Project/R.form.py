                      #Student DATA Form

from tkinter import*
n=Tk()
n.geometry("500x500")
n.title("STUDENT FORM")
C=Canvas(n,bg="lightblue",height=900,width=1600)
C.pack()
Heading = Label(n,text = "STUDENT DATA FORM",width = 90,font = ("bold",20)).place(x=50,y=54)


def Submit():
    print("Submitted Successfully")

    
name=Label(n,text="Name",width = 15,font = ("times new roman",23)).place(x=95,y=100)
e1=Entry(n,width = 40).place(x=450,y=116)

Regno=Label(n,text="Reg no",width = 15,font = ("times new roman",23)).place(x=95,y=140)
e2=Entry(n,width = 40).place(x=450,y=156)

Email=Label(n,text="Email",width = 15,font = ("times new roman",23)).place(x=95,y=180)
e3=Entry(n,width = 40).place(x=450,y=196)

Aadhaar_no=Label(n,text="Aadhaar no",width = 15,font = ("times new roman",23)).place(x=95,y=220)
e4=Entry(n,width = 40).place(x=450,y=236)

Date_of_Birth=Label(n,text="Date of Birth",width = 15,font = ("times new roman",23)).place(x=95,y=260)
spin=Spinbox(n,from_=1,to=31 ,width = 5).place(x=450,y=276)
spin=Spinbox(n,from_=1,to=12 ,width = 5).place(x=510,y=276)
spin=Spinbox(n,from_=2000,to=2026 ,width = 5).place(x=580,y=276)

Blood_Group=Label(n,text="Blood Group",width = 15,font = ("times new roman",23)).place(x=95,y=300)
e6=Entry(n,width = 40).place(x=450,y=316)

Gender=Label(n,text="Gender",width = 15,font = ("times new roman",23)).place(x=95,y=340)
Radiobutton(n,text="Male",padx=5,value=1).place(x=450,y=356)
Radiobutton(n,text="Female",padx=10,value=2).place(x=520,y=356)
Radiobutton(n,text="Others",padx=15,value=3).place(x=610,y=356)

Nationality=Label(n,text="Nationality",width = 15,font = ("times new roman",23)).place(x=95,y=380)
e8=Entry(n,width = 40).place(x=450,y=396)

Religion=Label(n,text="Religion",width = 15,font = ("times new roman",23)).place(x=95,y=420)
e9=Entry(n,width = 40).place(x=450,y=436)

Caste=Label(n,text ="Caste",width = 15,font = ("times new roman",23)).place(x=95,y=460)
e10=Entry(n,width = 40).place(x=450,y=476)

Department=Label(n,text="Department",width = 15,font = ("times new roman",23)).place(x=95,y=500)
e11=Entry(n,width = 40).place(x=450,y=516)

Course_Name=Label(n,text="Course Name",width = 15,font = ("times new roman",23)).place(x=95,y=540)
e12=Entry(n,width = 40).place(x=450,y=556)

Degree=Label(n,text="Degree",width = 15,font = ("times new roman",23)).place(x=95,y=580)
e13=Entry(n,width = 40).place(x=450,y=596)

College_Name=Label(n,text="College Name",width = 15,font = ("times new roman",23)).place(x=95,y=620)
e14=Entry(n,width = 40).place(x=450,y=636)

Student_Num=Label(n,text="Student Number",width = 18,font = ("times new roman",23)).place(x=805,y=100)
e15=Entry(n,width = 40).place(x=1200,y=116)

Quota=Label(n,text="Quota",width = 18,font = ("times new roman",23)).place(x=805,y=140)
Checkbutton(n,text="GQ",variable=IntVar()).place(x=1200,y=156)
Checkbutton(n,text="MQ",variable=IntVar()).place(x=1300,y=156)

DaySch=Label(n,text="Day Scholar",width = 18,font = ("times new roman",23)).place(x=805,y=180)
Checkbutton(n,text="YES",variable=IntVar()).place(x=1200,y=196)
Checkbutton(n,text="NIL",variable=IntVar()).place(x=1300,y=196)

Host=Label(n,text="Hosteller",width = 18,font = ("times new roman",23)).place(x=805,y=220)
Checkbutton(n,text="YES",variable=IntVar()).place(x=1200,y=236)
Checkbutton(n,text="NIL",variable=IntVar()).place(x=1300,y=236)

Academic_Year=Label(n,text="Academic Year",width = 18,font = ("times new roman",23)).place(x=805,y=260)
spin=Spinbox(n,from_=2008,to=2030,width = 5).place(x=1200,y=276)
spin=Spinbox(n,from_=2008,to=2030 ,width = 5).place(x=1300,y=276)

Father_Name=Label(n,text="Father/Guardian Name",width = 18,font = ("times new roman",23)).place(x=805,y=300)
e5=Entry(n,width = 40).place(x=1200,y=316)

Father_Num=Label(n,text="Father Number",width = 18,font = ("times new roman",23)).place(x=805,y=340)
e7=Entry(n,width = 40).place(x=1200,y=356)

Mother_Name=Label(n,text="Mother Name",width = 18,font = ("times new roman",23)).place(x=805,y=380)
e16=Entry(n,width = 40).place(x=1200,y=396)

Mother_Num=Label(n,text="Mother Number",width = 18,font = ("times new roman",23)).place(x=805,y=420)
e17=Entry(n,width = 40).place(x=1200,y=436)

Mother_Tongue=Label(n,text="Mother Tongue",width = 18,font = ("times new roman",23)).place(x=805,y=460)
e18=Entry(n,width = 40).place(x=1200,y=476)

Address=Label(n,text="Address",width = 18,font = ("times new roman",23)).place(x=805,y=500)
e19=Entry(n,width = 40).place(x=1200,y=516)

City=Label(n,text="City",width = 18,font = ("times new roman",23)).place(x=805,y=540)
e19=Entry(n,width = 40).place(x=1200,y=556)

State=Label(n,text="State",width = 18,font = ("times new roman",23)).place(x=805,y=580)
e19=Entry(n,width = 40).place(x=1200,y=596)

Pincode=Label(n,text="Pincode",width = 18,font = ("times new roman",23)).place(x=805,y=620)
e19=Entry(n,width = 40).place(x=1200,y=636)

submit=Button(n,text="Submit",width=10,command=Submit).place(x=500,y=690)
Reset=Button(n,text="Reset",width=10).place(x=630,y=690)

n.mainloop()
