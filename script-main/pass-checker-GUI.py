# script for password checker

import tkinter as tk
from tkinter import messagebox
import re
import os

def check_password(password):
    
    # check if the password is at least 8 characters long
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    # check if the password contains at least one numeric character
    elif not any(i.isdigit() for i in password):
        return "Password must contain at least one numeric character."
    
    # check if the password contains at least one special character
    elif not any(i in "!@#$%^&*()_+-=[]{};:'\"\\|,.<>/?" for i in password):
        return "Password must contain at least one special character."
    
    # check if the password contains more than 2 consecutive repeating characters
    elif re.search(r"(\w)\1{2,}", password):
        return "Password can contain only 2 consecutive repeating characters."
    
    # check if the password is in any of the .txt files in the directory
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'db-SecLists')
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            with open(os.path.join(directory, filename)) as file:
                if password in file.read():
                    return "Breached Password. The Password you entered is in the compromised database. Please use difficult another password"
    
    # if the password pass all the above conditions, then return valid
    else:
        return "Secure password."
  

def on_submit():
    password = entry.get()
    result = check_password(password)
    messagebox.showinfo("Password Checker", result)

root = tk.Tk()
root.geometry("300x400")
root.title("SINS | Password Checker")

label = tk.Label(root, text="Enter password:")
label.pack()

entry = tk.Entry(root)
entry.pack()

submit = tk.Button(root, text="Submit", command=on_submit)
submit.pack()

root.mainloop()
