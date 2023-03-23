from tkinter import *
from tkinter import ttk, messagebox
from manage import *
from main import Dashboard


class Login():

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
        Label(self.window, text="Login", font='Verdana 25 bold').place(x=80, y=150)
        Label(self.window, text="User Name :",font='Verdana 10 bold').place(x=80, y=220)
        Label(self.window, text="Password :",font='Verdana 10 bold').place(x=80, y=260)

        # Entry Box
        self.user_name = StringVar()
        self.password = StringVar()

        self.userentry = Entry(self.window, width=40, textvariable=self.user_name).place(x=200, y=223)
        self.passentry = Entry(self.window, width=40,show="*", textvariable=self.password).place(x=200, y=260)

        # # button login and clear

        Button(self.window, text="Login",font='Verdana 10 bold', command= self.login).place(x=200, y=293)
        Button(self.window, text="Clear",font='Verdana 10 bold', command=self.clear).place(x=260, y=293)

        # # signup button

        Button(self.window, text="Switch To Signup", command= self.switch).place(x=350, y=20)

        self.window.mainloop()

    def clear(self):
        self.userentry.delete(0, END)
        self.passentry.delete(0, END)

    def login(self):
        if self.user_name.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","Enter User Name And Password",parent=self.window)
        else:
            try:
                user = cursor.execute("SELECT * FROM Users WHERE Username = ? AND Password = ?",(str(self.user_name.get()),str(self.password.get()),)).fetchone()
                if user==None:
                    messagebox.showerror("Error" , "Invalid User Name And Password", parent = self.window)
                    self.clear()
                else:
                    self.window.destroy()
                    Dashboard(Tk(),user)
            except Exception as es:
                messagebox.showerror("Error" , f"Error Do to : {str(es)}", parent = self.window)

    def switch(self):
        self.window.destroy()
        Register()

class Register():

    def __init__(self):
        self.window = Tk()
        self.window.title("CyberNation")
        self.window.maxsize(width=500 ,  height=500)
        self.window.minsize(width=500 ,  height=500)

        # Window Icon Photo
        icon = PhotoImage(file='images\\icon.png')
        self.window.iconphoto(True, icon)

        #heading label
        Label(self.window , text = "Signup" , font = 'Verdana 20 bold').place(x=70 , y=60)

	    # form data label
        Label(self.window, text= "First Name :" , font='Verdana 10 bold').place(x=70,y=130)
        Label(self.window, text= "Last Name :" , font='Verdana 10 bold').place(x=70,y=160)
        Label(self.window, text= "Gender :" , font='Verdana 10 bold').place(x=70,y=190)
        Label(self.window, text= "Organization :" , font='Verdana 10 bold').place(x=70,y=220)
        Label(self.window, text= "Contact No.:" , font='Verdana 10 bold').place(x=70,y=250)
        Label(self.window, text= "User Name :" , font='Verdana 10 bold').place(x=70,y=280)
        Label(self.window, text= "Password :" , font='Verdana 10 bold').place(x=70,y=310)
        Label(self.window, text= "Verify Password:" , font='Verdana 10 bold').place(x=70,y=340)

	    # Entry Box ------------------------------------------------------------------
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.phone = IntVar()
        self.var= StringVar()
        self.org = StringVar()
        self.user_name = StringVar()
        self.password = StringVar()
        self.very_pass = StringVar()
        
        Entry(self.window, width=40 ,textvariable = self.first_name).place(x=200 , y=133)
        Entry(self.window, width=40 ,textvariable = self.last_name).place(x=200 , y=163)
        ttk.Radiobutton(self.window ,text='Male', value="Male", variable = self.var).place(x= 200 , y= 190)
        ttk.Radiobutton(self.window ,text='Female', value="Female", variable = self.var).place(x= 260 , y= 190)
        Entry(self.window, width=40 ,textvariable = self.org).place(x=200 , y=223)
        Entry(self.window, width=40 ,textvariable = self.phone).place(x=200 , y=253)
        Entry(self.window, width=40 ,textvariable = self.user_name).place(x=200 , y=283)
        Entry(self.window, width=40 ,show="*" ,textvariable = self.password).place(x=200 , y=313)
        Entry(self.window, width=40 ,show="*" , textvariable = self.very_pass).place(x=200 , y=343)

	    # button login and clear
        Button(self.window, text = "Signup", width= 15 ,font='Verdana 10 bold', command = self.register).place(x=200, y=383)
        Button(self.window , text="Switch To Login" , command = self.switch ).place(x=350 , y =20)
        self.window.mainloop()

    def register(self):
        if self.first_name.get()=="" or self.last_name.get()=="" or self.org.get()=="" or self.user_name.get()=="" or self.password.get()=="" or self.very_pass.get()=="":
            messagebox.showerror("Error" , "All Fields Are Required" , parent = self.window)
        elif self.password.get() != self.very_pass.get():
            messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = self.window)
        else:
            try:
                saveUser(self.first_name.get(),self.last_name.get(),self.var.get(),self.org.get(),self.phone.get(),self.user_name.get(),self.password.get())
                messagebox.showinfo("Success" , "Ragistration Successfull" , parent = self.window)
                self.switch()
            except Exception as es:
                messagebox.showerror("Error" , f"Error do to : {str(es)}", parent = self.window)

    def switch(self):
        self.window.destroy()
        Login()

if __name__ == '__main__':
    Login()
