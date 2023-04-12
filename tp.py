from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image, ImageDraw
from manage import *
from ipaddress import *
from config import *
from datetime import *
import json

newWindow = Tk()
newWindow.title("OSPF Routing")
newWindow.resizable(False,False)
newWindow.geometry("500x250")
newWindow.config(background="black")

# heading label
Label(newWindow, text="Process ID :", font='Verdana 10 bold',foreground="white", bg="black").place(x=30, y=40)
Label(newWindow, text="Network IP Address :", font='Verdana 10 bold',foreground="white", bg="black").place(x=30, y=80)
Label(newWindow, text="Network Subnet Mask :", font='Verdana 10 bold',foreground="white", bg="black").place(x=30, y=120)
Label(newWindow, text="Area :", font='Verdana 10 bold',foreground="white", bg="black").place(x=30, y=160)

# Entry Box
processID = StringVar()
networkIP = StringVar()
networkSub = StringVar()
area = StringVar()

Entry(newWindow, width=20, textvariable= processID,font='Verdana 10 bold').place(x=250, y=40)
Entry(newWindow, width=20, textvariable=networkIP,font='Verdana 10 bold').place(x=250, y=80)
Entry(newWindow, width=20, textvariable=networkSub,font='Verdana 10 bold').place(x=250, y=120)
Entry(newWindow, width=20, textvariable= area,font='Verdana 10 bold').place(x=250, y=160)

def check():
    try:
        IPv4Network(networkIP.get())
        IPv4Address(networkSub.get())
        # config = {
        #         'deviceID': self.device[0],
        #         'Name': 'RIP Routing',
        #         'Device_Type': self.device[10],
        #         'Username': self.device[7],
        #         'Password': self.device[8],
        #         'Enable': self.device[9],
        #         'IP': self.device[3],
        #         'Network-IP': networkIP.get(),
        #         'Network-SubIP': networkSub.get(),
        #         'Process-ID':processID.get(),
        #         'Area': area.get(),
        #         'Last_Modify': datetime.today()
        # }
        # routing(config, newWindow)
    except ValueError as e:
            messagebox.showerror("Error", e, parent=newWindow)

# # button config
Button(newWindow, text="Config", font='Verdana 10 bold', width=30, bg="#9FFF5A", command=check).place(x=100, y= 210)
newWindow.mainloop()
