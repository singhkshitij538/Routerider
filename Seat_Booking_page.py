from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import sqlite3
import random

root=Tk()
root.title("Bus Booking System")
with sqlite3.connect('Bus_Booking.db') as con:
    cur=con.cursor()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

#gender drop_menu options
gender_type=StringVar()
gender_type.set("Gender")
options_gender_type=["Male","Female","Others"]

#adding bus image to the page
busImage=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=busImage).grid(row=0,column=0,padx=w//2.5,columnspan=8)

#Adding Application name
Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font='Arial 20 bold').grid(row=1,column=0,columnspan=8)
Label(root,text='Enter Journey Details',bg='pale green',fg='dark green',font='Arial 15 bold').grid(row=2,column=0,columnspan=8,pady=h//20)

#function to check if all fields are filled or not

def checkTo(boarding):
    return boarding.isalpha()

def checkFrom(destinate):
    return destinate.isalpha()

def checkDate(datee):
    s=[]
    s=datee.split('-')
    if len(s)==3:
        if s[0].isnumeric() and s[1].isnumeric() and s[2].isnumeric():
            if (int)(s[2])>=1 and (int)(s[2])<=31:
                if (int)(s[1])>=1 and (int)(s[1])<=12:
                    if len(s[0])==4:
                        return True
                    else:
                        False
                else:
                    False
            else:
                False
        else:
            False
    else:
        False
        

def check_seat_mob_age(num):
    return num.isnumeric()

def bookingref():
    return (random.randint(10000,99999))

#yes no and the end
def sure(name,seats,mobile,age,JDate,going,idd):
    booking_ref=bookingref()
    bkddate=cur.execute("Select Date('now')")
    bookedDate=bkddate.fetchall()
    fare=cur.execute('Select distinct Fare from Bus where Bus_ID=?;',(idd,))
    faree=fare.fetchall()
    avail=cur.execute('Select distinct Seats_Available from Run where Bus_ID=?;',(idd,))
    leftseat=avail.fetchall()
    x=(int)(seats)
    seatleft=leftseat[0][0]-x
    cur.execute('Update Run set Seats_Available=? where Bus_ID=?;',(seatleft,idd,))
    price=faree[0][0]*x
    mobilee=(int)(mobile)
    temp=cur.execute('Select count(*) from Passenger_details')
    idpass=temp.fetchall()
    operatorName=cur.execute('Select op.Name from Bus as b, Operator as op where op.Operator_ID=b.Operator_ID and b.Bus_ID=?;',(idd,))
    operatorNamee=operatorName.fetchall()
    passengerid=[111,112,113,114,115,116,117,118,119,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,11122,11123,11124,11125,11126,11127,11128,11129,11130]
    messagebox.askyesno("bus confirmation", "You sure want to book bus")
    passengerDetails=cur.execute('''insert into Passenger_details(Passenger,Seats,Age,Booking_ref,travelDate,Phone,Fare,Bus_details,Booked_date,Boarding_point,Gender,passengerID)
     values(?,?,?,?,?,?,?,?,?,?,?,?);''',(name,seats,age,booking_ref,JDate,mobilee,price,operatorNamee[0][0],bookedDate[0][0],going,gender_type.get(),passengerid[idpass[0][0]]))
    con.commit()
    root.destroy()
    import Booking_Details

    
def checkFilling():
    if len(goingTo.get())==0:
        messagebox.showerror('Value missing','Enter Boarding')
    elif len(destination.get())==0:
        messagebox.showerror('Value missing','Enter Destination')
    elif len(Jdate.get())==0:
        messagebox.showerror('Value missing','Enter Date')
    else:
        if checkTo(goingTo.get())==True and checkFrom(destination.get())==True and checkDate(Jdate.get())==True:
            showDetails(Jdate.get(),destination.get(),goingTo.get())
        else:
            messagebox.showerror('Invalid Entry',"Enter Details Properly")

name_entt=''
mobile_entt=0
age_entt=0
seats_entt=0

def showDetails(Jdate,fromm,tto):
    temp=cur.execute('''Select distinct op.Name ,b.Type, b.Capacity, b.Fare, b.Bus_ID from Operator as op, Bus as b, Route as r, Run as rn
      where r.Route_ID=b.Route_ID and op.Operator_ID=b.Operator_ID and rn.Date=? and rn.Bus_ID=b.Bus_ID and r.stationName=? and 
      r.destinationName=?;''',(Jdate,tto,fromm,))
    details=temp.fetchall()
    select_text = Label(root, text = "Select Bus", fg = "green",pady=h//30)
    select_text.grid(row = 4, column=0)
    opt_text = Label(root, text = "Operator", fg = "green")
    opt_text.grid(row = 4, column=1)

    type_text = Label(root, text = "Bus Type", fg = "green")
    type_text.grid(row = 4, column=2)

    available_text = Label(root, text = "Available/Capacity", fg = "green")
    available_text.grid(row = 4, column=3)

    fare_text = Label(root, text = "Fare", fg = "green")
    fare_text.grid(row = 4, column=4)

    j=1
    x=5
    ip_type=IntVar()
    for i in range(0,len(details)):
        r=ttk.Radiobutton(root,text='Bus'+str(j),variable=ip_type, value=details[i][4])
        r.grid(row=5+i,column=0)
        temp1=cur.execute('''Select distinct rn.Seats_Available from Operator as op, Bus as b, Run as rn where op.Operator_ID=b.Operator_ID and b.Bus_ID=rn.Bus_ID and b.Capacity=?;''',(details[i][2],))
        xyz=temp1.fetchall()
        Label(root,text=details[i][0]).grid(row=5+i,column=1)
        Label(root,text=details[i][1]).grid(row=5+i,column=2)
        Label(root,text=str(xyz[0][0])+"/"+str(details[i][2])).grid(row=5+i,column=3)
        Label(root,text=details[i][3]).grid(row=5+i,column=4)
        x+=1
        j+=1
    book_button = Button(root, text="Proceed to Book", bg = "lightgreen", command =lambda:book(ip_type.get(),x,Jdate,fromm))
    book_button.grid(row =5 , column= 5, pady=h//50)

def book(idd,x,JDate,going):
     fill_label = Label(root, text = "Fill Passenger Details to book the bus ticket" , fg = 'red' , bg = 'lightblue', font = 'Arian 14 bold')
     fill_label.grid(row = x+1, column = 0, columnspan = 8,pady=h//30)

     name_text = Label(root, text = "Name")
     name_text.grid(row = x+2, column=0)

     name_ent = Entry(root)
     name_ent.grid(row =x+2, column=1)
     name_entt=name_ent.get()

     Label(root,text='Gender',font='Arial 13').grid(row=x+2,column=2)
     d_menu=OptionMenu(root,gender_type,*options_gender_type)
     d_menu.grid(row=x+2,column=3)

     seats_text = Label(root, text = "No of Seats")
     seats_text.grid(row = x+2, column=4)

     seats_ent = Entry(root)
     seats_ent.grid(row =x+2, column=5)

     mobile_text = Label(root, text = "Mobile No")
     mobile_text.grid(row = x+2, column=6)

     mobile_ent = Entry(root)
     mobile_ent.grid(row =x+2, column=7)

     age_text = Label(root, text = "Age")
     age_text.grid(row = x+3, column=4,pady=h//50)

     age_ent = Entry(root)
     age_ent.grid(row =x+3, column=5)

     book_button = Button(root, text = "Book Seat", bg ="lightgreen", command =lambda:checking(name_ent.get(),seats_ent.get(),mobile_ent.get(),age_ent.get(),JDate,going,idd))
     book_button.grid(row = x+3, column=6)




           
def checking(name,seats,mobileNumber,age,JDate,going,idd):
    a=cur.execute('Select Seats_Available from Run where Bus_ID=?;',(idd,))
    enw=a.fetchall()
    cap=enw[0][0]
    capac=int(cap)
    def checkseatslimit(x):
        y=int(x)
        if capac>y and y>0:
            return True
        else:
            return False
    # aage=(int)(age)
    if len(name)==0:
        messagebox.showerror('Invalid Entry',"Enter Name Properly")
    elif len(str(mobileNumber))<10:
        messagebox.showerror('Invalid Entry',"Enter Number Properly")
    elif len(str(age))==0:
        messagebox.showerror('Invalid Entry',"Enter Age Properly")
    elif len(str(seats))==0 or checkseatslimit(seats)==False:
        messagebox.showerror    ('Invalid Entry',"Enter seats Properly")
    else:       
        if checkTo(name)==True and check_seat_mob_age(seats)==True and check_seat_mob_age(mobileNumber)==True and check_seat_age(age)==True:
            sure(name,seats,mobileNumber,age,JDate,going,idd)
        else:
            messagebox.showwarning('Invalid Entry',"Enter Details Properly")


#to
Label(root,text="To:").grid(row=3,column=0)
goingTo=Entry(root)
goingTo.grid(row=3,column=1)
tto=goingTo.get()

#from
Label(root,text="From:").grid(row=3,column=2)
destination=Entry(root)
destination.grid(row=3,column=3)
fromm=destination.get()

#Journey date
Label(root,text="Journey Date:").grid(row=3,column=4)
Label(root,text="(DD/MM/YYYY)").grid(row=4,column=5)

Jdate=Entry(root)
Jdate.grid(row=3,column=5)

#Buttons
Button(root,text="Show Bus",bg="pale green",command=checkFilling).grid(row=3,column=6)
#Button(root,image=home_Image).grid(row=3,column=7)

root.mainloop()