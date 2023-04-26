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

# #         def delete():
# #             IP = self.trv_device.selection()[0]
# #             self.trv_device.delete(self.trv_device.selection())
# #             Database().deleteDevice(IP)
# #             newWindow.destroy()
# #         Button(newWindow, text='Delete Device', width=15,
# #                bg='red', command=delete).place(x=290, y=380)

# def routing(config, window, commands):
#         # create a flag to stop the progress bar
#         stop_flag = threading.Event()
#         global output
#         output = ""

#         def ssh():
#             global output
#             device = {
#                 'device_type': "autodetect",
#                 'host': config['IP'],
#                 'username': config['Username'],
#                 'password': config['Password'],
#                 'secret': config['Enable'],
#             }
#             try:
#                 device['device_type'] = SSHDetect(**device).autodetect()
#                 with ConnectHandler(**device) as ssh:
#                     # ssh.enable()
#                     output = ssh.send_config_set(commands)
#                 Database().saveconfig(config)
#                 messagebox.showinfo(
#                     "Success", "Configured Successfully", parent=window)

#             except (NetmikoTimeoutException, NetmikoAuthenticationException) as error:
#                 messagebox.showerror("Error", error, parent=window)
#                 output = error
#             finally:
#                 stop_flag.set()

#         def telnet():
#             global output
#             def to_bytes(line): return line.encode('ascii') + b"\n"
#             try:
#                 with telnetlib.Telnet(config['IP']) as telnet:
#                     telnet.read_until(b"Username")
#                     telnet.write(to_bytes(config['Username']))
#                     telnet.read_until(b"Password")
#                     telnet.write(to_bytes(config['Password']))
#                     index, m, output = telnet .expect([b">", b"#"])
#                     if index == 0:
#                         telnet.write(b"enable \n")
#                         telnet.read_until(b"Password")
#                         telnet.write(to_bytes(config['Enable']))
#                         telnet.read_until(b"#", timeout=5)
#                         telnet.write(b"terminal length 0\n")
#                     telnet.read_until(b"#", timeout=5)
#                     time.sleep(3)
#                     telnet.read_very_eager()

#                     telnet.write(to_bytes("configure terminal"))
#                     for command in commands:
#                         telnet.write(to_bytes(command))
#                         output = telnet.read_until(b"#").decode("utf-8")

#                     telnet.write(to_bytes("end"))
#                     output = telnet.read_all().decode('ascii')
#                     output = output.replace("\r\n", "\n")
#                 Database().saveconfig(config)
#                 messagebox.showinfo(
#                     "Success", "Configured Successfully", parent=window)
#             except TimeoutError as error:
#                 messagebox.showerror("Error", error, parent=window)
#                 output = error
#             finally:
#                 stop_flag.set()

#         progress_bar_window = Frame(window, width=280, bg="black")
#         progress_bar_window.place(x=120, y=230, height=30)

#         progress_bar = ttk.Progressbar(progress_bar_window, orient="horizontal",
#                                        length=280, mode="indeterminate")

#         # progress_bar.config()
#         progress_bar.pack()
#         progress_bar.start()

#         def progress_check():
#             # If the flag is set (function f has completed):
#             if stop_flag.is_set():
#                 global output
#                 # Stop the progressbar and destroy the toplevel
#                 Dashboard.output(output)
#                 progress_bar.stop()
#                 progress_bar_window.destroy()

#             else:
#                 # Schedule another call to progress_check in 100 milliseconds
#                 progress_bar.after(100, progress_check)

#         # start executing f in another thread
#         threading.Thread(target=telnet, daemon=True).start()
#         # Start the tkinter loop
#         progress_check()


# from netmiko import (ConnectHandler)


# device={
#     "device_type":"cisco_xe",
#     "host":"192.168.",
#     "port":22,
#     "username":"admin",
#     "password":"cisco",
#     "secret":"a223B",
#     }
# #device['device_type']= SSHDetect(**device).autodetect()
# ConnectHandler(**device)
# #     ssh.enable()
# #     output = ssh.send_command('show ip inter brief')
# # print(output)