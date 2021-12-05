from tkinter import *
#import tkinter as tk

try:
    def Signin_click():
        str_loginid=txtbx_login.get()
        str_password=txtbx_password.get()
        
        if str_loginid==str_password:
            print(str_loginid,"sign in clicked!!!")
        else:
            print('Invalid password')
        
    
    window=Tk()
    window.geometry("500x500")
    window.title("exercise1")
    
    
    lbl_loginid=Label(window,
                      text="Login ID",
                      font=('ebrima',14),
                      fg='#000000')
    #lbl_loginid.pack()
    lbl_loginid.place(x=50,y=100)
    
    lbl_password=Label(window,
                      text="Password",
                      font=('ebrima',14),
                      fg='#000000')
    #lbl_loginid.pack()
    lbl_password.place(x=50,y=200)
    
    #textbox for login
    txtbx_login=Entry(window,font=('ebrima',14))
    txtbx_login.place(x=200,y=100)
    
    #textbox for password
    txtbx_password=Entry(window,show='*',font=('ebrima',14))
    txtbx_password.place(x=200,y=200)
    
    #login button    
    btn_login=Button(window,text='Sign In',command=Signin_click,
                     fg='#ffffff',
                     bg='#000000',
                     activebackground='#dddddd')
    btn_login.place(x=200,y=300)
    
    
    window.mainloop()
except Exception as ex:
    print(ex)
