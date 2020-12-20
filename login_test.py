#Andrew Caron-DiPietro
#Programming for IT- Final Project
#12/20/20
#This project involves a Tkinter graphical interface and a login authentication process.

# coding=utf-8

from Tkinter import *
import os
import hashlib
import re

#main window
def init_window():
    global main_win #Global variable for our main window
    color="DarkGrey"
    main_win=Tk()
    main_win.geometry("300x250")#window dimensions
    main_win.title("Login Project")#Title
    Label(text="Options", bg="LightGreen", width="300", height="2", font=("Calibri", 13)).pack()#label 
    Label(text="").pack()
    Button(text="Login", height="2", width="30", bg=color, command=login).pack() #Login Button
    Label(text="").pack()
    Button(text="Register", height="2", width="30", bg=color, command=register).pack() #Register Button
    Label(text="").pack()
    main_win.mainloop()

#Register Window.
def register():
    global register_win #Global variable for our register window
    register_win = Toplevel(main_win)
    register_win.title("Register")
    register_win.geometry("300x250")
 
    global username
    global password
    global name_input
    global password_input
    username = StringVar() #We declare String the type of data for our "username"
    password = StringVar() #We declare String the type of data for our "password"
 
    Label(register_win, text="Complete the fields", bg="LightGreen").pack()#Label 
    Label(register_win, text="").pack()
    name_label = Label(register_win, text="* Username *")
    name_label.pack()
    name_input = Entry(register_win, textvariable=username) #Input for username.
    name_input.pack()
    password_label = Label(register_win, text="* Password * ")
    password_label.pack()
    password_input = Entry(register_win, textvariable=password, show='*') #Input for password.
    password_input.pack()
    Label(register_win, text="").pack()
    Button(register_win, text="Sign up", width=10, height=1, bg="LightGreen",command = user_registration).pack() #Register Button


#Login Window
def login():
    global login_window #Global variable for our login window
    login_window = Toplevel(main_win)
    login_window.title("Access") #Title
    login_window.geometry("300x250") #Dimensions
    Label(login_window, text="Enter username and password").pack()
    Label(login_window, text="").pack()
 
    global verify_user
    global verify_password
 
    verify_user = StringVar()
    verify_password = StringVar()
 
    global login_input_user
    global login_input_password
 
    Label(login_window, text="* Username *").pack()
    login_input_user = Entry(login_window, textvariable=verify_user) #User input
    login_input_user.pack()
    Label(login_window, text="").pack()
    Label(login_window, text="* Password *").pack()
    login_input_password = Entry(login_window, textvariable=verify_password, show= '*')#Password input
    login_input_password.pack()
    Label(login_window, text="").pack()
    Button(login_window, text="Sign in", width=10, height=1,command = verify_login).pack()

#Window verify login
def verify_login():

    user1 = verify_user.get()
    password1= verify_password.get()
    login_input_user.delete(0, END) 
    login_input_password.delete(0, END) 
    users={}
    db=open("database.txt","r")

    #Hashig the password 
    h = hashlib.md5()
    h.update(password1.encode('utf-8'))#hashing password

    for line in db.readlines():

        fields=line.split(" ")

        users[fields[0]]=fields[1]

    #cleaning the line break from the hasshed password
    for key in users:
        users[key]=users[key].rstrip('\n')


    if user1 in users:
        # if user exists and the password is correct
        if h.hexdigest() in users.values():
            succesfull_login() #...execute  "succesfull_login()"
        #if not ....
        else:
            no_password() #...execute "no_password()"
    # if the user not exists...
    else:
        no_user() #..execute "no_user()".


# window succesfull_login
def succesfull_login():
    global success_window
    success_window = Toplevel(login_window)
    success_window.title("Success")
    success_window.geometry("300x300")
    Label(success_window, text="Login completed successfully").pack()
    Button(success_window, text="OK", command=delete_succesfull_login).pack()
 

#window no password 
def no_password():
    global window_no_password
    window_no_password = Toplevel(login_window)
    window_no_password.title("ERROR")
    window_no_password.geometry("150x100")
    Label(window_no_password, text="Wrong password").pack()
    Button(window_no_password, text="OK", command=delete_no_password).pack() #execute "delete_no_password()".
 
#window user not found 
def no_user():
    global window_no_user
    window_no_user = Toplevel(login_window)
    window_no_user.title("ERROR")
    window_no_user.geometry("150x100")
    Label(window_no_user, text="User not Found").pack()
    Button(window_no_user, text="OK", command=delete_no_user).pack() #execute "delete_no_user()"

#Closing window
def delete_succesfull_login():
    success_window.destroy()
 
 
def delete_no_password():
    window_no_password.destroy()
 
 
def delete_no_user():
    window_no_user.destroy()

#user registration
def user_registration():
 
    user_info = username.get()
    password_info = password.get()

    
    h = hashlib.md5()#hashing password
    h.update(password_info.encode('utf-8'))

 
    file = open("database.txt", "a") #open database file with the users
    file.write(user_info + " "+h.hexdigest()+"\n")
 
    file.close()
 
    name_input.delete(0, END)
    password_input.delete(0, END)
 
    Label(register_win, text="Successfully registered", fg="green", font=("calibri", 11)).pack()
 
 
init_window()  #Execution of the main window
