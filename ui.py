from tkinter import *
import customtkinter
from PIL import ImageTk,Image
import mysql.connector

import employee as e

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')


def add_emp_submitbtn():
    MainLabel.place_forget()
    SecondaryLabel.place_forget()
    Name_entry.place_forget()
    Dept_entry.place_forget()
    Salary_entry.place_forget()
    submit_btn.place_forget()
    
    emp_name = Name_entry.get()
    emp_dept = Dept_entry.get()
    emp_sal = Salary_entry.get()
    
    e.add_emp(emp_name,emp_dept,emp_sal)
    MANAGER_EMP()

def add_employee():
    Add_Employee_btn.place_forget()
    Dismiss_Employee_btn.place_forget()
    Info_Employee_btn.place_forget()
    Name_entry.delete(0,END)
    Dept_entry.delete(0,END)
    Salary_entry.delete(0,END)
    
    MainLabel.configure(text='EMPLOYEE RECRUITMENT')
    SecondaryLabel.configure(text = 'ENTER EMPLOYEE DETAILS')
    submit_btn.configure(command= lambda:add_emp_submitbtn())
    Left_arrow_btn.configure(command=lambda:MANAGER_EMP())
    Name_entry.configure(placeholder_text="ENTER EMPLOYEE NAME")
    Dept_entry.configure(placeholder_text="ENTER EMPLOYEE DEPARTMENT")
    Salary_entry.configure(placeholder_text="ENTER EMPLOYEE SALARY")
    
    MainLabel.place(relx = 0.5,rely = 0.2,anchor = 'center')
    SecondaryLabel.place(relx = 0.5,rely = 0.3,anchor = 'center')
    Name_entry.place(relx = 0.5,rely = 0.45,anchor = 'center')
    Dept_entry.place(relx = 0.5,rely = 0.58,anchor = 'center')
    Salary_entry.place(relx =0.5,rely = 0.71,anchor = 'center')
    Left_arrow_btn.place(relx=0.025,rely=0.03)
    submit_btn.place(relx = 0.5,rely=0.85 ,anchor='center')
    
    a.bind('<Return>',lambda event:add_emp_submitbtn())

def dismiss_emp_submitbtn():
    EID = EID_entry.get()
    print(EID)
    MainLabel.place_forget()
    SecondaryLabel.place_forget()
    EID_entry.place_forget()
    submit_btn.place_forget()
    
    e.del_emp(EID)
    MANAGER_EMP()

def dismiss_employee():
    Add_Employee_btn.place_forget()
    Dismiss_Employee_btn.place_forget()
    Info_Employee_btn.place_forget()
    Left_arrow_btn.place_forget()
    EID_entry.delete(0,END)
    
    MainLabel.configure(text='EMPLOYEE DISMISSAL')
    SecondaryLabel.configure(text = 'ENTER EMPLOYEE ID TO DISMISS')
    EID_entry.configure(placeholder_text= 'ENTER EID')
    submit_btn.configure(command= lambda:dismiss_emp_submitbtn())
    Left_arrow_btn.configure(command=lambda:MANAGER_EMP())
    
    MainLabel.place(relx = 0.5,rely = 0.2,anchor = 'center')
    SecondaryLabel.place(relx = 0.5,rely = 0.3,anchor = 'center')
    Left_arrow_btn.place(relx=0.025,rely=0.03)
    submit_btn.place(relx = 0.5,rely=0.85 ,anchor='center')
    EID_entry.place(relx= 0.5, rely= 0.5,anchor= 'center')
    
    a.bind('<Return>',lambda event:dismiss_emp_submitbtn())

def MANAGER_EMP():
    Menu_btn.place_forget()
    Salesman_btn.place_forget()
    Order_history_btn.place_forget()
    LogOut_btn.place_forget()
    MainLabel.place_forget()
    SecondaryLabel.place_forget()
    Name_entry.place_forget()
    Dept_entry.place_forget()
    Salary_entry.place_forget()
    EID_entry.place_forget()
    Left_arrow_btn.place_forget()
    submit_btn.place_forget()
    
    Left_arrow_btn.configure(command=lambda:MANAGER())
    
    Add_Employee_btn.place(relx= 0.35,rely= 0.3, anchor= 'center')
    Dismiss_Employee_btn.place(relx = 0.65,rely = 0.3,anchor = 'center')
    Info_Employee_btn.place(relx= 0.35,rely= 0.725, anchor= 'center')
    Left_arrow_btn.place(relx=0.025,rely=0.03)
    return

def History():
    return

def FoodMenu():
    return

def MANAGER():
    id_entry.place_forget()
    pass_entry.place_forget()
    MainLabel.place_forget()
    Left_arrow_btn.place_forget()
    submit_btn.place_forget()
    Add_Employee_btn.place_forget()
    Dismiss_Employee_btn.place_forget()
    Info_Employee_btn.place_forget()
    Left_arrow_btn.place_forget()
    
    Salesman_btn.configure(command = lambda:MANAGER_EMP())
    LogOut_btn.configure(command= lambda:login())
    
    Salesman_btn.place(relx = 0.65,rely = 0.3,anchor = 'center')
    Menu_btn.place(relx= 0.35,rely= 0.3, anchor= 'center')
    Order_history_btn.place(relx= 0.35,rely= 0.725, anchor= 'center')
    LogOut_btn.place(relx= 0.65,rely= 0.725, anchor= 'center')

def EMPLOYEE():
    id_entry.place_forget()
    pass_entry.place_forget()
    MainLabel.place_forget()
    submit_btn.place_forget()
    Left_arrow_btn.place_forget()
    Menu_btn.place_forget()
    
    #UpperFrame = customtkinter.CTkFrame(a,width = 100, height = 100)
    Left_arrow_btn.configure(command= lambda:login_btn())
    
    #UpperFrame.place(relx=0,rely=0,relwidth = 2,relheight = 0.11)
    Left_arrow_btn.place(relx=0.025,rely=0.03)

def submitbtn():
    global incorrectIdLabel
    global incorrectPassLabel
    
    ID_ENTERED = id_entry.get()
    PASS_ENTERED = pass_entry.get()
    
    cursor.execute('select EID,PASS,USER from employee')
    for record in cursor:
        if str(record[0]) == ID_ENTERED:
            if record[2] == 'MANAGER':
                MANAGER()
            elif record[2] == 'EMPLOYEE':
                EMPLOYEE()
    
def login_btn():
    global id_entry
    global pass_entry
    global submit_btn
    
    Manager_btn.place_forget()
    Salesman_btn.place_forget()
    Menu_btn.place_forget()
    Order_history_btn.place_forget()
    LogOut_btn.place_forget()
    MainLabel.place_forget()
    id_entry.delete(0,END)
    pass_entry.delete(0,END)
        
    MainLabel.configure(text = "Enter Login credentials")
    Left_arrow_btn.configure(command= lambda:login())
    id_entry.configure(placeholder_text='ENTER YOUR EMPLOYEE ID')
    pass_entry.configure(placeholder_text='ENTER YOUR PASSWORD')
    
    id_entry.place(relx = 0.5,rely = 0.4,anchor = 'center')
    pass_entry.place(relx = 0.5,rely = 0.52,anchor = 'center')
    submit_btn.place(relx = 0.5,rely = 0.7,anchor = 'center')
    Left_arrow_btn.place(relx=0.025,rely=0.03)
    MainLabel.place(rely = 0.2,relx = 0.5,anchor = 'center')
    
    a.bind('<Return>',lambda event:submitbtn())

def login():
    
    id_entry.place_forget()
    pass_entry.place_forget()
    submit_btn.place_forget()
    Menu_btn.place_forget()
    Order_history_btn.place_forget()
    LogOut_btn.place_forget()
    Left_arrow_btn.place_forget()
    
    MainLabel.configure(text="Welcome to Restaurant Management System")
    Manager_btn.configure(command= lambda:login_btn())
    Salesman_btn.configure(command= lambda:login_btn())
    
    Manager_btn.place(relx = 0.35,rely = 0.6,anchor = 'center')
    Salesman_btn.place(relx = 0.65,rely = 0.6,anchor = 'center')
    MainLabel.place(rely = 0.2,relx = 0.5,anchor = 'center')
     
    
a = customtkinter.CTk()
#code to insert title
a.title('RESTAURANT MANAGEMENT SYSTEM')
#code to insert icon
a.iconbitmap('images/logo.ico')
#code to give size of the form
a.geometry('1000x600')
a.minsize(900,600)
a.maxsize(1000,700)
#a.resizable(0,0)

db = mysql.connector.connect(host = 'localhost', user='root',\
                             passwd='1234',\
                             auth_plugin = 'mysql_native_password')

cursor = db.cursor()
cursor.execute('use rms')


Manager_img = Image.open('images/Manager_img.png')
Salesman_img = Image.open('images/Salesman_img.png')
Menu_img = Image.open('images/menu.png')
Order_history_img = Image.open('images/Order_history.png')
LogOut_img = Image.open('images/logout.png')
Add_Employee_img = Image.open('images/add_employee.png')
Dismiss_Employee_img = Image.open('images/dismiss_employee.png')
Info_Employee_img = Image.open('images/info_employee.png')
Left_arrow_img = Image.open('images/left-arrow2.png')

Manager_img = Manager_img.resize((120,120))
Salesman_img = Salesman_img.resize((120,120))
Menu_img = Menu_img.resize((120,120))
Order_history_img = Order_history_img.resize((120,120))
LogOut_img = LogOut_img.resize((120,120))
Add_Employee_img = Add_Employee_img.resize((120,120))
Dismiss_Employee_img = Dismiss_Employee_img.resize((120,120))
Info_Employee_img = Info_Employee_img.resize((120,120))
Left_arrow_img = Left_arrow_img.resize((30,30))

Manager_icon = ImageTk.PhotoImage(Manager_img)
Salesman_icon = ImageTk.PhotoImage(Salesman_img)
Menu_icon = ImageTk.PhotoImage(Menu_img)
Order_history_icon = ImageTk.PhotoImage(Order_history_img)
LogOut_icon = ImageTk.PhotoImage(LogOut_img)
Add_Employee_icon = ImageTk.PhotoImage(Add_Employee_img)
Dismiss_Employee_icon = ImageTk.PhotoImage(Dismiss_Employee_img)
Info_Employee_icon = ImageTk.PhotoImage(Info_Employee_img)
Left_arrow_icon = ImageTk.PhotoImage(Left_arrow_img)

Manager_btn = customtkinter.CTkButton(a,text = 'Manager',image = Manager_icon,height= 170,width= 150,
                                      compound='top',command=None,text_color= 'silver')
                                    
Salesman_btn = customtkinter.CTkButton(a,text = 'Salesman',image = Salesman_icon,height= 170,width= 150,
                                       compound='top',command= None)

Menu_btn = customtkinter.CTkButton(a,text='MENU',image=Menu_icon,compound='top',height= 170,width= 150,
                                   command = lambda:FoodMenu())

Order_history_btn = customtkinter.CTkButton(a,image = Order_history_icon,text = 'Order History',height= 170,
                                            width= 150,compound='top',command=lambda:History())

LogOut_btn = customtkinter.CTkButton(a,image=LogOut_icon,text='Log Out',compound='top',height= 170,width= 150,
                                   command = None)

Add_Employee_btn = customtkinter.CTkButton(a,image=Add_Employee_icon,text='RECRUIT EMPLOYEE',compound='top',
                                           height= 170,width= 150,command = lambda:add_employee())
Dismiss_Employee_btn = customtkinter.CTkButton(a,image=Dismiss_Employee_icon,text='DISMISS EMPLOYEE',
                                               compound='top',height= 170,width= 150,
                                               command = lambda:dismiss_employee())
Info_Employee_btn = customtkinter.CTkButton(a,image= Info_Employee_icon,text='EMPLOYEE INFO',compound='top',
                                            height= 170,width= 150,command = None)

Left_arrow_btn = customtkinter.CTkButton(a,image=Left_arrow_icon,text = '',width=40,height=20,
                                         corner_radius=1000,command=None)

MainLabel = customtkinter.CTkLabel(a,text="Main Label",font=customtkinter.CTkFont(size = 40),
                                   text_color='#2fa572')

SecondaryLabel = customtkinter.CTkLabel(a,text="Secondary Label",font=customtkinter.CTkFont(size = 30),
                                   text_color='#2fa572')

id_entry = customtkinter.CTkEntry(a,placeholder_text='ENTER YOUR EMPLOYEE ID',height=50,
                                  font=('halvatica',16),width=300)

pass_entry = customtkinter.CTkEntry(a,placeholder_text='ENTER YOUR PASSWORD',height=50,
                                    font=('halvatica',15),width=300,show= '*')

Name_entry = customtkinter.CTkEntry(a,placeholder_text="ENTER EMPLOYEE NAME",height=50,
                                  font=('halvatica',16),width=300)

Dept_entry = customtkinter.CTkEntry(a,placeholder_text="ENTER EMPLOYEE DEPARTMENT",height=50,
                                  font=('halvatica',16),width=300)

Salary_entry = customtkinter.CTkEntry(a,placeholder_text="ENTER EMPLOYEE SALARY",height=50,
                                  font=('halvatica',16),width=300)

EID_entry = customtkinter.CTkEntry(a,placeholder_text='EID',height=50,
                                  font=('halvatica',16),width=300)

submit_btn = customtkinter.CTkButton(a,text='SUBMIT',height=50,font = ('halvatica',16,'bold'),
                                     command=lambda:submitbtn())
            
#login()
#MANAGER()
add_employee()
a.mainloop()
