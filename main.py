from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageDraw
from datetime import *
import time
from manage import *


class Dashboard:
    def __init__(self, window):
        self.window = window
        self.window.title("CyberNation")
        self.window.geometry("1366x768")
        self.window.state('zoomed')
        self.window.config(background='#eff5f6')
        
        # Window Icon Photo
        icon = PhotoImage(file='images\\icon.png')
        self.window.iconphoto(True, icon)

        # ================== HEADER ====================================================
        self.header = Frame(self.window, bg='#009df4')
        self.header.place(x=300, y=0, width=1070, height=60)

        # self.logout_text = Button(self.header, text="Logout", bg='#32cf8e', font=("", 13, "bold"), bd=0, fg='white',
        #                           cursor='hand2', activebackground='#32cf8e')
        # self.logout_text.place(x=950, y=15)

        # ================== SIDEBAR ===================================================
        self.sidebar = Frame(self.window, bg='#ffffff')
        self.sidebar.place(x=0, y=0, width=300, height=750)

        # ============= BODY ==========================================================

        self.heading = Label(self.window, text='Dashboard', font=("", 15, "bold"), fg='#0064d3', bg='#eff5f6')
        self.heading.place(x=325, y=70)

        # body frame 1
        self.list_device = Frame(self.window, bg='#ffffff')
        self.list_device.place(x=328, y=110, width=1040, height=350)

        # body frame 2
        self.bodyFrame2 = Frame(self.window, bg='#009aa5')
        self.bodyFrame2.place(x=328, y=495, width=310, height=220)

        # body frame 3
        self.bodyFrame3 = Frame(self.window, bg='#e21f26')
        self.bodyFrame3.place(x=680, y=495, width=310, height=220)

        # body frame 4
        self.bodyFrame4 = Frame(self.window, bg='#ffcb1f')
        self.bodyFrame4.place(x=1030, y=495, width=310, height=220)

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
        self.logoImage = ImageTk.PhotoImage(file='images/hyy.png')
        self.logo = Label(self.sidebar, image=self.logoImage, bg='#ffffff')
        self.logo.place(x=70, y=80)

        # Name of brand/person
        self.brandName = Label(
            self.sidebar, text='USER NAME', bg='#ffffff', font=("", 15, "bold"))
        self.brandName.place(x=80, y=200)

        # Add Device
        self.routerImage = ImageTk.PhotoImage(file='images/router.png')
        self.router = Label(
            self.sidebar, image=self.routerImage, bg='#ffffff')
        self.router.place(x=35, y=289)

        self.router_text = Button(self.sidebar, text="Add Device", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                     cursor='hand2', activebackground='#ffffff', command= self.add_device)
        self.router_text.place(x=80, y=287)

        # Manage
        self.manageImage = ImageTk.PhotoImage(file='images/manage-icon.png')
        self.manage = Label(self.sidebar, image=self.manageImage, bg='#ffffff')
        self.manage.place(x=35, y=340)

        self.manage_text = Button(self.sidebar, text="Manage", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                  cursor='hand2', activebackground='#ffffff')
        self.manage_text.place(x=80, y=345)

        # Settings
        self.settingsImage = ImageTk.PhotoImage(
            file='images/settings-icon.png')
        self.settings = Label(
            self.sidebar, image=self.settingsImage, bg='#ffffff')
        self.settings.place(x=35, y=402)

        self.settings_text = Button(self.sidebar, text="Settings", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                    cursor='hand2', activebackground='#ffffff')
        self.settings_text.place(x=80, y=402)

        # =============================================================================
        # ============= BODY ==========================================================
        # =============================================================================

        # Body Frame 1
        self.devices()

        # Body Frame 2

        # Body Frame 3

        # Body Frame 4

        

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
        for data in getAlldevice():
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
        # A Label widget to show in toplevel
        lb1= Label(newWindow, text="Name", width=15, font=("arial",12))  
        lb1.place(x=10, y=120)  
        en1= Entry(newWindow,width=25, font=("arial",12)) 
        en1.place(x=200, y=120)  
  
        lb2= Label(newWindow, text="IP Address", width=15, font=("arial",12))  
        lb2.place(x=9, y=160)  
        en2= Entry(newWindow, width=25, font=("arial",12))
        en2.place(x=200, y=160)  
  
        lb3= Label(newWindow, text="Description", width=15,font=("arial",12))  
        lb3.place(x=10, y=200)  
        en3= Entry(newWindow,width=25, font=("arial",12))
        en3.place(x=200, y=200)  

        lb4= Label(newWindow, text="Select Device", width=15,font=("arial",12))  
        lb4.place(x=10,y=240) 
        type_of_devices = ("Router", "Switch")  
        cv = StringVar()  
        cv.set("Router") 
        en4= OptionMenu(newWindow, cv, *type_of_devices)  
        en4.config(width=20)    
        en4.place(x=200, y=240)  
  
        lb5= Label(newWindow, text="SSH Username", width=15,font=("arial",12))  
        lb5.place(x=11, y=280)  
        en5= Entry(newWindow, width=25, font=("arial",12))
        en5.place(x=200, y=280)  
  
        lb6= Label(newWindow, text="SSH Password", width=15,font=("arial",12))  
        lb6.place(x=11, y=320)  
        en6 = Entry(newWindow,show='*', width=25, font=("arial",12)) 
        en6.place(x=200, y=320)
        
        def check_empty():
    
            if db.devices.find_one({ "IP" : en2.get()}):
                lb = Label(newWindow, text="IP address had already used", fg='red', font=('Arial',11,'bold'))
                lb.place(x=100, y=350)
            elif en1.get() and en2.get() and en3.get() and cv.get() and en5.get() and en6.get():
                global count
                count = count + 1
                lst = [count,en1.get(),en2.get(),cv.get(),datetime.today()]
                self.trv.insert("",'end',iid=en2.get(),values=lst)
                savedevice(en1.get(), en2.get(), en3.get(), cv.get(), en5.get(), en6.get(), datetime.today())
                newWindow.destroy()
                
            else:
                lb = Label(newWindow, text="Device Information can not be left blank", fg='red', font=('Arial',11,'bold'))
                lb.place(x=100, y=350)

        Button(newWindow, text="ADD", width=30, command=check_empty).place(x=100,y=400)
    
    def deviceInfo(self,event):
        IP = self.trv.selection()[0]
        data = getdevice(IP)
        newWindow = Toplevel(self.window)
        newWindow.title("Device Information")
        newWindow.resizable(False,False)
        newWindow.geometry("450x500")
        frame = Frame(newWindow, width=450, height=500)
        frame.pack()
        device_img = ImageTk.PhotoImage(Image.open('images/device.png'))
        device_info = Label(frame, image= device_img, bg= '#ffffff')
        device_info.pack()
        device_info.place(x=130, y= 20)
        
        # A Label widget to show in toplevel
        lb1= Label(newWindow, text="Name", width=15, font=("arial",12))  
        lb1.place(x=10, y=140)  
        en1= Label(newWindow, text= data['Name'], width=25, font=("arial",12)) 
        en1.place(x=200, y=140)  
  
        lb2= Label(newWindow, text="IP Address", width=15, font=("arial",12))  
        lb2.place(x=9, y=180)  
        en2= Label(newWindow,text= data['IP'], width=25, font=("arial",12))
        en2.place(x=200, y=180)  
  
        lb3= Label(newWindow, text="Description", width=15,font=("arial",12))  
        lb3.place(x=10, y=220)  
        en3= Label(newWindow,text= data['Description'], width=25, font=("arial",12))
        en3.place(x=200, y=220)  

        # lb4= Label(newWindow, text="Select Device", width=15,font=("arial",12))  
        # lb4.place(x=10,y=260) 
        # type_of_devices = ("Router", "Switch")  
        # cv = StringVar()  
        # cv.set("Router") 
        # en4= OptionMenu(newWindow, cv, *type_of_devices)  
        # en4.config(width=20)    
        # en4.place(x=200, y=260)  
  
        lb5= Label(newWindow, text="SSH Username", width=15,font=("arial",12))  
        lb5.place(x=11, y=300)  
        en5= Label(newWindow,text= data['Username'], width=25, font=("arial",12))
        en5.place(x=200, y=300)  
  
        lb6= Label(newWindow, text="SSH Password", width=15,font=("arial",12))  
        lb6.place(x=11, y=340)  
        en6 = Label(newWindow, text= data['Password'], width=25, font=("arial",12)) 
        en6.place(x=200, y=340)
    


if __name__ == '__main__':
    window = Tk()
    Dashboard(window)
    window.mainloop()
