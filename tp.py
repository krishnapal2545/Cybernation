from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image, ImageDraw
from manage import *
from ipaddress import *
from config import *
from datetime import *
import json

newWindow = Tk()
newWindow.title("Configuration History")
newWindow.geometry("500x270")
newWindow.config(background="white")

trv_history = ttk.Treeview(newWindow, selectmode='browse')
trv_history.grid(row=1, column=0, columnspan=3, padx=20, pady=20)
trv_history['height'] = 10 # Number of rows to display, default is 10
trv_history['show'] = 'headings'
trv_history["columns"] = [1, 2, 3]  # column identifiers
trv_history.column(1, width=80, anchor='c')
trv_history.heading(1, text='Sr. No.')
trv_history.column(2, width=150, anchor='c')
trv_history.heading(2, text='Routing')
trv_history.column(3, width=200, anchor='c')
trv_history.heading(3, text='Last Modify')

count = 0
for data in getconfig(5):
    count = count + 1
    lst = [count, data[2], data[4]]
    trv_history.insert("",'end',values=lst)

vs = ttk.Scrollbar(newWindow,orient='vertical',command=trv_history.yview)
vs.grid(row=1,column=3, sticky= 'ns',pady= 20)
trv_history.config(yscrollcommand= vs.set)


newWindow.mainloop()
