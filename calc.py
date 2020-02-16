from tkinter import *
expression=""
m=0

def press(num):
    global expression
    expression=expression+str(num)
    var.set(expression)
    e1.config(fg="gray")
def equal(c):
    try:
        global expression
        toatl=str(eval(expression))
        var.set(toatl)
        e1.config(fg="green")
        expression=" "
    except(ZeroDivisionError):
        var.set("Can't divided by zero")
        expression=" "
        e1.config(fg="blue")
    except:
        var.set("Error")
        expression=" "
        e1.config(fg="red")
def allclear(c):
    global expression
    expression=" "
    var.set(" ")
def clear(c):
    global expression
    e1.delete(first=len(e1.get())-1,last=len(e1.get()))
    expression =e1.get()
    print(expression)



root=Tk()
root.title("Simple Calculator")
root.geometry("290x300")
root.wm_minsize(width=400,height=400)
root.wm_maxsize(width=400,height=400)

var=StringVar()
f0=Frame(root,bg="white")
f0.config(width=390,height=70)
f0.place(x=5,y=5)
f1=Frame(root,bg="gray")
f1.config(width=280,height=315)
f1.place(x=5,y=80)
f3=Frame(root,bg="lightblue")
f3.config(width=105,height=315)
f3.place(x=290,y=80)

e1=Entry(f0,width=22,font=("calibri",25,"bold"),fg="gray",textvariable=var)
e1.place(x=2,y=5)
l=Label(root,text="",font=("calibri",14),fg="red",bg="white")
l.place(x=240,y=45)






b0=Button(f1,text="0",width=6,height=1,font=("calibri",19,"bold"),command=lambda c="0":press(c))
b0.place(x=97,y=190)

b1=Button(f1,text="1",width=6,height=1,font=("calibri",19,"bold"),command=lambda c="1":press(c))
b1.place(x=5,y=10)

b2=Button(f1,text="2",width=6,height=1,font=("calibri",19,"bold"),command=lambda c="2":press(c))
b2.place(x=97,y=10)

b3=Button(f1,text="3",width=6,height=1,font=("calibri",19,"bold"),command=lambda c="3":press(c))
b3.place(x=190,y=10)

b4=Button(f1,text="4",width=6,height=1,font=("calibri",19,"bold"),command=lambda c="4":press(c))
b4.place(x=5,y=70)

b5=Button(f1,text="5",width=6,height=1,font=("calibri",19,"bold"),command=lambda c="5":press(c))
b5.place(x=97,y=70)

b6=Button(f1,text="6",width=6,height=1,font=("calibri",19,"bold"),command=lambda c="6":press(c))
b6.place(x=190,y=70)

b7=Button(f1,text="7",width=6,height=1,font=("calibri",19,"bold"),command=lambda c="7":press(c))
b7.place(x=5,y=130)

b8=Button(f1,text="8",width=6,height=1,font=("calibri",19,"bold"),command=lambda c="8":press(c))
b8.place(x=97,y=130)

b9=Button(f1,text="9",width=6,height=1,font=("calibri",19,"bold"),command=lambda c="9":press(c))
b9.place(x=190,y=130)

"""b_allclear=Button(f1,text="AC",width=6,height=1,font=("calibri",19,"bold"),command=lambda c="1":clear(c))
b_allclear.place(x=97,y=190)
"""
b_equal=Button(f1,text="=",width=6,height=1,font=("calibri",19,"bold"),command=lambda c="1":equal(c))
b_equal.place(x=190,y=190)

b_point=Button(f1,text=".",width=6,height=1,font=("calibri",19,"bold"),command=lambda c=".":press(c))
b_point.place(x=5,y=190)



b_par=Button(f1,text="(",width=6,height=1,font=("calibri",19,"bold"),command=lambda c="(":press(c))
b_par.place(x=5,y=250)

b_par2=Button(f1,text=")",width=6,height=1,font=("calibri",19,"bold"),command=lambda c=")":press(c))
b_par2.place(x=97,y=250)

b_allclear=Button(f1,text="AC",width=6,height=1,font=("calibri",19,"bold"),command=lambda c="4":allclear(c))
b_allclear.place(x=190,y=250)


b_clear=Button(f3,text="C",width=7,height=1,font=("calibri",19,"bold"),command=lambda c="1":clear(c))
b_clear.place(x=2,y=10)

b_add=Button(f3,text="+",width=7,height=1,font=("calibri",19,"bold"),command=lambda c="+":press(c))
b_add.place(x=2,y=70)

b_sub=Button(f3,text="-",width=7,height=1,font=("calibri",19,"bold"),command=lambda c="-":press(c))
b_sub.place(x=2,y=130)

b_mul=Button(f3,text="x",width=7,height=1,font=("calibri",19,"bold"),command=lambda c="*":press(c))
b_mul.place(x=2,y=190)

b_div=Button(f3,text="/",width=7,height=1,font=("calibri",19,"bold"),command=lambda c="/":press(c))
b_div.place(x=2,y=250)

root.mainloop()