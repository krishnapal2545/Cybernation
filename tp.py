from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image, ImageDraw
from ipaddress import *
from datetime import *
from main import *

newWindow = Tk()
newWindow.title("Device Summary")
newWindow.resizable(False, False)
newWindow.geometry("430x450")
newWindow.configure(bg='white')
newWindow.grab_set()

# Button for operation
add = Menubutton(newWindow, text='Add Configuration', width= 17, height= 1, activebackground='light blue',
                         bg='light blue',underline=4,relief='raised')
        # , command=lambda: Configuration(newWindow, data))
add.place(x=30, y=380)
add.menu = Menu(add, tearoff=False)
add["menu"] = add.menu
add.menu.add_cascade(label="Create VLAN", command=lambda: Configuration.configHistory(newWindow, {}) )
add.menu.add_cascade(label="Static Routing", command=lambda: Configuration.configHistory(newWindow, {}) )
add.menu.add_cascade(label="RIP Routing", command=lambda: Configuration.configHistory(newWindow, {}) )
add.menu.add_cascade(label="EIGRP Routing", command=lambda: Configuration.configHistory(newWindow, {}) )
add.menu.add_cascade(label="OSPF Routing", command=lambda: Configuration.configHistory(newWindow, {}) )
    

Button(newWindow, text='Config History', width=15, bg='light green',
               command=lambda: Configuration.configHistory(newWindow, {})).place(x=160, y=380)

def delete():
    pass
Button(newWindow, text='Delete Device', width=15,
               bg='red', command=delete).place(x=290, y=380)

newWindow.mainloop()