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
    # if the password pass all the above conditions, then return valid
    else:
        return "Password is valid."

# function to execute when the submit button is clicked
def on_submit():
    # get the password from the text input field
    password = entry.get()
    # check the password
    result = check_password(password)
    # display a message box with the result
    messagebox.showinfo("Password Checker", result)

# create the root window
root = tk.Tk()
root.title("Password Checker")

# create a label for the text input field
label = tk.Label(root, text="Enter password:")
label.pack()

# create the text input field
entry = tk.Entry(root, show="*")
entry.pack()

# create the submit button
submit = tk.Button(root, text="Submit", command=on_submit)
submit.pack()

# start the GUI event loop
root.mainloop()
