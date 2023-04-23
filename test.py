# def routing(config, window):
#     try:
#         with telnetlib.Telnet(config['IP']) as telnet:
#             telnet.read_until(b"Username")
#             telnet.write(to_bytes(config['Username']))
#             telnet.read_until(b"Password")
#             telnet.write(to_bytes(config['Password']))
#             index, m, output = telnet.expect([b">", b"#"])
#             if index == 0:
#                 telnet.write(b"enable\n")
#                 telnet.read_until(b"Password")
#                 telnet.write(to_bytes(config['Enable']))
#                 telnet.read_until(b"#", timeout=5)
#             telnet.write(b"terminal length 0\n")
#             telnet.read_until(b"#", timeout=5)
#             time.sleep(3)
#             telnet.read_very_eager()

#             result = {}
#             commands = typeconfig(config)
#             for command in commands:
#                 telnet.write(to_bytes(command))
#                 output = telnet.read_until(b"#", timeout=5).decode("utf-8")
#                 result[command] = output.replace("\r\n", "\n")
#             telnet.write(to_bytes("show running-config"))
#             output = telnet.read_until(b"#", timeout=5).decode("utf-8")
#             result["show running-config"] = output.replace("\r\n", "\n")
#             pprint(result, width=120)
#             saveconfig(config)
#             return result
#     except TimeoutError as e:
#         messagebox.showerror("Error", e, parent=window)


  # self.window.title("Add Configuration")
        # self.window.resizable(False, False)
        # self.window.geometry("530x400")
        # self.window.configure(bg='white')
        # self.window.grab_set()

        # # image
        # device_img = PhotoImage(file='images\device.png')
        # device_info = Label(self.window, image=device_img, bg='white')
        # device_info.pack()
        # device_info.place(x=170, y=20)

        # Label(self.window, text="Configurations : ",
        #       font='Verdana 15 bold', bg='white').place(x=30, y=150)

        # Button(self.window, width=15, height=3, text="VLAN",
        #        bg="#FF9191", command=self.vlan).place(x=210, y=200)
        # if(device[6] == "Router"):
        #     Button(self.window, width=15, height=3, text="Static Routing",
        #            bg="#33FFE9", command=self.staticRouting).place(x=30, y=270)
        #     Button(self.window, width=15, height=3, text="RIP Routing",
        #            bg="#A533FF", command=self.ripRouting).place(x=150, y=270)
        #     Button(self.window, width=15, height=3, text="EIGRP Routing",
        #            bg="#E9FF33", command=self.eigrpRouting).place(x=270, y=270)
        #     Button(self.window, width=15, height=3, text="OSPF Routing",
        #            bg="#9FFF5A", command=self.ospfRouting).place(x=390, y=270)

        # self.window.mainloop()

#device INFO
# image
        # device_img = PhotoImage(file='images\device.png')
        # device_info = Label(newWindow, image=device_img, bg='white')
        # # device_info.pack()
        # device_info.place(x=130, y=20)
# # A Label widget to show in toplevel
#         Label(newWindow, text="Name : ", font=(
#             "arial", 12), bg='white').place(x=40, y= 500)
#         Label(newWindow, text=data[2], font=(
#             "arial", 12), bg='white').place(x=180, y=160)
#         Label(newWindow, text="IP Address : ", font=(
#             "arial", 12), bg='white').place(x=40, y=200)
#         Label(newWindow, text=data[3], font=(
#             "arial", 12), bg='white').place(x=180, y=200)
#         Label(newWindow, text="Description : ", font=(
#             "arial", 12), bg='white').place(x=40, y=240)
#         Label(newWindow, text=data[5], font=(
#             "arial", 12), bg='white').place(x=180, y=240)
#         Label(newWindow, text="Username : ", font=(
#             "arial", 12), bg='white').place(x=40, y=280)
#         Label(newWindow, text=data[7], font=(
#             "arial", 12), bg='white').place(x=180, y=280)
#         Label(newWindow, text="Last Modify : ", font=(
#             "arial", 12), bg='white').place(x=40, y=320)
#         Label(newWindow, text=data[11], font=(
#             "arial", 12), bg='white').place(x=180, y=320)

#         # Button for operation
#         add = Menubutton(newWindow, text='Add Configuration', width=17, height=1, activebackground='light blue',
#                          bg='light blue', relief='raised', borderwidth=2)
#         add.place(x=30, y=380)
#         add.menu = Menu(add, tearoff=False)
#         add["menu"] = add.menu
#         add.menu.add_cascade(
#             label="Create VLAN", command=lambda: Configuration(newWindow, data).vlan())
#         if(data[6] == 'Router'):
#             add.menu.add_cascade(label="Static Routing", command=lambda: Configuration(
#                 newWindow, data).static())
#             add.menu.add_cascade(
#                 label="RIP Routing", command=lambda: Configuration(newWindow, data).rip())
#             add.menu.add_cascade(
#                 label="EIGRP Routing", command=lambda: Configuration(newWindow, data).eigrp())
#             add.menu.add_cascade(
#                 label="OSPF Routing", command=lambda: Configuration(newWindow, data).ospf())

#         Button(newWindow, text='Config History', width=15, bg='light green',
#                command=lambda: Configuration(newWindow, data).configHistory()).place(x=160, y=380)

#         def delete():
#             IP = self.trv_device.selection()[0]
#             self.trv_device.delete(self.trv_device.selection())
#             Database().deleteDevice(IP)
#             newWindow.destroy()
#         Button(newWindow, text='Delete Device', width=15,
#                bg='red', command=delete).place(x=290, y=380)


#    def add_device(self):
#         # Toplevel object which will be treated as a new window
#         newWindow = Toplevel(self.window)
#         # sets the title of the Toplevel widget
#         newWindow.title("Add Device")
#         newWindow.resizable(False, False)
#         # sets the geometry of toplevel
#         newWindow.geometry("450x550")
#         # image
#         device_img = PhotoImage(file='images/device.png')
#         device_info = Label(newWindow, image=device_img, height=100)
#         device_info.pack()
#         device_info.place(x=130, y=20)
#         # A Label widget to show in toplevel
#         en1 = StringVar()
#         en2 = StringVar()
#         en3 = StringVar()
#         en4 = StringVar()
#         en5 = StringVar()
#         en6 = StringVar()
#         en7 = StringVar()
#         en8 = StringVar()

#         Label(newWindow, text="Host Name", font=(
#             "arial", 12)).place(x=40, y=140)
#         Entry(newWindow, width=25, font=("arial", 12),
#               textvariable=en1).place(x=200, y=140)

#         Label(newWindow, text="IP Address", font=(
#             "arial", 12)).place(x=40, y=180)
#         Entry(newWindow, width=25, font=("arial", 12),
#               textvariable=en2).place(x=200, y=180)

#         Label(newWindow, text="Subnet Mask", font=(
#             "arial", 12)).place(x=40, y=220)
#         Entry(newWindow, width=25, font=("arial", 12),
#               textvariable=en3).place(x=200, y=220)

#         Label(newWindow, text="Description", font=(
#             "arial", 12)).place(x=40, y=260)
#         Entry(newWindow, width=25, font=("arial", 12),
#               textvariable=en4).place(x=200, y=260)

#         Label(newWindow, text="Select Device",
#               font=("arial", 12)).place(x=40, y=300)
#         type_of_devices = ("Router", "Switch")
#         en5.set("Router")
#         menu = OptionMenu(newWindow, en5, *type_of_devices)
#         menu.config(width=20)
#         menu.place(x=200, y=300)

#         Label(newWindow, text="Username", font=(
#             "arial", 12)).place(x=40, y=340)
#         Entry(newWindow, width=25, font=("arial", 12),
#               textvariable=en6).place(x=200, y=340)

#         Label(newWindow, text="Password", font=(
#             "arial", 12)).place(x=40, y=380)
#         Entry(newWindow, show='*', width=25, font=("arial", 12),
#               textvariable=en7).place(x=200, y=380)

#         Label(newWindow, text="Enable Password",
#               font=("arial", 12)).place(x=40, y=420)
#         Entry(newWindow, show='*', width=25, font=("arial", 12),
#               textvariable=en8).place(x=200, y=420)

#         def check():
#             try:
#                 IPv4Address(en2.get())
#                 IPv4Address(en3.get())
#                 if Database().getdevice(en2.get()):
#                     messagebox.showerror(
#                         "Error", "IP address had already used", parent=newWindow)
#                 elif en1.get() and en2.get() and en3.get() and en4.get() and en5.get() and en6.get() and en7.get() and en8.get():
#                     data = {
#                         "userID": self.user[0],
#                         "Name": en1.get(),
#                         "IP": en2.get(),
#                         "Subnet": en3.get(),
#                         "Description": en4.get(),
#                         "Type": en5.get(),
#                         "Username": en6.get(),
#                         "Password": en7.get(),
#                         "Enable": en8.get(),
#                         "Last_Modify": datetime.today(),
#                     }
#                     Database().savedevice(data)
#                     global count
#                     count = count + 1
#                     lst = [count, en1.get(), en2.get(), en5.get(),
#                            datetime.today()]
#                     self.trv_device.insert(
#                         "", 'end', iid=en2.get(), values=lst)
#                     messagebox.showinfo(
#                         "Success", "Device Added Successfull", parent=newWindow)
#                     newWindow.destroy()
#                 else:
#                     messagebox.showerror(
#                         "Error", "Device Information can not be left blank", parent=newWindow)
#             except ValueError as e:
#                 messagebox.showerror("Error", e, parent=newWindow)

#         Button(newWindow, text="ADD", width=30,
#                command=check).place(x=100, y=480)
#         newWindow.mainloop()