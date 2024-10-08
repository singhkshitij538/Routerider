from tkinter import *
from tkinter import messagebox
import sqlite3
import random

root=Tk()
with sqlite3.connect('Bus_Booking.db') as con:
    cur=con.cursor()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
root.title("Bus Booking System")
busImage=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=busImage).grid(row=0,column=0,padx=w//2.5,columnspan=12)
Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font='Arial 20 bold').grid(row=1,column=0,columnspan=12,pady=h/50)
Label(root,text='Check Bus Booking',fg='dark green',font='Arial 15 bold',bg='pale green').grid(row=2,column=0,columnspan=12)
Label(root,text='Enter Your Mobile No:',font='Arial 10 bold').grid(row=3,column=4,pady=h/50)
mobNumber=Entry(root)
mobNumber.grid(row=3,column=5)
def checknumber(s):
    count=0
    for i in s:
        if i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
            count+=1
    if count==10:
        return True
    else:
        return False
def entrycheck():
    if len(mobNumber.get())!=10:
        messagebox.showerror('Value missing','Enter correct Mobile Number')
    elif checknumber(mobNumber.get())==False:
        messagebox.showerror('Invalid input','Enter number properly')
    else:
        mobile=mobNumber.get()
        temp=cur.execute('Select * from Passenger_details where Phone=?;',(mobile,))
        alldetails=temp.fetchall()
        final = Frame(root,relief='groove',bd=5)
        final.grid(row = 5, column =4, columnspan=3,pady=h//20)
        #passengerName
        passenger_text = Label(final, text = "Passenger: ")
        passenger_text.grid(row =5, column=0)
        passenger_text1 = Label(final, text = alldetails[0][0])
        passenger_text1.grid(row =5, column=1)

        #passengerseat
        seats_text = Label(final, text = "No of seats: ")
        seats_text.grid(row =6, column=0)
        seats_text1 = Label(final, text = alldetails[0][1])
        seats_text1.grid(row =6, column=1)

        #Age
        age_text = Label(final, text = "Age: ")
        age_text.grid(row =7, column=0)
        age_text1 = Label(final, text = alldetails[0][2])
        age_text1.grid(row =7, column=1)

        #booking_Ref
        bookingref=Label(final, text = "Booking Ref: ")
        bookingref.grid(row =8, column=0)
        bookingref1=Label(final, text = alldetails[0][3])
        bookingref1.grid(row =8, column=1)

        #Travel_date
        bookingref2=Label(final, text = "Travel Date: ")
        bookingref2.grid(row =9, column=0)
        bookingref3=Label(final, text = alldetails[0][4])
        bookingref3.grid(row =9, column=1)

        #gender
        g_text = Label(final, text = "Gender: ")
        g_text.grid(row =5, column=2)
        g_text1 = Label(final, text = alldetails[0][10])
        g_text1.grid(row =5, column=3)

        #Mobile Number
        phone_text = Label(final, text = "Phone: ")
        phone_text.grid(row =6, column=2)
        phone_text1 = Label(final, text = alldetails[0][5])
        phone_text1.grid(row =6, column=3)

        #Price
        flare_text = Label(final, text = "Fare Rs: ")
        flare_text.grid(row =7, column=2)
        flare_text1 = Label(final, text =alldetails[0][6])
        flare_text1.grid(row =7, column=3)

        #Bus
        detail_text = Label(final, text = "Bus Detail: ")
        detail_text.grid(row =8, column=2)
        detail_text1 = Label(final, text = alldetails[0][7])
        detail_text1.grid(row =8, column=3)

        #Booked on
        booked_text = Label(final, text = "Booked On: ")
        booked_text.grid(row =9, column=2)
        booked_text1 = Label(final, text = alldetails[0][8])
        booked_text1.grid(row =9, column=3)

        #Boarding
        point_text = Label(final, text = "Boarding Point: ")
        point_text.grid(row =10, column=2)
        point_text1 = Label(final, text = alldetails[0][9])
        point_text1.grid(row =10, column=3)

        price=alldetails[0][6]*alldetails[0][1]
        last_text = Label(final, text = "Total amount Rs"+str(price)+" to be paid at the time of boarding the bus",font="Arial 8 italic")
        last_text.grid(row =11, column=2)


Button(root,text='Check Booking',command=entrycheck).grid(row=3,column=6)


root.mainloop()