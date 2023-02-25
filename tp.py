from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image, ImageDraw
from manage import *
from ipaddress import *
from config import *
from datetime import *

newWindow = Tk()
newWindow.title("Static Routing")
newWindow.geometry("480x250")
newWindow.config(background="black")

# heading label
Label(newWindow, text="Destination Network Address :",font='Verdana 10 bold', foreground= "white", bg="black").place(x=20, y= 40)
Label(newWindow, text="Destination Subnet Mask :",font='Verdana 10 bold', foreground= "white", bg="black").place(x=20, y= 90 )
Label(newWindow, text="Next Hop :",font='Verdana 10 bold',foreground= "white", bg="black").place(x=20, y= 140)

# Entry Box
destIP = StringVar()
destSub = StringVar()
nextHop = StringVar()

Entry(newWindow, width=20, textvariable= destIP,font='Verdana 10 bold').place(x=270, y=40)
Entry(newWindow, width=20, textvariable= destSub,font='Verdana 10 bold').place(x=270, y=90)
Entry(newWindow, width=20, textvariable= nextHop,font='Verdana 10 bold').place(x=270, y=140)

def check():
    try:
        IPv4Network(destIP.get())
        IPv4Address(destSub.get())
        IPv4Address(nextHop.get())

        config = {
        'deviceID' : '00oekd',
        'Name':'Static Routing',
        'Username': 'admin',
        'Password': 'cisco',
        'Enable': 'cisco',
        'IP': '192.168.10.5',
        'Dest-IP': destIP.get(),
        'Dest-SubIP': destSub.get(),
        'NextHop': nextHop.get(),
        'Last_Modify': datetime.today()
        }
        routing(config, newWindow)
    except ValueError as e:
        messagebox.showerror("Error", e ,parent=newWindow)



# # button config
Button(newWindow, text="Config",font='Verdana 10 bold', width= 30, bg="#33FFE9", command= check).place(x= 100, y= 200)
newWindow.mainloop()
