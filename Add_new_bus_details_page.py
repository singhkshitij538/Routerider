from tkinter import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

#Adding bus image 
busImage=PhotoImage(file='.\\Bus_for_project.png')
Label(root,image=busImage).grid(row=0,column=0,padx=w//2.5,columnspan=12)

#Adding text
Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font='Arial 20 bold').grid(row=1,column=0,columnspan=12)

#Page Detail
Label(root,text='Add New Details to Database',fg='green',font='Arial 15 bold').grid(row=2,column=0,pady=h/40,columnspan=12)

def seat_booking_page1(x=0):
    root.destroy()
    import New_Operator
def seat_booking_page2(x=0):
    root.destroy()
    import New_Bus

def seat_booking_page3(x=0):
    root.destroy()
    import New_Route

def seat_booking_page4(x=0):
    root.destroy()
    import New_Run



#Buttons
Button(root,text='New Operator',bg='pale green',font='Arial 15',command=seat_booking_page1).grid(row=3,column=4)
Button(root,text='New Bus',font='Arial 15',bg='salmon1',command=seat_booking_page2).grid(row=3,column=5)
Button(root,text='New Route',font='Arial 15',bg='cornflower Blue',command=seat_booking_page3).grid(row=3,column=6)
Button(root,text='New Run',font='Arial 15',bg='indian red',command=seat_booking_page4).grid(row=3,column=7)

root.mainloop()
