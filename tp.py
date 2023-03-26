from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image, ImageDraw
from manage import *
from ipaddress import *
from config import *
from datetime import *

newWindow = Tk()
newWindow.title("EIGRP Routing")
newWindow.geometry("480x200")
newWindow.config(background="black")

# heading label
Label(newWindow, text="Network Address :",font='Verdana 10 bold', foreground= "white", bg="black").place(x=30, y= 40)
Label(newWindow, text="Autonomous-System No.:",font='Verdana 10 bold', foreground= "white", bg="black").place(x=30, y= 90 )

# Entry Box
networkIP = StringVar()
as_number = StringVar()

Entry(newWindow, width=20, textvariable= networkIP,font='Verdana 10 bold').place(x=250, y=40)
Entry(newWindow, width=20, textvariable= as_number,font='Verdana 10 bold').place(x=250, y=90)

def check():
    try:
        IPv4Network(networkIP.get())

        config = {
        'deviceID' : '00oekd',
        'Name':'Static Routing',
        'Username': 'admin',
        'Password': 'cisco',
        'Enable': 'cisco',
        'IP': '192.168.10.5',
        'Network-IP': networkIP.get(),
        'Version': as_number.get(),
        'Last_Modify': datetime.today()
        }
        routing(config, newWindow)
    except ValueError as e:
        messagebox.showerror("Error", e ,parent=newWindow)



# # button config
Button(newWindow, text="Config",font='Verdana 10 bold', width= 30, bg="#E9FF33", command= check).place(x= 100, y= 150)
newWindow.mainloop()
