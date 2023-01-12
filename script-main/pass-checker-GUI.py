import tkinter as tk
from tkinter import messagebox
import re

# function to check the password
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
    # check if the password contains any consecutive repeating characters
    elif re.search(r"(\w)\1", password):
        return "Password cannot contain any consecutive repeating characters."
    # check if the password is in the list of passwords
    elif not any(password.startswith(line[0]) and password in line for line in open('passwords.txt').read().splitlines()):
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
root.title("Password Checker")

label = tk.Label(root, text="Enter password:")
label.pack()

entry = tk.Entry(root)
entry.pack()

submit = tk.Button(root, text="Submit", command=on_submit)
submit.pack()

root.mainloop()
