from tkinter import *
from tkinter import messagebox
import sqlite3
root=Tk()
root.title("Bus Booking System")
with sqlite3.connect('Bus_Booking.db') as con:
    cur=con.cursor()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))

#Bus image 
busImage=PhotoImage(file='.//Bus_for_project.png')
homeImage=PhotoImage(file='.//home.png')
Label(root,image=busImage).grid(row=0,column=0,padx=w//2.5,columnspan=15)

#online bus booking system
Label(root,text='Online Bus Booking System',fg='Red',bg='LightBlue1',font='Arial 25 bold').grid(row=1,column=0,columnspan=15)
Label(root,text='Add Bus Route Details',fg='green',font='Arial 20 bold').grid(row=2,column=0,pady=h/40,columnspan=15)

def checkname(name):
    return name.isalpha()

def checknum(num):
    return num.isnumeric()

def checking2():
    root.destroy()
    import Home_page


def check():
    if len(route.get())==0 or len(sname.get())==0 or len(stationid.get())==0 or len(dname.get())==0 or len(destinationid.get())==0:
        messagebox.showerror("value Error","Enter Details Properly")
    else:
        if checknum(route.get())==False:
            messagebox.showerror("value Error","Enter Details Properly")
        elif checkname(sname.get())==False:
            messagebox.showerror("value Error","Enter Details Properly")
        elif checknum(stationid.get())==False:
            messagebox.showerror("value Error","Enter Details Properly")
        elif checkname(dname.get())==False:
            messagebox.showerror("value Error","Enter Details Properly")
        elif checknum(destinationid.get())==False:
            messagebox.showerror("value Error","Enter Details Properly")
        else:
            showdetails()
            route.delete(0,END)
            sname.delete(0,END)
            stationid.delete(0,END)
            destinationid.delete(0,END)
            dname.delete(0,END)

def check1():
    if len(route.get())==0 or len(sname.get())==0 or len(stationid.get())==0 or len(dname.get())==0 or len(destinationid.get())==0:
        messagebox.showerror("value Error","Enter Details Properly")
    else:
        if checknum(route.get())==False:
            messagebox.showerror("value Error","Enter Details Properly")
        elif checkname(sname.get())==False:
            messagebox.showerror("value Error","Enter Details Properly")
        elif checknum(stationid.get())==False:
            messagebox.showerror("value Error","Enter Details Properly")
        elif checkname(dname.get())==False:
            messagebox.showerror("value Error","Enter Details Properly")
        elif checknum(destinationid.get())==False:
            messagebox.showerror("value Error","Enter Details Properly")
        else:
            r=route.get()
            s=sname.get()
            sid=stationid.get()
            did=destinationid.get()
            d=dname.get()
            cur.execute('Delete from Route where Route_ID=? and stationName=? and Station_ID=? and destinationName=? and destinatin_ID=?;',(r,s,sid,d,did,))

def insertintodata(*args):
    routte=route.get()
    name=sname.get()
    station=stationid.get()
    ddname=dname.get()
    destation=destinationid.get()
    cur.execute('''insert into Route(Route_ID, Station_ID, stationName, destinationName, Destination_ID) values(?,?,?,?,?);''',(routte,station,name,ddname,destation))
    con.commit()
    messagebox.showinfo('Route Entry','Added Succesfully')

def showdetails():
    insertintodata()
    Label(root,text='Route Details',fg='Red',bg='LightBlue1',font='Arial 15').grid(row=6,column=0, columnspan=15,pady=h//30)
    Label(root,text='Route ID: ',font='Arial 13').grid(row=7,column=3)
    Label(root,text=route.get(),font='Arial 13').grid(row=7,column=4)
    Label(root,text='Station Name: ',font='Arial 13').grid(row=7,column=5)
    Label(root,text=sname.get(),font='Arial 13').grid(row=7,column=6)
    Label(root,text='Station Id: ',font='Arial 13').grid(row=7,column=7)
    Label(root,text=stationid.get(),font='Arial 13').grid(row=7,column=8)
    Label(root,text='Destination Name: ',font='Arial 13').grid(row=7,column=5)
    Label(root,text=dname.get(),font='Arial 13').grid(row=7,column=6)
    Label(root,text='Destination Id: ',font='Arial 13').grid(row=7,column=7)
    Label(root,text=destinationid.get(),font='Arial 13').grid(row=7,column=8)

    
#Route ID
Label(root,text='Route ID',font='Arial 10').grid(row=3,column=3)
route=Entry(root)
route.grid(row=3,column=4)

#Station Name
Label(root,text='Station Name',font='Arial 10').grid(row=3,column=5)
sname=Entry(root)
sname.grid(row=3,column=6)

#Station Name
Label(root,text='Station ID',font='Arial 10').grid(row=3,column=7)
stationid=Entry(root)
stationid.grid(row=3,column=8)

#Destination ID
Label(root,text='Destination Name',font='Arial 10').grid(row=3,column=9)
dname=Entry(root)
dname.grid(row=3,column=10)

#destination Name
Label(root,text='Destination ID',font='Arial 10').grid(row=3,column=11)
destinationid=Entry(root)
destinationid.grid(row=3,column=12)

# Buttons for add edit and home
Button(root,text='Add Route',font='Arial 10',bg='pale green',command=check).grid(row=3,column=13)
Button(root,text='Delete Route',font='Arial 10',bg='pale green',fg="Red",command=check1).grid(row=3,column=14)
Button(root,image=homeImage,font='Arial 10',bg='pale green',command=checking2).grid(row=5,column=8,pady=h/10)

root.mainloop()