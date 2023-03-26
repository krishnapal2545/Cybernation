from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image, ImageDraw
from datetime import *
import time, sqlite3
from manage import *
from ipaddress import *
from config import *


class Dashboard:
    
    def __init__(self, window,user):
        self.user = user
        self.window = window
        self.window.title("CyberNation")
        self.window.geometry("1366x768")
        self.window.state('zoomed')
        self.window.config(background='#eff5f6')
        
        # Window Icon Photo
        icon = PhotoImage(file='images\\icon.png')
        self.window.iconphoto(True, icon)

        # ================== HEADER ====================================================
        self.header = Frame(self.window, bg='#009df4').place(x=300, y=0, width=1070, height=60)

        # ================== SIDEBAR ===================================================
        self.sidebar = Frame(self.window, bg='#ffffff').place(x=0, y=0, width=300, height=750)

        # ============= BODY ==========================================================
        # body frame 1
        Label(self.window, text='Dashboard', font=("", 15, "bold"), fg='black', bg='white', width=20).place(x=325, y=30)
        self.list_device = Frame(self.window, bg='white')
        self.list_device.place(x=325, y=60, width=1020, height=340)

        # body frame 2
        Label(self.window, text='Output', font=("", 15, "bold"), fg='white', bg='black', width=20).place(x=325, y= 410)
        global list_output
        list_output = Frame(self.window, bg='black')
        list_output.place(x=325, y= 440, width= 1020, height=260)

        # ==============================================================================
        # ================== SIDEBAR ===================================================
        # ==============================================================================

        # date and Time
        self.clock_image = PhotoImage(file="images/time.png")
        self.date_time_image = Label(self.sidebar, image=self.clock_image, bg="white")
        self.date_time_image.place(x=75, y=30)

        self.date_time = Label(self.window)
        self.date_time.place(x=105, y=25)
        self.show_time()

        # logo
        gender = user[3]
        self.logoImage = ImageTk.PhotoImage(file=f'images/{gender}.png')
        self.logo = Label(self.sidebar, image=self.logoImage, bg='#ffffff').place(x=60, y=80)

        # Name of brand/person
        uname = user[1] + ' '+ user [2]
        self.Username = Label(self.sidebar, text= uname, bg='#ffffff', font=("", 15, "bold")).place(x=80, y=240)

        #Gender
        self.gen_img = PhotoImage(file='images/gender.png').subsample(2,2)
        Label(self.sidebar, image= self.gen_img, bg='#ffffff').place(x=30, y= 290)
        Label(self.sidebar, text= user[3], bg='#ffffff', font='Verdana 11 ').place(x=80,y=290)

        #Organi
        self.org_img = PhotoImage(file='images/org.png').subsample(2,2)
        Label(self.sidebar, image= self.org_img, bg='#ffffff').place(x=30, y= 330)
        Label(self.sidebar, text= user[4], bg='#ffffff', font='Verdana 11 ').place(x=80,y=330)

        #Contact
        self.contact_img = PhotoImage(file='images/contact.png').subsample(2,2)
        Label(self.sidebar, image= self.contact_img, bg='#ffffff').place(x=30, y= 370)
        Label(self.sidebar, text= user[5], bg='#ffffff', font='Verdana 11').place(x=80,y=370)
        
        # Separator object
        separator = ttk.Separator(self.sidebar, orient='horizontal')
        separator.place(x=0, y= 610, width=300)

        # Add Device
        self.routerImage = PhotoImage(file='images/device.png').subsample(4,4)
        Button(self.sidebar, text="  Add Device", bg='#ffffff', font=("", 13, "bold"), bd=0, image= self.routerImage, compound= LEFT,
        cursor='hand2',activebackground='#ffffff', command= self.add_device).place(x=50, y= 620)

        # Separator object
        separator = ttk.Separator(self.sidebar, orient='horizontal')
        separator.place(x=0, y= 660, width= 300)

        # Settings
        self.settingsImage = PhotoImage(file='images/setting.png').subsample(2,2)
        Button(self.sidebar, text="Settings", bg='#ffffff', font=("", 13, "bold"), bd=0, image= self.settingsImage, compound= LEFT,
        cursor='hand2', activebackground='#ffffff').place(x= 10, y= 670)
        
        # Separator object
        separator = ttk.Separator(self.sidebar, orient='vertical').place(x= 150, y= 660, height= 40)

        # Logout
        self.logoutImage = PhotoImage(file='images/logout.png').subsample(2,2)
        Button(self.sidebar, text="  Logout!  ", bg='#ffffff', font=("", 13, "bold"), bd=0, image= self.logoutImage, compound= LEFT,
        cursor='hand2', activebackground='#ffffff', command= lambda : self.window.destroy()).place(x=170, y=670)

        # =============================================================================
        # ============= BODY ==========================================================
        # =============================================================================

        # Body Frame 1
        self.devices()

        # Body Frame 2
        self.output({})

        self.window.mainloop()
    
    def show_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        set_text = f"  {self.time} \n {self.date}"
        self.date_time.configure(text=set_text, font=(
            "", 13, "bold"), bd=0, bg="white", fg="black")
        self.date_time.after(100, self.show_time)
    
    def devices(self):
        
        self.trv_device = ttk.Treeview(self.list_device, selectmode = 'browse')
        self.trv_device.grid(row=1,column=0,columnspan=3,padx=20,pady=20)
        self.trv_device['height']=14 # Number of rows to display, default is 10
        self.trv_device['show'] = 'headings' 
        self.trv_device["columns"] = [1,2,3,4,5] # column identifiers 
        self.trv_device.column(1, width = 120, anchor ='c') # Headings of respective columns
        self.trv_device.heading(1, text = 'Sr. No.')
        self.trv_device.column(2, width = 200, anchor ='c') # Headings of respective columns
        self.trv_device.heading(2, text = 'Device Name')
        self.trv_device.column(3, width = 200, anchor ='c') # Headings of respective columns
        self.trv_device.heading(3, text = 'IP Adress')
        self.trv_device.column(4, width = 200, anchor ='c') # Headings of respective columns
        self.trv_device.heading(4, text = 'Device Type')
        self.trv_device.column(5, width = 230, anchor ='c') # Headings of respective columns
        self.trv_device.heading(5, text = 'Last Modify')
        global count
        count = 0
        for data in getAlldevice(self.user):
            count = count + 1
            lst = [count,data[2],data[3],data[6],data[10]]
            self.trv_device.insert("",'end',iid=data[3],values=lst)

        self.trv_device.bind("<Double-1>", self.deviceInfo)
        vs = ttk.Scrollbar(self.list_device,orient='vertical',command=self.trv_device.yview)
        vs.grid(row=1,column=3, sticky= 'ns',pady= 20)
        self.trv_device.config(yscrollcommand= vs.set)
    
    def add_device(self):
        # Toplevel object which will be treated as a new window
        newWindow = Toplevel(self.window)
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
            try:
                IPv4Address(en2.get())
                IPv4Address(en3.get())
                if conn.cursor().execute("SELECT IP FROM Devices WHERE IP = ?",(str(en2.get()),)).fetchone():
                    messagebox.showerror("Error", "IP address had already used" ,parent=newWindow)
                elif en1.get() and en2.get() and en3.get() and en4.get() and en5.get() and en6.get() and en7.get() and en8.get():  
                    data = {
                    "userID" : self.user[0],
                    "Name": en1.get(),
                    "IP": en2.get(),
                    "Subnet" : en3.get(),
                    "Description": en4.get(),
                    "Type" : en5.get(),
                    "Username" : en6.get(),
                    "Password" : en7.get(),
                    "Enable" : en8.get(),
                    "Last_Modify" : datetime.today(),
                    }
                    savedevice(data)
                    global count
                    count = count + 1
                    lst = [count,en1.get(),en2.get(),en5.get(),datetime.today()]
                    self.trv_device.insert("",'end',iid=en2.get(),values=lst)
                    messagebox.showinfo("Success" , "Device Added Successfull" , parent = newWindow)
                    newWindow.destroy()      
                else:
                    messagebox.showerror("Error", "Device Information can not be left blank" ,parent=newWindow)
            except ValueError as e:
                messagebox.showerror("Error", e ,parent=newWindow)

        Button(newWindow, text="ADD", width=30, command=check).place(x=100,y=480)
        newWindow.mainloop()
     
    def deviceInfo(self,event): 
        IP = self.trv_device.selection()[0]
        data = getdevice(IP)
        newWindow = Toplevel(self.window)
        newWindow.title("Device Summary")
        newWindow.resizable(False,False)
        newWindow.geometry("430x450")
        newWindow.configure(bg='white')
        newWindow.grab_set()
        
        #image
        device_img = PhotoImage(file='images\device.png')
        device_info = Label(newWindow, image= device_img, bg='white')
        device_info.pack()
        device_info.place(x=130, y= 20)
        
        # A Label widget to show in toplevel
        Label(newWindow, text="Name : ",font=("arial",12),bg='white').place(x = 40,y = 160)  
        Label(newWindow, text= data[2], font=("arial",12),bg='white').place(x= 180, y=160) 
        Label(newWindow, text="IP Address : ", font=("arial",12),bg='white').place(x=40, y=200)  
        Label(newWindow,text= data[3], font=("arial",12),bg='white').place(x=180, y=200)
        Label(newWindow, text="Description : ", font=("arial",12),bg='white').place(x=40, y=240)   
        Label(newWindow,text= data[5], font=("arial",12),bg='white').place(x=180, y=240)
        Label(newWindow, text="SSH Username : ", font=("arial",12),bg='white').place(x=40, y=280)  
        Label(newWindow,text= data[7],font=("arial",12),bg='white').place(x=180, y=280)
        Label(newWindow,text="Last Modify : ",font=("arial",12),bg='white').place(x = 40,y= 320)
        Label(newWindow,text=data[10],font=("arial",12),bg='white').place(x=180, y=320)

        # Button for operation
        Button(newWindow, text= 'New Configuration', width= 15,bg='light blue', 
               command= lambda: Configuration(newWindow, data)).place(x=30, y= 380)
        Button(newWindow, text= 'Old Configuration', width= 15,bg='light green').place(x=160, y= 380)

        def deletedevice():
            IP = self.trv_device.selection()[0]
            self.trv_device.delete(self.trv_device.selection())
            deleteDevice(IP)
            newWindow.destroy()
        Button(newWindow, text= 'Delete Device', width= 15,bg='red',command= deletedevice).place(x=290, y= 380)

        newWindow.mainloop()
    
    def output(self, result):
        global list_output
        self.trv_output = ttk.Treeview(list_output, selectmode = 'browse')
        self.trv_output.grid(row=1,column=0,columnspan=3,padx=20,pady=20)
        self.trv_output['height']=10 # Number of rows to display, default is 10
        self.trv_output['show'] = 'headings' 
        self.trv_output["columns"] = [1] # column identifiers 
        self.trv_output.column(1, width = 950, anchor ='w') 
        vs = ttk.Scrollbar(list_output,orient='vertical',command=self.trv_output.yview)
        vs.grid(row=1,column=3, sticky= 'ns',pady= 20)
        self.trv_output.config(yscrollcommand= vs.set)

        for data in result:
            data = ' ' + data + ' $ ' + result[data]
            lst = [data]
            self.trv_output.insert("",'end',values=lst)

class Configuration (Dashboard):

    def __init__(self, window, device):
        self.device = device
        self.window = Toplevel(window)
        self.window.title("Add Configuration")
        self.window.resizable(False,False)
        self.window.geometry("430x450")
        self.window.configure(bg='white')
        self.window.grab_set()
        
        #image
        device_img = PhotoImage(file='images\device.png')
        device_info = Label(self.window, image= device_img, bg='white')
        device_info.pack()
        device_info.place(x=130, y= 20)

        Label(self.window, text="Configurations :- ", font='Verdana 15 bold', bg='white').place(x=10, y=150)
        
        Button(self.window, width= 15, height= 3, text="Static Routing",  bg="#33FFE9", command= self.staticRouting).place(x = 50, y= 200)
        Button(self.window, width= 15, height= 3, text="RIP Routing",     bg="#A533FF", command= self.ripRouting).place(x = 250,  y= 200)
        Button(self.window, width= 15, height= 3, text="OSPF Routing",    bg="#ff1111", command= self.ospfRouting).place(x = 50, y= 275)
        Button(self.window, width= 15, height= 3, text="BGP Routing",     bg="#33FF5B", command= self.bgpRouting).place(x = 250,  y= 275)
        Button(self.window, width= 15, height= 3, text="EIGRP Routing",   bg="#E9FF33", command= self.eigrpRouting).place(x = 50, y= 350)
        
        self.window.mainloop()
    
    def staticRouting(self):
        newWindow = Toplevel(self.window)
        newWindow.title("Static Routing")
        newWindow.resizable(False, False)
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
                    'deviceID' : self.device[0],
                    'Name':'Static Routing',
                    'Username': self.device[7],
                    'Password': self.device[8],
                    'Enable': self.device[9],
                    'IP': self.device[3],
                    'Dest-IP': destIP.get(),
                    'Dest-SubIP': destSub.get(),
                    'NextHop': nextHop.get(),
                    'Last_Modify': datetime.today()
                    }
                self.output(routing(config, newWindow))
            except ValueError as e:
                messagebox.showerror("Error", e ,parent=newWindow)
                
        # # button config
        Button(newWindow, text="Config",font='Verdana 10 bold', width= 30, bg="#33FFE9", command= check).place(x= 100, y= 200)
        newWindow.mainloop()

    def ripRouting(self):
        newWindow = Toplevel(self.window)
        newWindow.title("RIP Routing")
        newWindow.geometry("480x200")
        newWindow.config(background="black")
        
        # heading label
        Label(newWindow, text="Network IP Address :",font='Verdana 10 bold', foreground= "white", bg="black").place(x=30, y= 40)
        Label(newWindow, text="Version :",font='Verdana 10 bold', foreground= "white", bg="black").place(x=30, y= 90 )

        # Entry Box
        networkIP = StringVar()
        version = StringVar()

        Entry(newWindow, width=20, textvariable= networkIP,font='Verdana 10 bold').place(x=250, y=40)
        Entry(newWindow, width=20, textvariable= version,font='Verdana 10 bold').place(x=250, y=90)

        def check():
            try:
                IPv4Network(networkIP.get())
                config = {
                    'deviceID' : self.device[0],
                    'Name':'RIP Routing',
                    'Username': self.device[7],
                    'Password': self.device[8],
                    'Enable': self.device[9],
                    'IP': self.device[3],
                    'Network-IP': networkIP.get(),
                    'Version': version.get(),
                    'Last_Modify': datetime.today()
                    }
                routing(config, newWindow)
            except ValueError as e:
                messagebox.showerror("Error", e ,parent=newWindow)

        # # button config
        Button(newWindow, text="Config",font='Verdana 10 bold', width= 30, bg="#A533FF", command= check).place(x= 100, y= 150)
        newWindow.mainloop()
    
    def ospfRouting(self):
        pass

    def bgpRouting(self):
        pass

    def eigrpRouting(self):
        newWindow = Toplevel(self.window)
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
                    'deviceID' : self.device[0],
                    'Name':'EIGRP Routing',
                    'Username': self.device[7],
                    'Password': self.device[8],
                    'Enable': self.device[9],
                    'IP': self.device[3],
                    'Network-IP': networkIP.get(),
                    'ASnumber': as_number.get(),
                    'Last_Modify': datetime.today()
                    }
                routing(config, newWindow)
            except ValueError as e:
                messagebox.showerror("Error", e ,parent=newWindow)

        # # button config
        Button(newWindow, text="Config",font='Verdana 10 bold', width= 30, bg="#E9FF33", command= check).place(x= 100, y= 150)
        newWindow.mainloop()




if __name__ == '__main__':
    cursor.execute("SELECT * FROM Users WHERE Username = 'kk_pl' AND Password = 'K2545' ;")
    Dashboard(Tk(),cursor.fetchone())


