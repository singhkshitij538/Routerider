from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Bus Booking System")
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
img=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=img).grid(row=0,column=0,columnspan=3,padx=w//2.5)

Label(root,text="Online Bus Booking System",fg="Red",bg="LightBlue",font="Arial 20 bold").grid(row=1,column=0,columnspan=3)

#Seat booking page
def seat_booking_page(x=0):
    root.destroy()
    import Seat_Booking_page

#Check Booked page
def check_booking_page(y=0):
    root.destroy()
    import Checking_booking

#Add Bus Details page
def add_bus_details_page(z=0):
    root.destroy()
    import Add_new_bus_details_page

#Buttons
b1=Button(root,text="Seat Booking", font='Arial 15 bold',bg='pale green',command=seat_booking_page).grid(row=2,column=0)
b2=Button(root,text="Check Booked Seat", font='Arial 15 bold',bg='lime green', command=check_booking_page).grid(row=2,column=1)
b3=Button(root,text="Add Bus Details", font='Arial 15 bold',bg='dark green',command=add_bus_details_page).grid(row=2,column=2,pady=h//15)

Label(root,text="For Admin Only",font='Arial 10 bold',fg="Red").grid(row=5,column=2)
root.mainloop()
