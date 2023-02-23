from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image, ImageDraw
from manage import *
from ipaddress import *

newWindow = Tk()
# sets the title of the Toplevel widget
newWindow.title("Add Device")
newWindow.resizable(False, False)
# sets the geometry of toplevel
newWindow.geometry("450x550")
# image
device_img = PhotoImage(file='images/device.png')
device_info = Label(newWindow, image=device_img, height=100)
device_info.pack()
device_info.place(x=130, y=20)
# A Label widget to show in toplevel
en1 = StringVar()
en2 = StringVar()
en3 = StringVar()
en4 = StringVar()
en5 = StringVar()
en6 = StringVar()
en7 = StringVar()
en8 = StringVar()

Label(newWindow, text="Host Name", font=("arial", 12)).place(x=40, y=140)
Entry(newWindow, width=25, font=("arial", 12),textvariable=en1).place(x=200, y=140)

Label(newWindow, text="IP Address", font=("arial", 12)).place(x=40, y=180)
Entry(newWindow, width=25, font=("arial", 12),textvariable=en2).place(x=200, y=180)

Label(newWindow, text="Subnet Mask", font=("arial", 12)).place(x=40, y=220)
Entry(newWindow, width=25, font=("arial", 12),textvariable=en3).place(x=200, y=220)

Label(newWindow, text="Description", font=("arial", 12)).place(x=40, y=260)
Entry(newWindow, width=25, font=("arial", 12),textvariable=en4).place(x=200, y=260)

Label(newWindow, text="Select Device",font=("arial", 12)).place(x=40, y=300)
type_of_devices = ("Router", "Switch")
en5.set("Router")
menu = OptionMenu(newWindow, en5, *type_of_devices)
menu.config(width=20)
menu.place(x=200, y=300)

Label(newWindow, text="Username",font=("arial", 12)).place(x=40, y=340)
Entry(newWindow, width=25, font=("arial", 12),textvariable=en6).place(x=200, y=340)

Label(newWindow, text="Password",font=("arial", 12)).place(x=40, y=380)
Entry(newWindow, show='*', width=25, font=("arial", 12),textvariable=en7).place(x=200, y=380)

Label(newWindow, text="Enable Password",font=("arial", 12)).place(x=40, y=420)
Entry(newWindow, show='*', width=25, font=("arial", 12),textvariable=en8).place(x=200, y=420)

def check():
    def subnet(net):
        subnet = net.split(".")
        print(subnet)
        if len(subnet) != 4: return True 
        for o in subnet:
            if not o.isalnum() : return True
            if  256 <= int(o) or 0 > int(o) : return True
        return False
    try:
        IPv4Address(en2.get())
        if subnet(en3.get()):
            messagebox.showerror("Error", "Enter valid Subnet Mask Address" ,parent=newWindow)
        elif db.devices.find_one({ "IP" : en2.get()}):
            messagebox.showerror("Error", "IP address had already used" ,parent=newWindow)
        elif en1.get() and en2.get() and en3.get() and en4.get() and en5.get() and en6.get():
            # global count
            # count = count + 1
            # lst = [count,en1.get(),en2.get(),en5.get(),datetime.today()]
            # self.trv.insert("",'end',iid=en2.get(),values=lst)
    #         data = {
    #             "userID" : user["_id"],
    #             "Name": en1.get(),
    #             "IP": en2.get(),
    #             "Subnet" : en3.get(),
    #             "Description": en4.get(),
    #             "Type" : en5.get(),
    #             "Username" : en6.get(),
    #             "Password" : en7.get(),
    #             "Enable" : en8.get(),
    #             "Last_Modify" : LM,
    # }
            # savedevice(data)
            # newWindow.destroy()
            pass         
        else:
            messagebox.showerror("Error", "Device Information can not be left blank" ,parent=newWindow)
    except AddressValueError as e:
        messagebox.showerror("Error", e ,parent=newWindow)


Button(newWindow, text="ADD", width=30, command=check).place(x=100,y=480)
newWindow.mainloop()
