from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageDraw
from datetime import *
import time
from manage import *


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

        self.heading = Label(self.window, text='Dashboard', font=("", 15, "bold"), fg='#0064d3', bg='#eff5f6').place(x=325, y=70)

        # body frame 1
        self.list_device = Frame(self.window, bg='#ffffff')
        self.list_device.place(x=328, y=110, width=1040, height=350)

        # body frame 2
        self.bodyFrame2 = Frame(self.window, bg='#009aa5').place(x=328, y=495, width=310, height=220)

        # body frame 3
        self.bodyFrame3 = Frame(self.window, bg='#e21f26').place(x=680, y=495, width=310, height=220)

        # body frame 4
        self.bodyFrame4 = Frame(self.window, bg='#ffcb1f').place(x=1030, y=495, width=310, height=220)

        # ==============================================================================
        # ================== SIDEBAR ===================================================
        # ==============================================================================

        # date and Time
        self.clock_image = ImageTk.PhotoImage(file="images/time.png")
        self.date_time_image = Label(
            self.sidebar, image=self.clock_image, bg="white")
        self.date_time_image.place(x=88, y=20)

        self.date_time = Label(self.window)
        self.date_time.place(x=115, y=15)
        self.show_time()

        # logo
        gender = user['Gender']
        self.logoImage = ImageTk.PhotoImage(file=f'images/{gender}.png')
        self.logo = Label(self.sidebar, image=self.logoImage, bg='#ffffff').place(x=60, y=80)

        # Name of brand/person
        uname = user['Fname'] + ' '+ user ['Lname']
        self.Username = Label(self.sidebar, text= uname, bg='#ffffff', font=("", 15, "bold")).place(x=80, y=240)

        #Gender
        self.gen_img = ImageTk.PhotoImage(file='images/gender.png')
        Label(self.sidebar, image= self.gen_img, bg='#ffffff').place(x=10, y= 290)
        Label(self.sidebar, text= user['Gender'], bg='#ffffff', font='Verdana 13 bold').place(x=80,y=300)

        #Organi
        self.org_img = ImageTk.PhotoImage(file='images/org.png')
        Label(self.sidebar, image= self.org_img, bg='#ffffff').place(x=10, y= 350)
        Label(self.sidebar, text= user['Org'], bg='#ffffff', font='Verdana 13 bold').place(x=80,y=370)

        #Contact
        self.contact_img = PhotoImage(file='images/contact.png')
        Label(self.sidebar, image= self.contact_img, bg='#ffffff').place(x=15, y= 420)
        Label(self.sidebar, text= '8318031071', bg='#ffffff', font='Verdana 13 bold').place(x=80,y=440)
        

        # Separator object
        separator = ttk.Separator(self.sidebar, orient='horizontal')
        separator.place(relx=0, rely= 0.83, relwidth=0.22)

        # Add Device
        self.routerImage = PhotoImage(file='images/device.png').subsample(3,3)
        Button(self.sidebar, text="  Add Device", bg='#ffffff', font=("", 14, "bold"), bd=0, image= self.routerImage, compound= LEFT,
        cursor='hand2', height=40,activebackground='#ffffff', command= self.add_device).place(relx= 0.035, rely= 0.835)

        # Separator object
        separator = ttk.Separator(self.sidebar, orient='horizontal')
        separator.place(relx=0, rely= 0.91, relwidth=0.22)

        # Settings
        self.settingsImage = PhotoImage(file='images/setting.png')
        Button(self.sidebar, text="Settings", bg='#ffffff', font=("", 13, "bold"), bd=0, image= self.settingsImage, compound= LEFT,
        cursor='hand2', activebackground='#ffffff').place(relx=0, rely=0.92)
        
        # Separator object
        separator = ttk.Separator(self.sidebar, orient='vertical').place(relx=0.109, rely= 0.91, relheight= 0.22)


        # Logout
        self.logoutImage = PhotoImage(file='images/logout.png')
        Button(self.sidebar, text="  Logout!  ", bg='#ffffff', font=("", 13, "bold"), bd=0, image= self.logoutImage, compound= LEFT,
        cursor='hand2', activebackground='#ffffff', command= lambda : self.window.destroy()).place(relx=0.12, rely=0.92)

        # =============================================================================
        # ============= BODY ==========================================================
        # =============================================================================

        # Body Frame 1
        self.devices()
        
    def show_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        set_text = f"  {self.time} \n {self.date}"
        self.date_time.configure(text=set_text, font=(
            "", 13, "bold"), bd=0, bg="white", fg="black")
        self.date_time.after(100, self.show_time)
    
    def devices(self):
        
        self.trv = ttk.Treeview(self.list_device, selectmode = 'browse')
        self.trv.grid(row=1,column=0,columnspan=3,padx=20,pady=20)
        self.trv['height']=14 # Number of rows to display, default is 10
        self.trv['show'] = 'headings' 
        self.trv["columns"] = [1,2,3,4,5] # column identifiers 
        self.trv.column(1, width = 120, anchor ='c') # Headings of respective columns
        self.trv.heading(1, text = 'Sr. No.')
        self.trv.column(2, width = 200, anchor ='c') # Headings of respective columns
        self.trv.heading(2, text = 'Device Name')
        self.trv.column(3, width = 200, anchor ='c') # Headings of respective columns
        self.trv.heading(3, text = 'IP Adress')
        self.trv.column(4, width = 200, anchor ='c') # Headings of respective columns
        self.trv.heading(4, text = 'Device Type')
        self.trv.column(5, width = 250, anchor ='c') # Headings of respective columns
        self.trv.heading(5, text = 'Last Modify')
        global count
        count = 0
        for data in getAlldevice(self.user):
            count = count + 1
            lst = [count,data['Name'],data['IP'],data['Type'],data['Last_Modify']]
            self.trv.insert("",'end',iid=data['IP'],values=lst)

        self.trv.bind("<Double-1>", self.deviceInfo)
        vs = ttk.Scrollbar(self.list_device,orient='vertical',command=self.trv.yview)
        # vs.pack(side= RIGHT, fill= Y)
        vs.grid(row=1,column=3, sticky= 'ns',pady= 20)
        self.trv.config(yscrollcommand= vs.set)
        
    def add_device(self):
        # Toplevel object which will be treated as a new window
        newWindow = Toplevel(self.window)
        # sets the title of the Toplevel widget
        newWindow.title("Add Device")
        newWindow.resizable(False,False)
        # sets the geometry of toplevel
        newWindow.geometry("450x500")
        #image
        device_img = PhotoImage(file='images/device.png')
        device_info = Label(newWindow, image= device_img, height= 100)
        device_info.pack()
        device_info.place(x=130, y= 20)
        # A Label widget to show in toplevel
        en1 = StringVar()
        en2 = StringVar()
        en3 = StringVar()
        en5 = StringVar()
        en6 = StringVar()

        Label(newWindow, text="Name",font=("arial",12)).place(x=40, y=140)  
        Entry(newWindow,width=25, font=("arial",12),textvariable = en1).place(x=200, y=140)  
  
        Label(newWindow, text="IP Address", font=("arial",12)).place(x=40, y=180)  
        Entry(newWindow, width=25, font=("arial",12), textvariable = en2).place(x=200, y=180) 
  
        Label(newWindow, text="Description",font=("arial",12)).place(x=40, y=220)  
        Entry(newWindow,width=25, font=("arial",12),textvariable = en3).place(x=200, y=220)  

        Label(newWindow, text="Select Device",font=("arial",12)).place(x=40,y=260) 
        type_of_devices = ("Router", "Switch")  
        cv = StringVar()  
        cv.set("Router") 
        en4= OptionMenu(newWindow, cv, *type_of_devices)  
        en4.config(width=20)    
        en4.place(x=200, y=260)  
  
        Label(newWindow, text="SSH Username",font=("arial",12)).place(x=40, y=300)  
        Entry(newWindow, width=25, font=("arial",12), textvariable = en5).place(x=200, y=300)  
  
        Label(newWindow, text="SSH Password",font=("arial",12)).place(x=40, y=340)  
        Entry(newWindow,show='*', width=25, font=("arial",12), textvariable = en6).place(x=200, y=340)
        
        def check_empty():
            # User = db.User.find({"Username" : self.user['Username'], "Password":self.user['Password']}).collection
            # collection = User['Devices']
            # print(collection)
            if db.devices.find_one({ "IP" : en2.get()}):
                lb = Label(newWindow, text="IP address had already used", fg='red', font=('Arial',11,'bold'))
                lb.place(x=100, y=360)
            elif en1.get() and en2.get() and en3.get() and cv.get() and en5.get() and en6.get():
                global count
                count = count + 1
                lst = [count,en1.get(),en2.get(),cv.get(),datetime.today()]
                self.trv.insert("",'end',iid=en2.get(),values=lst)
                savedevice(self.user,en1.get(), en2.get(), en3.get(), cv.get(), en5.get(), en6.get(), datetime.today())
                newWindow.destroy()
                
            else:
                lb = Label(newWindow, text="Device Information can not be left blank", fg='red', font=('Arial',11,'bold'))
                lb.place(x=100, y=360)

        Button(newWindow, text="ADD", width=30, command=check_empty).place(x=100,y=400)
        newWindow.mainloop()
     
    def configWindow(self):
        newWindow = Toplevel(self.window)
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
        
        Button(newWindow, width= 15, height= 3, text="Default Routing", bg="#FF33B2").place(x = 50,  y= 200)
        Button(newWindow, width= 15, height= 3, text="Static Routing",  bg="#33FFE9").place(x = 250, y= 200)
        Button(newWindow, width= 15, height= 3, text="RIP Routing",     bg="#A533FF").place(x = 50,  y= 275)
        Button(newWindow, width= 15, height= 3, text="OSPF Routing",    bg="#ff1111").place(x = 250, y= 275)
        Button(newWindow, width= 15, height= 3, text="BGP Routing",     bg="#33FF5B").place(x = 50,  y= 350)
        Button(newWindow, width= 15, height= 3, text="EIGRP Routing",   bg="#E9FF33").place(x = 250, y= 350)
        

        newWindow.mainloop()

    def deviceInfo(self,event):
        IP = self.trv.selection()[0]
        data = getdevice(IP)
        newWindow = Toplevel(self.window)
        newWindow.title("Device Information")
        newWindow.resizable(False,False)
        newWindow.geometry("430x450")
        newWindow.configure(bg='white')
        
        #image
        device_img = PhotoImage(file='images\device.png')
        device_info = Label(newWindow, image= device_img, bg='white')
        device_info.pack()
        device_info.place(x=130, y= 20)
        
        # A Label widget to show in toplevel
        Label(newWindow, text="Name : ",font=("arial",12),bg='white').place(x = 40,y = 160)  
        Label(newWindow, text= data['Name'], font=("arial",12),bg='white').place(x= 180, y=160) 
        Label(newWindow, text="IP Address : ", font=("arial",12),bg='white').place(x=40, y=200)  
        Label(newWindow,text= data['IP'], font=("arial",12),bg='white').place(x=180, y=200)
        Label(newWindow, text="Description : ", font=("arial",12),bg='white').place(x=40, y=240)   
        Label(newWindow,text= data['Description'], font=("arial",12),bg='white').place(x=180, y=240)
        Label(newWindow, text="SSH Username : ", font=("arial",12),bg='white').place(x=40, y=280)  
        Label(newWindow,text= data['Username'],font=("arial",12),bg='white').place(x=180, y=280)
        Label(newWindow,text="Last Modify : ",font=("arial",12),bg='white').place(x = 40,y= 320)
        Label(newWindow,text=data['Last_Modify'],font=("arial",12),bg='white').place(x=180, y=320)

        # Button for operation
        Button(newWindow, text= 'New Configuration', width= 15,bg='light blue', command= self.configWindow).place(x=30, y= 380)
        Button(newWindow, text= 'Old Configuration', width= 15,bg='light green').place(x=160, y= 380)

        def deletedevice():
            IP = self.trv.selection()[0]
            self.trv.delete(self.trv.selection())
            deleteDevice(IP)
            newWindow.destroy()

        Button(newWindow, text= 'Delete Device', width= 15,bg='red',command= deletedevice).place(x=290, y= 380)

        newWindow.mainloop()


if __name__ == '__main__':
    collection = db.User
    x = collection.find_one({"Username": "kk_pl", "Password":"K2545" })
    window = Tk()
    Dashboard(window,x)
    window.mainloop()
