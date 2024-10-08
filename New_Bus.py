from tkinter import *
from tkinter import messagebox
import sqlite3
root=Tk()
root.title("Bus Booking System")
with sqlite3.connect('Bus_Booking.db') as con:
    cur=con.cursor()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

bus_type=StringVar()
bus_type.set("Bus Type")
options_Bus_Type=["AC 2X2","Non-AC 2X2","AC 3X2","Non-AC 3X2","AC Sleeper 2X1","Non-AC Sleeper 2X1"]
#Bus image 
busImage=PhotoImage(file='.\\Bus_for_project.png')
homeImage=PhotoImage(file='.\\home.png')
Label(root,image=busImage).grid(row=0,column=0,padx=w//2.5,columnspan=15)

def checkcapacity(cap):
    return cap.isnumeric()

def checkfare(num):
    return num.isnumeric()

def checking2():
    root.destroy()
    import Home_page

def checking():
    if len(busid.get())==0 or len(capacity.get())==0 or len(fare.get())==0 or len(operator.get())==0 or len(route.get())==0:
        messagebox.showerror('Value Error','Enter Details properly')
    else:
        if checkcapacity(capacity.get())==False:
            messagebox.showerror('Value Error','Enter Details properly')
        elif checkfare(fare.get())==False:
            messagebox.showerror('Value Error','Enter Details properly')
        else:
            insertintodata()


def checking1():
    if len(busid.get())==0 or len(capacity.get())==0 or len(fare.get())==0 or len(operator.get())==0 or len(route.get())==0:
        messagebox.showerror('Value Error','Enter Details properly')
    else:
        if checkcapacity(capacity.get())==False:
            messagebox.showerror('Value Error','Enter Details properly')
        elif checkfare(fare.get())==False:
            messagebox.showerror('Value Error','Enter Details properly')
        else:
            buss=busid.get()
            cap=capacity.get()
            price=fare.get()
            oprtr=operator.get()
            rout=route.get()
            bustype=bus_type.get()
            cur.execute('Update Bus set Type=? and Capacity=? and Fare=? and Route_ID=? Operator_ID=? where Bus_ID=?;',(bustype,cap,price,oprtr,rout,bustype,))

            
def insertintodata(*args):
    buss=busid.get()
    capacty=capacity.get()
    price=fare.get()
    optr=operator.get()
    routte=route.get()
    bustype=bus_type.get()
    cur.execute('''insert into bus(Bus_ID,Type,Capacity,Fare,Route_ID,Operator_ID) values(?,?,?,?,?,?);''',(buss,bustype,capacty,price,routte,optr))
    con.commit()
    con.close()
    messagebox.showinfo('Bus Entry','Added Succesfully')

#online bus booking system
Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font='Arial 25 bold').grid(row=1,column=0,columnspan=15)
Label(root,text='Add Bus Details',fg='green',font='Arial 20 bold').grid(row=2,column=0,pady=h/40,columnspan=15)

#Bus ID
Label(root,text='Bus ID',font='Arial 13').grid(row=3,column=2)
busid=Entry(root)
busid.grid(row=3,column=3)

#drop down menu option
Label(root,text='Bus Type',font='Arial 13').grid(row=3,column=4)
d_menu=OptionMenu(root,bus_type,*options_Bus_Type)
d_menu.grid(row=3,column=5)

#capacity
Label(root,text='Capacity',font='Arial 13').grid(row=3,column=6)
capacity=Entry(root)
capacity.grid(row=3,column=7)

#Fare Price
Label(root,text='Fare Rs.',font='Arial 13').grid(row=3,column=8)
fare=Entry(root)
fare.grid(row=3,column=9)

#Operator ID
Label(root,text='Operator ID',font='Arial 13').grid(row=3,column=10)
operator=Entry(root)
operator.grid(row=3,column=11)

#Route ID
Label(root,text='Route ID',font='Arial 13').grid(row=3,column=12)
route=Entry(root)
route.grid(row=3,column=13)

# Buttons for add edit and home
Button(root,text='Add',font='Arial 15',bg='pale green',command=checking).grid(row=4,column=7,pady=h/10)
Button(root,text='Edit',font='Arial 15',bg='pale green',command=checking1).grid(row=4,column=8)
Button(root,image=homeImage,font='Arial 15',bg='pale green',command=checking2).grid(row=4,column=9)

root.mainloop()