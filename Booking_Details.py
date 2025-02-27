from tkinter import *
from tkinter import messagebox
import sqlite3
import random

root=Tk()
with sqlite3.connect('Bus_Booking.db') as con:
    cur=con.cursor()
root.title("Bus Booking System")
h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
#bus image
busImage=PhotoImage(file='.\\Bus_for_project.png')
home_Image=PhotoImage(file='.\\home.png')
Label(root,image=busImage).grid(row=0,column=0,padx=w//2.5,columnspan=3)
Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font='Arial 20 bold').grid(row=1,column=0,columnspan=4)
Label(root,text="Bus Ticket").grid(row=2,column=0,columnspan=3,pady=h//40)


passengerid=[111,112,113,114,115,116,117,118,119,1110,1111,1112,1113,1114,1115,1116,1117,1118,1119,1120,1121,11122,11123,11124,11125,11126,11127,11128,11129,11130]

temp=cur.execute('Select count(*) from Passenger_details')
idpasse=temp.fetchall()

temp1=cur.execute('Select * from Passenger_details where passengerID=?;',(passengerid[idpasse[0][0]-1],))
alldetails=temp1.fetchall()

final = Frame(root,relief='groove',bd=5)
final.grid(row = 3, column =0, columnspan=3)

#passengerName
passenger_text = Label(final, text = "Passenger: ")
passenger_text.grid(row =3, column=0)
passenger_text1 = Label(final, text = alldetails[0][0])
passenger_text1.grid(row =3, column=1)

#passengerseat
seats_text = Label(final, text = "No of seats: ")
seats_text.grid(row =4, column=0)
seats_text1 = Label(final, text = alldetails[0][1])
seats_text1.grid(row =4, column=1)

#Age
age_text = Label(final, text = "Age: ")
age_text.grid(row =5, column=0)
age_text1 = Label(final, text = alldetails[0][2])
age_text1.grid(row =5, column=1)

#booking_Ref
bookingref=Label(final, text = "Booking Ref: ")
bookingref.grid(row =6, column=0)
bookingref1=Label(final, text = alldetails[0][3])
bookingref1.grid(row =6, column=1)

#Travel_date
bookingref=Label(final, text = "Travel Date: ")
bookingref.grid(row =7, column=0)
bookingref1=Label(final, text = alldetails[0][4])
bookingref1.grid(row =7, column=1)

#gender
g_text = Label(final, text = "Gender: ")
g_text.grid(row =3, column=2)
g_text1 = Label(final, text = alldetails[0][10])
g_text1.grid(row =3, column=3)

#Mobile Number
phone_text = Label(final, text = "Phone: ")
phone_text.grid(row =4, column=2)
phone_text1 = Label(final, text = alldetails[0][5])
phone_text1.grid(row =4, column=3)

#Price
flare_text = Label(final, text = "Fare Rs: ")
flare_text.grid(row =5, column=2)
flare_text1 = Label(final, text =alldetails[0][6])
flare_text1.grid(row =5, column=3)

#Bus
detail_text = Label(final, text = "Bus Detail: ")
detail_text.grid(row =6, column=2)
detail_text1 = Label(final, text = alldetails[0][7])
detail_text1.grid(row =6, column=3)

#Booked on
booked_text = Label(final, text = "Booked On: ")
booked_text.grid(row =7, column=2)
booked_text1 = Label(final, text = alldetails[0][8])
booked_text1.grid(row =7, column=3)

#Boarding
point_text = Label(final, text = "Boarding Point: ")
point_text.grid(row =8, column=2)
point_text1 = Label(final, text = alldetails[0][9])
point_text1.grid(row =8, column=3)

price=alldetails[0][6]*alldetails[0][1]

last_text = Label(final, text = "Total amount Rs"+str(price)+" to be paid at the time of boarding the bus",font="Arial 8 italic")
last_text.grid(row =9, column=2)

messagebox.showinfo("Booking conformed", "Booked!!!")

root.mainloop()
