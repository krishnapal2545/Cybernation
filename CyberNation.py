from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk
from datetime import *
import sqlite3
import time
import threading
import telnetlib
from ipaddress import *
from netmiko import (ConnectHandler, SSHDetect, NetmikoTimeoutException,
                     NetmikoAuthenticationException)


class Database:

    def __init__(self):
        self.conn = sqlite3.connect('Cybernation.db')
        self.cursor = self.conn.cursor()

        self.conn.execute('''
        CREATE TABLE IF NOT EXISTS Users(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Fname           TEXT     NOT NULL,
        Lname           TEXT     NOT NULL,
        Gender          TEXT     NOT NULL,
        Org             TEXT     NOT NULL,
        Phone           INT      NOT NULL,
        Username        TEXT     NOT NULL,
        Password        TEXT     NOT NULL);''')

        self.conn.execute('''
        CREATE TABLE IF NOT EXISTS Devices(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID         INTEGER  NOT NULL,
        Name           TEXT     NOT NULL,    
        IP             TEXT     NOT NULL   UNIQUE,
        Subnet         TEXT     NOT NULL,
        Description    TEXT     NOT NULL,
        Type           TEXT     NOT NULL,
        Username       TEXT     NOT NULL,
        Password       TEXT     NOT NULL,
        Enable         TEXT     NOT NULL,
        Device_Type    TEXT     NOT NULL  DEFAULT 'autodetect',
        Last_Modify    DATETIME NOT NULL);''')

        self.conn.execute('''
        CREATE TABLE IF NOT EXISTS Configs(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        DeviceID           TEXT     NOT NULL,
        Name               TEXT     NOT NULL,
        Config             TEXT     NOT NULL,
        Activity           TEXT     NOT NULL,
        Last_Modify        DATETIME NOT NULL);''')

    def saveUser(self, fname, lname, gen, org, phone, uname, passw):
        self.conn.execute('''
        INSERT INTO Users (Fname,Lname,Gender,Org,Phone,Username,Password) 
        VALUES(?,?,?,?,?,?,?)''', (fname, lname, gen, org, phone, uname, passw))
        self.conn.commit()

    def getUser(self, uname, passw):
        self.cursor.execute(
            "SELECT * FROM Users WHERE Username = ? AND Password = ?", (uname, passw,))
        return self.cursor.fetchone()

    def savedevice(self, data):
        self.conn.execute('''
        INSERT INTO Devices (UserID,Name,IP,Subnet,Description,Type,Username,Password,Enable,Last_Modify) 
        VALUES(?,?,?,?,?,?,?,?,?,?)''',
                          (str(data['userID']), str(data['Name']), str(data['IP']), str(data['Subnet']), str(data['Description']), str(data['Type']), str(data['Username']), str(data['Password']), str(data['Enable']), str(data['Last_Modify'])))
        self.conn.commit()

    def getAlldevice(self, user):
        self.cursor.execute(
            "SELECT * FROM Devices WHERE UserID = ?", (user[0],))
        return self.cursor.fetchall()

    def getdevice(self, IP):
        self.cursor.execute("SELECT * FROM Devices WHERE IP = ?", (IP,))
        return self.cursor.fetchone()

    def deleteDevice(self, IP):
        self.cursor.execute("DELETE FROM Devices WHERE IP = ?", (IP,))
        self.conn.commit()

    def saveconfig(self, config):
        self.conn.execute('''
        INSERT INTO Configs (DeviceID, Name, Config, Activity ,Last_Modify) 
        VALUES(?,?,?,?)''', (str(config['deviceID']), str(config['Name']), str(config['Destination']), str(config['Activity']), str(config['Last_Modify']),))
        self.conn.execute('''
        UPDATE Devices SET Last_Modify = ? WHERE ID = ?''', (datetime.today(), str(config['deviceID']),))
        self.conn.commit()

    def getconfig(self, deviceID):
        self.cursor.execute(
            "SELECT * FROM Configs WHERE DeviceID = ?", (deviceID,))
        return self.cursor.fetchall()


class Register:

    def __init__(self):
        self.window = Tk()
        self.window.title("CyberNation")
        self.window.maxsize(width=500,  height=500)
        self.window.minsize(width=500,  height=500)

        # Window Icon Photo
        icon = PhotoImage(file='images\\icon.png')
        self.window.iconphoto(True, icon)

        # heading label
        Label(self.window, text="Signup",
              font='Verdana 20 bold').place(x=70, y=60)

        # form data label
        Label(self.window, text="First Name :",
              font='Verdana 10 bold').place(x=70, y=130)
        Label(self.window, text="Last Name :",
              font='Verdana 10 bold').place(x=70, y=160)
        Label(self.window, text="Gender :",
              font='Verdana 10 bold').place(x=70, y=190)
        Label(self.window, text="Organization :",
              font='Verdana 10 bold').place(x=70, y=220)
        Label(self.window, text="Contact No.:",
              font='Verdana 10 bold').place(x=70, y=250)
        Label(self.window, text="User Name :",
              font='Verdana 10 bold').place(x=70, y=280)
        Label(self.window, text="Password :",
              font='Verdana 10 bold').place(x=70, y=310)
        Label(self.window, text="Verify Password:",
              font='Verdana 10 bold').place(x=70, y=340)

        # Entry Box ------------------------------------------------------------------
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.phone = IntVar()
        self.var = StringVar()
        self.org = StringVar()
        self.user_name = StringVar()
        self.password = StringVar()
        self.very_pass = StringVar()

        Entry(self.window, width=40,
              textvariable=self.first_name).place(x=200, y=133)
        Entry(self.window, width=40,
              textvariable=self.last_name).place(x=200, y=163)
        ttk.Radiobutton(self.window, text='Male', value="Male",
                        variable=self.var).place(x=200, y=190)
        ttk.Radiobutton(self.window, text='Female', value="Female",
                        variable=self.var).place(x=260, y=190)
        Entry(self.window, width=40, textvariable=self.org).place(x=200, y=223)
        Entry(self.window, width=40, textvariable=self.phone).place(x=200, y=253)
        Entry(self.window, width=40,
              textvariable=self.user_name).place(x=200, y=283)
        Entry(self.window, width=40, show="*",
              textvariable=self.password).place(x=200, y=313)
        Entry(self.window, width=40, show="*",
              textvariable=self.very_pass).place(x=200, y=343)

        # button login and clear
        Button(self.window, text="Signup", width=15, font='Verdana 10 bold',
               command=self.register).place(x=200, y=383)
        Button(self.window, text="Switch To Login",
               command=self.switch).place(x=350, y=20)
        self.window.mainloop()

    def register(self):
        if self.first_name.get() == "" or self.last_name.get() == "" or self.org.get() == "" or self.user_name.get() == "" or self.password.get() == "" or self.very_pass.get() == "":
            messagebox.showerror(
                "Error", "All Fields Are Required", parent=self.window)
        elif self.password.get() != self.very_pass.get():
            messagebox.showerror(
                "Error", "Password & Confirm Password Should Be Same", parent=self.window)
        else:
            try:
                Database().saveUser(self.first_name.get(), self.last_name.get(), self.var.get(),
                                    self.org.get(), self.phone.get(), self.user_name.get(), self.password.get())
                messagebox.showinfo(
                    "Success", "Ragistration Successfull", parent=self.window)
                self.switch()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error do to : {str(es)}", parent=self.window)

    def switch(self):
        self.window.destroy()
        Login()


class Login:

    def __init__(self):
        self.window = Tk()
        self.window.title("CyberNation")
        self.window.maxsize(width=500,  height=500)
        self.window.minsize(width=500,  height=500)
        # self.window.config(background='white')

        # Window Icon Photo
        icon = PhotoImage(file='images\\icon.png')
        self.window.iconphoto(True, icon)

        # heading label
        Label(self.window, text="Login",
              font='Verdana 25 bold').place(x=80, y=150)
        Label(self.window, text="User Name :",
              font='Verdana 10 bold').place(x=80, y=220)
        Label(self.window, text="Password :",
              font='Verdana 10 bold').place(x=80, y=260)

        # Entry Box
        self.user_name = StringVar()
        self.password = StringVar()

        self.userentry = Entry(self.window, width=40,
                               textvariable=self.user_name).place(x=200, y=223)
        self.passentry = Entry(self.window, width=40, show="*",
                               textvariable=self.password).place(x=200, y=260)

        # # button login and clear

        Button(self.window, text="Login", font='Verdana 10 bold',width=20,
               command=self.login).place(x=200, y=293)

        # # signup button

        Button(self.window, text="Switch To Signup",
               command=self.switch).place(x=350, y=20)

        self.window.mainloop()

    def login(self):
        if self.user_name.get() == "" or self.password.get() == "":
            messagebox.showerror(
                "Error", "Enter Username And Password", parent=self.window)
        else:
            try:
                user = Database().getUser(self.user_name.get(), self.password.get())
                if user == None:
                    messagebox.showerror(
                        "Error", "Invalid User Name And Password", parent=self.window)
                else:
                    self.window.destroy()
                    Dashboard(Tk(), user)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error Do to : {str(es)}", parent=self.window)

    def switch(self):
        self.window.destroy()
        Register()


class Dashboard:

    def __init__(self, window, user):
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
        self.header = Frame(self.window, bg='#009df4').place(
            x=300, y=0, width=1070, height=60)

        # ================== SIDEBAR ===================================================
        self.sidebar()

        # ============= BODY ==========================================================
        self.body()

        self.window.mainloop()

    def sidebar(self):
        newWindow = Frame(self.window, bg='#ffffff').place(
            x=0, y=0, width=300, height=700)

        # date and Time
        self.clock_image = PhotoImage(file="images/time.png")
        self.date_time_image = Label(
            newWindow, image=self.clock_image, bg="white")
        self.date_time_image.place(x=75, y=30)

        self.date_time = Label(self.window)
        self.date_time.place(x=105, y=25)
        self.show_time()

        # logo
        gender = self.user[3]
        self.logoImage = ImageTk.PhotoImage(file=f'images/{gender}.png')
        self.logo = Label(newWindow, image=self.logoImage,
                          bg='#ffffff').place(x=60, y=80)

        # Name of brand/person
        uname = self.user[1] + ' ' + self.user[2]
        self.Username = Label(newWindow, text=uname, bg='#ffffff', font=(
            "", 15, "bold")).place(x=80, y=240)

        # Gender
        self.gen_img = PhotoImage(file='images/gender.png').subsample(2, 2)
        Label(newWindow, image=self.gen_img,
              bg='#ffffff').place(x=30, y=290)
        Label(newWindow, text=self.user[3], bg='#ffffff',
              font='Verdana 11 ').place(x=80, y=290)

        # Organi
        self.org_img = PhotoImage(file='images/org.png').subsample(2, 2)
        Label(newWindow, image=self.org_img,
              bg='#ffffff').place(x=30, y=330)
        Label(newWindow, text=self.user[4], bg='#ffffff',
              font='Verdana 11 ').place(x=80, y=330)

        # Contact
        self.contact_img = PhotoImage(
            file='images/contact.png').subsample(2, 2)
        Label(newWindow, image=self.contact_img,
              bg='#ffffff').place(x=30, y=370)
        Label(newWindow, text=self.user[5], bg='#ffffff',
              font='Verdana 11').place(x=80, y=370)

        # Separator object
        separator = ttk.Separator(newWindow, orient='horizontal')
        separator.place(x=0, y=610, width=300)

        # Add Device
        self.routerImage = PhotoImage(file='images/device.png').subsample(3, 3)
        Button(newWindow, text="  Add Device", bg='#ffffff', font=("", 13, "bold"), bd=0, image=self.routerImage, compound=LEFT,
               cursor='hand2', activebackground='#ffffff', command=self.add_device).place(x=70, y=620)

        # Separator object
        separator = ttk.Separator(newWindow, orient='horizontal')
        separator.place(x=0, y=660, width=300)

        # Close Window
        self.settingsImage = PhotoImage(file='images/close.png')
        Button(newWindow, text=" Close ", bg='#ffffff', font=("", 13, "bold"), bd=0, image=self.settingsImage, compound=LEFT,
               cursor='hand2', activebackground='#ffffff', command=lambda: self.window.destroy()).place(x=30, y=670)

        # Separator object
        separator = ttk.Separator(newWindow, orient='vertical').place(
            x=150, y=660, height=40)

        def logout():
            self.window.destroy()
            Login()
        # Logout
        self.logoutImage = PhotoImage(file='images/logout.png')
        Button(newWindow, text=" Logout  ", bg='#ffffff', font=("", 13, "bold"), bd=0, image=self.logoutImage, compound=LEFT,
               cursor='hand2', activebackground='#ffffff', command=logout).place(x=180, y=670)

    def body(self):
        # body frame 1
        Label(self.window, text='Dashboard', font=("", 15, "bold"),
              fg='black', bg='white', width=20).place(x=325, y=30)
        self.frame1 = Frame(self.window, bg='white')
        self.frame1.place(x=325, y=60, width=1020, height=340)
        # Body Frame 1
        self.devices()

        # body frame 2
        Label(self.window, text='Output', font=("", 15, "bold"),
              fg='white', bg='black', width=20).place(x=325, y=410)
        self.list_output = Frame(self.window, bg='black')
        self.list_output.place(x=325, y=440, width=1020, height=260)
        global CLI
        CLI = Text(self.list_output, state="disabled",
                   padx=20, pady=20, width=114, height=11)
        CLI.place(x=25, y=25)
        vs = ttk.Scrollbar(
            self.list_output, orient='vertical', command=CLI.yview)
        vs.place(x=990, y=25, height=220)
        CLI.config(yscrollcommand=vs.set)

        # Body Frame 2
        config = "You will see all the activity done by you here in this window"
        Dashboard.output(config)

    def show_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        set_text = f"  {self.time} \n {self.date}"
        self.date_time.configure(text=set_text, font=(
            "", 13, "bold"), bd=0, bg="white", fg="black")
        self.date_time.after(100, self.show_time)

    def devices(self):

        self.trv_device = ttk.Treeview(self.frame1, selectmode='browse')
        self.trv_device.grid(row=1, column=0, columnspan=3, padx=20, pady=20)
        # Number of rows to display, default is 10
        self.trv_device['height'] = 14
        self.trv_device['show'] = 'headings'
        self.trv_device["columns"] = [1, 2, 3, 4, 5]  # column identifiers
        # Headings of respective columns
        self.trv_device.column(1, width=120, anchor='c')
        self.trv_device.heading(1, text='Sr. No.')
        # Headings of respective columns
        self.trv_device.column(2, width=200, anchor='c')
        self.trv_device.heading(2, text='Device Name')
        # Headings of respective columns
        self.trv_device.column(3, width=200, anchor='c')
        self.trv_device.heading(3, text='IP Adress')
        # Headings of respective columns
        self.trv_device.column(4, width=200, anchor='c')
        self.trv_device.heading(4, text='Device Type')
        # Headings of respective columns
        self.trv_device.column(5, width=230, anchor='c')
        self.trv_device.heading(5, text='Last Modify')
        global count
        count = 0
        for data in Database().getAlldevice(self.user):
            count = count + 1
            lst = [count, data[2], data[3], data[6], data[11]]
            self.trv_device.insert("", 'end', iid=data[3], values=lst)

        self.trv_device.bind("<Double-1>", self.deviceInfo)
        vs = ttk.Scrollbar(self.frame1, orient='vertical',
                           command=self.trv_device.yview)
        vs.grid(row=1, column=3, sticky='ns', pady=20)
        self.trv_device.config(yscrollcommand=vs.set)

    def add_device(self):
        # Toplevel object which will be treated as a new window
        newWindow = Frame(self.window, bg='white')
        newWindow.place(x=325, y=60, width=1020, height=340)

        def back():
            newWindow.destroy()
            bb.destroy()
        Button(newWindow, text='<- Back', width=10, bg='black',
               fg='white', command=back).place(x=1, y=25)

        bb = Button(self.window, text="  Add Device", bg='#ffffff', font=("", 13, "bold"), bd=0, image=self.routerImage, compound=LEFT,
                    cursor='hand2', activebackground='#ffffff')
        bb.place(x=50, y=620)
        # image
        device_img = PhotoImage(file='images/device.png')
        device_info = Label(newWindow, image=device_img, bg='white')
        device_info.pack()
        device_info.place(x=420, y=15)
        # A Label widget to show in toplevel
        en1 = StringVar()
        en2 = StringVar()
        en3 = StringVar()
        en4 = StringVar()
        en5 = StringVar()
        en6 = StringVar()
        en7 = StringVar()
        en8 = StringVar()

        Label(newWindow, text="Host Name", bg='white',
              font=("arial", 12)).place(x=100, y=125)
        Label(newWindow, text="IP Address", bg='white',
              font=("arial", 12)).place(x=100, y=165)
        Label(newWindow, text="Subnet Mask", bg='white',
              font=("arial", 12)).place(x=100, y=205)
        Label(newWindow, text="Description", bg='white',
              font=("arial", 12)).place(x=100, y=245)
        Entry(newWindow, width=20, bd=2, font=("arial", 12),
              textvariable=en1).place(x=250, y=125)
        Entry(newWindow, width=20, bd=2, font=("arial", 12),
              textvariable=en2).place(x=250, y=165)
        Entry(newWindow, width=20, bd=2, font=("arial", 12),
              textvariable=en3).place(x=250, y=205)
        Entry(newWindow, width=20, bd=2, font=("arial", 12),
              textvariable=en4).place(x=250, y=245)

        Label(newWindow, text="Device Type", bg='white',
              font=("arial", 12)).place(x=550, y=125)
        Label(newWindow, text="Username", bg='white',
              font=("arial", 12)).place(x=550, y=165)
        Label(newWindow, text="Password", bg='white',
              font=("arial", 12)).place(x=550, y=205)
        Label(newWindow, text="Enable Secret", bg='white',
              font=("arial", 12)).place(x=550, y=245)
        option = ['Router', 'Switch']
        ttk.Combobox(newWindow, values=option, width=27,
                     state='readonly', textvariable=en5).place(x=700, y=125)
        Entry(newWindow, width=20,          bd=2, font=(
            "arial", 12), textvariable=en6).place(x=700, y=165)
        Entry(newWindow, show='*', width=20, bd=2, font=("arial", 12),
              textvariable=en7).place(x=700, y=205)
        Entry(newWindow, show='*', width=20, bd=2, font=("arial", 12),
              textvariable=en8).place(x=700, y=245)

        def check():
            try:
                IPv4Address(en2.get())
                IPv4Address(en3.get())
                if Database().getdevice(en2.get()):
                    messagebox.showerror(
                        "Error", "IP address had already used", parent=newWindow)
                elif en1.get() and en2.get() and en3.get() and en4.get() and en5.get() and en6.get() and en7.get() and en8.get():
                    data = {
                        "userID": self.user[0],
                        "Name": en1.get(),
                        "IP": en2.get(),
                        "Subnet": en3.get(),
                        "Description": en4.get(),
                        "Type": en5.get(),
                        "Username": en6.get(),
                        "Password": en7.get(),
                        "Enable": en8.get(),
                        "Last_Modify": datetime.today(),
                    }
                    Database().savedevice(data)
                    global count
                    count = count + 1
                    lst = [count, en1.get(), en2.get(), en5.get(),
                           datetime.today()]
                    self.trv_device.insert(
                        "", 'end', iid=en2.get(), values=lst)
                    messagebox.showinfo(
                        "Success", "Device Added Successfull", parent=newWindow)
                    newWindow.destroy()
                else:
                    messagebox.showerror(
                        "Error", "Device Information can not be left blank", parent=newWindow)
            except ValueError as e:
                messagebox.showerror("Error", e, parent=newWindow)

        Button(newWindow, text="Add Device", width=40, command=check, bg='black',
               fg='white', font=("arial", 12, "bold")).place(x=300, y=290)
        newWindow.mainloop()

    def deviceInfo(self, event):
        IP = self.trv_device.selection()[0]
        data = Database().getdevice(IP)
        newWindow = Frame(self.window, bg='white')
        newWindow.place(x=325, y=60, width=1020, height=340)
        def back(): newWindow.destroy()
        Button(newWindow, text='<- Back', width=10, bg='black',
               fg='white', command=back).place(x=1, y=25)

        def delete():
            answer = messagebox.askokcancel(title='Confirmation',
                                            message='Deleting will delete all the data.', icon=messagebox.WARNING)
            if answer:
                IP = self.trv_device.selection()[0]
                self.trv_device.delete(self.trv_device.selection())
                Database().deleteDevice(IP)
                newWindow.destroy()

        delete_img = PhotoImage(file=f'images/delete.png')
        Button(newWindow, image=delete_img, bg="white",
               command=delete, border=0).place(x=380, y=20)

        inWindow = Frame(newWindow, padx=20, pady=20)
        inWindow.place(x=450, y=20, width=550, height=300)
        # image
        device_img = PhotoImage(file=f'images/{data[6]}.png')
        device_info = Label(newWindow, image=device_img)
        device_info.pack()
        device_info.place(x=600, y=30)
        Label(newWindow, text=data[6], font=(
            "arial", 20, 'bold')).place(x=680, y=280)

        # A Label widget to show in toplevel
        Label(newWindow, text="Host Name : ", font=(
            "arial", 12), bg='white').place(x=50, y=80)
        Label(newWindow, text=data[2], font=(
            "arial", 12), bg='white').place(x=180, y=80)
        Label(newWindow, text="IP Address : ", font=(
            "arial", 12), bg='white').place(x=50, y=120)
        Label(newWindow, text=data[3], font=(
            "arial", 12), bg='white').place(x=180, y=120)
        Label(newWindow, text="Description : ", font=(
            "arial", 12), bg='white').place(x=50, y=160)
        Label(newWindow, text=data[5], font=(
            "arial", 12), bg='white').place(x=180, y=160)
        Label(newWindow, text="Username : ", font=(
            "arial", 12), bg='white').place(x=50, y=200)
        Label(newWindow, text=data[7], font=(
            "arial", 12), bg='white').place(x=180, y=200)
        Label(newWindow, text="Last Modify : ", font=(
            "arial", 12), bg='white').place(x=50, y=240)
        Label(newWindow, text=datetime.strptime(data[11], '%Y-%m-%d %H:%M:%S.%f').date(), font=(
            "arial", 12), bg='white').place(x=180, y=240)

        # Button for operation

        ###
        add = Menubutton(newWindow, text='Add Configuration', width=17, height=1, activebackground='light blue',
                         bg='light blue', relief='raised', borderwidth=2)
        add.place(x=50, y=290)
        add.menu = Menu(add, tearoff=False)
        add["menu"] = add.menu
        if(data[6] == 'Switch'):
            add.menu.add_cascade(
                label="Virtual LAN", command=lambda: AddConfig(newWindow, data).vlan())
        if(data[6] == 'Router'):
            add.menu.add_cascade(
                label="VPN ", command=lambda: AddConfig(newWindow, data).vpn())
            add.menu.add_cascade(
                label="RIP Routing", command=lambda: AddConfig(newWindow, data).rip())
            add.menu.add_cascade(
                label="Static Routing", command=lambda: AddConfig(newWindow, data).static())
            add.menu.add_cascade(
                label="EIGRP Routing", command=lambda: AddConfig(newWindow, data).eigrp())
            add.menu.add_cascade(
                label="OSPF Routing", command=lambda: AddConfig(newWindow, data).ospf())

        ###
        def configHistory(window, device):
            newWindow = Frame(window, bg='black', padx=20, pady=20)
            newWindow.place(x=450, y=20, width=550, height=300)

            trv_history = ttk.Treeview(newWindow, selectmode='none', height=11)
            trv_history.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

            trv_history['show'] = 'headings'
            trv_history["columns"] = [1, 2, 3, 4]  # column identifiers
            trv_history.column(1, width=100, anchor='c')
            trv_history.heading(1, text='Action Done')
            trv_history.column(2, width=120, anchor='c')
            trv_history.heading(2, text='Configured')
            trv_history.column(3, width=120, anchor='c')
            trv_history.heading(3, text='Destination')
            trv_history.column(4, width=120, anchor='c')
            trv_history.heading(4, text='Last Modify')

            for data in Database().getconfig(device[0]):
                lst = [data[4], data[2], data[3], datetime.strptime(
                    data[5], '%Y-%m-%d %H:%M:%S.%f').date()]
                trv_history.insert("", 'end', values=lst)

            vs = ttk.Scrollbar(newWindow, orient='vertical',
                               command=trv_history.yview)
            vs.grid(row=0, column=3, sticky='ns', pady=10)
            trv_history.config(yscrollcommand=vs.set)

        Button(newWindow, text='Configured History', width=16, height=1, bg='light green',
               command=lambda: configHistory(newWindow, data)).place(x=170, y=290)

        ###
        remove = Menubutton(newWindow, text='Remove Configuration', width=20, height=1, activebackground='#FF5050',
                            bg='#FF5050', relief='raised', borderwidth=2)
        remove.place(x=300, y=290)
        remove.menu = Menu(remove, tearoff=False)
        remove["menu"] = remove.menu
        if(data[6] == 'Switch'):
            remove.menu.add_cascade(
                label="Virtual LAN", command=lambda: RemoveConfig(newWindow, data).vlan())
        if(data[6] == 'Router'):
            remove.menu.add_cascade(
                label="VPN", command=lambda: RemoveConfig(newWindow, data).vpn())
            remove.menu.add_cascade(
                label="RIP Routing", command=lambda: RemoveConfig(newWindow, data).rip())
            remove.menu.add_cascade(
                label="Static Routing", command=lambda: RemoveConfig(newWindow, data).static())
            remove.menu.add_cascade(
                label="EIGRP Routing", command=lambda: RemoveConfig(newWindow, data).eigrp())
            remove.menu.add_cascade(
                label="OSPF Routing", command=lambda: RemoveConfig(newWindow, data).ospf())

        newWindow.mainloop()

    def output(result):
        global CLI
        CLI.config(state="normal")
        CLI.insert(END, result)
        CLI.insert(END, '\n\n')
        CLI.config(state="disabled")
        CLI.see("end")


class Routing():

    def __init__(self, config, window, commands) -> None:
        self.config = config
        self.window = window
        self.commands = commands
        self.output = " None "
        self.flag = threading.Event()

        self.newWindow = Frame(self.window, width=280, bg="black")
        self.newWindow.place(x=120, y=230, height=30)
        self.progress_bar = ttk.Progressbar(
            self.newWindow, orient="horizontal", length=280, mode="indeterminate")
        self.progress_bar.pack()
        self.progress_bar.start()
        # start executing f in another thread
        threading.Thread(target=self.telnet, daemon=True).start()
        # Start the tkinter loop
        self.progress()

    def progress(self):
        # If the flag is set (function f has completed):
        if self.flag.is_set():
            # Stop the progressbar and destroy the toplevel
            Dashboard.output(self.output)
            self.progress_bar.stop()
            self.newWindow.destroy()

        else:
            # Schedule another call to progress_check in 100 milliseconds
            self.progress_bar.after(100, self.progress)

    def ssh(self):
        device = {
            'device_type': "autodetect",
            'host': self.config['IP'],
            'username': self.config['Username'],
            'password': self.config['Password'],
            'secret': self.config['Enable'],
        }
        try:
            device['device_type'] = SSHDetect(**device).autodetect()
            with ConnectHandler(**device) as ssh:
                # ssh.enable()
                self.output = ssh.send_config_set(self.commands)
            Database().saveconfig(self.config)
            messagebox.showinfo(
                "Success", "Configured Successfully", parent=self.window)

        except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
            messagebox.showerror("Error", error, parent=self.window)
            self.output = error
        finally:
            self.flag.set()

    def telnet(self):
        def to_bytes(line): return line.encode('ascii') + b"\n"
        try:
            with telnetlib.Telnet(self.config['IP']) as telnet:
                telnet.read_until(b"Username")
                telnet.write(to_bytes(self.config['Username']))
                telnet.read_until(b"Password")
                telnet.write(to_bytes(self.config['Password']))
                index, m, output = telnet .expect([b">", b"#"])
                if index == 0:
                    telnet.write(b"enable \n")
                    telnet.read_until(b"Password")
                    telnet.write(to_bytes(self.config['Enable']))
                    telnet.read_until(b"#", timeout=5)
                    telnet.write(b"terminal length 0\n")
                telnet.read_until(b"#", timeout=5)
                time.sleep(3)
                telnet.read_very_eager()

                telnet.write(to_bytes("configure terminal"))
                for command in self.commands:
                    telnet.write(to_bytes(command))
                    self.output = telnet.read_until(b"#").decode("utf-8")

                telnet.write(to_bytes("end"))
                self.output = telnet.read_all().decode('ascii')
                self.output = self.output.replace("\r\n", "\n")
            Database().saveconfig(self.config)
            messagebox.showinfo(
                "Success", "Configured Successfully", parent=self.window)
        except TimeoutError as error:
            messagebox.showerror("Error", error, parent=self.window)
            self.output = error
        finally:
            self.flag.set()


class AddConfig (Dashboard):

    def __init__(self, window, device):
        self.device = device
        self.window = window

    def vlan(self):
        newWindow = Frame(self.window, bg='black', padx=20, pady=20)
        newWindow.place(x=450, y=20, width=550, height=300)
        # heading label
        Label(newWindow, text="VLAN ID :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=40)
        Label(newWindow, text="Name :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=80)
        Label(newWindow, text="Interface :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=120)

        # Entry Box
        vlanID = StringVar()
        name = StringVar()
        inter = StringVar()

        Entry(newWindow, width=20, textvariable=vlanID,
              font='Verdana 10 bold').place(x=250, y=40)
        Entry(newWindow, width=20, textvariable=name,
              font='Verdana 10 bold').place(x=250, y=80)
        Entry(newWindow, width=20, textvariable=inter,
              font='Verdana 10 bold').place(x=250, y=120)

        def check():
            try:
                if vlanID.get() and name.get() and inter.get():
                    pass
                    config = {
                        'deviceID': self.device[0],
                        'Name': 'VLAN - ' + name.get(),
                        'Device_Type': self.device[10],
                        'Username': self.device[7],
                        'Password': self.device[8],
                        'Enable': self.device[9],
                        'IP': self.device[3],
                        'Destination': inter.get(),
                        'Activity': 'Add',
                        'Last_Modify': datetime.today()
                    }
                    vlan = [f"vlan {vlanID.get()}", f"name {name.get()}", "exit",
                            f"interface {inter.get()}", f"switchport access vlan {vlanID.get()}"]
                    Routing(config, newWindow, vlan)
                else:
                    messagebox.showerror(
                        "Error", "Information can not be left blank", parent=newWindow)
            except ValueError as e:
                messagebox.showerror("Error", e, parent=newWindow)

        # # button config
        Button(newWindow, text="Config", font='Verdana 10 bold',
               width=30, bg="light blue", command=check).place(x=120, y=230)

    def static(self):
        newWindow = Frame(self.window, bg='black', padx=20, pady=20)
        newWindow.place(x=450, y=20, width=550, height=300)
        # heading label
        Label(newWindow, text="Destination Network Address :",
              font='Verdana 10 bold', foreground="white", bg="black").place(x=20, y=40)
        Label(newWindow, text="Destination Subnet Mask :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=20, y=90)
        Label(newWindow, text="Next Hop :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=20, y=140)

        # Entry Box
        destIP = StringVar()
        destSub = StringVar()
        nextHop = StringVar()

        Entry(newWindow, width=20, textvariable=destIP,
              font='Verdana 10 bold').place(x=270, y=40)
        Entry(newWindow, width=20, textvariable=destSub,
              font='Verdana 10 bold').place(x=270, y=90)
        Entry(newWindow, width=20, textvariable=nextHop,
              font='Verdana 10 bold').place(x=270, y=140)

        def check():
            try:
                IPv4Network(destIP.get())
                IPv4Address(destSub.get())
                IPv4Address(nextHop.get())

                config = {
                    'deviceID': self.device[0],
                    'Name': 'STATIC',
                    'Device_Type': self.device[10],
                    'Username': self.device[7],
                    'Password': self.device[8],
                    'Enable': self.device[9],
                    'IP': self.device[3],
                    'Destination': destIP.get(),
                    'Activity': 'Add',
                    'Last_Modify': datetime.today()
                }
                static = [
                    f"ip route {destIP.get()} {destSub.get()} {nextHop.get()}"]
                Routing(config, newWindow, static)
            except ValueError as e:
                messagebox.showerror("Error", e, parent=newWindow)

        # # button config
        Button(newWindow, text="Config", font='Verdana 10 bold',
               width=30, bg="light blue", command=check).place(x=120, y=230)

    def rip(self):
        newWindow = Frame(self.window, bg='black', padx=20, pady=20)
        newWindow.place(x=450, y=20, width=550, height=300)

        # heading label
        Label(newWindow, text="Network IP Address :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=40)
        Label(newWindow, text="Version :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=90)

        # Entry Box
        networkIP = StringVar()
        version = StringVar()

        Entry(newWindow, width=20, textvariable=networkIP,
              font='Verdana 10 bold').place(x=250, y=40)
        Entry(newWindow, width=20, textvariable=version,
              font='Verdana 10 bold').place(x=250, y=90)

        def check():
            try:
                IPv4Network(networkIP.get())
                config = {
                    'deviceID': self.device[0],
                    'Name': 'RIP',
                    'Device_Type': self.device[10],
                    'Username': self.device[7],
                    'Password': self.device[8],
                    'Enable': self.device[9],
                    'IP': self.device[3],
                    'Destination': networkIP.get(),
                    'Activity': 'Add',
                    'Last_Modify': datetime.today()
                }
                rip = [
                    "router rip", f"version {version.get()}", f"network {networkIP.get()}", "no auto-summary"]
                Routing(config, newWindow, rip)
            except ValueError as e:
                messagebox.showerror("Error", e, parent=newWindow)

        # # button config
        Button(newWindow, text="Config", font='Verdana 10 bold',
               width=30, bg="light blue", command=check).place(x=120, y=230)

    def eigrp(self):
        newWindow = Frame(self.window, bg='black', padx=20, pady=20)
        newWindow.place(x=450, y=20, width=550, height=300)

        # heading label
        Label(newWindow, text="Network Address :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=40)
        Label(newWindow, text="Autonomous-System No.:", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=90)

        # Entry Box
        networkIP = StringVar()
        as_number = StringVar()

        Entry(newWindow, width=20, textvariable=networkIP,
              font='Verdana 10 bold').place(x=250, y=40)
        Entry(newWindow, width=20, textvariable=as_number,
              font='Verdana 10 bold').place(x=250, y=90)

        def check():
            try:
                IPv4Network(networkIP.get())
                config = {
                    'deviceID': self.device[0],
                    'Name': 'EIGRP',
                    'Device_Type': self.device[10],
                    'Username': self.device[7],
                    'Password': self.device[8],
                    'Enable': self.device[9],
                    'IP': self.device[3],
                    'Destination': networkIP.get(),
                    'Activity': 'Add',
                    'Last_Modify': datetime.today()
                }
                eigrp = [
                    f"router eigrp {as_number.get()}", f"network {networkIP.get()}"]
                Routing(config, newWindow, eigrp)
            except ValueError as e:
                messagebox.showerror("Error", e, parent=newWindow)

        # # button config
        # # button config
        Button(newWindow, text="Config", font='Verdana 10 bold',
               width=30, bg="light blue", command=check).place(x=120, y=230)

    def ospf(self):
        newWindow = Frame(self.window, bg='black', padx=20, pady=20)
        newWindow.place(x=450, y=20, width=550, height=300)

        # heading label
        Label(newWindow, text="Process ID :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=40)
        Label(newWindow, text="Network IP Address :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=80)
        Label(newWindow, text="Network Subnet Mask :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=120)
        Label(newWindow, text="Area :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=160)

        # Entry Box
        processID = StringVar()
        networkIP = StringVar()
        networkSub = StringVar()
        area = StringVar()

        Entry(newWindow, width=20, textvariable=processID,
              font='Verdana 10 bold').place(x=250, y=40)
        Entry(newWindow, width=20, textvariable=networkIP,
              font='Verdana 10 bold').place(x=250, y=80)
        Entry(newWindow, width=20, textvariable=networkSub,
              font='Verdana 10 bold').place(x=250, y=120)
        Entry(newWindow, width=20, textvariable=area,
              font='Verdana 10 bold').place(x=250, y=160)

        def check():
            try:
                IPv4Network(networkIP.get())
                IPv4Address(networkSub.get())
                config = {
                    'deviceID': self.device[0],
                    'Name': 'OSPF',
                    'Device_Type': self.device[10],
                    'Username': self.device[7],
                    'Password': self.device[8],
                    'Enable': self.device[9],
                    'IP': self.device[3],
                    'Destination': networkIP.get(),
                    'Activity': 'Add',
                    'Last_Modify': datetime.today()
                }
                ospf = [f"router ospf {processID.get()}",
                        f"network {networkIP.get()} {networkSub.get()} area {area.get()}", "no shut"]
                Routing(config, newWindow, ospf)
            except ValueError as e:
                messagebox.showerror("Error", e, parent=newWindow)

        # # button config
        Button(newWindow, text="Config", font='Verdana 10 bold',
               width=30, bg="light blue", command=check).place(x=120, y=230)

    def vpn(self):
        newWindow = Frame(self.window, bg='black', padx=20, pady=20)
        newWindow.place(x=450, y=20, width=550, height=300)

        # heading label
        Label(newWindow, text="Tunnel No. :", font='Verdana 10 bold',
              fg="white", bg="black").place(x=30, y=40)
        Label(newWindow, text="IP Address :", font='Verdana 10 bold',
              fg="white", bg="black").place(x=30, y=70)
        Label(newWindow, text="Subnet Mask :", font='Verdana 10 bold',
              fg="white", bg="black").place(x=30, y=100)
        Label(newWindow, text="Source Address :", font='Verdana 10 bold',
              fg="white", bg="black").place(x=30, y=130)
        Label(newWindow, text="Destination Address :", font='Verdana 10 bold',
              fg="white", bg="black").place(x=30, y=160)

        # Entry Box
        tunnel = StringVar()
        ip = StringVar()
        sub = StringVar()
        source = StringVar()
        dest = StringVar()

        Entry(newWindow, width=20, textvariable=tunnel,
              font='Verdana 10 bold').place(x=250, y=40)
        Entry(newWindow, width=20, textvariable=ip,
              font='Verdana 10 bold').place(x=250, y=70)
        Entry(newWindow, width=20, textvariable=sub,
              font='Verdana 10 bold').place(x=250, y=100)
        Entry(newWindow, width=20, textvariable=source,
              font='Verdana 10 bold').place(x=250, y=130)
        Entry(newWindow, width=20, textvariable=dest,
              font='Verdana 10 bold').place(x=250, y=160)

        def check():
            try:
                IPv4Network(ip.get())
                IPv4Address(sub.get())
                IPv4Address(source.get())
                IPv4Address(dest.get())
                config = {
                    'deviceID': self.device[0],
                    'Name': 'VPN',
                    'Device_Type': self.device[10],
                    'Username': self.device[7],
                    'Password': self.device[8],
                    'Enable': self.device[9],
                    'IP': self.device[3],
                    'Destination': dest.get(),
                    'Activity': 'Add',
                    'Last_Modify': datetime.today()
                }
                vpn = [f"interface tunnel {tunnel.get()}",
                       f"ip address {ip.get()} {sub.get()}", f"tunnel source {source.get()}", f"tunnel destination {dest.get()}"]
                Routing(config, newWindow, vpn)
            except ValueError as e:
                messagebox.showerror("Error", e, parent=newWindow)

        # # button config
        Button(newWindow, text="Config", font='Verdana 10 bold',
               width=30, bg="light blue", command=check).place(x=120, y=230)


class RemoveConfig (Dashboard):

    def __init__(self, window, device):
        self.device = device
        self.window = window

    def vlan(self):
        newWindow = Frame(self.window, bg='black', padx=20, pady=20)
        newWindow.place(x=450, y=20, width=550, height=300)
        # heading label
        Label(newWindow, text="VLAN ID :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=40)
        Label(newWindow, text="Name :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=80)
        Label(newWindow, text="Interface :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=120)

        # Entry Box
        vlanID = StringVar()
        name = StringVar()
        inter = StringVar()

        Entry(newWindow, width=20, textvariable=vlanID,
              font='Verdana 10 bold').place(x=250, y=40)
        Entry(newWindow, width=20, textvariable=name,
              font='Verdana 10 bold').place(x=250, y=80)
        Entry(newWindow, width=20, textvariable=inter,
              font='Verdana 10 bold').place(x=250, y=120)

        def check():
            try:
                if vlanID.get() and name.get() and inter.get():
                    pass
                    config = {
                        'deviceID': self.device[0],
                        'Name': 'VLAN - ' + name.get(),
                        'Device_Type': self.device[10],
                        'Username': self.device[7],
                        'Password': self.device[8],
                        'Enable': self.device[9],
                        'IP': self.device[3],
                        'Destination': inter.get(),
                        'Activity': 'Remove',
                        'Last_Modify': datetime.today()
                    }
                    vlan = [f"interface {inter.get()}", f"switchport access vlan 1", "exit",
                            f"no vlan {vlanID.get()}"]
                    Routing(config, newWindow, vlan)
                else:
                    messagebox.showerror(
                        "Error", "Information can not be left blank", parent=newWindow)
            except ValueError as e:
                messagebox.showerror("Error", e, parent=newWindow)

        # # button config
        Button(newWindow, text="Config", font='Verdana 10 bold',
               width=30, bg='#FF5050', command=check).place(x=120, y=230)

    def static(self):
        newWindow = Frame(self.window, bg='black', padx=20, pady=20)
        newWindow.place(x=450, y=20, width=550, height=300)
        # heading label
        Label(newWindow, text="Destination Network Address :",
              font='Verdana 10 bold', foreground="white", bg="black").place(x=20, y=40)
        Label(newWindow, text="Destination Subnet Mask :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=20, y=90)
        Label(newWindow, text="Next Hop :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=20, y=140)

        # Entry Box
        destIP = StringVar()
        destSub = StringVar()
        nextHop = StringVar()

        Entry(newWindow, width=20, textvariable=destIP,
              font='Verdana 10 bold').place(x=270, y=40)
        Entry(newWindow, width=20, textvariable=destSub,
              font='Verdana 10 bold').place(x=270, y=90)
        Entry(newWindow, width=20, textvariable=nextHop,
              font='Verdana 10 bold').place(x=270, y=140)

        def check():
            try:
                IPv4Network(destIP.get())
                IPv4Address(destSub.get())
                IPv4Address(nextHop.get())

                config = {
                    'deviceID': self.device[0],
                    'Name': 'STATIC',
                    'Device_Type': self.device[10],
                    'Username': self.device[7],
                    'Password': self.device[8],
                    'Enable': self.device[9],
                    'IP': self.device[3],
                    'Destination': destIP.get(),
                    'Activity': 'Remove',
                    'Last_Modify': datetime.today()
                }
                static = [
                    f"no ip route {destIP.get()} {destSub.get()} {nextHop.get()}"]
                Routing(config, newWindow, static)
            except ValueError as e:
                messagebox.showerror("Error", e, parent=newWindow)

         # # button config
        Button(newWindow, text="Config", font='Verdana 10 bold',
               width=30, bg='#FF5050', command=check).place(x=120, y=230)

    def rip(self):
        newWindow = Frame(self.window, bg='black', padx=20, pady=20)
        newWindow.place(x=450, y=20, width=550, height=300)

        # heading label
        Label(newWindow, text="Network IP Address :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=40)
        # Entry Box
        networkIP = StringVar()

        Entry(newWindow, width=20, textvariable=networkIP,
              font='Verdana 10 bold').place(x=250, y=40)

        def check():
            try:
                IPv4Network(networkIP.get())
                config = {
                    'deviceID': self.device[0],
                    'Name': 'RIP',
                    'Device_Type': self.device[10],
                    'Username': self.device[7],
                    'Password': self.device[8],
                    'Enable': self.device[9],
                    'IP': self.device[3],
                    'Destination': networkIP.get(),
                    'Activity': 'Remove',
                    'Last_Modify': datetime.today()
                }
                rip = ["router rip", f"no network {networkIP.get()}"]
                Routing(config, newWindow, rip)
            except ValueError as e:
                messagebox.showerror("Error", e, parent=newWindow)

         # # button config
        Button(newWindow, text="Config", font='Verdana 10 bold',
               width=30, bg='#FF5050', command=check).place(x=120, y=230)

    def eigrp(self):
        newWindow = Frame(self.window, bg='black', padx=20, pady=20)
        newWindow.place(x=450, y=20, width=550, height=300)

        # heading label
        Label(newWindow, text="Network Address :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=40)
        Label(newWindow, text="Autonomous-System No.:", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=90)

        # Entry Box
        networkIP = StringVar()
        as_number = StringVar()

        Entry(newWindow, width=20, textvariable=networkIP,
              font='Verdana 10 bold').place(x=250, y=40)
        Entry(newWindow, width=20, textvariable=as_number,
              font='Verdana 10 bold').place(x=250, y=90)

        def check():
            try:
                IPv4Network(networkIP.get())
                config = {
                    'deviceID': self.device[0],
                    'Name': 'EIGRP',
                    'Device_Type': self.device[10],
                    'Username': self.device[7],
                    'Password': self.device[8],
                    'Enable': self.device[9],
                    'IP': self.device[3],
                    'Destination': networkIP.get(),
                    'Activity': 'Remove',
                    'Last_Modify': datetime.today()
                }
                eigrp = [
                    f"router eigrp {as_number.get()}", f"no network {networkIP.get()}"]
                Routing(config, newWindow, eigrp)
            except ValueError as e:
                messagebox.showerror("Error", e, parent=newWindow)

        # # button config
        Button(newWindow, text="Config", font='Verdana 10 bold',
               width=30, bg='#FF5050', command=check).place(x=120, y=230)

    def ospf(self):
        newWindow = Frame(self.window, bg='black', padx=20, pady=20)
        newWindow.place(x=450, y=20, width=550, height=300)

        # heading label
        Label(newWindow, text="Process ID :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=40)
        Label(newWindow, text="Network IP Address :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=80)
        Label(newWindow, text="Network Subnet Mask :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=120)
        Label(newWindow, text="Area :", font='Verdana 10 bold',
              foreground="white", bg="black").place(x=30, y=160)

        # Entry Box
        processID = StringVar()
        networkIP = StringVar()
        networkSub = StringVar()
        area = StringVar()

        Entry(newWindow, width=20, textvariable=processID,
              font='Verdana 10 bold').place(x=250, y=40)
        Entry(newWindow, width=20, textvariable=networkIP,
              font='Verdana 10 bold').place(x=250, y=80)
        Entry(newWindow, width=20, textvariable=networkSub,
              font='Verdana 10 bold').place(x=250, y=120)
        Entry(newWindow, width=20, textvariable=area,
              font='Verdana 10 bold').place(x=250, y=160)

        def check():
            try:
                IPv4Network(networkIP.get())
                IPv4Address(networkSub.get())
                config = {
                    'deviceID': self.device[0],
                    'Name': 'OSPF',
                    'Device_Type': self.device[10],
                    'Username': self.device[7],
                    'Password': self.device[8],
                    'Enable': self.device[9],
                    'IP': self.device[3],
                    'Destination': networkIP.get(),
                    'Activity': 'Remove',
                    'Last_Modify': datetime.today()
                }
                ospf = [f"router ospf {processID.get()}",
                        f"no network {networkIP.get()} {networkSub.get()} area {area.get()}", "shut", "no shut"]
                Routing(config, newWindow, ospf)
            except ValueError as e:
                messagebox.showerror("Error", e, parent=newWindow)

         # # button config
        Button(newWindow, text="Config", font='Verdana 10 bold',
               width=30, bg='#FF5050', command=check).place(x=120, y=230)

    def vpn(self):
        newWindow = Frame(self.window, bg='black', padx=20, pady=20)
        newWindow.place(x=450, y=20, width=550, height=300)

        # heading label
        Label(newWindow, text="Tunnel No. :", font='Verdana 10 bold',
              fg="white", bg="black").place(x=30, y=40)
        # Entry Box
        tunnel = StringVar()

        Entry(newWindow, width=20, textvariable=tunnel,
              font='Verdana 10 bold').place(x=250, y=40)

        def check():
            try:
                config = {
                    'deviceID': self.device[0],
                    'Name': 'VPN',
                    'Device_Type': self.device[10],
                    'Username': self.device[7],
                    'Password': self.device[8],
                    'Enable': self.device[9],
                    'IP': self.device[3],
                    'Destination': tunnel.get(),
                    'Activity': 'Remove',
                    'Last_Modify': datetime.today()
                }
                vpn = [f"remove interface tunnel {tunnel.get()}"]
                self.output(Routing(config, newWindow, vpn))
            except ValueError as e:
                messagebox.showerror("Error", e, parent=newWindow)

         # # button config
        Button(newWindow, text="Config", font='Verdana 10 bold',
               width=30, bg='#FF5050', command=check).place(x=120, y=230)


if __name__ == '__main__':

    # Dashboard(Tk(), Database().getUser('kk_pl', 'K2545'))
    Login()
