from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from datetime import *
import time
import csv
import json
from tkinter.filedialog import asksaveasfile


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

        self.logout_text = Button(self.header, text="Logout", bg='#32cf8e', font=("", 13, "bold"), bd=0, fg='white',
                                  cursor='hand2', activebackground='#32cf8e')
        self.logout_text.place(x=950, y=15)

        # ==============================================================================
        # ================== SIDEBAR ===================================================
        # ==============================================================================
        self.sidebar = Frame(self.window, bg='#ffffff')
        self.sidebar.place(x=0, y=0, width=300, height=750)

        # =============================================================================
        # ============= BODY ==========================================================
        # =============================================================================
        self.heading = Label(self.window, text='Dashboard', font=("", 15, "bold"), fg='#0064d3', bg='#eff5f6')
        self.heading.place(x=325, y=70)

        # body frame 1
        self.list_device = Frame(self.window, bg='#ffffff')
        self.list_device.place(x=328, y=110, width=1040, height=350)
        # v = Scrollbar(self.list_device)
        # # v.pack(side = RIGHT, fill = Y)

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

        # logo
        self.logoImage = ImageTk.PhotoImage(file='images/hyy.png')
        self.logo = Label(self.sidebar, image=self.logoImage, bg='#ffffff')
        self.logo.place(x=70, y=80)

        # Name of brand/person
        self.brandName = Label(
            self.sidebar, text='USER NAME', bg='#ffffff', font=("", 15, "bold"))
        self.brandName.place(x=80, y=200)

        # Add Device
        self.dashboardImage = ImageTk.PhotoImage(file='images/router.png')
        self.dashboard = Label(
            self.sidebar, image=self.dashboardImage, bg='#ffffff')
        self.dashboard.place(x=35, y=289)

        self.dashboard_text = Button(self.sidebar, text="Add Device", bg='#ffffff', font=("", 13, "bold"), bd=0,
                                     cursor='hand2', activebackground='#ffffff', command= self.add_router)
        self.dashboard_text.place(x=80, y=287)

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
        # self.total_people = Label(
        #     self.bodyFrame2, text='230', bg='#009aa5', font=("", 25, "bold"))
        # self.total_people.place(x=120, y=100)

        # self.totalPeopleImage = ImageTk.PhotoImage(file='images/left-icon.png')
        # self.totalPeople = Label(
        #     self.bodyFrame2, image=self.totalPeopleImage, bg='#009aa5')
        # self.totalPeople.place(x=220, y=0)

        # self.totalPeople_label = Label(self.bodyFrame2, text="Total People", bg='#009aa5', font=("", 12, "bold"),
        #                                fg='white')
        # self.totalPeople_label.place(x=5, y=5)

        # Body Frame 3
        # self.people_left = Label(
        #     self.bodyFrame3, text='50', bg='#e21f26', font=("", 25, "bold"))
        # self.people_left.place(x=120, y=100)

        # left icon
        # self.LeftImage = ImageTk.PhotoImage(file='images/left-icon.png')
        # self.Left = Label(self.bodyFrame3, image=self.LeftImage, bg='#e21f26')
        # self.Left.place(x=220, y=0)

        # self.peopleLeft_label = Label(self.bodyFrame3, text="Left", bg='#e21f26', font=("", 12, "bold"),
        #                               fg='white')
        # self.peopleLeft_label.place(x=5, y=5)

        # Body Frame 4
        # self.total_earnings = Label(
        #     self.bodyFrame4, text='$40,000.00', bg='#ffcb1f', font=("", 25, "bold"))
        # self.total_earnings.place(x=80, y=100)

        # self.earnings_label = Label(self.bodyFrame4, text="Total Earnings", bg='#ffcb1f', font=("", 12, "bold"),
        #                             fg='white')
        # self.earnings_label.place(x=5, y=5)
        # Frame 4 icon
        # self.earningsIcon_image = ImageTk.PhotoImage(file='images/earn3.png')
        # self.earningsIcon = Label(
        #     self.bodyFrame4, image=self.earningsIcon_image, bg='#ffcb1f')
        # self.earningsIcon.place(x=220, y=0)

        # date and Time
        self.clock_image = ImageTk.PhotoImage(file="images/time.png")
        self.date_time_image = Label(
            self.sidebar, image=self.clock_image, bg="white")
        self.date_time_image.place(x=88, y=20)

        self.date_time = Label(self.window)
        self.date_time.place(x=115, y=15)
        self.show_time()

    def show_time(self):
        self.time = time.strftime("%H:%M:%S")
        self.date = time.strftime('%Y/%m/%d')
        set_text = f"  {self.time} \n {self.date}"
        self.date_time.configure(text=set_text, font=(
            "", 13, "bold"), bd=0, bg="white", fg="black")
        self.date_time.after(100, self.show_time)
    
    def devices(self):
        lst = [ ('List of Devices:', '', '',''),
               ('Serial No.','Description','IP Address', 'Device Type')]
        for i in range(len(lst)):
            for j in range(len(lst[0])):
                 
                self.e = Label(self.list_device, text= str(lst[i][j]),bg='#ffffff',
                               width=20, fg='blue', font=('Arial',16,'bold'))
                self.e.grid(row=i, column=j)

    def add_router(self):
        # Toplevel object which will be treated as a new window
        newWindow = Toplevel(self.window)
        # sets the title of the Toplevel widget
        newWindow.title("Add Device")
        newWindow.resizable(False,False)
        # sets the geometry of toplevel
        newWindow.geometry("450x500")
        # A Label widget to show in toplevel
        lb1= Label(newWindow, text="IP Address", width=15, font=("arial",12))  
        lb1.place(x=10, y=120)  
        en1= Entry(newWindow,width=25, font=("arial",12)) 
        en1.place(x=200, y=120)  
  
        lb3= Label(newWindow, text="Password", width=15, font=("arial",12))  
        lb3.place(x=9, y=160)  
        en3= Entry(newWindow, show='*', width=25, font=("arial",12))
        en3.place(x=200, y=160)  
  
        lb4= Label(newWindow, text="Description", width=15,font=("arial",12))  
        lb4.place(x=10, y=200)  
        en4= Entry(newWindow,width=25, font=("arial",12))
        en4.place(x=200, y=200)  

        list_of_devices = ("Router", "Switch")  
        cv = StringVar()  
        drplist= OptionMenu(newWindow, cv, *list_of_devices)  
        drplist.config(width=20)  
        cv.set("Router")  
        lb2= Label(newWindow, text="Select Device", width=15,font=("arial",12))  
        lb2.place(x=10,y=240)  
        drplist.place(x=200, y=240)  
  
        lb6= Label(newWindow, text="SSH Username", width=15,font=("arial",12))  
        lb6.place(x=11, y=280)  
        en6= Entry(newWindow, width=25, font=("arial",12))
        en6.place(x=200, y=280)  
  
        lb7= Label(newWindow, text="SSH Password", width=15,font=("arial",12))  
        lb7.place(x=11, y=320)  
        en7 = Entry(newWindow,show='*', width=25, font=("arial",12)) 
        en7.place(x=200, y=320)

        def check_empty():
            if en1.get() and en3.get():
                add_to_list(en4.get(),en1.get(),"Router")
            else:
                lb = Label(newWindow, text="IP & Password Required!", width=20, fg='red', font=('Arial',11,'bold'))
                lb.place(x=100, y=350)
  
        Button(newWindow, text="ADD", width=30, command=check_empty).place(x=100,y=400)

        def add_to_list(desc, ip, cv):
            print(desc, " ", ip, " ", cv)
            list_devices = [desc, ip, cv]
            # open the file in the write mode
            f = open('IP.csv', 'w')

            # create the csv writer
            writer = csv.writer(f)

            # write a row to the csv file
            writer.writerow(list_devices)

            # close the file
            f.close()
            
            

if __name__ == '__main__':
    window = Tk()
    Dashboard(window)
    window.mainloop()