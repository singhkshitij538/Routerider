from tkinter import *
root=Tk()
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry('%dx%d+0+0'%(w,h))
root.title("Bus Booking System")
busImage=PhotoImage(file=".\\Bus_for_project.png")
Label(root,image=busImage).grid(row=0,column=0,padx=(w//2.5))
Label(root,text="Online Bus Booking System",font='Arial 20 bold',fg='Red',bg="SkyBlue1").grid(row=1,column=0,pady=h//25)
Label(root,text="Name : Himanshu Kumar Mahto",font='Arial 11 bold',fg='Blue').grid(row=2,column=0,pady=h//50)
Label(root,text="Er : 211B137",fg="BLue",font='Arial 11 bold').grid(row=3,column=0,pady=h//50)
Label(root,text="Mobile : 9044707947",fg="BLue",font='Arial 11 bold').grid(row=4,column=0,pady=h//50)
Label(root,text="Submitted to : Dr. Mahesh Kumar",fg="Red",bg="SkyBlue1",font='Arial 20 bold').grid(row=5,column=0,pady=h//25)
Label(root,text="Project Based Learning",font='Arial 11 bold',fg="Red").grid(row=6,column=0)

def close(x=0):
    root.destroy()
    import Home_page

root.after(1000,close)

root.mainloop()
