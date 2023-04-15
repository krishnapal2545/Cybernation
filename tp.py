from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image, ImageDraw
from manage import *
from ipaddress import *
from config import *
from datetime import *

newWindow = Tk()
newWindow.title("Virtual LAN")
newWindow.resizable(False,False)
newWindow.geometry("500x250")
newWindow.config(background="black")

# heading label
Label(newWindow, text="VLAN ID :", font='Verdana 10 bold',foreground="white", bg="black").place(x=30, y=40)
Label(newWindow, text="Name :", font='Verdana 10 bold',foreground="white", bg="black").place(x=30, y=80)
Label(newWindow, text="Interface :", font='Verdana 10 bold',foreground="white", bg="black").place(x=30, y=120)

# Entry Box
vlanID = StringVar()
name = StringVar()
inter = StringVar()

Entry(newWindow, width=20, textvariable= vlanID,font='Verdana 10 bold').place(x=250, y=40)
Entry(newWindow, width=20, textvariable=name,font='Verdana 10 bold').place(x=250, y=80)
Entry(newWindow, width=20, textvariable=inter,font='Verdana 10 bold').place(x=250, y=120)

def check():
    try:
        if vlanID.get() and name.get() and inter.get():
             pass
            # config = {
            #         'deviceID': self.device[0],
            #         'Name': 'VLAN',
            #         'Device_Type': self.device[10],
            #         'Username': self.device[7],
            #         'Password': self.device[8],
            #         'Enable': self.device[9],
            #         'IP': self.device[3],
            #         'Vlan-ID': networkIP.get(),
            #         'Vlan-Name': networkSub.get(),
            #         'Interface-ID':processID.get(),
            #         'Last_Modify': datetime.today()
            # }
            # routing(config, newWindow)
        else:
            messagebox.showerror("Error", "Information can not be left blank" ,parent=newWindow)
    except ValueError as e:
            messagebox.showerror("Error", e, parent=newWindow)

# # button config
Button(newWindow, text="Config", font='Verdana 10 bold', width=30, bg="#FFFFFF", command=check).place(x=100, y= 190)
newWindow.mainloop()
