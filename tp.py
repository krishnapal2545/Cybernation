from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageDraw


newWindow = Tk()
newWindow.title("Device New Configuration")
newWindow.resizable(False,False)
newWindow.geometry("430x450")
newWindow.configure(bg='white')
        
#image
device_img = PhotoImage(file='images\device.png')
device_info = Label(newWindow, image= device_img, bg='white')
device_info.pack()
device_info.place(x=130, y= 20)

Label(newWindow, text="Configurations :- ", font='Verdana 15 bold', bg='white').place(x=10, y=150)

Button(newWindow, width= 15, height= 3, text="Default Routing", bg="#FF33B2").place(x = 50, y= 200)
Button(newWindow, width= 15, height= 3, text="Static Routing", bg="#33FFE9").place(x = 250, y= 200)

Button(newWindow, width= 15, height= 3, text="RIP Routing", bg="#A533FF").place(x = 50, y= 275)
Button(newWindow, width= 15, height= 3, text="OSPF Routing", bg="#ff1111").place(x = 250, y= 275)

Button(newWindow, width= 15, height= 3, text="BGP Routing", bg="#33FF5B").place(x = 50, y= 350)
Button(newWindow, width= 15, height= 3, text="EIGRP Routing", bg="#E9FF33").place(x = 250, y= 350)

newWindow.mainloop()
