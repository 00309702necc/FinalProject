# coding=utf-8

from Tkinter import *
import os
import hashlib

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
    Button(register_win, text="Sign up", width=10, height=1, bg="LightGreen").pack() #Register Button


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
    Button(login_window, text="Sign in", width=10, height=1).pack()

init_window()